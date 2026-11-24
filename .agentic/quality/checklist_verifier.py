"""Quality Gate Checklist Verifier for Agentic Software Factory V3.
Evaluates gate criteria, checks evidence logs, and enforces strict quality barriers.
"""
import os
import json
from typing import Dict, List, Any, Tuple

class ChecklistVerifier:
    """Verifies compliance with Quality Gates."""

    def __init__(self, quality_dir: Optional[str] = None):
        if quality_dir is None:
            self.quality_dir = os.path.dirname(os.path.abspath(__file__))
        else:
            self.quality_dir = quality_dir
        self.criteria_dir = os.path.join(self.quality_dir, "criteria")

    def load_gate(self, gate_id: str) -> Dict[str, Any]:
        """Find and load gate definition."""
        for fname in os.listdir(self.criteria_dir):
            if fname.endswith(".json"):
                fpath = os.path.join(self.criteria_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    gate = json.load(f)
                    if gate.get("gate_id") == gate_id:
                        return gate
        raise FileNotFoundError(f"Gate criteria not found for ID: {gate_id}")

    def verify_gate(self, gate_id: str, evidence_artifacts: List[Dict[str, Any]]) -> Tuple[bool, Dict[str, Any]]:
        """Verify whether a gate passes based on supplied evidence."""
        gate = self.load_gate(gate_id)
        results = []
        overall_pass = True

        for check in gate.get("checks", []):
            check_id = check["check_id"]
            name = check["name"]
            
            # Find matching evidence
            matching_evidence = [e for e in evidence_artifacts if e.get("check_id") == check_id or e.get("type") == check.get("category")]
            passed = any(e.get("passed", False) for e in matching_evidence) if matching_evidence else False

            # In dry-run or simulated environment without live errors, record verified status
            if matching_evidence and passed:
                status = "PASSED"
            else:
                status = "FAILED"
                overall_pass = False

            results.append({
                "check_id": check_id,
                "name": name,
                "status": status,
                "required": check.get("required_result")
            })

        verdict = {
            "gate_id": gate_id,
            "name": gate.get("name"),
            "passed": overall_pass,
            "blocking": gate.get("blocking", True),
            "check_results": results
        }

        return overall_pass, verdict
