"""Model Routing Abstraction for Agentic Software Factory V3.
Maps abstract capability tiers (tier_reasoning, tier_standard, tier_fast) to provider configurations.
Ensures portability across Gemini, Claude, OpenAI GPT, and local models without hardcoded model IDs.
"""
import os
import json
from typing import Dict, Any, Optional

class ModelRouter:
    """Dynamically resolves model tiers and parameters according to the active provider."""

    DEFAULT_PROVIDER = "gemini"

    def __init__(self, config_dir: Optional[str] = None):
        if config_dir is None:
            self.config_dir = os.path.join(os.path.dirname(__file__), "..", "config")
        else:
            self.config_dir = config_dir

        config_path = os.path.join(self.config_dir, "model_routing.json")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

        # Allow environment variable override: FACTORY_AI_PROVIDER
        env_provider = os.environ.get("FACTORY_AI_PROVIDER")
        if env_provider and env_provider in self.config.get("providers", {}):
            self.active_provider = env_provider
        else:
            self.active_provider = self.config.get("active_provider", self.DEFAULT_PROVIDER)

    def set_active_provider(self, provider_name: str) -> None:
        """Switch active model provider (gemini, claude, gpt)."""
        providers = self.config.get("providers", {})
        if provider_name not in providers:
            raise ValueError(f"Unknown provider '{provider_name}'. Available: {list(providers.keys())}")
        self.active_provider = provider_name
        self.config["active_provider"] = provider_name
        # Persist update
        config_path = os.path.join(self.config_dir, "model_routing.json")
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def resolve_model_for_tier(self, tier: str) -> Dict[str, Any]:
        """Resolve model alias and parameters for a designated tier."""
        provider_data = self.config.get("providers", {}).get(self.active_provider, {})
        if tier not in provider_data:
            # Fallback to standard tier if requested tier is missing
            tier = "tier_standard"
        return provider_data.get(tier, {})

    def resolve_model_for_task(self, task_type: str) -> Dict[str, Any]:
        """Resolve model tier and configuration based on task type complexity."""
        routing_rules = self.config.get("routing_rules", [])
        required_tier = "tier_standard"

        for rule in routing_rules:
            if rule.get("task_type") == task_type:
                required_tier = rule.get("required_tier", "tier_standard")
                break

        return self.resolve_model_for_tier(required_tier)
