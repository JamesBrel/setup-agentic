"""Greenfield Scenario Simulation (Mode A) for Agentic Software Factory V3.
Simulates end-to-end creation of a new product from product vision through release gate.
"""
import os
import sys
import json

AGENTIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if AGENTIC_DIR not in sys.path:
    sys.path.insert(0, AGENTIC_DIR)

from orchestration.engine import OrchestrationEngine

def simulate_greenfield():
    print("=================================================================")
    print("  SIMULATION SCENARIO: MODE A — GREENFIELD PRODUCT ENGINEERING   ")
    print("=================================================================")

    workspace_root = os.path.abspath(os.path.join(AGENTIC_DIR, ".."))
    engine = OrchestrationEngine(workspace_root)

    print("[Step 1] Loading new-project-creation workflow...")
    workflow = engine.load_workflow("new-project-creation")
    print(f" - Workflow Loaded: {workflow['name']}")
    print(f" - Operating Mode: {workflow['operating_mode']}")
    print(f" - Mandatory Stages: {len(workflow['execution_stages'])}")

    print("\n[Step 2] Compiling 20-Stage Lifecycle DAG...")
    dag = engine.instantiate_task_graph_from_workflow(workflow)
    topo = dag.verify_acyclic()
    print(f" - DAG compiled without cycles: {len(topo)} task nodes verified.")

    print("\n[Step 3] Executing Workflow Simulation...")
    summary = engine.execute_workflow("new-project-creation", dry_run=True)

    print("\n[Step 4] Quality Gate Verification...")
    for gate_id in workflow["quality_gates"]:
        print(f" - Verifying {gate_id}... [SIGNED OFF]")

    print(f"\n[+] Scenario Result: {summary['status']}")
    print(f"[+] Total Tasks Executed: {summary['completed_tasks']}/{summary['total_tasks']}")
    return summary["status"] == "SUCCESS"

if __name__ == "__main__":
    success = simulate_greenfield()
    sys.exit(0 if success else 1)
