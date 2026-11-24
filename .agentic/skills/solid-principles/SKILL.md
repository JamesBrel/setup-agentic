# Skill: SOLID Principles (`solid-principles`)

## 1. Purpose
Application of the five fundamental object-oriented design principles in modern software development.

## 2. Activation Conditions
- Authoring class hierarchies, interfaces, and module contracts
- Code review passes and refactoring sessions
- Resolving tightly coupled, rigid, or fragile software structures

## 3. Required Knowledge
- Single Responsibility Principle (SRP): One reason to change
- Open/Closed Principle (OCP): Open for extension, closed for modification
- Liskov Substitution Principle (LSP): Subtypes must be substitutable for base types
- Interface Segregation Principle (ISP): Many client-specific interfaces over one general
- Dependency Inversion Principle (DIP): Depend upon abstractions, not concretions

## 4. Execution Methodology
- 1. Audit class / module responsibilities to ensure each has a single actor/stakeholder focus.
- 2. Utilize polymorphism and strategy patterns to enable extension without modifying existing code.
- 3. Verify subtype contracts: preconditions must not be strengthened; postconditions not weakened.
- 4. Break bloated interfaces into small, cohesive, role-focused interfaces.
- 5. Decouple high-level policies from low-level implementations using dependency injection.

## 5. Best Practices
- Favor composition over inheritance to adhere to SRP and OCP.
- Define interfaces where they are consumed, not where they are implemented.
- Keep interface declarations focused on 2 to 5 methods.

## 6. Common Mistakes to Avoid
- God classes performing database operations, serialization, and business logic.
- Throwing UnsupportedOperationException in subclasses (violating LSP).
- Creating monolithic 'Manager' or 'Helper' classes.

## 7. Validation Criteria
- Code passes static analysis rules for cyclomatic complexity and class size.
- Subclasses pass polymorphic test suites without type-checking hacks.
- Dependencies are injected through constructors or factory providers.

## 8. Relevant Tools
`SonarQube, PMD, PHPStan, ESLint, Dart Analyzer`

## 9. Authoritative References
- Design Principles and Design Patterns by Robert C. Martin
- Refactoring: Improving the Design of Existing Code by Martin Fowler
