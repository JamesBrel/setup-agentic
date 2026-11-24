# Skill: Domain-Driven Design (`domain-driven-design`)

## 1. Purpose
Strategic and tactical DDD: Ubiquitous Language, Bounded Contexts, Aggregates, and Value Objects.

## 2. Activation Conditions
- Complex business domains with rich business rules
- Aligning engineering code with business stakeholder terminology
- Defining bounded contexts and anti-corruption layers

## 3. Required Knowledge
- Strategic DDD: Ubiquitous Language, Bounded Contexts, Context Mapping
- Tactical DDD: Entities, Value Objects, Aggregates, Domain Events, Repositories
- Aggregate root boundaries and transactional invariants
- Anti-Corruption Layers (ACL) for legacy integrations

## 4. Execution Methodology
- 1. Event Storming: Collaborate on domain timeline, commands, events, and read models.
- 2. Establish Ubiquitous Language glossary and enforce it across code identifiers.
- 3. Define Bounded Contexts and establish Context Map relationships (Customer/Supplier, ACL).
- 4. Design Aggregates ensuring transactional consistency within boundary.
- 5. Implement immutable Value Objects with structural equality.
- 6. Publish Domain Events when aggregate state transitions occur.

## 5. Best Practices
- Aggregates should be kept as small as possible while preserving invariants.
- Reference other aggregates strictly by identity (ID), never by object reference.
- Make Value Objects immutable; mutating operations should return a new instance.

## 6. Common Mistakes to Avoid
- Anemic Domain Model: entities consisting solely of getters and setters without logic.
- Giant aggregates that lock large portions of the database and cause contention.
- Using technical database names instead of Ubiquitous Language in domain code.

## 7. Validation Criteria
- Every aggregate root enforces its internal invariants before state persistence.
- Value objects are immutable and implement structural equality checks.
- Domain event handlers are decoupled from aggregate transaction boundaries.

## 8. Relevant Tools
`Miro / Event Storming, TypeScript, Dart, PHP / PHPStan`

## 9. Authoritative References
- Domain-Driven Design: Tackling Complexity in the Heart of Software by Eric Evans
- Implementing Domain-Driven Design by Vaughn Vernon
