# Skill: Clean Architecture (`clean-architecture`)

## 1. Purpose
Implementation of Uncle Bob's Clean Architecture and Hexagonal / Ports & Adapters patterns.

## 2. Activation Conditions
- Designing domain, use case, and presentation layers
- Isolating business logic from databases, UI, and external frameworks
- Ensuring long-term testability and framework independence

## 3. Required Knowledge
- The Dependency Rule: Dependencies point strictly inward toward domain policies
- Layer taxonomy: Entities -> Use Cases -> Interface Adapters -> Frameworks & Drivers
- Dependency Inversion Principle (DIP): High-level modules depend on abstractions
- Repository and Adapter patterns

## 4. Execution Methodology
- 1. Domain Layer: Define pure business entities, value objects, and domain errors.
- 2. Application Layer: Implement use cases / interactors orchestrating domain flow.
- 3. Interface Adapters: Create controllers, presenters, and repository interfaces.
- 4. Infrastructure Layer: Implement database drivers, HTTP clients, and external SDKs.
- 5. Dependency Injection: Wire dependencies in composition root outside domain layer.
- 6. Verify with static boundary checks that inner layers import nothing from outer layers.

## 5. Best Practices
- Domain entities must never import ORMs, HTTP libraries, or framework packages.
- Use cases accept plain data transfer objects (DTOs) and return output models.
- All I/O operations must be abstracted behind interfaces declared in the use case layer.

## 6. Common Mistakes to Avoid
- Leaking database entity annotations or SQL types into the domain model.
- Passing HTTP request/response objects directly into application use cases.
- Creating bidirectional dependencies between presentation and persistence layers.

## 7. Validation Criteria
- Inner layer source files contain zero imports from outer infrastructure packages.
- Domain entities can be unit-tested without initializing any database or web server.
- All use cases depend exclusively on abstract repository interfaces.

## 8. Relevant Tools
`Dependency-Cruiser, ArchUnit, ESLint import-resolver, pytest`

## 9. Authoritative References
- Clean Architecture: A Craftsman's Guide to Software Structure by Robert C. Martin
- Hexagonal Architecture by Alistair Cockburn
