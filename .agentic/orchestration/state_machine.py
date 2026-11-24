"""State machine module for Agentic Software Factory V3.
Enforces the controlled lifecycle of tasks with strict transition guards and evidence requirements.
"""
from enum import Enum
from typing import Dict, List, Set, Any, Optional

class TaskState(str, Enum):
    PROPOSED = "PROPOSED"
    ANALYZED = "ANALYZED"
    PLANNED = "PLANNED"
    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    IMPLEMENTED = "IMPLEMENTED"
    VERIFYING = "VERIFYING"
    ACCEPTED = "ACCEPTED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"

class StateMachineError(Exception):
    """Raised when an invalid state transition or missing precondition is encountered."""
    pass

class TaskStateMachine:
    """Finite State Machine governing task lifecycles."""

    VALID_TRANSITIONS: Dict[TaskState, Set[TaskState]] = {
        TaskState.PROPOSED: {TaskState.ANALYZED, TaskState.CANCELLED},
        TaskState.ANALYZED: {TaskState.PLANNED, TaskState.CANCELLED, TaskState.BLOCKED},
        TaskState.PLANNED: {TaskState.READY, TaskState.BLOCKED, TaskState.CANCELLED},
        TaskState.BLOCKED: {TaskState.READY, TaskState.CANCELLED},
        TaskState.READY: {TaskState.IN_PROGRESS, TaskState.BLOCKED, TaskState.CANCELLED},
        TaskState.IN_PROGRESS: {TaskState.IMPLEMENTED, TaskState.FAILED, TaskState.BLOCKED},
        TaskState.IMPLEMENTED: {TaskState.VERIFYING, TaskState.FAILED},
        TaskState.VERIFYING: {TaskState.ACCEPTED, TaskState.FAILED},
        TaskState.FAILED: {TaskState.IN_PROGRESS, TaskState.REJECTED, TaskState.CANCELLED},
        TaskState.ACCEPTED: set(), # Terminal success
        TaskState.REJECTED: set(), # Terminal failure / human intervention
        TaskState.CANCELLED: set() # Terminal withdrawal
    }

    @classmethod
    def can_transition(cls, current_state: TaskState, target_state: TaskState) -> bool:
        """Check if transition is theoretically valid."""
        return target_state in cls.VALID_TRANSITIONS.get(current_state, set())

    @classmethod
    def transition(cls, task_data: Dict[str, Any], target_state: TaskState) -> Dict[str, Any]:
        """Attempt to transition task to target_state, enforcing invariants."""
        current_state_str = task_data.get("status")
        try:
            current_state = TaskState(current_state_str)
        except ValueError:
            raise StateMachineError(f"Task has invalid current state: {current_state_str}")

        if not cls.can_transition(current_state, target_state):
            raise StateMachineError(
                f"Illegal state transition from {current_state.value} to {target_state.value}. "
                f"Allowed targets: {[s.value for s in cls.VALID_TRANSITIONS.get(current_state, set())]}"
            )

        # Invariant Checks
        cls._verify_guards(task_data, current_state, target_state)

        # Apply state update
        task_data["status"] = target_state.value
        return task_data

    @classmethod
    def _verify_guards(cls, task_data: Dict[str, Any], current_state: TaskState, target_state: TaskState) -> None:
        """Verify preconditions and guards before committing state transition."""
        if target_state == TaskState.ACCEPTED:
            evidence = task_data.get("evidence", [])
            if not evidence:
                raise StateMachineError("Guard failed: Cannot transition to ACCEPTED without verifiable evidence.")
            has_passed_evidence = any(e.get("passed", False) is True for e in evidence)
            if not has_passed_evidence:
                raise StateMachineError("Guard failed: Cannot transition to ACCEPTED without at least one passed evidence entry.")

        if target_state == TaskState.READY:
            dependencies = task_data.get("dependencies", [])
            # Dependencies must be empty or satisfied (checked by task graph)
            if not task_data.get("assigned_agent"):
                raise StateMachineError("Guard failed: Cannot transition to READY without an assigned agent.")

        if target_state == TaskState.IN_PROGRESS:
            allowed_paths = task_data.get("allowed_paths", [])
            if not allowed_paths:
                raise StateMachineError("Guard failed: Task must define explicit allowed_paths before starting.")

        if target_state == TaskState.FAILED:
            retry_count = task_data.get("retry_count", 0)
            task_data["retry_count"] = retry_count + 1
