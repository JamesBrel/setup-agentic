"""Security Boundary Guard for Agentic Software Factory V4.
Enforces autonomy boundaries, intercepting and blocking dangerous or unauthorized operations,
and enforcing strict V4 domain isolation:
- All source code and application development must reside strictly in app/.
- All design assets, Stitch/Figma mockups, logos, icons, and specifications must reside strictly in docs/.
"""
import os
import json
import re
from typing import Dict, List, Any, Tuple, Optional

class SecurityBoundaryViolation(Exception):
    """Raised when an operation breaches safety policies, domain isolation, or lacks explicit approval."""
    pass

class BoundaryGuard:
    """Intercepts and verifies commands, paths, and operations against security policies."""

    def __init__(self, config_dir: Optional[str] = None):
        if config_dir is None:
            self.config_dir = os.path.join(os.path.dirname(__file__), "..", "config")
        else:
            self.config_dir = config_dir

        policy_path = os.path.join(self.config_dir, "security_boundaries.json")
        with open(policy_path, "r", encoding="utf-8") as f:
            self.policy = json.load(f)

    def validate_command(self, command_str: str, has_human_approval: bool = False) -> Tuple[bool, str]:
        """Inspect command string for prohibited patterns."""
        prohibited = self.policy.get("strictly_prohibited_without_approval", [])

        for item in prohibited:
            op_name = item.get("operation")
            patterns = item.get("pattern", [])
            for pat in patterns:
                if re.search(re.escape(pat), command_str, re.IGNORECASE):
                    if not has_human_approval:
                        raise SecurityBoundaryViolation(
                            f"Command blocked by BoundaryGuard: Operation '{op_name}' matches prohibited pattern '{pat}'. "
                            f"Requires explicit human authorization."
                        )

        return True, "Command authorized"

    def validate_path_access(self, file_path: str, is_write: bool, allowed_paths: List[str], forbidden_paths: List[str]) -> bool:
        """Verify that the target path does not violate task boundaries."""
        norm_path = os.path.normpath(file_path).replace("\\", "/")

        # Check forbidden paths
        for forbidden in forbidden_paths:
            norm_forbidden = os.path.normpath(forbidden).replace("\\", "/")
            if norm_path.startswith(norm_forbidden):
                raise SecurityBoundaryViolation(f"Path access violation: '{file_path}' is in forbidden_paths.")

        # If writing, check allowed paths
        if is_write and allowed_paths:
            allowed = False
            for allowed_prefix in allowed_paths:
                norm_allowed = os.path.normpath(allowed_prefix).replace("\\", "/")
                if norm_path.startswith(norm_allowed) or norm_allowed in norm_path:
                    allowed = True
                    break
            if not allowed:
                raise SecurityBoundaryViolation(
                    f"Path write violation: '{file_path}' is outside designated allowed_paths {allowed_paths}."
                )

        return True

    def validate_v4_domain_isolation(self, file_path: str, operation_category: str) -> bool:
        """Enforce strict V4 domain isolation:
        - Application code & development must be inside app/
        - Design, mockups, logos, icons, and documentation must be inside docs/
        """
        norm_path = os.path.normpath(file_path).replace("\\", "/")

        # Application code operations
        if operation_category in ["CODE_DEVELOPMENT", "SOURCE_CODE", "BUILD", "IMPLEMENTATION"]:
            if not (norm_path.startswith("app/") or norm_path == "app"):
                raise SecurityBoundaryViolation(
                    f"V4 Domain Isolation Violation: Application code implementation must be written strictly inside 'app/'. Attempted: '{file_path}'"
                )

        # Design and documentation operations
        elif operation_category in ["DESIGN", "UI_UX", "STITCH", "FIGMA", "MOCKUP", "LOGO", "ICON", "DOCUMENTATION"]:
            if not (norm_path.startswith("docs/") or norm_path == "docs" or norm_path.startswith(".agentic/")):
                raise SecurityBoundaryViolation(
                    f"V4 Domain Isolation Violation: Design mockups (Stitch/Figma), logos, icons, and specifications must be written strictly inside 'docs/'. Attempted: '{file_path}'"
                )

        return True
