# Skill: Requirements Engineering (`requirements-engineering`)

## 1. Purpose
Systematic elicitating, analyzing, specifying, and validating software requirements.

## 2. Activation Conditions
- Initiation of new project or feature discovery
- Ambiguous stakeholder requests needing structured user stories
- Defining non-functional requirements (SLA, security, scale)

## 3. Required Knowledge
- User story formatting (As a [role], I want [capability] so that [benefit])
- Given-When-Then acceptance criteria specification
- INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Non-functional requirement categorization (ISO/IEC 25010)

## 4. Execution Methodology
- 1. Domain Discovery: Elicit stakeholder goals and map core business domain entities.
- 2. Persona Definition: Characterize user archetypes, pain points, and workflows.
- 3. Feature Decomposition: Break high-level capabilities into atomic user stories.
- 4. Acceptance Criteria Authoring: Specify explicit Given-When-Then scenarios for each story.
- 5. NFR Definition: Quantify measurable thresholds for performance, security, and accessibility.
- 6. Traceability Tagging: Assign unique REQ IDs (e.g. REQ-F-001) for downstream traceability.

## 5. Best Practices
- Keep requirements technology-agnostic at the functional requirements stage.
- Ensure all criteria are quantitatively testable; avoid subjective adjectives like 'intuitive' or 'fast'.
- Explicitly define what is OUT of scope to avoid scope creep.

## 6. Common Mistakes to Avoid
- Specifying technical implementation details instead of user-visible outcomes.
- Omitting edge cases, negative flows, and unauthorized access scenarios.
- Failing to tie non-functional requirements to concrete measurement metrics.

## 7. Validation Criteria
- 100% of user stories satisfy INVEST criteria.
- Every story contains at least one testable Given-When-Then acceptance condition.
- Scope boundaries (in-scope and out-of-scope) are formally documented.

## 8. Relevant Tools
`Jira, Linear, Markdown, Mermaid.js`

## 9. Authoritative References
- IEEE 29148:2018 - Systems and software engineering - Life cycle processes - Requirements engineering
- User Story Mapping by Jeff Patton
