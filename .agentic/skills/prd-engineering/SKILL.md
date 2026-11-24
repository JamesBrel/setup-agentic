# Skill: PRD Engineering (`prd-engineering`)

## 1. Purpose
Standardized authoring, structuring, and schema validation of Product Requirements Documents.

## 2. Activation Conditions
- Completion of requirements engineering discovery
- Greenfield project kickoff (Mode A)
- Major architectural addition or product line expansion

## 3. Required Knowledge
- PRD structure and lifecycle states
- User journey mapping and scenario modeling
- Success metrics definition (North Star, Pirate Metrics, OKRs)
- JSON schema validation against prd.schema.json

## 4. Execution Methodology
- 1. Intake business analysis and formalized requirements matrix.
- 2. Author Executive Summary, Problem Statement, and Target Personas.
- 3. Structure functional specifications mapped to user journeys.
- 4. Specify Non-Functional Requirements matrix with measurable SLA targets.
- 5. Clearly delineate Out-of-Scope boundaries to protect project scope.
- 6. Serialize PRD into docs/PRD.md and .agentic/memory/prd.json and validate against prd.schema.json.

## 5. Best Practices
- Maintain bidirectional links between business goals and functional items.
- Ensure the document is readable by both business stakeholders and AI agents.
- Version-control all changes to the PRD with explicit signoff history.

## 6. Common Mistakes to Avoid
- Mixing technical architecture (TRD) decisions into the product requirements.
- Vague success metrics that cannot be instrumented or validated.
- Skipping formal schema validation.

## 7. Validation Criteria
- Validation against .agentic/schemas/prd.schema.json exits with code 0.
- Zero unquantified non-functional requirements.
- Gate 1 (GATE-REQ-001) approval logged with evidence.

## 8. Relevant Tools
`prd.schema.json, Mermaid.js, Markdown lint`

## 9. Authoritative References
- Inspired: How to Create Tech Products Customers Love by Marty Cagan
- Shape Up: Stop Running in Circles and Ship Work that Matters by Basecamp
