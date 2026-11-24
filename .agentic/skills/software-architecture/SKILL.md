# Skill: Software Architecture (`software-architecture`)

## 1. Purpose
High-level software design, modular decomposition, trade-off analysis, and ADR governance.

## 2. Activation Conditions
- Greenfield architecture planning
- Major refactoring or legacy system decomposition
- Evaluating high-impact structural decisions and trade-offs

## 3. Required Knowledge
- Software architecture styles (Monolith, Modular Monolith, Microservices, Event-Driven)
- Quality attribute trade-offs (Performance vs Modifiability, Security vs Usability)
- ADR (Architecture Decision Record) lifecycle and documentation
- Coupling and cohesion metrics (Connascence, Afferent/Efferent coupling)

## 4. Execution Methodology
- 1. Analyze functional drivers and non-functional quality attributes.
- 2. Define system context diagram and external integration boundaries.
- 3. Partition system into loosely coupled modules with explicit interfaces.
- 4. Evaluate candidate architectures using trade-off analysis matrices.
- 5. Formalize decisions using standard ADR templates in .agentic/memory/adrs/.
- 6. Establish architectural fitness functions and automated guardrails.

## 5. Best Practices
- Favor simpler modular monoliths until microservice boundaries are proven necessary.
- Explicitly document negative consequences and rejected options in ADRs.
- Protect core domain models from contamination by third-party frameworks.

## 6. Common Mistakes to Avoid
- Premature distribution (microservices) before domain boundaries stabilize.
- Failing to document the context and drivers behind critical technical decisions.
- Allowing circular dependencies across system modules.

## 7. Validation Criteria
- System boundary diagrams clearly illustrate data and dependency flows.
- ADRs conform to adr.schema.json and are indexed in memory.
- Module dependency graph contains zero circular references.

## 8. Relevant Tools
`ArchUnit, Mermaid.js, Dependency-Cruiser, adr-tools`

## 9. Authoritative References
- Software Architecture: The Hard Parts by Neal Ford & Mark Richards
- Documenting Software Architectures by Paul Clements et al.
