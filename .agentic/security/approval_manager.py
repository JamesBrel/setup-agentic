"""Human Approval Manager for Agentic Software Factory V3.
Manages authorization tokens and escalation requests for high-risk operations.
"""
import os
import json
import uuid
from typing import Dict, Any, Optional
from datetime import datetime, timezone

class ApprovalManager:
    """Handles requests and token validation for human-in-the-loop authorizations."""

    def __init__(self, log_dir: Optional[str] = None):
        if log_dir is None:
            self.log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        else:
            self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self.approvals_file = os.path.join(self.log_dir, "approvals.json")

        if not os.path.exists(self.approvals_file):
            with open(self.approvals_file, "w", encoding="utf-8") as f:
                json.dump({"pending": {}, "granted": {}}, f, indent=2)

    def request_approval(self, operation: str, description: str, requester: str) -> str:
        """Create a pending human approval ticket and return request_id."""
        request_id = f"REQ-AUTH-{uuid.uuid4().hex[:8].upper()}"
        ticket = {
            "request_id": request_id,
            "operation": operation,
            "description": description,
            "requester": requester,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "PENDING"
        }

        with open(self.approvals_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["pending"][request_id] = ticket

        with open(self.approvals_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return request_id

    def grant_approval(self, request_id: str, approver: str = "human_operator") -> str:
        """Grant approval for a pending request and generate an authorization token."""
        with open(self.approvals_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if request_id not in data["pending"]:
            raise ValueError(f"Approval request ID not found in pending list: {request_id}")

        ticket = data["pending"].pop(request_id)
        auth_token = f"AUTH-TOKEN-{uuid.uuid4().hex}"
        ticket["status"] = "GRANTED"
        ticket["approver"] = approver
        ticket["granted_at"] = datetime.now(timezone.utc).isoformat()
        ticket["auth_token"] = auth_token

        data["granted"][auth_token] = ticket

        with open(self.approvals_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return auth_token

    def verify_token(self, auth_token: str) -> bool:
        """Verify if an authorization token is valid."""
        with open(self.approvals_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return auth_token in data.get("granted", {})
