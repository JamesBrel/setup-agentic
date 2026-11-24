# Skill: TRD Engineering (`trd-engineering`)

## 1. Purpose
Authoring Technical Requirements Documents with 100% PRD traceability and architectural specifications.

## 2. Activation Conditions
- PRD has passed GATE-REQ-001 approval
- Transitioning from product discovery to technical design
- Designing data schemas, API contracts, and infrastructure topologies

## 3. Required Knowledge
- Technical architecture patterns (Clean Arch, MVC, CQRS, Hexagonal)
- Data modeling and normalization principles
- OpenAPI / AsyncAPI contract specifications
- Traceability matrices linking PRD IDs to technical components

## 4. Execution Methodology
- 1. Ingest approved PRD and extract all functional (REQ-F-*) and non-functional (REQ-NF-*) items.
- 2. Select architecture pattern, runtime environment, and core framework stack.
- 3. Design data schema, entity relationships, and migration strategies.
- 4. Define API contracts, endpoints, protocols, and authentication methods.
- 5. Specify security controls, threat mitigations, and infrastructure topology.
- 6. Construct traceability matrix ensuring 100% of PRD items are mapped to components.
- 7. Serialize to docs/TRD.md and validate against trd.schema.json for Gate 2.

## 5. Best Practices
- Ensure every database entity and API endpoint directly serves a PRD requirement.
- Document architectural trade-offs and rationale behind stack choices.
- Define explicit failure modes and circuit breakers for external integrations.

## 6. Common Mistakes to Avoid
- Leaving PRD requirements unaddressed in the traceability matrix.
- Selecting libraries based on hype rather than verified compatibility.
- Omitting migration and rollback strategies for database changes.

## 7. Validation Criteria
- Validation against trd.schema.json passes with 0 errors.
- 100% coverage in the PRD-to-TRD Traceability Matrix.
- Gate 2 (GATE-ARCH-002) signoff achieved.

## 8. Relevant Tools
`trd.schema.json, OpenAPI, Mermaid.js, PlantUML`

## 9. Authoritative References
- Software Architecture in Practice (SEI Series in Software Engineering)
- IEEE 1016-2009 - IEEE Standard for Information Technology - Systems Design
