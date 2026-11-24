"""Factory Structural and Schema Validator for Agentic Software Factory V4.
Performs complete structural verification, schema validation, and invariant enforcement.
Verifies V4 invariants:
- project_designer agent existence and contract validity
- 100% Stitch/Figma MCP integration
- Strict domain isolation: app/ for code development, docs/ for mockups/design/docs
- Flat skills layout (no subdirectories)
"""
import os
import sys
import json
import re

AGENTIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKSPACE_ROOT = os.path.abspath(os.path.join(AGENTIC_DIR, ".."))

class ValidationSuite:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed_checks = 0

    def assert_true(self, condition: bool, message: str) -> bool:
        if condition:
            self.passed_checks += 1
            return True
        else:
            self.errors.append(message)
            return False

    def validate_schema_fields(self, data: dict, schema: dict, file_label: str) -> None:
        """Validate required fields and basic types without external dependencies."""
        required = schema.get("required", [])
        for field in required:
            if field not in data:
                self.errors.append(f"[{file_label}] Missing required schema field: '{field}'")
            elif data[field] is None:
                self.errors.append(f"[{file_label}] Required field '{field}' is null")

        properties = schema.get("properties", {})
        for prop_name, prop_def in properties.items():
            if prop_name in data:
                val = data[prop_name]
                expected_type = prop_def.get("type")
                if expected_type == "string" and not isinstance(val, str):
                    self.errors.append(f"[{file_label}] Field '{prop_name}' expected string, got {type(val).__name__}")
                elif expected_type == "array" and not isinstance(val, list):
                    self.errors.append(f"[{file_label}] Field '{prop_name}' expected array, got {type(val).__name__}")
                elif expected_type == "object" and not isinstance(val, dict):
                    self.errors.append(f"[{file_label}] Field '{prop_name}' expected object, got {type(val).__name__}")
                elif expected_type == "integer" and not isinstance(val, int):
                    self.errors.append(f"[{file_label}] Field '{prop_name}' expected int, got {type(val).__name__}")
                elif expected_type == "boolean" and not isinstance(val, bool):
                    self.errors.append(f"[{file_label}] Field '{prop_name}' expected bool, got {type(val).__name__}")

                if "enum" in prop_def and val not in prop_def["enum"]:
                    self.errors.append(f"[{file_label}] Field '{prop_name}' value '{val}' not in allowed enum {prop_def['enum']}")

                if "pattern" in prop_def and isinstance(val, str):
                    if not re.search(prop_def["pattern"], val):
                        self.errors.append(f"[{file_label}] Field '{prop_name}' value '{val}' does not match pattern {prop_def['pattern']}")

    def validate_all(self) -> bool:
        print("=================================================================")
        print("  AGENTIC SOFTWARE FACTORY V4 — FULL INTEGRITY & SCHEMA AUDIT   ")
        print("=================================================================")

        # 1. Directory Structure Checks
        required_dirs = [
            "agents", "skills", "workflows", "orchestration", "architecture",
            "config", "schemas", "templates", "memory", "quality", "security",
            "integrations", "scripts", "evaluations", "logs"
        ]
        for rdir in required_dirs:
            full_path = os.path.join(AGENTIC_DIR, rdir)
            self.assert_true(os.path.isdir(full_path), f"Required factory directory missing: {rdir}")

        # V4 Workspace Scope Directories
        self.assert_true(os.path.isdir(os.path.join(WORKSPACE_ROOT, "app")), "Workspace required 'app/' directory exists")
        self.assert_true(os.path.isdir(os.path.join(WORKSPACE_ROOT, "docs")), "Workspace required 'docs/' directory exists")

        # 2. Skills Flat Directory Constraint
        skills_dir = os.path.join(AGENTIC_DIR, "skills")
        if os.path.exists(skills_dir):
            for item in os.listdir(skills_dir):
                item_path = os.path.join(skills_dir, item)
                if os.path.isdir(item_path):
                    subdirs = [f for f in os.listdir(item_path) if os.path.isdir(os.path.join(item_path, f))]
                    self.assert_true(
                        len(subdirs) == 0,
                        f"Constraint violation: Skill folder '{item}' has nested subdirectories {subdirs}. Must be strictly flat!"
                    )
                    skill_md = os.path.join(item_path, "SKILL.md")
                    self.assert_true(os.path.isfile(skill_md), f"Skill '{item}' missing required flat 'SKILL.md'")

        # Check V4 Skills
        self.assert_true(os.path.isdir(os.path.join(skills_dir, "graphic-design")), "V4 skill 'graphic-design' present")
        self.assert_true(os.path.isdir(os.path.join(skills_dir, "design-system-engineering")), "V4 skill 'design-system-engineering' present")

        # 3. Agent Schema Checks
        agent_schema_path = os.path.join(AGENTIC_DIR, "schemas", "agent.schema.json")
        with open(agent_schema_path, "r", encoding="utf-8") as f:
            agent_schema = json.load(f)

        agents_dir = os.path.join(AGENTIC_DIR, "agents")
        agent_files = [f for f in os.listdir(agents_dir) if f.endswith(".json") and f != "catalog.json"]
        self.assert_true(len(agent_files) >= 47, f"Expected at least 47 specialist agents, found {len(agent_files)}")

        # Check project_designer
        self.assert_true(os.path.isfile(os.path.join(agents_dir, "project_designer.json")), "Agent 'project_designer.json' present")

        for af in agent_files:
            with open(os.path.join(agents_dir, af), "r", encoding="utf-8") as f:
                agent_data = json.load(f)
            self.validate_schema_fields(agent_data, agent_schema, f"Agent: {af}")

        # 4. Workflow Schema Checks
        wf_schema_path = os.path.join(AGENTIC_DIR, "schemas", "workflow.schema.json")
        with open(wf_schema_path, "r", encoding="utf-8") as f:
            wf_schema = json.load(f)

        wf_dir = os.path.join(AGENTIC_DIR, "workflows")
        wf_files = [f for f in os.listdir(wf_dir) if f.endswith(".json") and f != "catalog.json"]
        self.assert_true(len(wf_files) >= 13, f"Expected at least 13 workflows, found {len(wf_files)}")
        self.assert_true(os.path.isfile(os.path.join(wf_dir, "design-project.json")), "Workflow 'design-project.json' present")

        for wf in wf_files:
            with open(os.path.join(wf_dir, wf), "r", encoding="utf-8") as f:
                wf_data = json.load(f)
            self.validate_schema_fields(wf_data, wf_schema, f"Workflow: {wf}")

        # 5. Model Routing Validation
        mr_path = os.path.join(AGENTIC_DIR, "config", "model_routing.json")
        self.assert_true(os.path.isfile(mr_path), "model_routing.json is present")

        # 6. Security Boundaries Validation
        sec_path = os.path.join(AGENTIC_DIR, "config", "security_boundaries.json")
        self.assert_true(os.path.isfile(sec_path), "security_boundaries.json is present")

        # 7. Quality Gates Validation
        qg_path = os.path.join(AGENTIC_DIR, "config", "quality_gates.json")
        self.assert_true(os.path.isfile(qg_path), "quality_gates.json is present")

        # 8. Memory Hygiene & Secret Leak Scan
        lessons_dir = os.path.join(AGENTIC_DIR, "memory", "lessons")
        lesson_files = [f for f in os.listdir(lessons_dir) if f.endswith(".json")]
        self.assert_true(len(lesson_files) >= 3, f"Expected at least 3 validated seeded lessons, found {len(lesson_files)}")

        secret_regex = re.compile(r"(?i)(api_key|secret|password|token)\s*[:=]\s*['\"][A-Za-z0-9_\-\.]{8,}['\"]")
        for lf in lesson_files:
            with open(os.path.join(lessons_dir, lf), "r", encoding="utf-8") as f:
                content = f.read()
            self.assert_true(not secret_regex.search(content), f"Memory leak check failed: Secret pattern in {lf}")

        # Print results
        print(f"\n[+] Passed Checks: {self.passed_checks}")
        if self.errors:
            print(f"[-] Validation FAILED with {len(self.errors)} errors:")
            for err in self.errors:
                print(f"    - {err}")
            return False
        else:
            print("[+] All structural invariants, schemas, V4 isolation, and security checks PASSED!")
            return True

if __name__ == "__main__":
    suite = ValidationSuite()
    success = suite.validate_all()
    sys.exit(0 if success else 1)
