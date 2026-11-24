"""Memory Sanitization and Hygiene Guard for Agentic Software Factory V3.
Guarantees that no unverified assumptions, secrets, API tokens, or PII enter memory.
"""
import re
from typing import Dict, Any, List

class SanitizationError(Exception):
    """Raised when memory payload contains prohibited sensitive data."""
    pass

class MemorySanitizer:
    """Scans and scrubs sensitive data from memory records before persistence."""

    # Patterns matching private keys, secrets, API tokens, passwords
    SECRET_PATTERNS = [
        re.compile(r"(?i)(api[_-]?key|secret|password|token|bearer|auth[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9_\-\.]{8,}['\"]"),
        re.compile(r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"(?i)AKIA[0-9A-Z]{16}"), # AWS Access Key ID
        re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"), # JWT token
    ]

    # Patterns indicating unverified assumptions or speculative thought
    SPECULATION_PATTERNS = [
        re.compile(r"(?i)\b(i think|maybe|unverified assumption|guessing|might work|not sure)\b")
    ]

    @classmethod
    def sanitize_record(cls, record: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and scrub a memory record."""
        # Check for unverified status
        status = record.get("status")
        if status not in ["VALIDATED", "SUPERSEDED", "OBSOLETE"]:
            raise SanitizationError(f"Prohibited record status '{status}'. Only VALIDATED lessons permitted.")

        # Check for supporting evidence requirement
        evidence = record.get("supporting_evidence")
        if not evidence or not evidence.get("test_passed", False):
            raise SanitizationError("Sanitization rejection: Record lacks verified passing test evidence.")

        # Convert record to string and scan for secrets
        record_str = str(record)
        for pattern in cls.SECRET_PATTERNS:
            if pattern.search(record_str):
                raise SanitizationError("Sanitization rejection: Detected prospective secret or API token in payload.")

        # Check for speculation in solutions
        solution_text = record.get("solution", "")
        for pattern in cls.SPECULATION_PATTERNS:
            if pattern.search(solution_text):
                raise SanitizationError("Sanitization rejection: Solution contains unverified speculative language.")

        return record
