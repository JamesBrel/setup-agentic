"""End-to-End Test Suite for Agentic Software Factory V4.
Verifies state machine invariants, DAG resolution, bounded recovery, memory sanitization,
security boundaries, V4 domain isolation (app/ and docs/), and model router abstractions.
"""
import unittest
import os
import sys
import json

AGENTIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if AGENTIC_DIR not in sys.path:
    sys.path.insert(0, AGENTIC_DIR)

from orchestration.state_machine import TaskStateMachine, TaskState, StateMachineError
from orchestration.task_graph import TaskGraph, TaskGraphError
from orchestration.recovery_manager import RecoveryManager, RecoveryDecision
from orchestration.engine import OrchestrationEngine
from memory.sanitization import MemorySanitizer, SanitizationError
from security.boundary_guard import BoundaryGuard, SecurityBoundaryViolation
from integrations.model_router import ModelRouter

class TestTaskStateMachine(unittest.TestCase):
    def test_valid_transitions(self):
        task = {
            "task_id": "TASK-001",
            "status": TaskState.PLANNED.value,
            "assigned_agent": "backend-developer",
            "allowed_paths": ["app/src/"],
            "dependencies": [],
            "evidence": []
        }
        # PLANNED -> READY
        TaskStateMachine.transition(task, TaskState.READY)
        self.assertEqual(task["status"], TaskState.READY.value)

        # READY -> IN_PROGRESS
        TaskStateMachine.transition(task, TaskState.IN_PROGRESS)
        self.assertEqual(task["status"], TaskState.IN_PROGRESS.value)

        # IN_PROGRESS -> IMPLEMENTED
        TaskStateMachine.transition(task, TaskState.IMPLEMENTED)
        self.assertEqual(task["status"], TaskState.IMPLEMENTED.value)

        # IMPLEMENTED -> VERIFYING
        TaskStateMachine.transition(task, TaskState.VERIFYING)
        self.assertEqual(task["status"], TaskState.VERIFYING.value)

        # Cannot transition to ACCEPTED without evidence
        with self.assertRaises(StateMachineError):
            TaskStateMachine.transition(task, TaskState.ACCEPTED)

        # Add valid evidence
        task["evidence"].append({
            "timestamp": "2026-11-24T00:00:00Z",
            "verifier": "unit_test_runner",
            "type": "TEST_RESULTS",
            "content_or_path": "All tests passed",
            "passed": True
        })

        # Now VERIFYING -> ACCEPTED succeeds
        TaskStateMachine.transition(task, TaskState.ACCEPTED)
        self.assertEqual(task["status"], TaskState.ACCEPTED.value)

    def test_illegal_transition(self):
        task = {
            "task_id": "TASK-002",
            "status": TaskState.PROPOSED.value
        }
        with self.assertRaises(StateMachineError):
            TaskStateMachine.transition(task, TaskState.ACCEPTED)

class TestTaskGraph(unittest.TestCase):
    def test_acyclic_and_concurrency(self):
        dag = TaskGraph()
        t1 = {
            "task_id": "T1",
            "status": TaskState.ACCEPTED.value,
            "dependencies": [],
            "allowed_paths": ["app/src/auth/"]
        }
        t2 = {
            "task_id": "T2",
            "status": TaskState.READY.value,
            "dependencies": ["T1"],
            "allowed_paths": ["app/src/frontend/"]
        }
        t3 = {
            "task_id": "T3",
            "status": TaskState.READY.value,
            "dependencies": ["T1"],
            "allowed_paths": ["app/src/backend/"]
        }
        dag.add_task(t1)
        dag.add_task(t2)
        dag.add_task(t3)
        dag.build_dependencies()

        order = dag.verify_acyclic()
        self.assertEqual(len(order), 3)

        ready = dag.get_ready_tasks()
        self.assertEqual(len(ready), 2)

        batches = dag.partition_concurrent_batches(ready)
        self.assertEqual(len(batches), 1)
        self.assertEqual(len(batches[0]), 2)

    def test_cycle_detection(self):
        dag = TaskGraph()
        t1 = {"task_id": "TA", "dependencies": ["TB"], "allowed_paths": []}
        t2 = {"task_id": "TB", "dependencies": ["TA"], "allowed_paths": []}
        dag.add_task(t1)
        dag.add_task(t2)
        with self.assertRaises(TaskGraphError):
            dag.build_dependencies()

