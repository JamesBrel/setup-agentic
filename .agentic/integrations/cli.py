"""Command Line Interface (CLI) for Agentic Software Factory V4.
Provides high-level management commands for workflow execution, validation, and provider selection.
"""
import sys
import os
import argparse
import json

# Add .agentic directory to sys.path
AGENTIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if AGENTIC_DIR not in sys.path:
    sys.path.insert(0, AGENTIC_DIR)

from orchestration.engine import OrchestrationEngine
from integrations.model_router import ModelRouter
from integrations.antigravity_adapter import AntigravityAdapter

def main():
    parser = argparse.ArgumentParser(
        description="Agentic Software Factory V4 CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Available factory commands")

    # Command: run-workflow
    wf_parser = subparsers.add_parser("run-workflow", help="Execute a factory workflow pipeline")
    wf_parser.add_argument("--workflow", "-w", required=True, help="Workflow ID (e.g. design-project, existing-project-onboarding)")
    wf_parser.add_argument("--dry-run", action="store_true", help="Simulate execution without modifications")

    # Command: set-provider
    prov_parser = subparsers.add_parser("set-provider", help="Switch the active foundation model provider")
    prov_parser.add_argument("--name", "-n", required=True, choices=["gemini", "claude", "gpt"], help="Provider name")

    # Command: list-agents
    subparsers.add_parser("list-agents", help="List all specialist agents")

    # Command: list-skills
    subparsers.add_parser("list-skills", help="List all modular skills")

    # Command: list-workflows
    subparsers.add_parser("list-workflows", help="List all canonical workflows")

    args = parser.parse_args()

    workspace_root = os.path.abspath(os.path.join(AGENTIC_DIR, ".."))

    if args.command == "run-workflow":
        print(f"[*] Instantiating Orchestration Engine V4 for workspace: {workspace_root}")
        engine = OrchestrationEngine(workspace_root)
        print(f"[*] Launching workflow: {args.workflow} (dry_run={args.dry_run})")
        result = engine.execute_workflow(args.workflow, dry_run=args.dry_run)
        print(f"[+] Workflow {args.workflow} completed with status: {result['status']}")
        print(f"[+] Total tasks: {result['total_tasks']} | Completed: {result['completed_tasks']}")

    elif args.command == "set-provider":
        router = ModelRouter()
        router.set_active_provider(args.name)
        print(f"[+] Successfully switched active provider to: {args.name}")

    elif args.command == "list-agents":
        catalog_path = os.path.join(AGENTIC_DIR, "agents", "catalog.json")
        with open(catalog_path, "r", encoding="utf-8") as f:
            catalog = json.load(f)
        print(f"=== Total Agents: {catalog['total_agents']} ===")
        for agent_id, data in catalog["agents"].items():
            print(f" - [{data['division'].upper()}] {agent_id}: {data['name']} ({data['model_tier']})")

    elif args.command == "list-skills":
        catalog_path = os.path.join(AGENTIC_DIR, "skills", "catalog.json")
        with open(catalog_path, "r", encoding="utf-8") as f:
            catalog = json.load(f)
        print(f"=== Total Skills: {catalog['total_skills']} ===")
        for skill_id, data in catalog["skills"].items():
            print(f" - [{data['category'].upper()}] {skill_id}: {data['name']}")

    elif args.command == "list-workflows":
        catalog_path = os.path.join(AGENTIC_DIR, "workflows", "catalog.json")
        with open(catalog_path, "r", encoding="utf-8") as f:
            catalog = json.load(f)
        print(f"=== Total Workflows: {catalog['total_workflows']} ===")
        for wf_id, data in catalog["workflows"].items():
            print(f" - [{data['operating_mode']}] {wf_id}: {data['name']} ({data['stages_count']} stages)")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
