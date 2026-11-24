# Project Workspace with Agentic Software Factory V4

This workspace is governed by **Agentic Software Factory V4**, an autonomous, multi-agent software engineering operating system with strict domain isolation:

- **[`app/`](app/)**: Dedicated exclusively to application source code implementation, builds, and development commands.
- **[`docs/`](docs/)**: Dedicated exclusively to UI/UX design mockups (Stitch / Figma), Design Systems, logos, application icons, PRDs, TRDs, and documentation.
- **[`.agentic/`](.agentic/README.md)**: Encapsulates all factory configurations, 47 specialist agents, 31 flat skills, 13 canonical workflows, orchestration logic, and governance files.

## Available Slash Commands
- `/design_project`: Invokes the `project_designer` agent to generate complete UI/UX screens, Design Systems, application icons, and logos using 100% Stitch or Figma MCP tools into `docs/`.
- `/new-project`: Initiates the full 20-stage greenfield product development lifecycle.
- `/adopt-project`: Scans, profiles, and baselines an existing codebase while protecting uncommitted user changes.
- `/add-new-features`: Develops targeted features inside `app/` adhering to existing contracts.
- `/fix-bug`: Diagnoses root causes, creates reproduction tests, and applies surgical fixes in `app/`.
- `/review-and-test`: Executes unit, integration, and accessibility test suites.
- `/security-audit`: Runs static code analysis, secret detection, and dependency vulnerability scans.

## Verification & Management
```bash
# Validate factory integrity (all 92 checks)
python .agentic/scripts/validate_factory.py

# Run unit and integration tests
python .agentic/evaluations/test_factory.py

# Trigger the UI/UX design workflow
python .agentic/scripts/run_workflow.py --workflow design-project
```
