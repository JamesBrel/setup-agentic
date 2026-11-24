"""Task Dependency Graph (DAG) manager for Agentic Software Factory V3.
Performs topological sorting, cycle detection, and concurrency safety analysis.
"""
from typing import Dict, List, Set, Any, Optional
from collections import deque
from .state_machine import TaskState

class TaskGraphError(Exception):
    """Raised on cyclic dependencies or graph inconsistency."""
    pass

class TaskGraph:
    """Manages directed acyclic graph of tasks."""

    def __init__(self):
        self.tasks: Dict[str, Dict[str, Any]] = {}
        self.adj_list: Dict[str, List[str]] = {} # u -> list of v (v depends on u)
        self.in_degree: Dict[str, int] = {}     # v -> number of dependencies

    def add_task(self, task: Dict[str, Any]) -> None:
        """Add a task node to the graph."""
        task_id = task["task_id"]
        if task_id in self.tasks:
            raise TaskGraphError(f"Duplicate task ID in graph: {task_id}")

        self.tasks[task_id] = task
        self.adj_list[task_id] = []
        self.in_degree[task_id] = 0

    def build_dependencies(self) -> None:
        """Construct graph edges based on tasks' dependencies."""
        for task_id, task in self.tasks.items():
            deps = task.get("dependencies", [])
            for dep_id in deps:
                if dep_id not in self.tasks:
                    raise TaskGraphError(f"Task {task_id} references non-existent dependency: {dep_id}")
                self.adj_list[dep_id].append(task_id)
                self.in_degree[task_id] += 1

        self.verify_acyclic()

    def verify_acyclic(self) -> List[str]:
        """Detect cycles using Kahn's algorithm. Returns a topological ordering if acyclic."""
        in_deg = dict(self.in_degree)
        queue = deque([t for t, deg in in_deg.items() if deg == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in self.adj_list[node]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != len(self.tasks):
            cyclic_nodes = [t for t, deg in in_deg.items() if deg > 0]
            raise TaskGraphError(f"Cycle detected in task graph involving tasks: {cyclic_nodes}")

        return topo_order

    def get_ready_tasks(self) -> List[Dict[str, Any]]:
        """Return tasks whose dependencies are all ACCEPTED and who are in READY or PLANNED state."""
        ready = []
        for task_id, task in self.tasks.items():
            current_status = task.get("status")
            if current_status not in [TaskState.PLANNED.value, TaskState.READY.value]:
                continue

            deps = task.get("dependencies", [])
            all_deps_accepted = all(
                self.tasks[dep_id].get("status") == TaskState.ACCEPTED.value
                for dep_id in deps
            )

            if all_deps_accepted:
                ready.append(task)

        return ready

    def partition_concurrent_batches(self, candidate_tasks: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
        """Group candidate tasks into disjoint execution batches.
        Tasks within the same batch have non-intersecting allowed_paths and can execute in parallel.
        Tasks with overlapping paths are placed in subsequent sequential batches.
        """
        batches: List[List[Dict[str, Any]]] = []

        for task in candidate_tasks:
            task_paths = set(task.get("allowed_paths", []))
            placed = False

            for batch in batches:
                # Check if task conflicts with any task already in this batch
                batch_paths = set().union(*(t.get("allowed_paths", []) for t in batch))
                # Intersect paths: if no overlap, task can join this batch
                if not task_paths.intersection(batch_paths):
                    batch.append(task)
                    placed = True
                    break

            if not placed:
                # Create a new batch
                batches.append([task])

        return batches
