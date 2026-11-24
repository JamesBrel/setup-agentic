# Agentic Software Factory V4

Welcome to **Agentic Software Factory V4**, an autonomous, multi-agent software engineering operating system developed for Google Antigravity and portable across modern AI model families.

## Strict Workspace Directory Separation (V4 Invariants)
- **`app/`**: All application source code generation, developer agent implementations, compilation, and development commands are restricted exclusively to this directory.
- **`docs/`**: All visual design mockups, Design Systems, Stitch MCP and Figma MCP outputs, logos, application icons, PRDs, TRDs, and documentation are restricted exclusively to this directory.
- **`.agentic/`**: All factory configuration, schemas, agent contracts, modular flat skills, workflows, state machine, and validated memory reside strictly inside this directory.

## Specialized Design Agent & `/design_project`
- **Agent `project_designer`**: Dedicated UI/UX Architect, Graphic Designer, and Brand Identity Engineer relying 100% on **Stitch MCP** (`StitchMCP`) or **Figma MCP** (`figma-dev-mode-mcp-server`) tools to craft professional design systems, logos, multi-resolution app icons, and interactive screens from initial ideas.
- **Antigravity Command `/design_project`**: Triggers the `design-project` workflow to invoke `project_designer` and output all assets into `docs/`.

## Quick Start
Run the factory validation suite:
```bash
python .agentic/scripts/validate_factory.py
```

Run the visual design workflow:
```bash
python .agentic/scripts/run_workflow.py --workflow design-project
```

Onboard an existing codebase:
```bash
python .agentic/scripts/run_workflow.py --workflow existing-project-onboarding
```
