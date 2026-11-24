"""Catalog and Overview updater for Agentic Software Factory V4.
Integrates project_designer agent, graphic-design skill, design-system-engineering skill,
and design-project workflow.
"""
import os
import json

AGENTIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def update_agents_catalog():
    agents_dir = os.path.join(AGENTIC_DIR, "agents")
    catalog_path = os.path.join(agents_dir, "catalog.json")

    agent_files = [f for f in os.listdir(agents_dir) if f.endswith(".json") and f != "catalog.json"]
    catalog = {
        "total_agents": len(agent_files),
        "divisions": {
            "management": [],
            "product": [],
            "architecture": [],
            "development": [],
            "quality": [],
            "infrastructure": [],
            "intelligence": []
        },
        "agents": {}
    }

    for af in sorted(agent_files):
        with open(os.path.join(agents_dir, af), "r", encoding="utf-8") as f:
            agent = json.load(f)
        agent_id = agent["id"]
        division = agent["division"]
        if division in catalog["divisions"]:
            catalog["divisions"][division].append(agent_id)
        catalog["agents"][agent_id] = {
            "name": agent["name"],
            "role": agent["role"],
            "division": division,
            "model_tier": agent["model_tier"],
            "file": f".agentic/agents/{af}"
        }

    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    print(f"[+] Agents catalog updated: {catalog['total_agents']} agents.")

def update_skills_catalog():
    skills_dir = os.path.join(AGENTIC_DIR, "skills")
    catalog_path = os.path.join(skills_dir, "catalog.json")

    skill_dirs = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
    catalog = {
        "total_skills": len(skill_dirs),
        "categories": {
            "product": [],
            "architecture": [],
            "development": [],
            "quality": [],
            "infrastructure": [],
            "security": []
        },
        "skills": {}
    }

    skill_meta = {
        "graphic-design": ("architecture", "Visual identity, logo design, application icons, color palettes, and typography using Stitch/Figma MCP"),
        "design-system-engineering": ("architecture", "Complete UI/UX Design System, tokens, atomic components, and high-fidelity screen mockups via Stitch/Figma MCP")
    }

    # Load existing if available
    existing = {}
    if os.path.exists(catalog_path):
        with open(catalog_path, "r", encoding="utf-8") as f:
            existing = json.load(f).get("skills", {})

    for sd in sorted(skill_dirs):
        cat = "architecture"
        desc = "Modular engineering skill"
        if sd in existing:
            cat = existing[sd].get("category", "architecture")
            desc = existing[sd].get("description", desc)
        elif sd in skill_meta:
            cat, desc = skill_meta[sd]

        if cat in catalog["categories"]:
            catalog["categories"][cat].append(sd)
        catalog["skills"][sd] = {
            "name": sd.replace("-", " ").title(),
            "category": cat,
            "description": desc,
            "path": f".agentic/skills/{sd}/SKILL.md"
        }

    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    print(f"[+] Skills catalog updated: {catalog['total_skills']} skills.")

def update_workflows_catalog():
    wf_dir = os.path.join(AGENTIC_DIR, "workflows")
    catalog_path = os.path.join(wf_dir, "catalog.json")

    wf_files = [f for f in os.listdir(wf_dir) if f.endswith(".json") and f != "catalog.json"]
    catalog = {
        "total_workflows": len(wf_files),
        "modes": {
            "GREENFIELD": [],
            "EXISTING_PROJECT": [],
            "HYBRID": []
        },
        "workflows": {}
    }

    for wf_file in sorted(wf_files):
        with open(os.path.join(wf_dir, wf_file), "r", encoding="utf-8") as f:
            wf = json.load(f)
        wf_id = wf["id"]
        mode = wf["operating_mode"]
        if mode in catalog["modes"]:
            catalog["modes"][mode].append(wf_id)
        catalog["workflows"][wf_id] = {
            "name": wf["name"],
            "operating_mode": mode,
            "description": wf["description"],
            "stages_count": len(wf.get("execution_stages", [])),
            "quality_gates": wf.get("quality_gates", []),
            "file": f".agentic/workflows/{wf_file}"
        }

    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    print(f"[+] Workflows catalog updated: {catalog['total_workflows']} workflows.")

if __name__ == "__main__":
    update_agents_catalog()
    update_skills_catalog()
    update_workflows_catalog()
