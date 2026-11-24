"""Structured Handoff Protocol for Agentic Software Factory V3.
Enforces contract-driven, auditable transfers between specialist agents.
"""
from typing import Dict, List, Any, Optional
from datetime import datetime, timezone
import json

class HandoffPayload:
    """Represents a validated handoff between two agents."""

    def __init__(
        self,
        sender_agent: str,
        receiver_agent: str,
        task_id: str,
        workflow_id: str,
        artifacts: List[Dict[str, str]],
        verification_status: str,
        evidence_summary: str,
        risks_and_caveats: List[str],
        state_transition: str
    ):
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.sender_agent = sender_agent
        self.receiver_agent = receiver_agent
        self.task_id = task_id
        self.workflow_id = workflow_id
        self.artifacts = artifacts
        self.verification_status = verification_status
        self.evidence_summary = evidence_summary
        self.risks_and_caveats = risks_and_caveats
        self.state_transition = state_transition

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "sender_agent": self.sender_agent,
            "receiver_agent": self.receiver_agent,
            "task_id": self.task_id,
            "workflow_id": self.workflow_id,
            "artifacts": self.artifacts,
            "verification_status": self.verification_status,
            "evidence_summary": self.evidence_summary,
            "risks_and_caveats": self.risks_and_caveats,
            "state_transition": self.state_transition
        }

    def serialize(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

class HandoffProtocol:
    """Protocol verifier for agent handoffs."""

    @classmethod
    def validate_handoff(cls, payload_data: Dict[str, Any]) -> bool:
        """Verify that handoff contains all mandatory structured fields."""
        required_fields = [
            "sender_agent",
            "receiver_agent",
            "task_id",
            "artifacts",
            "verification_status",
            "evidence_summary"
        ]
        for field in required_fields:
            if field not in payload_data or payload_data[field] is None:
                raise ValueError(f"Handoff validation failed: missing field '{field}'")

        if not isinstance(payload_data.get("artifacts"), list):
            raise ValueError("Handoff validation failed: 'artifacts' must be an array")

        return True
