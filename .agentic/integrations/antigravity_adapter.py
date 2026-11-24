"""Google Antigravity Adapter for Agentic Software Factory V4.
Bridges Antigravity subagent invocation, slash commands, and workspace boundaries.
Enforces strict directory separation:
- app/: All code implementation, compilation, source code files, and build commands.
- docs/: All UI/UX mockups (Stitch/Figma), design systems, logos, icons, and specifications.
- .agentic/: Factory governance, schemas, agent definitions, workflows, and memory.
"""
import os
import json
from typing import Dict, List, Any, Optional

class AntigravityAdapter:
    """Interface bridging factory operations with Google Antigravity environment."""

    SLASH_COMMAND_MAPPINGS = {
        "/new-project": "new-project-creation",
        "/adopt-project": "existing-project-onboarding",
        "/add-new-features": "feature-development",
        "/fix-bug": "bug-fixing",
        "/review-and-test": "testing-validation",
        "/security-audit": "security-remediation",
        "/update-app": "refactoring",
        "/design_project": "design-project",
        "/design-project": "design-project",
        "!design_project": "design-project",
        "!design-project": "design-project"
    }

    def __init__(self, workspace_root: Optional[str] = None):
        if workspace_root is None:
            self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        else:
            self.workspace_root = workspace_root
        self.agentic_dir = os.path.join(self.workspace_root, ".agentic")

    def resolve_workflow_from_command(self, command_or_prompt: str) -> Optional[str]:
        """Map slash commands or keywords to canonical factory workflow IDs."""
        for cmd, wf_id in self.SLASH_COMMAND_MAPPINGS.items():
            if cmd in command_or_prompt:
                return wf_id
        return None

    def export_subagent_definitions(self) -> List[Dict[str, Any]]:
        """Export specialist agents in Antigravity define_subagent compatible format."""
        agents_dir = os.path.join(self.agentic_dir, "agents")
        subagents = []

        if not os.path.exists(agents_dir):
            return subagents

        for fname in os.listdir(agents_dir):
            if fname.endswith(".json") and fname != "catalog.json":
                fpath = os.path.join(agents_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    agent = json.load(f)
                    subagents.append({
                        "Name": agent.get("id"),
                        "Description": f"{agent.get('name')} - {agent.get('role')}",
                        "SystemPrompt": (
                            f"Identity: {agent.get('identity')}\n"
                            f"Mission: {agent.get('mission')}\n"
                            f"Responsibilities: {', '.join(agent.get('responsibilities', []))}\n"
                            f"Allowed Operations: {', '.join(agent.get('allowed_operations', []))}\n"
                            f"Forbidden Operations: {', '.join(agent.get('forbidden_operations', []))}\n"
                            f"Directory Policy (V4): Code strictly in app/, designs/docs strictly in docs/.\n"
                        ),
                        "EnableWriteTools": True,
                        "EnableMCPTools": True,
                        "EnableSubagentTools": agent.get("division") == "management"
                    })
        return subagents

    def generate_antigravity_rules(self) -> str:
        """Generate Antigravity project rules encapsulating V4 factory invariants."""
        return """# Antigravity Rules for Agentic Software Factory V4

1. Single Source of Truth: All factory specifications, schemas, agents, workflows, and memory reside in `.agentic/`.
2. Strict Application Code Boundary: All application implementation, source code generation, and development commands MUST execute and reside strictly in `app/`.
3. Strict Design & Documentation Boundary: All UI/UX design operations, Stitch/Figma mockups, logos, application icons, and specifications MUST reside strictly in `docs/`.
4. Dedicated Design Agent: The agent `project_designer` handles all UI/UX architecture, Design Systems, logos, and app icons using 100% Stitch MCP or Figma MCP tools.
5. Flat Skills Layout: All skills in `.agentic/skills/<skill-name>/` must be strictly flat (no nested subdirectories).
6. Zero-Trust Verification: No task transitions to ACCEPTED without verifiable test or static analysis evidence.
7. Brownfield Protection: When working on existing projects, never overwrite uncommitted user modifications or restructure without prior profiling.
8. Security Boundary: Never execute destructive database statements, push to remote git, or modify security controls without explicit human approval.
"""
