"""Cryptographic Audit Logger for Agentic Software Factory V3.
Records all factory actions in an append-only, SHA-256 hash-chained audit log.
"""
import os
import json
import hashlib
from typing import Dict, Any, Optional
from datetime import datetime, timezone

class AuditLogger:
    """Tamper-evident audit log for factory operations."""

    def __init__(self, log_dir: Optional[str] = None):
        if log_dir is None:
            self.log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        else:
            self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.audit_file = os.path.join(self.log_dir, "audit_trail.jsonl")

    def _get_last_hash(self) -> str:
        """Read the hash of the last log entry, or return genesis hash."""
        if not os.path.exists(self.audit_file):
            return "0" * 64
        last_line = ""
        with open(self.audit_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    last_line = line
        if not last_line:
            return "0" * 64
        entry = json.loads(last_line)
        return entry.get("entry_hash", "0" * 64)

    def log_action(self, agent: str, action: str, details: Dict[str, Any], status: str = "SUCCESS") -> str:
        """Append an action entry to the chained audit trail."""
        prev_hash = self._get_last_hash()
        timestamp = datetime.now(timezone.utc).isoformat()

        raw_payload = {
            "prev_hash": prev_hash,
            "timestamp": timestamp,
            "agent": agent,
            "action": action,
            "details": details,
            "status": status
        }

        # Calculate entry hash
        payload_bytes = json.dumps(raw_payload, sort_keys=True).encode("utf-8")
        entry_hash = hashlib.sha256(payload_bytes).hexdigest()
        raw_payload["entry_hash"] = entry_hash

        with open(self.audit_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(raw_payload) + "\n")

        return entry_hash
