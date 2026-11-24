# Operating Principles — Agentic Software Factory V3

## 1. Core Operating Modes

The factory supports two foundational operating paradigms:

### Mode A: Greenfield Project Engineering
For engineering a new software product from conception to release.
Execution must strictly advance through the 20-stage mandatory lifecycle:

1. **Idea Discovery**: Intake problem domain, stakeholders, and market space.
2. **Business & Product Analysis**: Value propositions, business drivers, ROI factors.
3. **Requirements Gathering**: User stories, functional capabilities, personas.
4. **Project Feasibility Analysis**: Technical, schedule, and complexity evaluation.
5. **PRD Generation**: Formal PRD authoring according to `prd.schema.json`.
6. **PRD Validation (Gate 1)**: Signoff criteria and acceptance rules verified.
7. **Technical Research**: Technology evaluation, library suitability, benchmarks.
8. **TRD Generation**: System architecture, data design, API specs (`trd.schema.json`).
9. **Architecture Validation (Gate 2)**: 100% PRD-to-TRD traceability check.
10. **Database & API Design**: Entities, migrations, schemas, OpenAPI specs.
11. **UI/UX Specification**: User journeys, layout tokens, accessibility constraints.
12. **Implementation Planning**: Task decomposition, DAG generation, file paths.
13. **Repository Scaffolding**: Directory creation, build tooling, gitignore, linting.
14. **Development**: Domain entities, business logic, UI components, adapters.
15. **Integration**: Subsystem binding, service composition, state management.
16. **Automated Testing (Gate 3)**: Unit tests, mock suites, code coverage checks.
17. **Security Audit (Gate 4)**: Dependency vulnerability scan, SAST, secret leak check.
18. **Performance Verification**: Benchmark runs, latency checks, memory profiles.
19. **Documentation**: Developer README, API reference, architecture summary.
20. **Release Preparation (Gate 5)**: Artifact tagging, changelog, delivery pack.

> **Rule**: No implementation code is written before Gates 1 & 2 pass, unless a proof-of-concept is explicitly requested by the user.

---

### Mode B: Existing Project Intelligence (Brownfield)
For working within an existing codebase.

#### Phase 1: Repository Intelligence & Baseline Scan
Before writing or modifying any code, the factory autonomously performs:
1. Complete tree discovery and language/framework detection.
2. Dependency manifest inspection (`package.json`, `pubspec.yaml`, `composer.json`, `pom.xml`, `requirements.txt`).
3. Architectural pattern identification (Clean Arch, MVC, Hexagonal, Modular).
4. Entry points mapping (`main.dart`, `index.ts`, `server.py`, `app.php`).
5. Module dependency graph generation.
6. Database schema & migration status check.
7. API contract identification.
8. Test runner discovery and baseline test execution.
9. Documentation inventory.
10. Git status inspection to protect user uncommitted modifications (`git status -s`).
11. Baseline build status capture.
12. Synthesis of `.agentic/memory/project_profile.json`.

#### Critical Invariants for Mode B:
- **Never rewrite or restructure** without first profiling the project.
- **Preserve unrelated code and contracts**: Changes must be surgical and scoped.
- **Protect user work**: If unstaged user modifications exist, never overwrite them.
- **Preserve conventions**: Match existing formatting, naming, and architectural idioms.

---

## 2. Collaboration and Execution Invariants

### Parallel vs. Sequential Execution Rules
The Orchestrator dispatches tasks concurrently **only** when all of the following conditions are met:
1. Tasks have zero mutual dependencies in the Task Graph.
2. The `allowed_paths` of concurrent tasks do not intersect (disjoint write paths).
3. Required input interfaces or shared contracts are already frozen and tested.
4. Concurrency does not cause database or shared state race conditions.

If any check fails, execution immediately falls back to sequential execution.

### Structured Task Handoff Protocol
Agents do not communicate via freeform chatter. All handoffs must be serialized JSON payloads matching `templates/handoff_template.json` containing:
- Sender agent ID and target agent ID.
- Associated Task ID and Workflow ID.
- Attached artifact paths and hashes.
- Executed verification commands and status.
- Remaining risks or caveats.
