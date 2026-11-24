"""Bounded Recovery Manager for Agentic Software Factory V3.
Enforces deterministic error recovery, root-cause diagnosis, retry limits, and escalation.
"""
from typing import Dict, Any, Optional, List
from enum import Enum
from datetime import datetime, timezone

class RecoveryDecision(str, Enum):
    RETRY_SCOPED = "RETRY_SCOPED"
    ESCALATE_TO_HUMAN = "ESCALATE_TO_HUMAN"
    REPLAN_SUBGRAPH = "REPLAN_SUBGRAPH"
    ABORT_BRANCH = "ABORT_BRANCH"

class RecoveryManager:
    """Manages bounded task recovery and prevents infinite retry loops."""

    DEFAULT_MAX_RETRIES = 3

    def __init__(self, default_max_retries: int = DEFAULT_MAX_RETRIES):
        self.default_max_retries = default_max_retries
        self.failure_log: List[Dict[str, Any]] = []

    def evaluate_failure(
        self,
        task_data: Dict[str, Any],
        error_message: str,
        stack_trace: Optional[str] = None
    ) -> Dict[str, Any]:
        """Analyze a failure and determine whether to retry or escalate."""
        current_retries = task_data.get("retry_count", 0)
        max_retries = task_data.get("max_retries", self.default_max_retries)

        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "task_id": task_data.get("task_id"),
            "agent": task_data.get("assigned_agent"),
            "retry_attempt": current_retries + 1,
            "max_retries": max_retries,
            "error_message": error_message,
            "stack_trace": stack_trace
        }
        self.failure_log.append(record)

        # Check if retry budget is exhausted
        if current_retries >= max_retries:
            return {
                "decision": RecoveryDecision.ESCALATE_TO_HUMAN.value,
                "reason": f"Retry budget exhausted ({current_retries}/{max_retries} retries used).",
                "record": record,
                "action": "HALT_TASK_AND_REQUEST_HUMAN_APPROVAL"
            }

        # Check for non-recoverable errors (e.g. security violations, destructive ops blocked)
        if "SECURITY_VIOLATION" in error_message or "AUTHORIZATION_REQUIRED" in error_message:
            return {
                "decision": RecoveryDecision.ESCALATE_TO_HUMAN.value,
                "reason": "Security boundary encountered or explicit authorization required.",
                "record": record,
                "action": "REQUIRE_HUMAN_SIGN_OFF"
            }

        # Otherwise, bounded scoped retry is permissible
        return {
            "decision": RecoveryDecision.RETRY_SCOPED.value,
            "reason": f"Retry permitted (attempt {current_retries + 1} of {max_retries}).",
            "record": record,
            "action": "APPLY_SCOPED_FIX_AND_REVERIFY"
        }
