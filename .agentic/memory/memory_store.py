"""Validated Knowledge & Memory Store for Agentic Software Factory V3.
Indexes validated engineering lessons, architectural decision records (ADRs), and enterprise patterns.
"""
import os
import json
from typing import Dict, List, Any, Optional
from .sanitization import MemorySanitizer, SanitizationError

class MemoryStore:
    """Persistent storage engine for validated factory memory."""

    def __init__(self, memory_dir: Optional[str] = None):
        if memory_dir is None:
            self.memory_dir = os.path.dirname(os.path.abspath(__file__))
        else:
            self.memory_dir = memory_dir

        self.lessons_dir = os.path.join(self.memory_dir, "lessons")
        self.adrs_dir = os.path.join(self.memory_dir, "adrs")
        self.patterns_dir = os.path.join(self.memory_dir, "patterns")

        os.makedirs(self.lessons_dir, exist_ok=True)
        os.makedirs(self.adrs_dir, exist_ok=True)
        os.makedirs(self.patterns_dir, exist_ok=True)

    def store_lesson(self, lesson_data: Dict[str, Any]) -> str:
        """Sanitize and persist a validated lesson conforming to lesson.schema.json."""
        sanitized = MemorySanitizer.sanitize_record(lesson_data)
        lesson_id = sanitized["lesson_id"]

        file_path = os.path.join(self.lessons_dir, f"{lesson_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(sanitized, f, indent=2)

        return file_path

    def store_adr(self, adr_data: Dict[str, Any]) -> str:
        """Persist an Architecture Decision Record conforming to adr.schema.json."""
        adr_id = adr_data["adr_id"]
        file_path = os.path.join(self.adrs_dir, f"{adr_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(adr_data, f, indent=2)

        return file_path

    def query_lessons(self, tag: Optional[str] = None, component: Optional[str] = None) -> List[Dict[str, Any]]:
        """Query lessons by tag or component."""
        results = []
        for file_name in os.listdir(self.lessons_dir):
            if file_name.endswith(".json"):
                with open(os.path.join(self.lessons_dir, file_name), "r", encoding="utf-8") as f:
                    lesson = json.load(f)
                    if tag and tag not in lesson.get("tags", []):
                        continue
                    if component and lesson.get("technical_context", {}).get("component") != component:
                        continue
                    results.append(lesson)
        return results

    def deduplicate_lessons(self) -> int:
        """Identify and mark duplicate lessons as SUPERSEDED."""
        lessons = self.query_lessons()
        seen_problems = {}
        duplicates_count = 0

        for lesson in lessons:
            problem = lesson.get("original_problem", "").strip().lower()
            lesson_id = lesson["lesson_id"]

            if problem in seen_problems:
                # Mark as superseded
                lesson["status"] = "SUPERSEDED"
                file_path = os.path.join(self.lessons_dir, f"{lesson_id}.json")
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(lesson, f, indent=2)
                duplicates_count += 1
            else:
                seen_problems[problem] = lesson_id

        return duplicates_count
