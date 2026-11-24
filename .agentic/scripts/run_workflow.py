"""Workflow Execution CLI for Agentic Software Factory V4.
Usage: python .agentic/scripts/run_workflow.py --workflow <workflow-id> [--dry-run]
"""
import os
import sys
import argparse

# Add .agentic directory to sys.path so modules inside it can import each other directly
AGENTIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if AGENTIC_DIR not in sys.path:
    sys.path.insert(0, AGENTIC_DIR)

from orchestration.engine import OrchestrationEngine

def main():
    parser = argparse.ArgumentParser(description="Agentic Factory Workflow Runner")
    parser.add_argument("--workflow", "-w", required=True, help="Workflow ID (e.g. design-project, existing-project-onboarding)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate execution without modifying files")
    args = parser.parse_args()

    workspace_root = os.path.abspath(os.path.join(AGENTIC_DIR, ".."))
    print(f"[*] Starting Agentic Software Factory V4 Engine...")
    print(f"[*] Target Workflow: {args.workflow}")
    print(f"[*] Workspace Root: {workspace_root}")

    engine = OrchestrationEngine(workspace_root)
    result = engine.execute_workflow(args.workflow, dry_run=args.dry_run)

    print("\n================ WORKFLOW EXECUTION SUMMARY ================")
    print(f"Workflow ID:      {result['workflow_id']}")
    print(f"Status:           {result['status']}")
    print(f"Total Tasks:      {result['total_tasks']}")
    print(f"Completed Tasks:  {result['completed_tasks']}")
    print(f"Execution Log:    {len(result['execution_log'])} task stages executed")
    print("============================================================\n")

if __name__ == "__main__":
    main()
