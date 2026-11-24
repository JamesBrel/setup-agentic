"""Workflow generator for Agentic Software Factory V3.
Produces all 12 canonical workflows conforming to workflow.schema.json.
"""
import os
import json

WORKFLOWS_DIR = os.path.join(os.path.dirname(__file__), "..", "workflows")
os.makedirs(WORKFLOWS_DIR, exist_ok=True)

workflows_data = [
    {
        "id": "new-project-creation",
        "name": "New Project Creation (Mode A Greenfield)",
        "description": "End-to-end 20-stage engineering lifecycle for creating a new software product from conception to release.",
        "operating_mode": "GREENFIELD",
        "trigger_conditions": [
            "User requests greenfield software creation from scratch",
            "Command: /new-project or !new-project",
            "CLI invocation: run_workflow.py --workflow new-project-creation"
        ],
        "required_agents": [
            "chief-orchestrator", "product-strategist", "business-analyst", "requirements-engineer",
            "prd-architect", "trd-architect", "principal-software-architect", "database-architect",
            "api-architect", "ui-ux-designer", "task-planning", "agent-coordination",
            "frontend-developer", "backend-developer", "database-engineer", "integration-engineer",
            "unit-testing", "qa-engineer", "security-auditor", "performance-engineer",
            "documentation-engineer", "release-manager"
        ],
        "input_artifacts": ["user_initial_brief"],
        "execution_stages": [
            {
                "stage_id": "STAGE-01-DISCOVERY",
                "name": "Idea Discovery and Product Vision",
                "order": 1,
                "agent": "product-strategist",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["user_initial_brief"],
                "outputs": ["product_vision.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-02-BUSINESS-ANALYSIS",
                "name": "Business Process & Persona Modeling",
                "order": 2,
                "agent": "business-analyst",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["product_vision.md"],
                "outputs": ["business_analysis.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-03-REQUIREMENTS",
                "name": "Requirements Elicitation and Acceptance Criteria",
                "order": 3,
                "agent": "requirements-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["business_analysis.md"],
                "outputs": ["requirements_matrix.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-04-PRD-GENERATION",
                "name": "PRD Authoring and Formalization",
                "order": 4,
                "agent": "prd-architect",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["requirements_matrix.json", "product_vision.md"],
                "outputs": ["docs/PRD.md", ".agentic/memory/prd.json"],
                "quality_gate_id": "GATE-REQ-001"
            },
            {
                "stage_id": "STAGE-05-TECHNICAL-RESEARCH",
                "name": "Technology Stack Research & Benchmarks",
                "order": 5,
                "agent": "technical-research",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/memory/prd.json"],
                "outputs": ["docs/TECH_EVALUATION.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-06-TRD-ARCHITECTURE",
                "name": "TRD Authoring and Traceability Mapping",
                "order": 6,
                "agent": "trd-architect",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/memory/prd.json", "docs/TECH_EVALUATION.md"],
                "outputs": ["docs/TRD.md", ".agentic/memory/trd.json"],
                "quality_gate_id": "GATE-ARCH-002"
            },
            {
                "stage_id": "STAGE-07-DATABASE-API-DESIGN",
                "name": "Database Schema and API Contract Design",
                "order": 7,
                "agent": "database-architect",
                "execution_mode": "PARALLEL",
                "parallel_group": "DESIGN_SLICE",
                "inputs": [".agentic/memory/trd.json"],
                "outputs": ["docs/DATABASE_SCHEMA.md", "docs/openapi.yaml"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-08-UIUX-SPEC",
                "name": "UI/UX Tokens and User Journey Specifications",
                "order": 8,
                "agent": "ui-ux-designer",
                "execution_mode": "PARALLEL",
                "parallel_group": "DESIGN_SLICE",
                "inputs": ["docs/PRD.md"],
                "outputs": ["docs/UI_UX_SPECIFICATION.md", "design/tokens.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-09-TASK-PLANNING",
                "name": "Task Decomposition and DAG Compilation",
                "order": 9,
                "agent": "task-planning",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/memory/trd.json", "docs/DATABASE_SCHEMA.md", "docs/openapi.yaml"],
                "outputs": [".agentic/orchestration/task_dag.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-10-DATABASE-SCAFFOLD",
                "name": "Database Migration Implementation",
                "order": 10,
                "agent": "database-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["docs/DATABASE_SCHEMA.md"],
                "outputs": ["migrations/", "seeds/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-11-BACKEND-DEV",
                "name": "Backend Services & API Implementation",
                "order": 11,
                "agent": "backend-developer",
                "execution_mode": "PARALLEL",
                "parallel_group": "DEV_SLICE",
                "inputs": ["docs/BACKEND_SPEC.md", "docs/openapi.yaml", "migrations/"],
                "outputs": ["src/domain/", "src/infrastructure/", "src/interfaces/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-12-FRONTEND-DEV",
                "name": "Frontend Web / Mobile Implementation",
                "order": 12,
                "agent": "frontend-developer",
                "execution_mode": "PARALLEL",
                "parallel_group": "DEV_SLICE",
                "inputs": ["docs/FRONTEND_SPEC.md", "design/tokens.json", "docs/openapi.yaml"],
                "outputs": ["src/components/", "src/pages/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-13-INTEGRATION",
                "name": "Subsystem Wiring and Adapter Binding",
                "order": 13,
                "agent": "integration-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["src/integrations/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-14-UNIT-TESTING",
                "name": "Unit and Mock Test Execution",
                "order": 14,
                "agent": "unit-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["tests/unit/", ".agentic/logs/unit_tests.log"],
                "quality_gate_id": "GATE-CODE-003"
            },
            {
                "stage_id": "STAGE-15-SECURITY-AUDIT",
                "name": "SAST, Vulnerability Scan and Secret Audit",
                "order": 15,
                "agent": "security-auditor",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/", "package.json"],
                "outputs": ["docs/SECURITY_AUDIT.md", ".agentic/logs/security_findings.json"],
                "quality_gate_id": "GATE-SEC-004"
            },
            {
                "stage_id": "STAGE-16-PERFORMANCE-TEST",
                "name": "Performance and Latency Profiling",
                "order": 16,
                "agent": "performance-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["docs/PERFORMANCE_REPORT.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-17-DOCUMENTATION",
                "name": "Developer Guides and Synchronized API Docs",
                "order": 17,
                "agent": "documentation-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/", "docs/PRD.md", "docs/TRD.md"],
                "outputs": ["README.md", "docs/DEVELOPER_GUIDE.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "STAGE-18-RELEASE-PREPARATION",
                "name": "Release Packaging, SemVer and Final Signoff",
                "order": 18,
                "agent": "release-manager",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/"],
                "outputs": ["CHANGELOG.md", "release_manifest.json"],
                "quality_gate_id": "GATE-REL-005"
            }
        ],
        "quality_gates": ["GATE-REQ-001", "GATE-ARCH-002", "GATE-CODE-003", "GATE-SEC-004", "GATE-REL-005"],
        "failure_handling": {
            "retry_limit": 3,
            "fallback_action": "RETRY_STAGE_WITH_ROOT_CAUSE_ANALYSIS",
            "escalation_target": "chief-orchestrator"
        },
        "completion_criteria": [
            "All 18 execution stages pass without error",
            "All 5 Quality Gates signed off with verifiable evidence",
            "Release package generated and checksummed"
        ],
        "expected_deliverables": [
            "docs/PRD.md", "docs/TRD.md", "src/", "tests/",
            "docs/SECURITY_AUDIT.md", "CHANGELOG.md", "release_manifest.json"
        ]
    },
    {
        "id": "existing-project-onboarding",
        "name": "Existing Project Onboarding (Mode B Intelligence)",
        "description": "Comprehensive autonomous repository discovery, architectural profiling, test baselining, and user diff preservation.",
        "operating_mode": "EXISTING_PROJECT",
        "trigger_conditions": [
            "User points factory to an existing software repository",
            "Command: /adopt-project or !adopt-project",
            "CLI invocation: run_workflow.py --workflow existing-project-onboarding"
        ],
        "required_agents": [
            "chief-orchestrator", "principal-software-architect", "technical-research",
            "qa-engineer", "security-auditor", "knowledge-manager"
        ],
        "input_artifacts": ["workspace_root"],
        "execution_stages": [
            {
                "stage_id": "ONBOARD-01-GIT-STATUS",
                "name": "Git Status & User Diff Preservation",
                "order": 1,
                "agent": "chief-orchestrator",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["workspace_root"],
                "outputs": [".agentic/memory/user_uncommitted_diff.patch"],
                "quality_gate_id": None
            },
            {
                "stage_id": "ONBOARD-02-STRUCTURE-SCAN",
                "name": "Repository Tree & Dependency Discovery",
                "order": 2,
                "agent": "technical-research",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["workspace_root"],
                "outputs": [".agentic/memory/raw_repo_inventory.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "ONBOARD-03-ARCH-PROFILING",
                "name": "Architectural Pattern & Entry Point Mapping",
                "order": 3,
                "agent": "principal-software-architect",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/memory/raw_repo_inventory.json"],
                "outputs": [".agentic/memory/project_profile.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "ONBOARD-04-BASELINE-VERIFY",
                "name": "Baseline Build & Test Execution",
                "order": 4,
                "agent": "qa-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/memory/project_profile.json"],
                "outputs": [".agentic/logs/baseline_test_results.log"],
                "quality_gate_id": None
            },
            {
                "stage_id": "ONBOARD-05-SECURITY-BASELINE",
                "name": "Baseline Dependency & Vulnerability Scan",
                "order": 5,
                "agent": "security-auditor",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["workspace_root"],
                "outputs": ["docs/INITIAL_SECURITY_BASELINE.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "ONBOARD-06-MEMORY-INDEX",
                "name": "Index Project Profile in Memory",
                "order": 6,
                "agent": "knowledge-manager",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/memory/project_profile.json"],
                "outputs": ["docs/PROJECT_ONBOARDING_SUMMARY.md"],
                "quality_gate_id": None
            }
        ],
        "quality_gates": [],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "RECORD_PARTIAL_PROFILE_AND_NOTIFY",
            "escalation_target": "chief-orchestrator"
        },
        "completion_criteria": [
            ".agentic/memory/project_profile.json conforms to project_profile.schema.json",
            "User uncommitted diff is preserved and isolated",
            "Baseline build and test status documented"
        ],
        "expected_deliverables": [
            ".agentic/memory/project_profile.json",
            "docs/PROJECT_ONBOARDING_SUMMARY.md",
            "docs/INITIAL_SECURITY_BASELINE.md"
        ]
    },
    {
        "id": "feature-development",
        "name": "Targeted Feature Development",
        "description": "Scoped feature addition adhering to existing architectural invariants and contracts.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "User requests new feature in greenfield or brownfield project",
            "Command: /add-new-features or !add-new-features"
        ],
        "required_agents": [
            "requirements-engineer", "task-planning", "agent-coordination",
            "backend-developer", "frontend-developer", "unit-testing",
            "code-reviewer", "qa-engineer"
        ],
        "input_artifacts": ["feature_request.md", ".agentic/memory/project_profile.json"],
        "execution_stages": [
            {
                "stage_id": "FEAT-01-REQUIREMENTS",
                "name": "Feature Acceptance Criteria Definition",
                "order": 1,
                "agent": "requirements-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["feature_request.md"],
                "outputs": ["feature_spec.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "FEAT-02-TASK-PLANNING",
                "name": "Task Plan & Path Boundary Definition",
                "order": 2,
                "agent": "task-planning",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["feature_spec.json"],
                "outputs": [".agentic/orchestration/feature_tasks.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "FEAT-03-DEV",
                "name": "Scoped Feature Implementation",
                "order": 3,
                "agent": "backend-developer",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/orchestration/feature_tasks.json"],
                "outputs": ["src/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "FEAT-04-UNIT-TESTS",
                "name": "Unit & Integration Test Addition",
                "order": 4,
                "agent": "unit-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["tests/"],
                "quality_gate_id": "GATE-CODE-003"
            },
            {
                "stage_id": "FEAT-05-CODE-REVIEW",
                "name": "Code Review and Invariant Check",
                "order": 5,
                "agent": "code-reviewer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["git_diff"],
                "outputs": [".agentic/logs/feature_review.json"],
                "quality_gate_id": None
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 3,
            "fallback_action": "REVERT_DIFF_AND_REPLAN",
            "escalation_target": "task-planning"
        },
        "completion_criteria": [
            "All new acceptance criteria satisfied with 100% passing tests",
            "Zero regressions in existing test suite",
            "Code review approved"
        ],
        "expected_deliverables": [
            "src/ modified files", "tests/ new test cases", ".agentic/logs/feature_review.json"
        ]
    },
    {
        "id": "bug-fixing",
        "name": "Autonomous Root-Cause Bug Fixing",
        "description": "Reproduce defect with failing test, isolate root cause, apply surgical fix, verify regression prevention, and record lesson.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "Bug report or failing test identified",
            "Command: /fix-bug or !fix-bug"
        ],
        "required_agents": [
            "unit-testing", "backend-developer", "code-reviewer", "learning-improvement"
        ],
        "input_artifacts": ["bug_report.md"],
        "execution_stages": [
            {
                "stage_id": "BUG-01-REPRODUCE",
                "name": "Reproduction Test Case Creation (Red)",
                "order": 1,
                "agent": "unit-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["bug_report.md"],
                "outputs": ["tests/reproduction_test.py"],
                "quality_gate_id": None
            },
            {
                "stage_id": "BUG-02-ROOT-CAUSE-FIX",
                "name": "Root Cause Identification and Surgical Fix",
                "order": 2,
                "agent": "backend-developer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["tests/reproduction_test.py"],
                "outputs": ["src/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "BUG-03-VERIFICATION",
                "name": "Regression Test Execution (Green)",
                "order": 3,
                "agent": "unit-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": [".agentic/logs/bug_fix_verification.log"],
                "quality_gate_id": "GATE-CODE-003"
            },
            {
                "stage_id": "BUG-04-LESSON-CAPTURE",
                "name": "Validated Lesson Recording",
                "order": 4,
                "agent": "learning-improvement",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/bug_fix_verification.log"],
                "outputs": [".agentic/memory/lessons/"],
                "quality_gate_id": None
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 3,
            "fallback_action": "REVERT_AND_RETRY_WITH_ALTERNATIVE_HYPOTHESIS",
            "escalation_target": "chief-orchestrator"
        },
        "completion_criteria": [
            "Reproduction test now passes consistently",
            "Zero regressions in baseline test suite",
            "Validated lesson recorded in .agentic/memory/lessons/"
        ],
        "expected_deliverables": [
            "Fixed source files", "Reproduction test case", ".agentic/memory/lessons/LESSON-*.json"
        ]
    },
    {
        "id": "refactoring",
        "name": "Behavior-Preserving Refactoring",
        "description": "Improve code architecture, reduce cyclomatic complexity, and adhere to SOLID principles without modifying observable behavior.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "Technical debt alert or code smell detected",
            "User requests refactoring of designated modules"
        ],
        "required_agents": [
            "principal-software-architect", "backend-developer", "unit-testing", "code-reviewer"
        ],
        "input_artifacts": ["refactor_scope.json"],
        "execution_stages": [
            {
                "stage_id": "REF-01-BASELINE-TESTS",
                "name": "Characterization Test Verification",
                "order": 1,
                "agent": "unit-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["refactor_scope.json"],
                "outputs": [".agentic/logs/characterization_baseline.log"],
                "quality_gate_id": None
            },
            {
                "stage_id": "REF-02-REFACTOR-APPLY",
                "name": "Stepwise Micro-Refactoring Execution",
                "order": 2,
                "agent": "backend-developer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["refactor_scope.json"],
                "outputs": ["src/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "REF-03-VERIFICATION",
                "name": "Behavioral Equivalence Verification",
                "order": 3,
                "agent": "unit-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": [".agentic/logs/refactor_verification.log"],
                "quality_gate_id": "GATE-CODE-003"
            },
            {
                "stage_id": "REF-04-REVIEW",
                "name": "Architecture & Complexity Review",
                "order": 4,
                "agent": "code-reviewer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["git_diff"],
                "outputs": [".agentic/logs/refactor_review.json"],
                "quality_gate_id": None
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "REVERT_TO_LAST_GREEN_COMMIT",
            "escalation_target": "principal-software-architect"
        },
        "completion_criteria": [
            "100% of characterization tests pass without divergence",
            "Cyclomatic complexity reduced",
            "Zero external API contract changes"
        ],
        "expected_deliverables": [
            "Refactored source files", ".agentic/logs/refactor_review.json"
        ]
    },
    {
        "id": "framework-migration",
        "name": "Framework and Runtime Migration",
        "description": "Systematic migration across major framework or language versions using the Strangler Fig pattern.",
        "operating_mode": "EXISTING_PROJECT",
        "trigger_conditions": [
            "Language or framework version reaching end-of-life",
            "User requests major framework upgrade"
        ],
        "required_agents": [
            "principal-software-architect", "technical-research", "backend-developer",
            "unit-testing", "qa-engineer"
        ],
        "input_artifacts": ["migration_brief.md"],
        "execution_stages": [
            {
                "stage_id": "MIG-01-BREAKING-CHANGES",
                "name": "Breaking Changes & Deprecation Analysis",
                "order": 1,
                "agent": "technical-research",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["migration_brief.md"],
                "outputs": ["docs/MIGRATION_ANALYSIS.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "MIG-02-STRANGLER-ADAPTER",
                "name": "Compatibility Layer / Shims Implementation",
                "order": 2,
                "agent": "principal-software-architect",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["docs/MIGRATION_ANALYSIS.md"],
                "outputs": ["src/adapters/compat/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "MIG-03-INCREMENTAL-UPGRADE",
                "name": "Module-by-Module Code Modernization",
                "order": 3,
                "agent": "backend-developer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/adapters/compat/"],
                "outputs": ["src/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "MIG-04-REGRESSION-SUITE",
                "name": "Full Test Matrix Regression Verification",
                "order": 4,
                "agent": "qa-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": [".agentic/logs/migration_regression.log"],
                "quality_gate_id": "GATE-CODE-003"
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "ROLLBACK_MIGRATION_SLICE",
            "escalation_target": "principal-software-architect"
        },
        "completion_criteria": [
            "All modules compile on new target runtime",
            "Zero deprecation warnings emitted",
            "100% of regression tests pass"
        ],
        "expected_deliverables": [
            "Updated dependency manifests", "Migrated source code", "docs/MIGRATION_ANALYSIS.md"
        ]
    },
    {
        "id": "dependency-upgrades",
        "name": "Automated Dependency Upgrades",
        "description": "Safe, non-breaking upgrade of project dependencies with lockfile verification and test validation.",
        "operating_mode": "EXISTING_PROJECT",
        "trigger_conditions": [
            "Scheduled weekly dependency refresh",
            "Security vulnerability in dependency requires patch upgrade"
        ],
        "required_agents": [
            "devops-engineer", "qa-engineer", "security-auditor"
        ],
        "input_artifacts": ["dependency_manifests"],
        "execution_stages": [
            {
                "stage_id": "DEP-01-OUTDATED-SCAN",
                "name": "Outdated Packages & CVE Discovery",
                "order": 1,
                "agent": "security-auditor",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["dependency_manifests"],
                "outputs": [".agentic/logs/outdated_dependencies.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "DEP-02-UPGRADE-EXECUTE",
                "name": "Lockfile Regeneration and Safe Update",
                "order": 2,
                "agent": "devops-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/outdated_dependencies.json"],
                "outputs": ["package-lock.json", "composer.lock", "pubspec.lock"],
                "quality_gate_id": None
            },
            {
                "stage_id": "DEP-03-BUILD-TEST",
                "name": "Build & Test Verification",
                "order": 3,
                "agent": "qa-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["package-lock.json"],
                "outputs": [".agentic/logs/dependency_test_run.log"],
                "quality_gate_id": "GATE-CODE-003"
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "REVERT_LOCKFILE_CHANGES",
            "escalation_target": "devops-engineer"
        },
        "completion_criteria": [
            "Lockfiles regenerated with compatible versions",
            "Full test suite passes green",
            "Zero new vulnerabilities introduced"
        ],
        "expected_deliverables": [
            "Updated lockfiles", ".agentic/logs/dependency_test_run.log"
        ]
    },
    {
        "id": "security-remediation",
        "name": "Security Vulnerability Remediation",
        "description": "Urgent patching of SAST, SCA, or secret leak findings to meet GATE-SEC-004 standards.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "GATE-SEC-004 failure",
            "Command: /security-audit or !security-audit"
        ],
        "required_agents": [
            "security-auditor", "security-architect", "backend-developer", "unit-testing"
        ],
        "input_artifacts": [".agentic/logs/security_findings.json"],
        "execution_stages": [
            {
                "stage_id": "SEC-01-TRIAGE",
                "name": "Vulnerability Triage & Exploitability Analysis",
                "order": 1,
                "agent": "security-architect",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/security_findings.json"],
                "outputs": ["docs/SECURITY_REMEDIATION_PLAN.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "SEC-02-PATCH",
                "name": "Security Patch Implementation",
                "order": 2,
                "agent": "backend-developer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["docs/SECURITY_REMEDIATION_PLAN.md"],
                "outputs": ["src/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "SEC-03-RETEST",
                "name": "SAST & Exploit Verification Rescan",
                "order": 3,
                "agent": "security-auditor",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["docs/SECURITY_AUDIT.md"],
                "quality_gate_id": "GATE-SEC-004"
            }
        ],
        "quality_gates": ["GATE-SEC-004"],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "ESCALATE_TO_SECURITY_ARCHITECT",
            "escalation_target": "chief-orchestrator"
        },
        "completion_criteria": [
            "Zero Critical or High severity vulnerabilities remaining",
            "GATE-SEC-004 passes green",
            "Regression tests confirm application functionality preserved"
        ],
        "expected_deliverables": [
            "docs/SECURITY_AUDIT.md", "Patched source code"
        ]
    },
    {
        "id": "performance-optimization",
        "name": "Performance and Latency Optimization",
        "description": "Systematic benchmarking, hotspot identification, query tuning, and verification of SLA targets.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "Latency exceeds TRD SLA thresholds",
            "Profiling indicates CPU or memory bottleneck"
        ],
        "required_agents": [
            "performance-engineer", "backend-developer", "database-engineer", "qa-engineer"
        ],
        "input_artifacts": ["performance_sla.json"],
        "execution_stages": [
            {
                "stage_id": "PERF-01-BENCHMARK-BASELINE",
                "name": "Initial Baseline Measurement & Flame Graph Capture",
                "order": 1,
                "agent": "performance-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["performance_sla.json"],
                "outputs": [".agentic/logs/perf_baseline.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "PERF-02-OPTIMIZATION-APPLY",
                "name": "Targeted Code & Query Optimization",
                "order": 2,
                "agent": "backend-developer",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/perf_baseline.json"],
                "outputs": ["src/"],
                "quality_gate_id": None
            },
            {
                "stage_id": "PERF-03-BENCHMARK-VERIFY",
                "name": "Post-Optimization Benchmark & Regression Test",
                "order": 3,
                "agent": "performance-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["docs/PERFORMANCE_REPORT.md"],
                "quality_gate_id": "GATE-CODE-003"
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "REVERT_OPTIMIZATION_IF_DEGRADED",
            "escalation_target": "performance-engineer"
        },
        "completion_criteria": [
            "Measured latency meets or exceeds TRD SLA targets",
            "Zero regressions in functional test suite",
            "docs/PERFORMANCE_REPORT.md signed off"
        ],
        "expected_deliverables": [
            "Optimized source files", "docs/PERFORMANCE_REPORT.md"
        ]
    },
    {
        "id": "testing-validation",
        "name": "Holistic Quality & Test Validation",
        "description": "Full-spectrum test execution: unit, integration, E2E, and accessibility verification.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "Pre-release quality certification",
            "Command: /review-and-test or !review-and-test"
        ],
        "required_agents": [
            "qa-engineer", "unit-testing", "integration-testing",
            "e2e-testing", "accessibility-auditor"
        ],
        "input_artifacts": ["src/"],
        "execution_stages": [
            {
                "stage_id": "VAL-01-UNIT-TESTS",
                "name": "Unit Test Suite Execution",
                "order": 1,
                "agent": "unit-testing",
                "execution_mode": "PARALLEL",
                "parallel_group": "TEST_SLICE",
                "inputs": ["src/"],
                "outputs": [".agentic/logs/unit_tests.log"],
                "quality_gate_id": None
            },
            {
                "stage_id": "VAL-02-INTEGRATION-TESTS",
                "name": "API & Integration Test Execution",
                "order": 2,
                "agent": "integration-testing",
                "execution_mode": "PARALLEL",
                "parallel_group": "TEST_SLICE",
                "inputs": ["src/"],
                "outputs": [".agentic/logs/integration_tests.log"],
                "quality_gate_id": None
            },
            {
                "stage_id": "VAL-03-A11Y-AUDIT",
                "name": "Automated Accessibility Audit",
                "order": 3,
                "agent": "accessibility-auditor",
                "execution_mode": "PARALLEL",
                "parallel_group": "TEST_SLICE",
                "inputs": ["src/"],
                "outputs": ["docs/ACCESSIBILITY_AUDIT.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "VAL-04-E2E-JOURNEYS",
                "name": "End-to-End User Journey Tests",
                "order": 4,
                "agent": "e2e-testing",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": [".agentic/logs/e2e_results.log"],
                "quality_gate_id": None
            },
            {
                "stage_id": "VAL-05-QA-SIGN-OFF",
                "name": "Quality Assurance Master Certification",
                "order": 5,
                "agent": "qa-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/"],
                "outputs": ["docs/TEST_REPORT.md"],
                "quality_gate_id": "GATE-CODE-003"
            }
        ],
        "quality_gates": ["GATE-CODE-003"],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "ISOLATE_FAILING_TESTS_AND_REPORT",
            "escalation_target": "qa-engineer"
        },
        "completion_criteria": [
            "100% of test suites pass without flaky retries",
            "Zero WCAG AA accessibility violations",
            "docs/TEST_REPORT.md generated with evidence"
        ],
        "expected_deliverables": [
            "docs/TEST_REPORT.md", "docs/ACCESSIBILITY_AUDIT.md"
        ]
    },
    {
        "id": "documentation-generation",
        "name": "Continuous Documentation Generation",
        "description": "Automated generation, synchronization, and link verification of developer guides and API docs.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "API or architecture change completed",
            "Pre-release documentation synchronization"
        ],
        "required_agents": [
            "documentation-engineer", "api-architect"
        ],
        "input_artifacts": ["src/", "docs/TRD.md"],
        "execution_stages": [
            {
                "stage_id": "DOC-01-API-GEN",
                "name": "API Reference Generation from OpenAPI Spec",
                "order": 1,
                "agent": "api-architect",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["docs/openapi.yaml"],
                "outputs": ["docs/API_DOCUMENTATION.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "DOC-02-DEV-GUIDE",
                "name": "Developer Guide & Setup Instructions",
                "order": 2,
                "agent": "documentation-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["docs/DEVELOPER_GUIDE.md", "README.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "DOC-03-LINK-CHECK",
                "name": "Markdown Linting and Link Verification",
                "order": 3,
                "agent": "documentation-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["docs/", "README.md"],
                "outputs": [".agentic/logs/doc_lint_results.log"],
                "quality_gate_id": None
            }
        ],
        "quality_gates": [],
        "failure_handling": {
            "retry_limit": 2,
            "fallback_action": "REPAIR_BROKEN_LINKS",
            "escalation_target": "documentation-engineer"
        },
        "completion_criteria": [
            "Zero broken internal links",
            "All documented commands verified executable",
            "Documentation matches current code release tag"
        ],
        "expected_deliverables": [
            "docs/DEVELOPER_GUIDE.md", "docs/API_DOCUMENTATION.md", "README.md"
        ]
    },
    {
        "id": "release-preparation",
        "name": "Release Packaging and Deployment Certification",
        "description": "Certify GATE-REL-005, calculate SemVer, generate CHANGELOG.md, package artifacts, and request human deployment approval.",
        "operating_mode": "HYBRID",
        "trigger_conditions": [
            "Milestone completion and release freeze",
            "User requests release packaging"
        ],
        "required_agents": [
            "release-manager", "cicd-engineer", "qa-engineer", "security-auditor"
        ],
        "input_artifacts": [".agentic/logs/", "git_history"],
        "execution_stages": [
            {
                "stage_id": "REL-01-GATE-AUDIT",
                "name": "Verification of All Preceding Quality Gates",
                "order": 1,
                "agent": "release-manager",
                "execution_mode": "SEQUENTIAL",
                "inputs": [".agentic/logs/"],
                "outputs": [".agentic/logs/gate_verification_manifest.json"],
                "quality_gate_id": None
            },
            {
                "stage_id": "REL-02-SEMVER-CHANGELOG",
                "name": "Semantic Versioning & CHANGELOG Generation",
                "order": 2,
                "agent": "release-manager",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["git_history"],
                "outputs": ["CHANGELOG.md", "docs/RELEASE_NOTES.md"],
                "quality_gate_id": None
            },
            {
                "stage_id": "REL-03-PACKAGING",
                "name": "Artifact Packaging & Checksum Generation",
                "order": 3,
                "agent": "cicd-engineer",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["src/"],
                "outputs": ["release_manifest.json"],
                "quality_gate_id": "GATE-REL-005"
            },
            {
                "stage_id": "REL-04-HUMAN-APPROVAL",
                "name": "Human-in-the-Loop Deployment Authorization",
                "order": 4,
                "agent": "release-manager",
                "execution_mode": "SEQUENTIAL",
                "inputs": ["release_manifest.json"],
                "outputs": [".agentic/logs/human_approval_status.json"],
                "quality_gate_id": None
            }
        ],
        "quality_gates": ["GATE-REL-005"],
        "failure_handling": {
            "retry_limit": 1,
            "fallback_action": "HALT_RELEASE_AND_ALERT_OPERATOR",
            "escalation_target": "chief-orchestrator"
        },
        "completion_criteria": [
            "All 5 Quality Gates proven with cryptographic evidence",
            "CHANGELOG.md generated according to Keep a Changelog standard",
            "Human deployment signoff obtained or queued"
        ],
        "expected_deliverables": [
            "CHANGELOG.md", "release_manifest.json", "docs/RELEASE_NOTES.md"
        ]
    }
]

catalog = {
    "total_workflows": len(workflows_data),
    "modes": {
        "GREENFIELD": [],
        "EXISTING_PROJECT": [],
        "HYBRID": []
    },
    "workflows": {}
}

for wf in workflows_data:
    wf_id = wf["id"]
    mode = wf["operating_mode"]
    file_path = os.path.join(WORKFLOWS_DIR, f"{wf_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2)
        
    catalog["modes"][mode].append(wf_id)
    catalog["workflows"][wf_id] = {
        "name": wf["name"],
        "operating_mode": mode,
        "description": wf["description"],
        "stages_count": len(wf["execution_stages"]),
        "quality_gates": wf["quality_gates"],
        "file": f".agentic/workflows/{wf_id}.json"
    }

catalog_path = os.path.join(WORKFLOWS_DIR, "catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2)

print(f"Successfully generated {len(workflows_data)} workflows and catalog at {catalog_path}")