class TestRecoveryManager(unittest.TestCase):
    def test_bounded_retries(self):
        rm = RecoveryManager(default_max_retries=3)
        task = {"task_id": "T-FAIL", "retry_count": 0, "max_retries": 3}

        for i in range(3):
            d = rm.evaluate_failure(task, "SyntaxError")
            self.assertEqual(d["decision"], RecoveryDecision.RETRY_SCOPED.value)
            task["retry_count"] = i + 1

        d4 = rm.evaluate_failure(task, "SyntaxError")
        self.assertEqual(d4["decision"], RecoveryDecision.ESCALATE_TO_HUMAN.value)

class TestMemorySanitization(unittest.TestCase):
    def test_reject_secrets(self):
        malicious_lesson = {
            "lesson_id": "LESSON-BAD",
            "status": "VALIDATED",
            "solution": "api_key = 'AIzaSyA_abcdef1234567890'",
            "supporting_evidence": {"test_passed": True}
        }
        with self.assertRaises(SanitizationError):
            MemorySanitizer.sanitize_record(malicious_lesson)

class TestV4SecurityAndDomainIsolation(unittest.TestCase):
    def setUp(self):
        self.guard = BoundaryGuard()

    def test_block_prohibited_command(self):
        with self.assertRaises(SecurityBoundaryViolation):
            self.guard.validate_command("DROP DATABASE production_users;", has_human_approval=False)

        ok, msg = self.guard.validate_command("DROP DATABASE production_users;", has_human_approval=True)
        self.assertTrue(ok)

    def test_v4_domain_isolation_app_for_code(self):
        # Code in app/ -> Valid
        self.assertTrue(self.guard.validate_v4_domain_isolation("app/src/main.dart", "CODE_DEVELOPMENT"))
        # Code outside app/ -> Violation
        with self.assertRaises(SecurityBoundaryViolation):
            self.guard.validate_v4_domain_isolation("src/main.dart", "CODE_DEVELOPMENT")

    def test_v4_domain_isolation_docs_for_design(self):
        # Design in docs/ -> Valid
        self.assertTrue(self.guard.validate_v4_domain_isolation("docs/design/design_system.md", "DESIGN"))
        self.assertTrue(self.guard.validate_v4_domain_isolation("docs/logos/logo.svg", "LOGO"))
        # Design in app/ or root -> Violation
        with self.assertRaises(SecurityBoundaryViolation):
            self.guard.validate_v4_domain_isolation("app/design/design_system.md", "DESIGN")
        with self.assertRaises(SecurityBoundaryViolation):
            self.guard.validate_v4_domain_isolation("logo.svg", "LOGO")

class TestProjectDesignerAndWorkflow(unittest.TestCase):
    def test_project_designer_agent(self):
        agent_path = os.path.join(AGENTIC_DIR, "agents", "project_designer.json")
        self.assertTrue(os.path.isfile(agent_path))
        with open(agent_path, "r", encoding="utf-8") as f:
            agent = json.load(f)
        self.assertEqual(agent["id"], "project_designer")
        self.assertIn("graphic-design", agent["required_skills"])
        self.assertIn("design-system-engineering", agent["required_skills"])
        self.assertIn("STITCH_MCP_OPERATIONS", agent["allowed_operations"])
        self.assertIn("FIGMA_MCP_OPERATIONS", agent["allowed_operations"])

    def test_design_project_workflow(self):
        workspace_root = os.path.abspath(os.path.join(AGENTIC_DIR, ".."))
        engine = OrchestrationEngine(workspace_root)
        wf = engine.load_workflow("design-project")
        self.assertEqual(wf["id"], "design-project")
        self.assertIn("project_designer", wf["required_agents"])
        
        # Test DAG instantiation and execution simulation
        dag = engine.instantiate_task_graph_from_workflow(wf)
        order = dag.verify_acyclic()
        self.assertEqual(len(order), len(wf["execution_stages"]))

        res = engine.execute_workflow("design-project", dry_run=True)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["completed_tasks"], len(wf["execution_stages"]))

if __name__ == "__main__":
    unittest.main()
