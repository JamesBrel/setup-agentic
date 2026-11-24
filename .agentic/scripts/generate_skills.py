"""Skill generator for Agentic Software Factory V3.
Produces 29 comprehensive, modular skills conforming to strict flat directory layout.
Each skill directory has only files directly inside it, no nested subdirectories.
"""
import os
import json

SKILLS_DIR = os.path.join(os.path.dirname(__file__), "..", "skills")
os.makedirs(SKILLS_DIR, exist_ok=True)

skills_data = [
    {
        "id": "requirements-engineering",
        "name": "Requirements Engineering",
        "category": "product",
        "description": "Systematic elicitating, analyzing, specifying, and validating software requirements.",
        "activation_conditions": [
            "Initiation of new project or feature discovery",
            "Ambiguous stakeholder requests needing structured user stories",
            "Defining non-functional requirements (SLA, security, scale)"
        ],
        "required_knowledge": [
            "User story formatting (As a [role], I want [capability] so that [benefit])",
            "Given-When-Then acceptance criteria specification",
            "INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)",
            "Non-functional requirement categorization (ISO/IEC 25010)"
        ],
        "execution_methodology": [
            "1. Domain Discovery: Elicit stakeholder goals and map core business domain entities.",
            "2. Persona Definition: Characterize user archetypes, pain points, and workflows.",
            "3. Feature Decomposition: Break high-level capabilities into atomic user stories.",
            "4. Acceptance Criteria Authoring: Specify explicit Given-When-Then scenarios for each story.",
            "5. NFR Definition: Quantify measurable thresholds for performance, security, and accessibility.",
            "6. Traceability Tagging: Assign unique REQ IDs (e.g. REQ-F-001) for downstream traceability."
        ],
        "best_practices": [
            "Keep requirements technology-agnostic at the functional requirements stage.",
            "Ensure all criteria are quantitatively testable; avoid subjective adjectives like 'intuitive' or 'fast'.",
            "Explicitly define what is OUT of scope to avoid scope creep."
        ],
        "common_mistakes": [
            "Specifying technical implementation details instead of user-visible outcomes.",
            "Omitting edge cases, negative flows, and unauthorized access scenarios.",
            "Failing to tie non-functional requirements to concrete measurement metrics."
        ],
        "validation_criteria": [
            "100% of user stories satisfy INVEST criteria.",
            "Every story contains at least one testable Given-When-Then acceptance condition.",
            "Scope boundaries (in-scope and out-of-scope) are formally documented."
        ],
        "relevant_tools": ["Jira", "Linear", "Markdown", "Mermaid.js"],
        "authoritative_references": [
            "IEEE 29148:2018 - Systems and software engineering - Life cycle processes - Requirements engineering",
            "User Story Mapping by Jeff Patton"
        ]
    },
    {
        "id": "prd-engineering",
        "name": "PRD Engineering",
        "category": "product",
        "description": "Standardized authoring, structuring, and schema validation of Product Requirements Documents.",
        "activation_conditions": [
            "Completion of requirements engineering discovery",
            "Greenfield project kickoff (Mode A)",
            "Major architectural addition or product line expansion"
        ],
        "required_knowledge": [
            "PRD structure and lifecycle states",
            "User journey mapping and scenario modeling",
            "Success metrics definition (North Star, Pirate Metrics, OKRs)",
            "JSON schema validation against prd.schema.json"
        ],
        "execution_methodology": [
            "1. Intake business analysis and formalized requirements matrix.",
            "2. Author Executive Summary, Problem Statement, and Target Personas.",
            "3. Structure functional specifications mapped to user journeys.",
            "4. Specify Non-Functional Requirements matrix with measurable SLA targets.",
            "5. Clearly delineate Out-of-Scope boundaries to protect project scope.",
            "6. Serialize PRD into docs/PRD.md and .agentic/memory/prd.json and validate against prd.schema.json."
        ],
        "best_practices": [
            "Maintain bidirectional links between business goals and functional items.",
            "Ensure the document is readable by both business stakeholders and AI agents.",
            "Version-control all changes to the PRD with explicit signoff history."
        ],
        "common_mistakes": [
            "Mixing technical architecture (TRD) decisions into the product requirements.",
            "Vague success metrics that cannot be instrumented or validated.",
            "Skipping formal schema validation."
        ],
        "validation_criteria": [
            "Validation against .agentic/schemas/prd.schema.json exits with code 0.",
            "Zero unquantified non-functional requirements.",
            "Gate 1 (GATE-REQ-001) approval logged with evidence."
        ],
        "relevant_tools": ["prd.schema.json", "Mermaid.js", "Markdown lint"],
        "authoritative_references": [
            "Inspired: How to Create Tech Products Customers Love by Marty Cagan",
            "Shape Up: Stop Running in Circles and Ship Work that Matters by Basecamp"
        ]
    },
    {
        "id": "trd-engineering",
        "name": "TRD Engineering",
        "category": "product",
        "description": "Authoring Technical Requirements Documents with 100% PRD traceability and architectural specifications.",
        "activation_conditions": [
            "PRD has passed GATE-REQ-001 approval",
            "Transitioning from product discovery to technical design",
            "Designing data schemas, API contracts, and infrastructure topologies"
        ],
        "required_knowledge": [
            "Technical architecture patterns (Clean Arch, MVC, CQRS, Hexagonal)",
            "Data modeling and normalization principles",
            "OpenAPI / AsyncAPI contract specifications",
            "Traceability matrices linking PRD IDs to technical components"
        ],
        "execution_methodology": [
            "1. Ingest approved PRD and extract all functional (REQ-F-*) and non-functional (REQ-NF-*) items.",
            "2. Select architecture pattern, runtime environment, and core framework stack.",
            "3. Design data schema, entity relationships, and migration strategies.",
            "4. Define API contracts, endpoints, protocols, and authentication methods.",
            "5. Specify security controls, threat mitigations, and infrastructure topology.",
            "6. Construct traceability matrix ensuring 100% of PRD items are mapped to components.",
            "7. Serialize to docs/TRD.md and validate against trd.schema.json for Gate 2."
        ],
        "best_practices": [
            "Ensure every database entity and API endpoint directly serves a PRD requirement.",
            "Document architectural trade-offs and rationale behind stack choices.",
            "Define explicit failure modes and circuit breakers for external integrations."
        ],
        "common_mistakes": [
            "Leaving PRD requirements unaddressed in the traceability matrix.",
            "Selecting libraries based on hype rather than verified compatibility.",
            "Omitting migration and rollback strategies for database changes."
        ],
        "validation_criteria": [
            "Validation against trd.schema.json passes with 0 errors.",
            "100% coverage in the PRD-to-TRD Traceability Matrix.",
            "Gate 2 (GATE-ARCH-002) signoff achieved."
        ],
        "relevant_tools": ["trd.schema.json", "OpenAPI", "Mermaid.js", "PlantUML"],
        "authoritative_references": [
            "Software Architecture in Practice (SEI Series in Software Engineering)",
            "IEEE 1016-2009 - IEEE Standard for Information Technology - Systems Design"
        ]
    },
    {
        "id": "software-architecture",
        "name": "Software Architecture",
        "category": "architecture",
        "description": "High-level software design, modular decomposition, trade-off analysis, and ADR governance.",
        "activation_conditions": [
            "Greenfield architecture planning",
            "Major refactoring or legacy system decomposition",
            "Evaluating high-impact structural decisions and trade-offs"
        ],
        "required_knowledge": [
            "Software architecture styles (Monolith, Modular Monolith, Microservices, Event-Driven)",
            "Quality attribute trade-offs (Performance vs Modifiability, Security vs Usability)",
            "ADR (Architecture Decision Record) lifecycle and documentation",
            "Coupling and cohesion metrics (Connascence, Afferent/Efferent coupling)"
        ],
        "execution_methodology": [
            "1. Analyze functional drivers and non-functional quality attributes.",
            "2. Define system context diagram and external integration boundaries.",
            "3. Partition system into loosely coupled modules with explicit interfaces.",
            "4. Evaluate candidate architectures using trade-off analysis matrices.",
            "5. Formalize decisions using standard ADR templates in .agentic/memory/adrs/.",
            "6. Establish architectural fitness functions and automated guardrails."
        ],
        "best_practices": [
            "Favor simpler modular monoliths until microservice boundaries are proven necessary.",
            "Explicitly document negative consequences and rejected options in ADRs.",
            "Protect core domain models from contamination by third-party frameworks."
        ],
        "common_mistakes": [
            "Premature distribution (microservices) before domain boundaries stabilize.",
            "Failing to document the context and drivers behind critical technical decisions.",
            "Allowing circular dependencies across system modules."
        ],
        "validation_criteria": [
            "System boundary diagrams clearly illustrate data and dependency flows.",
            "ADRs conform to adr.schema.json and are indexed in memory.",
            "Module dependency graph contains zero circular references."
        ],
        "relevant_tools": ["ArchUnit", "Mermaid.js", "Dependency-Cruiser", "adr-tools"],
        "authoritative_references": [
            "Software Architecture: The Hard Parts by Neal Ford & Mark Richards",
            "Documenting Software Architectures by Paul Clements et al."
        ]
    },
    {
        "id": "clean-architecture",
        "name": "Clean Architecture",
        "category": "architecture",
        "description": "Implementation of Uncle Bob's Clean Architecture and Hexagonal / Ports & Adapters patterns.",
        "activation_conditions": [
            "Designing domain, use case, and presentation layers",
            "Isolating business logic from databases, UI, and external frameworks",
            "Ensuring long-term testability and framework independence"
        ],
        "required_knowledge": [
            "The Dependency Rule: Dependencies point strictly inward toward domain policies",
            "Layer taxonomy: Entities -> Use Cases -> Interface Adapters -> Frameworks & Drivers",
            "Dependency Inversion Principle (DIP): High-level modules depend on abstractions",
            "Repository and Adapter patterns"
        ],
        "execution_methodology": [
            "1. Domain Layer: Define pure business entities, value objects, and domain errors.",
            "2. Application Layer: Implement use cases / interactors orchestrating domain flow.",
            "3. Interface Adapters: Create controllers, presenters, and repository interfaces.",
            "4. Infrastructure Layer: Implement database drivers, HTTP clients, and external SDKs.",
            "5. Dependency Injection: Wire dependencies in composition root outside domain layer.",
            "6. Verify with static boundary checks that inner layers import nothing from outer layers."
        ],
        "best_practices": [
            "Domain entities must never import ORMs, HTTP libraries, or framework packages.",
            "Use cases accept plain data transfer objects (DTOs) and return output models.",
            "All I/O operations must be abstracted behind interfaces declared in the use case layer."
        ],
        "common_mistakes": [
            "Leaking database entity annotations or SQL types into the domain model.",
            "Passing HTTP request/response objects directly into application use cases.",
            "Creating bidirectional dependencies between presentation and persistence layers."
        ],
        "validation_criteria": [
            "Inner layer source files contain zero imports from outer infrastructure packages.",
            "Domain entities can be unit-tested without initializing any database or web server.",
            "All use cases depend exclusively on abstract repository interfaces."
        ],
        "relevant_tools": ["Dependency-Cruiser", "ArchUnit", "ESLint import-resolver", "pytest"],
        "authoritative_references": [
            "Clean Architecture: A Craftsman's Guide to Software Structure by Robert C. Martin",
            "Hexagonal Architecture by Alistair Cockburn"
        ]
    },
    {
        "id": "domain-driven-design",
        "name": "Domain-Driven Design",
        "category": "architecture",
        "description": "Strategic and tactical DDD: Ubiquitous Language, Bounded Contexts, Aggregates, and Value Objects.",
        "activation_conditions": [
            "Complex business domains with rich business rules",
            "Aligning engineering code with business stakeholder terminology",
            "Defining bounded contexts and anti-corruption layers"
        ],
        "required_knowledge": [
            "Strategic DDD: Ubiquitous Language, Bounded Contexts, Context Mapping",
            "Tactical DDD: Entities, Value Objects, Aggregates, Domain Events, Repositories",
            "Aggregate root boundaries and transactional invariants",
            "Anti-Corruption Layers (ACL) for legacy integrations"
        ],
        "execution_methodology": [
            "1. Event Storming: Collaborate on domain timeline, commands, events, and read models.",
            "2. Establish Ubiquitous Language glossary and enforce it across code identifiers.",
            "3. Define Bounded Contexts and establish Context Map relationships (Customer/Supplier, ACL).",
            "4. Design Aggregates ensuring transactional consistency within boundary.",
            "5. Implement immutable Value Objects with structural equality.",
            "6. Publish Domain Events when aggregate state transitions occur."
        ],
        "best_practices": [
            "Aggregates should be kept as small as possible while preserving invariants.",
            "Reference other aggregates strictly by identity (ID), never by object reference.",
            "Make Value Objects immutable; mutating operations should return a new instance."
        ],
        "common_mistakes": [
            "Anemic Domain Model: entities consisting solely of getters and setters without logic.",
            "Giant aggregates that lock large portions of the database and cause contention.",
            "Using technical database names instead of Ubiquitous Language in domain code."
        ],
        "validation_criteria": [
            "Every aggregate root enforces its internal invariants before state persistence.",
            "Value objects are immutable and implement structural equality checks.",
            "Domain event handlers are decoupled from aggregate transaction boundaries."
        ],
        "relevant_tools": ["Miro / Event Storming", "TypeScript", "Dart", "PHP / PHPStan"],
        "authoritative_references": [
            "Domain-Driven Design: Tackling Complexity in the Heart of Software by Eric Evans",
            "Implementing Domain-Driven Design by Vaughn Vernon"
        ]
    },
    {
        "id": "solid-principles",
        "name": "SOLID Principles",
        "category": "architecture",
        "description": "Application of the five fundamental object-oriented design principles in modern software development.",
        "activation_conditions": [
            "Authoring class hierarchies, interfaces, and module contracts",
            "Code review passes and refactoring sessions",
            "Resolving tightly coupled, rigid, or fragile software structures"
        ],
        "required_knowledge": [
            "Single Responsibility Principle (SRP): One reason to change",
            "Open/Closed Principle (OCP): Open for extension, closed for modification",
            "Liskov Substitution Principle (LSP): Subtypes must be substitutable for base types",
            "Interface Segregation Principle (ISP): Many client-specific interfaces over one general",
            "Dependency Inversion Principle (DIP): Depend upon abstractions, not concretions"
        ],
        "execution_methodology": [
            "1. Audit class / module responsibilities to ensure each has a single actor/stakeholder focus.",
            "2. Utilize polymorphism and strategy patterns to enable extension without modifying existing code.",
            "3. Verify subtype contracts: preconditions must not be strengthened; postconditions not weakened.",
            "4. Break bloated interfaces into small, cohesive, role-focused interfaces.",
            "5. Decouple high-level policies from low-level implementations using dependency injection."
        ],
        "best_practices": [
            "Favor composition over inheritance to adhere to SRP and OCP.",
            "Define interfaces where they are consumed, not where they are implemented.",
            "Keep interface declarations focused on 2 to 5 methods."
        ],
        "common_mistakes": [
            "God classes performing database operations, serialization, and business logic.",
            "Throwing UnsupportedOperationException in subclasses (violating LSP).",
            "Creating monolithic 'Manager' or 'Helper' classes."
        ],
        "validation_criteria": [
            "Code passes static analysis rules for cyclomatic complexity and class size.",
            "Subclasses pass polymorphic test suites without type-checking hacks.",
            "Dependencies are injected through constructors or factory providers."
        ],
        "relevant_tools": ["SonarQube", "PMD", "PHPStan", "ESLint", "Dart Analyzer"],
        "authoritative_references": [
            "Design Principles and Design Patterns by Robert C. Martin",
            "Refactoring: Improving the Design of Existing Code by Martin Fowler"
        ]
    },
    {
        "id": "database-architecture",
        "name": "Database Architecture",
        "category": "architecture",
        "description": "Relational and NoSQL data modeling, schema migration engineering, indexing, and ACID guarantees.",
        "activation_conditions": [
            "Database schema creation or modification",
            "Writing migration scripts and rollback procedures",
            "Optimizing slow queries and configuring indices"
        ],
        "required_knowledge": [
            "Relational normalization (1NF, 2NF, 3NF, BCNF) and deliberate denormalization",
            "Index architectures (B-Tree, Hash, GIN, GiST) and query execution EXPLAIN plans",
            "ACID transactions, isolation levels, and optimistic vs pessimistic locking",
            "Zero-downtime migration patterns (Expand-Contract / Parallel Run)"
        ],
        "execution_methodology": [
            "1. Entity-Relationship Modeling: Map entities, cardinality, and referential integrity.",
            "2. DDL Drafting: Specify tables, strict column types, NOT NULL defaults, and constraints.",
            "3. Indexing Strategy: Create indices for foreign keys and query predicate columns.",
            "4. Migration Authoring: Write reversible up() and down() migration scripts.",
            "5. Reversibility Verification: Execute migrate -> rollback -> migrate in test environment.",
            "6. Query Optimization: Inspect EXPLAIN ANALYZE output to eliminate sequential scans on large tables."
        ],
        "best_practices": [
            "Always use UTC timestamps for created_at and updated_at columns.",
            "Ensure every foreign key has a supporting index to avoid table locks.",
            "Use transactions inside migrations to ensure atomic schema changes."
        ],
        "common_mistakes": [
            "Missing down() rollback logic or non-reversible migration statements.",
            "Over-indexing tables leading to severe write performance degradation.",
            "Storing unhashed passwords or plain-text PII in database columns."
        ],
        "validation_criteria": [
            "Automated test executes migration and complete rollback without errors.",
            "Zero unindexed foreign keys in relational schema.",
            "EXPLAIN output confirms index scan utilization for primary query filters."
        ],
        "relevant_tools": ["PostgreSQL", "MySQL", "SQLite", "Prisma", "Doctrine", "Eloquent"],
        "authoritative_references": [
            "Designing Data-Intensive Applications by Martin Kleppmann",
            "SQL Antipatterns: Avoiding the Pitfalls of Database Programming by Bill Karwin"
        ]
    },
    {
        "id": "api-engineering",
        "name": "API Engineering",
        "category": "architecture",
        "description": "Design, standardization, versioning, and documentation of RESTful, GraphQL, and gRPC APIs.",
        "activation_conditions": [
            "Designing client-server or service-to-service interfaces",
            "Authoring OpenAPI (Swagger) specifications",
            "Standardizing error payloads and pagination models"
        ],
        "required_knowledge": [
            "HTTP semantics, status codes (200, 201, 204, 400, 401, 403, 404, 409, 422, 500)",
            "REST resource modeling, idempotency (GET, PUT, DELETE), and caching headers",
            "RFC 7807 Problem Details for standardized error payloads",
            "OpenAPI 3.0 / 3.1 schema specification and contract testing"
        ],
        "execution_methodology": [
            "1. Resource Modeling: Identify nouns, hierarchies, and sub-resources (e.g. /users/{id}/orders).",
            "2. Method Binding: Assign appropriate HTTP verbs respecting idempotency.",
            "3. OpenAPI Authoring: Draft complete OpenAPI spec including request/response schemas.",
            "4. Standardization: Enforce standard pagination (cursor or limit/offset) and RFC 7807 error format.",
            "5. Authentication & Security: Define Bearer JWT auth, CORS policies, and rate limits.",
            "6. Contract Verification: Validate OpenAPI document with Spectral linter and contract tests."
        ],
        "best_practices": [
            "Always version APIs via URL (/v1/) or Accept header to maintain backward compatibility.",
            "Provide consistent snake_case or camelCase JSON naming conventions across all endpoints.",
            "Validate incoming request payloads strictly against schema before executing business logic."
        ],
        "common_mistakes": [
            "Returning 200 OK with an error payload inside the response body.",
            "Using verbs in URL paths (/getUser, /createOrder) instead of HTTP methods.",
            "Exposing internal database IDs or stack traces in error responses."
        ],
        "validation_criteria": [
            "OpenAPI specification passes Spectral validation with 0 errors.",
            "All endpoints return RFC 7807 compliant error structures on invalid input.",
            "Automated contract tests pass against actual endpoint responses."
        ],
        "relevant_tools": ["Spectral", "Swagger UI", "Postman / Newman", "Prism Mock Server"],
        "authoritative_references": [
            "RESTful Web APIs by Leonard Richardson & Mike Amundsen",
            "RFC 7807: Problem Details for HTTP APIs (IETF)"
        ]
    },
    {
        "id": "flutter-dart",
        "name": "Flutter & Dart",
        "category": "development",
        "description": "Cross-platform mobile and multi-platform development using Flutter framework and Dart language.",
        "activation_conditions": [
            "Building mobile applications for iOS and Android",
            "Authoring Flutter widgets, state management (Bloc/Riverpod), and platform channels",
            "Optimizing 60fps rendering and mobile performance"
        ],
        "required_knowledge": [
            "Dart 3 language features (Sound null safety, records, patterns, sealed classes)",
            "Flutter widget tree, element tree, and render object pipeline",
            "Predictable state management (flutter_bloc, Riverpod, Provider)",
            "Platform channels, method channels, and native event streams"
        ],
        "execution_methodology": [
            "1. Architecture Setup: Structure project using feature-first or Clean Architecture layers.",
            "2. State Management: Implement Bloc / Cubit classes with immutable states and events.",
            "3. UI Implementation: Build responsive widget hierarchies using layout builders and tokens.",
            "4. API & Data Binding: Integrate Dio or http with interceptors and json_serializable models.",
            "5. Offline Storage: Configure Hive, Isar, or sqflite for local persistence.",
            "6. Verification: Run flutter analyze, flutter test, and widget tests."
        ],
        "best_practices": [
            "Use const constructors wherever possible to avoid unnecessary widget rebuilds.",
            "Keep widgets small, focused, and composed of specialized child widgets.",
            "Offload expensive computations (JSON parsing, crypto) to Dart isolates."
        ],
        "common_mistakes": [
            "Calling setState() at the root of a large widget tree.",
            "Blocking the UI isolate with synchronous file or network I/O.",
            "Ignoring platform-specific design guidelines (Material vs Cupertino)."
        ],
        "validation_criteria": [
            "flutter analyze reports 0 issues, 0 warnings.",
            "flutter test passes 100% of unit and widget tests.",
            "Zero frame drops during standard scroll interactions in profile mode."
        ],
        "relevant_tools": ["flutter", "dart analyze", "flutter_test", "mocktail", "bloc_test"],
        "authoritative_references": [
            "Official Flutter Documentation (flutter.dev)",
            "Effective Dart: Style and Design Guidelines"
        ]
    },
    {
        "id": "laravel-php",
        "name": "Laravel & PHP",
        "category": "development",
        "description": "Modern enterprise PHP development using the Laravel framework, Eloquent ORM, and Artisan tooling.",
        "activation_conditions": [
            "Building Laravel backend web applications and REST APIs",
            "Authoring Eloquent models, migrations, and database seeders",
            "Implementing queue workers, scheduled tasks, and event listeners"
        ],
        "required_knowledge": [
            "PHP 8.2+ modern features (enums, readonly classes, fibers, attributes)",
            "Laravel service container, service providers, and dependency injection",
            "Eloquent ORM, eager loading, query scopes, and relationships",
            "Laravel testing tools (PHPUnit, Pest, database migrations, HTTP assertions)"
        ],
        "execution_methodology": [
            "1. Domain / Feature Scaffolding: Create migrations, models, controllers, and Form Requests.",
            "2. Business Logic Implementation: Implement domain actions or use cases outside controllers.",
            "3. Eloquent Relations: Define relationships with explicit foreign keys and eager loading.",
            "4. Validation & Authorization: Author Form Requests and Policies for access control.",
            "5. Asynchronous Work: Dispatch queue jobs with backoff and timeout parameters.",
            "6. Verification: Run php artisan test --parallel and phpstan analyse --level=8."
        ],
        "best_practices": [
            "Keep controllers skinny; delegate business logic to dedicated Action classes or Services.",
            "Always prevent N+1 queries by eager loading relationships with with().",
            "Use strict types declaration (declare(strict_types=1);) in every PHP file."
        ],
        "common_mistakes": [
            "Executing database queries directly inside Blade templates or API resource transformations.",
            "Failing to protect mass assignment with $fillable or strict casting.",
            "Disabling CSRF or authentication middleware without documented rationale."
        ],
        "validation_criteria": [
            "php artisan test passes with zero failures.",
            "PHPStan analysis passes at level 8 with zero errors.",
            "Zero N+1 query warnings detected in test profiling."
        ],
        "relevant_tools": ["PHPStan", "Pest PHP", "PHP_CodeSniffer", "Laravel Pint", "Artisan"],
        "authoritative_references": [
            "Official Laravel Documentation (laravel.com/docs)",
            "PHP Standards Recommendations (PHP-FIG PSR-1, PSR-4, PSR-12)"
        ]
    },
    {
        "id": "react-typescript",
        "name": "React & TypeScript",
        "category": "development",
        "description": "Web client application development using React 18+, TypeScript, functional components, and hooks.",
        "activation_conditions": [
            "Building interactive web UI applications and SPAs/SSGs",
            "Developing custom React hooks and reusable component libraries",
            "State management with Zustand, Redux Toolkit, or React Query"
        ],
        "required_knowledge": [
            "TypeScript strict mode (generics, mapped types, discriminated unions)",
            "React fiber reconciliation, hooks lifecycle (useState, useEffect, useMemo, useCallback)",
            "Server components vs Client components (Next.js App Router)",
            "State management libraries (TanStack Query, Zustand, Context)"
        ],
        "execution_methodology": [
            "1. Project Configuration: Setup tsconfig.json with strict: true and path aliases.",
            "2. Component Design: Author typed functional components with explicit Props interfaces.",
            "3. Hook Engineering: Encapsulate stateful logic and data fetching in custom hooks.",
            "4. Data Management: Implement React Query for server cache and Zustand for client state.",
            "5. Styling & Tokens: Apply Tailwind CSS or CSS Modules referencing design tokens.",
            "6. Verification: Run tsc --noEmit, eslint ., and vitest run."
        ],
        "best_practices": [
            "Never use any; use unknown with type guards or discriminated unions.",
            "Keep useEffect focused on synchronization with external systems, not derived state.",
            "Memoize callbacks and expensive computations passed down to memoized child components."
        ],
        "common_mistakes": [
            "Missing dependencies in useEffect dependency arrays causing stale closures.",
            "Mutating state directly instead of creating immutable updates.",
            "Prop drilling through many component levels instead of using composition or store."
        ],
        "validation_criteria": [
            "tsc --noEmit passes with zero TypeScript diagnostic errors.",
            "ESLint passes with zero warnings or errors.",
            "Unit tests achieve > 80% branch coverage with React Testing Library."
        ],
        "relevant_tools": ["TypeScript", "Vite", "ESLint", "Vitest", "React Testing Library"],
        "authoritative_references": [
            "React Official Documentation (react.dev)",
            "TypeScript Handbook (typescriptlang.org)"
        ]
    },
    {
        "id": "nodejs-typescript",
        "name": "Node.js & TypeScript",
        "category": "development",
        "description": "Asynchronous backend microservices and API development on Node.js using TypeScript.",
        "activation_conditions": [
            "Developing Node.js REST, GraphQL, or gRPC backend services",
            "Authoring Express, Fastify, or NestJS service modules",
            "Handling asynchronous streams, workers, and event loop performance"
        ],
        "required_knowledge": [
            "Node.js event loop architecture (timers, poll, check, close, process.nextTick)",
            "Modern asynchronous JavaScript (async/await, Promise combinators, AbortController)",
            "Fastify and Express framework middleware pipelines and error handling",
            "Worker threads and child processes for CPU-intensive tasks"
        ],
        "execution_methodology": [
            "1. Project Scaffolding: Setup TypeScript compilation, tsx/ts-node, and ESLint.",
            "2. Server Bootstrap: Configure Fastify/Express with security middleware (Helmet, CORS).",
            "3. Route & Controller Implementation: Map REST endpoints to controller handlers.",
            "4. Service & Repository Layer: Implement domain logic with dependency injection.",
            "5. Error Handling: Centralize error middleware converting domain exceptions to RFC 7807.",
            "6. Verification: Run tsc, eslint, and jest/vitest suites."
        ],
        "best_practices": [
            "Always use Fastify for high-throughput JSON APIs over older Express versions.",
            "Never execute synchronous blocking I/O (fs.readFileSync) in request handlers.",
            "Always register unhandledRejection and uncaughtException listeners for graceful shutdown."
        ],
        "common_mistakes": [
            "Blocking the single-threaded event loop with expensive cryptographic or CPU loops.",
            "Swallowing unhandled promise rejections leading to hung HTTP requests.",
            "Failing to clean up event listeners causing memory leaks."
        ],
        "validation_criteria": [
            "TypeScript compiles cleanly with strict null checks enabled.",
            "Server demonstrates zero unhandled promise rejections under load testing.",
            "Integration test suite validates all endpoints."
        ],
        "relevant_tools": ["Node.js", "TypeScript", "Fastify", "Jest", "Vitest", "Pino Logger"],
        "authoritative_references": [
            "Node.js Documentation (nodejs.org/docs)",
            "Node.js Best Practices GitHub Repository"
        ]
    },
    {
        "id": "python-engineering",
        "name": "Python Engineering",
        "category": "development",
        "description": "Production Python development, type annotations, packaging, async programming, and pytest.",
        "activation_conditions": [
            "Building Python backend services, automation scripts, or data pipelines",
            "Developing FastAPI, Flask, or Django applications",
            "Authoring pytest suites and enforcing strict typing with mypy/pyright"
        ],
        "required_knowledge": [
            "Python 3.10+ features (structural pattern matching, type unions, asyncio task groups)",
            "Static type checking with mypy / pyright and typing protocols",
            "Python packaging standards (pyproject.toml, poetry, uv, pip-tools)",
            "Pytest fixtures, parametrization, and async test plugins"
        ],
        "execution_methodology": [
            "1. Environment & Package Configuration: Setup pyproject.toml with dependencies and tool configs.",
            "2. Type-Annotated Implementation: Author domain models and logic with complete type signatures.",
            "3. Framework Integration: Implement FastAPI routes with Pydantic v2 schemas.",
            "4. Async Execution: Manage asynchronous coroutines with proper cancellation tokens.",
            "5. Test Authoring: Construct isolated pytest fixtures with monkeypatch or unittest.mock.",
            "6. Quality Checks: Execute ruff check, ruff format --check, mypy, and pytest."
        ],
        "best_practices": [
            "Use Pydantic v2 for data parsing and validation at system boundaries.",
            "Enforce strict mypy configuration (disallow_untyped_defs = True).",
            "Use ruff for blazing fast linting and formatting."
        ],
        "common_mistakes": [
            "Mutable default arguments in function signatures (def func(items=[])).",
            "Mixing synchronous blocking code inside asyncio event loop without run_in_executor.",
            "Catching bare except: instead of specific exception classes."
        ],
        "validation_criteria": [
            "mypy passes in strict mode with zero type errors.",
            "ruff check and ruff format report zero issues.",
            "pytest achieves 100% pass rate with coverage reporting."
        ],
        "relevant_tools": ["uv", "ruff", "mypy", "pytest", "FastAPI", "Pydantic"],
        "authoritative_references": [
            "Fluent Python: Clear, Concise, and Effective Programming by Luciano Ramalho",
            "PEP 8 - Style Guide for Python Code & PEP 484 - Type Hints"
        ]
    },
    {
        "id": "java-engineering",
        "name": "Java Engineering",
        "category": "development",
        "description": "Enterprise Java development with Spring Boot, JPA/Hibernate, Gradle/Maven, and JUnit 5.",
        "activation_conditions": [
            "Building enterprise Java services, Spring Boot applications, or Kafka consumers",
            "Authoring JPA entities, repositories, and transactional services",
            "Enforcing code style with Checkstyle, SpotBugs, and SonarQube"
        ],
        "required_knowledge": [
            "Modern Java (Java 17 / 21 LTS: records, sealed interfaces, virtual threads)",
            "Spring Boot 3 ecosystem (Spring Data JPA, Spring Security, Actuator)",
            "JPA lifecycle, entity relationships, and second-level caching",
            "JUnit 5, Mockito, and Testcontainers for integration testing"
        ],
        "execution_methodology": [
            "1. Project Scaffolding: Configure build.gradle.kts or pom.xml with dependencies.",
            "2. Domain Model: Define JPA entities with proper equals/hashCode on immutable identifiers.",
            "3. Repositories: Implement Spring Data repositories with explicit query methods.",
            "4. Service Layer: Implement transactional use cases with @Transactional(readOnly = true).",
            "5. Controller Layer: Implement REST endpoints with OpenAPI annotations and bean validation.",
            "6. Verification: Execute gradle test check or mvn verify with Testcontainers."
        ],
        "best_practices": [
            "Use Java records for immutable Data Transfer Objects (DTOs).",
            "Use Testcontainers for authentic database and message queue integration tests.",
            "Explicitly define fetch = FetchType.LAZY on all @ManyToOne and @OneToOne JPA mappings."
        ],
        "common_mistakes": [
            "Using default FetchType.EAGER causing massive unintended join queries.",
            "Calling transactional methods from within the same class (bypassing Spring proxies).",
            "Catching Throwable or generic Exception."
        ],
        "validation_criteria": [
            "Gradle / Maven build compiles with zero warnings.",
            "Checkstyle and SpotBugs report zero violations.",
            "All unit and Testcontainers integration tests pass."
        ],
        "relevant_tools": ["Gradle", "Maven", "Spring Boot", "Testcontainers", "JUnit 5", "SpotBugs"],
        "authoritative_references": [
            "Effective Java (3rd Edition) by Joshua Bloch",
            "Spring Framework Documentation (spring.io)"
        ]
    },
    {
        "id": "csharp-dotnet",
        "name": "C# and .NET",
        "category": "development",
        "description": "Cross-platform enterprise .NET 8+ development, ASP.NET Core, Entity Framework Core, and xUnit.",
        "activation_conditions": [
            "Building .NET 8+ Web APIs, microservices, or background worker services",
            "Designing Entity Framework Core DbContexts, migrations, and LINQ queries",
            "Authoring xUnit / FluentAssertions test suites"
        ],
        "required_knowledge": [
            "C# 12 modern language features (primary constructors, collection expressions, pattern matching)",
            "ASP.NET Core Minimal APIs and Controller architectures",
            "EF Core change tracking, migrations, and compiled queries",
            "Asynchronous programming with async/await, Task, and CancellationToken"
        ],
        "execution_methodology": [
            "1. Solution Structure: Scaffold solution adhering to Clean Architecture project layout.",
            "2. Domain & Application: Implement domain entities and MediatR / command handlers.",
            "3. Infrastructure & EF Core: Configure DbContext with Fluent API configurations.",
            "4. API Endpoints: Define Minimal API routes with endpoint filters and validation.",
            "5. Resiliency: Configure Polly retry and circuit breaker policies for external HTTP clients.",
            "6. Verification: Run dotnet build --warnaserror and dotnet test."
        ],
        "best_practices": [
            "Always pass CancellationToken down through all asynchronous I/O methods.",
            "Use AsNoTracking() for read-only queries in Entity Framework Core.",
            "Enable nullable reference types (<Nullable>enable</Nullable>) in all .csproj files."
        ],
        "common_mistakes": [
            "Using .Result or .Wait() on Tasks causing thread-pool starvation and deadlocks.",
            "Executing unbounded client-side evaluation of LINQ queries.",
            "Ignoring CancellationToken parameters in API controllers."
        ],
        "validation_criteria": [
            "dotnet build passes with zero warnings (warnings treated as errors).",
            "xUnit test suite passes with 100% success rate.",
            "Code adheres to .editorconfig formatting standards."
        ],
        "relevant_tools": ["dotnet CLI", "xUnit", "FluentAssertions", "Polly", "Testcontainers-dotnet"],
        "authoritative_references": [
            "Microsoft .NET Documentation (learn.microsoft.com/dotnet)",
            "C# in Depth by Jon Skeet"
        ]
    },
    {
        "id": "mobile-engineering",
        "name": "Mobile Engineering",
        "category": "architecture",
        "description": "Mobile application lifecycle, offline-first architectures, memory constraints, and app store readiness.",
        "activation_conditions": [
            "Architecting mobile applications across iOS, Android, and cross-platform runtimes",
            "Designing offline synchronization and local caching strategies",
            "Configuring push notifications, background tasks, and battery efficiency"
        ],
        "required_knowledge": [
            "Mobile OS lifecycles (foreground, background, suspended, terminated)",
            "Local storage engines (SQLite, Realm, Keychain / Keystore secure storage)",
            "Mobile network resiliency, exponential backoff, and offline queueing",
            "Mobile security (SSL pinning, root/jailbreak detection, code obfuscation)"
        ],
        "execution_methodology": [
            "1. Architecture Definition: Establish offline-first data synchronization patterns.",
            "2. State & Storage: Configure secure credential storage and encrypted local database.",
            "3. Network Layer: Implement request interceptors with automatic token refresh and offline queue.",
            "4. Performance Profiling: Profile memory footprint, UI thread frame rate, and startup time.",
            "5. Platform Integration: Configure push notification handlers and deep linking routers.",
            "6. Release Hardening: Apply ProGuard/R8 rules and verify permissions manifest."
        ],
        "best_practices": [
            "Design for intermittent connectivity: all user actions should optimistic-update locally.",
            "Never store sensitive API tokens or secrets in unencrypted SharedPreferences/UserDefaults.",
            "Keep cold app startup time under 1.5 seconds."
        ],
        "common_mistakes": [
            "Performing synchronous disk or database operations on the main UI thread.",
            "Requesting excessive device permissions at initial app launch before context is clear.",
            "Failing to handle push notification payloads when the app is in terminated state."
        ],
        "validation_criteria": [
            "App functions gracefully in airplane mode with offline queue sync on reconnection.",
            "Zero ANRs (Application Not Responding) or main thread jank.",
            "All private credentials stored in secure hardware-backed keystore/keychain."
        ],
        "relevant_tools": ["Xcode Instruments", "Android Profiler", "Flipper", "Fastlane"],
        "authoritative_references": [
            "Apple Human Interface Guidelines & iOS Architecture Guides",
            "Android Developer Guides & Architecture Guidelines (developer.android.com)"
        ]
    },
    {
        "id": "web-engineering",
        "name": "Web Engineering",
        "category": "architecture",
        "description": "Modern web platform standards, Core Web Vitals, SSR/SSG architectures, and browser performance.",
        "activation_conditions": [
            "Architecting web applications, portals, and e-commerce platforms",
            "Optimizing Core Web Vitals (LCP, INP, CLS)",
            "Designing client-side caching, service workers, and SEO foundations"
        ],
        "required_knowledge": [
            "Core Web Vitals: Largest Contentful Paint (LCP), Interaction to Next Paint (INP), Cumulative Layout Shift (CLS)",
            "Rendering paradigms: Client-Side Rendering (CSR), Server-Side Rendering (SSR), Static Site Generation (SSG), Incremental Static Regeneration (ISR)",
            "HTTP caching, Cache-Control headers, CDN edge routing, and service workers",
            "Web security: Content Security Policy (CSP), CORS, SameSite cookies"
        ],
        "execution_methodology": [
            "1. Architecture Selection: Choose optimal rendering model (SSR for content/SEO, CSR for rich apps).",
            "2. Asset Optimization: Configure responsive image pipelines (AVIF/WebP), font subsetting, and critical CSS.",
            "3. Code Splitting: Implement dynamic imports to minimize initial JavaScript bundle size.",
            "4. Caching & CDN: Configure immutable asset caching with content hashes and stale-while-revalidate.",
            "5. Security Hardening: Implement strict Content Security Policy headers and secure cookies.",
            "6. Performance Audit: Run automated Lighthouse and WebPageTest checks in CI."
        ],
        "best_practices": [
            "Preload critical fonts and hero images; lazy-load all below-the-fold media.",
            "Set explicit width and height dimensions on images and containers to prevent CLS.",
            "Keep initial JavaScript bundle size below 150KB gzipped."
        ],
        "common_mistakes": [
            "Blocking DOM rendering with render-blocking synchronous scripts in <head>.",
            "Serving uncompressed, full-resolution JPEG/PNG images to mobile viewports.",
            "Permitting layout shifts from dynamically injected advertisements or widgets."
        ],
        "validation_criteria": [
            "Lighthouse Performance score >= 90.",
            "LCP < 2.5s, INP < 200ms, CLS < 0.1 on emulated mobile device.",
            "Strict CSP header configured and verified without console evaluation errors."
        ],
        "relevant_tools": ["Lighthouse", "WebPageTest", "Chrome DevTools", "Bundle Analyzer"],
        "authoritative_references": [
            "web.dev: Learn Web Vitals & Web Performance Guidelines",
            "MDN Web Docs: Web Security and HTTP Headers"
        ]
    },
    {
        "id": "desktop-engineering",
        "name": "Desktop Engineering",
        "category": "architecture",
        "description": "Cross-platform desktop application engineering with Electron, Tauri, Flutter Desktop, and OS integration.",
        "activation_conditions": [
            "Building native desktop applications for Windows, macOS, and Linux",
            "Implementing desktop IPC, native system menus, and tray management",
            "Packaging installers, code signing, and auto-updating"
        ],
        "required_knowledge": [
            "Desktop architectures: Electron (Chromium + Node), Tauri (Rust + Webview), Flutter Desktop",
            "Desktop window lifecycles, multi-window management, and native menus",
            "Secure Inter-Process Communication (IPC) and context isolation",
            "Desktop packaging formats: MSIX, DMG, AppImage, DEB, RPM"
        ],
        "execution_methodology": [
            "1. Framework Selection: Select Tauri for minimal memory footprint or Flutter/Electron.",
            "2. IPC Hardening: Implement strictly validated, message-based IPC bridge with contextIsolation.",
            "3. OS Integration: Implement system tray, native menus, keyboard shortcuts, and file associations.",
            "4. Auto-Update Pipeline: Configure secure, signed auto-update manifests (Sparkle, Squirrel).",
            "5. Installer Packaging: Generate target installers with bundled runtime dependencies.",
            "6. Verification: Test window resize, multi-monitor display, sleep/resume, and uninstall."
        ],
        "best_practices": [
            "Always enable contextIsolation: true and nodeIntegration: false in Electron WebPreferences.",
            "Validate and sanitize all arguments passed across IPC boundaries.",
            "Minimize idle CPU and memory consumption when window is minimized or hidden."
        ],
        "common_mistakes": [
            "Exposing raw Node.js child_process or filesystem APIs directly to the renderer process.",
            "Failing to handle high-DPI scaling across heterogeneous multi-monitor setups.",
            "Leaving zombie background processes running after main window is closed."
        ],
        "validation_criteria": [
            "Zero security warnings in Electron / Tauri security audit tools.",
            "Clean installation and uninstallation on target Windows, macOS, and Linux systems.",
            "Application cleanly terminates all child worker processes upon window exit."
        ],
        "relevant_tools": ["Tauri CLI", "Electron Forge", "electron-builder", "WiX Toolset"],
        "authoritative_references": [
            "Tauri Architecture and Security Guide (tauri.app)",
            "Electron Security Tutorial and Checklist (electronjs.org/docs)"
        ]
    },
    {
        "id": "testing-qa",
        "name": "Testing and QA",
        "category": "quality",
        "description": "Comprehensive testing pyramid strategy: unit, integration, contract, mutation, and E2E testing.",
        "activation_conditions": [
            "Defining test strategy, coverage targets, and test matrices",
            "Authoring automated test suites across all application layers",
            "Executing regression tests and evaluating test flakiness"
        ],
        "required_knowledge": [
            "Testing Pyramid: Many unit tests, moderate integration tests, few E2E tests",
            "Test Doubles taxonomy: Dummy, Stub, Spy, Mock, Fake (Martin Fowler)",
            "Test-Driven Development (TDD) Red-Green-Refactor cycle",
            "Code coverage metrics (Line, Branch, Condition) and mutation testing"
        ],
        "execution_methodology": [
            "1. Test Planning: Derive test cases directly from PRD acceptance criteria.",
            "2. Unit Testing: Author isolated tests for domain entities, algorithms, and use cases.",
            "3. Integration Testing: Test database persistence, API endpoints, and message queues.",
            "4. Contract Testing: Verify API consumer/provider contracts with Pact or OpenAPI.",
            "5. End-to-End Testing: Automate critical user journey browser tests.",
            "6. Quality Gate Verification: Verify test pass rate is 100% and coverage threshold is met."
        ],
        "best_practices": [
            "Follow the AAA pattern: Arrange, Act, Assert clearly demarcated in each test.",
            "Ensure tests are independent and idempotent: running in any order produces identical results.",
            "Test behaviors, not implementation details; do not mock what you do not own."
        ],
        "common_mistakes": [
            "Inverted test pyramid: relying almost entirely on slow, brittle E2E tests.",
            "Writing flaky tests dependent on network timing or uncoordinated sleep() intervals.",
            "Asserting against mocks instead of validating actual return values or state changes."
        ],
        "validation_criteria": [
            "100% of test suite passes without flaky retries.",
            "Line coverage >= 80% and branch coverage >= 75% on core domain modules.",
            "Test suite execution completes within CI time budget."
        ],
        "relevant_tools": ["Jest", "Vitest", "Pytest", "PHPUnit", "Playwright", "Stryker Mutation"],
        "authoritative_references": [
            "xUnit Test Patterns: Refactoring Test Code by Gerard Meszaros",
            "Working Effectively with Legacy Code by Michael Feathers"
        ]
    },
    {
        "id": "application-security",
        "name": "Application Security",
        "category": "security",
        "description": "Secure coding practices, OWASP Top 10 mitigation, cryptographic standards, and vulnerability remediation.",
        "activation_conditions": [
            "Designing authentication and authorization subsystems",
            "Security code reviews and vulnerability assessments",
            "Remediating SAST/DAST findings and patching CVEs"
        ],
        "required_knowledge": [
            "OWASP Top 10 (Injection, Broken Auth, Sensitive Data Exposure, SSRF, XSS, CSRF)",
            "Cryptographic best practices (Argon2id for passwords, AES-256-GCM for encryption)",
            "Token security: JWT signing, rotation, expiration, and revocation algorithms",
            "Input sanitization, output encoding, and parameterized database queries"
        ],
        "execution_methodology": [
            "1. Threat Identification: Map entry points, untrusted input boundaries, and sensitive data flows.",
            "2. Input Validation: Enforce strict allow-lists and schema validation on all inputs.",
            "3. Parameterization: Ensure all database interactions utilize parameterized prepared statements.",
            "4. Authentication & Authorization: Enforce strong password hashing and RBAC checks on every route.",
            "5. Sensitive Data Protection: Encrypt sensitive data at rest and in transit (TLS 1.3).",
            "6. Security Verification: Run SAST analyzers and secret scanners to certify Gate 4."
        ],
        "best_practices": [
            "Never implement custom cryptographic algorithms; use battle-tested standard libraries.",
            "Never log sensitive data (passwords, payment cards, session tokens, PII).",
            "Apply principle of least privilege to all service accounts and database users."
        ],
        "common_mistakes": [
            "Concatenating raw strings into SQL queries or shell execution strings.",
            "Hardcoding credentials or API keys into git repository code or configuration files.",
            "Relying solely on client-side validation without backend verification."
        ],
        "validation_criteria": [
            "Zero Critical or High severity findings in SAST and dependency scans.",
            "Automated secret scanning confirms zero committed secrets.",
            "All endpoints requiring authorization return 401/403 when unauthenticated."
        ],
        "relevant_tools": ["Semgrep", "SonarQube", "OWASP ZAP", "TruffleHog", "Gitleaks"],
        "authoritative_references": [
            "OWASP Top Ten & OWASP ASVS (Application Security Verification Standard)",
            "NIST SP 800-63B: Digital Identity Guidelines"
        ]
    },
    {
        "id": "devsecops",
        "name": "DevSecOps",
        "category": "infrastructure",
        "description": "Integrating automated security scanning, policy-as-code, and compliance gates into DevOps lifecycles.",
        "activation_conditions": [
            "Configuring CI/CD security scanning stages",
            "Container vulnerability scanning and base image hardening",
            "Enforcing branch protection rules and signed commits"
        ],
        "required_knowledge": [
            "Security shifting left: SAST, DAST, SCA (Software Composition Analysis), and Secret Scanning",
            "Container security: Minimal distroless base images, non-root users, vulnerability scanners (Trivy)",
            "Policy as Code (Open Policy Agent, Conftest, Kyverno)",
            "Supply chain security: SBOM generation (CycloneDX, SPDX) and artifact signing (Cosign)"
        ],
        "execution_methodology": [
            "1. Pipeline Integration: Embed SCA (npm audit, pip-audit) and SAST into pull request triggers.",
            "2. Secret Detection: Add pre-commit and CI secret scanning hooks (Gitleaks).",
            "3. Container Hardening: Author Dockerfiles using unprivileged users and distroless/alpine bases.",
            "4. Container Scanning: Execute Trivy vulnerability scans on built images in CI.",
            "5. SBOM Generation: Export Software Bill of Materials for release artifacts.",
            "6. Quality Gate Enforcer: Configure automated build failure on any High or Critical CVE."
        ],
        "best_practices": [
            "Fail CI builds immediately upon detecting newly introduced High/Critical vulnerabilities.",
            "Pin all CI third-party actions to full commit SHA hashes instead of mutable tags.",
            "Run containers with read-only root filesystems whenever feasible."
        ],
        "common_mistakes": [
            "Running containers as the default root user inside production clusters.",
            "Allowing developers to bypass CI security gates without signed executive exemption.",
            "Failing to scan transitive dependencies in lockfiles."
        ],
        "validation_criteria": [
            "CI pipeline executes SAST, SCA, and secret scanning on every pull request.",
            "Container image scan reports zero unpatched Critical vulnerabilities.",
            "SBOM artifact generated and attached to release bundle."
        ],
        "relevant_tools": ["Trivy", "Snyk", "Gitleaks", "Cosign", "Open Policy Agent"],
        "authoritative_references": [
            "NIST Special Publication 800-204: Security Strategies for Microservices",
            "CIS Benchmarks for Docker and Kubernetes"
        ]
    },
    {
        "id": "cloud-engineering",
        "name": "Cloud Engineering",
        "category": "infrastructure",
        "description": "Cloud infrastructure architecture, serverless, container orchestration, and Well-Architected frameworks.",
        "activation_conditions": [
            "Designing cloud infrastructure on GCP, AWS, or Azure",
            "Authoring Terraform / OpenTofu Infrastructure as Code",
            "Configuring cloud networking, load balancers, and managed databases"
        ],
        "required_knowledge": [
            "Cloud Well-Architected Framework: Reliability, Security, Cost, Performance, Operations",
            "Infrastructure as Code (Terraform, CloudFormation) modularization and state management",
            "Container orchestration (Kubernetes, GCP Cloud Run, AWS ECS)",
            "Cloud networking: VPC, subnets, NAT gateways, peering, and security groups"
        ],
        "execution_methodology": [
            "1. Architecture Topology: Design cloud resource diagram with multi-zone redundancy.",
            "2. IaC Definition: Author declarative Terraform modules with explicit variables and outputs.",
            "3. Networking & Security: Restrict database subnets to private access; route traffic via API Gateway.",
            "4. Observability Integration: Configure centralized cloud logging and metric dashboards.",
            "5. Cost Estimation: Calculate monthly infrastructure expenditure using pricing calculators.",
            "6. IaC Validation: Execute terraform validate, tflint, and tfsec."
        ],
        "best_practices": [
            "Store Terraform remote state in encrypted cloud storage with state locking enabled.",
            "Never open database ports (5432, 3306) to the public internet (0.0.0.0/0).",
            "Tag all cloud resources with Project, Environment, and Owner metadata for cost tracking."
        ],
        "common_mistakes": [
            "Hardcoding cloud credentials in Terraform files or provider blocks.",
            "Over-provisioning resources resulting in unnecessary cloud expenses.",
            "Creating single-zone architectures for production workloads."
        ],
        "validation_criteria": [
            "terraform validate and tflint pass with 0 errors.",
            "tfsec / checkov security scan reports zero high-severity misconfigurations.",
            "Architecture review confirms multi-AZ failover capability."
        ],
        "relevant_tools": ["Terraform", "OpenTofu", "tflint", "tfsec", "Google Cloud SDK", "AWS CLI"],
        "authoritative_references": [
            "Google Cloud Architecture Framework (cloud.google.com/architecture/framework)",
            "AWS Well-Architected Framework Documentation"
        ]
    },
    {
        "id": "cicd-engineering",
        "name": "CI/CD Engineering",
        "category": "infrastructure",
        "description": "Continuous integration, automated testing workflows, and automated continuous deployment pipelines.",
        "activation_conditions": [
            "Constructing GitHub Actions, GitLab CI, or Cloud Build pipelines",
            "Automating build, test, lint, and packaging tasks on branch pushes",
            "Configuring release tagging, semver generation, and artifact publishing"
        ],
        "required_knowledge": [
            "Declarative CI/CD pipeline syntaxes (GitHub Actions workflow YAML)",
            "Pipeline caching strategies (dependency caches, Docker layer caches)",
            "Matrix builds across OS platforms and runtime language versions",
            "Deployment strategies: Blue-Green, Canary, Rolling updates"
        ],
        "execution_methodology": [
            "1. Trigger Definition: Configure workflow triggers for pull_request and push to main.",
            "2. Job Parallelization: Split linting, testing, and security scanning into concurrent jobs.",
            "3. Dependency Caching: Cache package manager directories (node_modules, pip cache, pub cache).",
            "4. Artifact Generation: Build production binaries, containers, or web distribution bundles.",
            "5. Quality Gate Enforcement: Block PR merge if any verification job fails.",
            "6. Release Automation: Automatically generate release notes and publish packages on git tags."
        ],
        "best_practices": [
            "Ensure total CI pipeline execution time remains under 10 minutes for fast feedback.",
            "Use environment secrets and OpenID Connect (OIDC) instead of static cloud access keys.",
            "Pin action dependencies to commit SHAs to prevent supply chain poisoning."
        ],
        "common_mistakes": [
            "Allowing failing test steps to continue with continue-on-error: true.",
            "Rebuilding Docker images or recompiling code from scratch without layer caching.",
            "Granting broad write permissions (GITHUB_TOKEN) when read-only is sufficient."
        ],
        "validation_criteria": [
            "actionlint passes on all workflow YAML files with zero errors.",
            "PR pipeline successfully runs all unit tests, linters, and gate checks.",
            "Build artifacts are cleanly packaged and published to registry."
        ],
        "relevant_tools": ["GitHub Actions", "actionlint", "GitLab CI", "act (local GitHub Actions)"],
        "authoritative_references": [
            "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation by Jez Humble & David Farley",
            "GitHub Actions Documentation (docs.github.com/actions)"
        ]
    },
    {
        "id": "performance-optimization",
        "name": "Performance Optimization",
        "category": "quality",
        "description": "Profiling, bottleneck identification, algorithmic optimization, memory leak resolution, and caching.",
        "activation_conditions": [
            "Application response latency exceeds TRD SLA thresholds",
            "High CPU or memory consumption detected under load",
            "Optimizing slow database queries and computational loops"
        ],
        "required_knowledge": [
            "Big-O algorithmic time and space complexity",
            "CPU profiling, flame graphs, and memory heap dump analysis",
            "Caching hierarchies: L1 in-memory, L2 distributed (Redis), HTTP edge (CDN)",
            "Database query optimization, index tuning, and connection pooling"
        ],
        "execution_methodology": [
            "1. Benchmark Baseline: Establish statistically sound latency and memory baselines.",
            "2. Profiling: Collect flame graphs and allocation traces to pinpoint hotspots.",
            "3. Root Cause Analysis: Distinguish between I/O bottlenecks, lock contention, and algorithmic complexity.",
            "4. Targeted Optimization: Optimize critical paths (add index, vectorize loop, cache query).",
            "5. Re-benchmarking: Run identical load test to measure percentage performance improvement.",
            "6. Regression Guard: Add performance benchmark assertions into automated test suite."
        ],
        "best_practices": [
            "Never optimize without first measuring; profile production-like workloads.",
            "Target the largest bottleneck first (Amdahl's Law).",
            "Always verify that optimization preserves 100% of functional test correctness."
        ],
        "common_mistakes": [
            "Premature optimization of non-critical code paths.",
            "Introducing complex concurrency that causes race conditions or deadlocks.",
            "Relying on micro-benchmarks that do not reflect real-world memory access patterns."
        ],
        "validation_criteria": [
            "Benchmark shows measurable latency reduction meeting TRD requirement.",
            "All functional unit and integration tests remain 100% passing.",
            "Memory heap analysis confirms zero dangling references or leaks after load cycle."
        ],
        "relevant_tools": ["clinic.js", "py-spy", "pprof", "Apache Bench", "k6", "Redis"],
        "authoritative_references": [
            "Systems Performance: Enterprise and the Cloud by Brendan Gregg",
            "High Performance Browser Networking by Ilya Grigorik"
        ]
    },
    {
        "id": "accessibility-engineering",
        "name": "Accessibility Engineering",
        "category": "quality",
        "description": "Accessible software design, WCAG 2.1 AA/AAA compliance, screen readers, and universal design.",
        "activation_conditions": [
            "Authoring or modifying frontend web and mobile user interfaces",
            "Running accessibility audits and remediating compliance defects",
            "Ensuring keyboard navigation and assistive technology compatibility"
        ],
        "required_knowledge": [
            "WCAG 2.1 guidelines (Perceivable, Operable, Understandable, Robust)",
            "Accessible Rich Internet Applications (WAI-ARIA) roles, states, and properties",
            "Color contrast requirements: 4.5:1 for normal text, 3:1 for large text / UI elements",
            "Screen reader interaction paradigms (VoiceOver, NVDA, TalkBack)"
        ],
        "execution_methodology": [
            "1. Semantic Markup: Utilize native semantic HTML elements (<button>, <main>, <nav>, <form>).",
            "2. Keyboard Traversal: Ensure all interactive elements have visible focus indicators and logical tab order.",
            "3. ARIA Implementation: Add aria-label, aria-expanded, and role attributes where native HTML is insufficient.",
            "4. Contrast Verification: Verify all text against background using color contrast analyzers.",
            "5. Automated Audit: Run axe-core / Lighthouse accessibility audits in automated tests.",
            "6. Manual Screen Reader Check: Test critical workflows with NVDA or VoiceOver."
        ],
        "best_practices": [
            "First rule of ARIA: Do not use ARIA if a native HTML element provides the required behavior.",
            "Never remove default CSS outline: none without providing an accessible :focus-visible replacement.",
            "Ensure all form controls have explicitly associated <label> elements."
        ],
        "common_mistakes": [
            "Using generic <div> or <span> elements as click handlers without keyboard event listeners.",
            "Empty alt attributes on informative images or missing alt on decorative images.",
            "Inaccessible modal dialogs that fail to trap focus inside the modal."
        ],
        "validation_criteria": [
            "Automated axe-core / Lighthouse audit reports zero WCAG 2.1 AA violations.",
            "Complete keyboard navigation possible across all user journeys without a mouse.",
            "All interactive controls announce meaningful labels in screen readers."
        ],
        "relevant_tools": ["axe-core", "Lighthouse", "WAVE Evaluation Tool", "Colour Contrast Analyser"],
        "authoritative_references": [
            "W3C Web Content Accessibility Guidelines (WCAG) 2.1",
            "WAI-ARIA Authoring Practices Guide (APG)"
        ]
    },
    {
        "id": "software-migration",
        "name": "Software Migration",
        "category": "architecture",
        "description": "Database migrations, framework upgrades, language migrations, and backward-compatible data evolution.",
        "activation_conditions": [
            "Upgrading major framework or runtime versions (e.g., Python 3.9 -> 3.12, Node 18 -> 22)",
            "Migrating monolithic database schemas or switching database engines",
            "Replacing deprecated third-party libraries across a codebase"
        ],
        "required_knowledge": [
            "Strangler Fig pattern for incremental component replacement",
            "Expand-Contract (Parallel Run) database migration pattern",
            "Semantic Versioning (SemVer) and deprecation analysis",
            "Automated AST refactoring tools (jscodeshift, OpenRewrite, Bowler)"
        ],
        "execution_methodology": [
            "1. Dependency Audit: Inspect lockfiles and release notes to map all breaking changes.",
            "2. Baseline Establishment: Run full test suite on pre-migration codebase to establish green baseline.",
            "3. Dual-Read / Dual-Write: Implement dual-adapter layer to support both legacy and new contracts.",
            "4. Incremental Migration: Migrate individual modules or endpoints behind feature flags.",
            "5. Verification: Execute regression suites and compare output equivalence.",
            "6. Decommissioning: Remove legacy code paths and deprecation shims once cutover is certified."
        ],
        "best_practices": [
            "Never attempt a big-bang rewrite; migrate incrementally with continuous verification.",
            "Keep migration PRs small, isolated, and reversible.",
            "Maintain comprehensive regression test suites that run against both old and new implementations."
        ],
        "common_mistakes": [
            "Upgrading multiple major dependencies simultaneously making root cause analysis impossible.",
            "Failing to plan for rollbacks if the new runtime fails under production load.",
            "Deleting legacy database columns before all client versions have stopped querying them."
        ],
        "validation_criteria": [
            "100% of baseline regression tests pass on the migrated system.",
            "Zero deprecated API warnings emitted during build or runtime.",
            "Rollback plan documented and verified in staging environment."
        ],
        "relevant_tools": ["OpenRewrite", "jscodeshift", "git diff", "AST Grep"],
        "authoritative_references": [
            "Monolith to Microservices by Sam Newman",
            "Refactoring Databases: Evolutionary Database Design by Scott Ambler & Pramod Sadalage"
        ]
    },
    {
        "id": "legacy-modernization",
        "name": "Legacy Modernization",
        "category": "architecture",
        "description": "Techniques for refactoring legacy codebases, adding characterization tests, and reducing technical debt.",
        "activation_conditions": [
            "Onboarding existing brownfield repositories with undocumented legacy code",
            "Refactoring complex legacy functions with high cyclomatic complexity",
            "Rescuing codebases with zero automated test coverage"
        ],
        "required_knowledge": [
            "Characterization Testing: Writing tests to capture current system behavior, flaws included",
            "Sprout Method and Wrap Method refactoring techniques (Michael Feathers)",
            "Sensing Variables and Seams to isolate untestable dependencies",
            "Static code smell identification (Shotgun Surgery, Feature Envy, Long Method)"
        ],
        "execution_methodology": [
            "1. Discovery & Profiling: Map application entry points and dependency graph without modifying code.",
            "2. Seam Identification: Locate insertion points where dependencies can be intercepted.",
            "3. Characterization Tests: Author golden master tests capturing exact current input/output pairs.",
            "4. Scoped Refactoring: Apply safe, automated refactorings (extract method, rename) under green tests.",
            "5. Modern Architecture Introduction: Introduce Clean Architecture interfaces via Strangler Fig.",
            "6. Regression Certification: Verify characterization tests remain green after each step."
        ],
        "best_practices": [
            "Never change code behavior and structure at the same time; separate refactoring from bug fixes.",
            "Protect all user uncommitted work; inspect git status before modifying files.",
            "Use version control commits after every single passing micro-refactoring."
        ],
        "common_mistakes": [
            "Attempting to rewrite entire modules from scratch without understanding legacy edge cases.",
            "Fixing 'bugs' in legacy code before verifying if downstream clients rely on that behavior.",
            "Refactoring without automated characterization tests in place."
        ],
        "validation_criteria": [
            "Golden master characterization tests verify zero unintended behavioral divergence.",
            "Cyclomatic complexity of target modules reduced measurably.",
            "Existing project build and tests pass without regression."
        ],
        "relevant_tools": ["ApprovalTests", "Michael Feathers Seam Tooling", "SonarQube", "git"],
        "authoritative_references": [
            "Working Effectively with Legacy Code by Michael Feathers",
            "Refactoring: Improving the Design of Existing Code (2nd Edition) by Martin Fowler"
        ]
    },
    {
        "id": "documentation-engineering",
        "name": "Documentation Engineering",
        "category": "infrastructure",
        "description": "Technical writing, API documentation, Mermaid diagramming, and markdown linting.",
        "activation_conditions": [
            "Authoring READMEs, architecture summaries, and developer portals",
            "Generating API references from code comments and OpenAPI specifications",
            "Verifying internal documentation links and code examples"
        ],
        "required_knowledge": [
            "Diátaxis documentation framework (Tutorials, How-To Guides, Reference, Explanation)",
            "GitHub Flavored Markdown (GFM) and alert syntax (> [!NOTE], > [!IMPORTANT])",
            "Mermaid.js diagramming syntax (flowcharts, sequence diagrams, state diagrams)",
            "Automated link checking and markdown linting rules"
        ],
        "execution_methodology": [
            "1. Audience Analysis: Determine developer reader personas and operational intent.",
            "2. Documentation Categorization: Structure content using the Diátaxis framework.",
            "3. Visual Architecture: Author Mermaid.js diagrams illustrating data flows and states.",
            "4. Code Snippet Testing: Ensure every documented command and snippet is verified executable.",
            "5. Link & Formatting Verification: Run markdownlint and markdown-link-check.",
            "6. Synchronization: Ensure documentation matches current codebase release tag."
        ],
        "best_practices": [
            "Keep documentation as close to the code as possible (docs/ and README.md).",
            "Use clear, active voice and provide copyable CLI commands with expected outputs.",
            "Include architecture decision context alongside pure procedural guides."
        ],
        "common_mistakes": [
            "Documenting aspirational features that have not yet been implemented.",
            "Letting code snippets fall out of sync with actual API changes.",
            "Writing wall-of-text documentation without visual diagrams or tables."
        ],
        "validation_criteria": [
            "markdownlint passes with zero formatting errors.",
            "Zero broken internal links or 404 image URLs.",
            "All documented terminal commands execute cleanly in a fresh workspace."
        ],
        "relevant_tools": ["markdownlint", "markdown-link-check", "Mermaid.js", "TypeDoc / JSDoc"],
        "authoritative_references": [
            "Diátaxis Documentation Framework (diataxis.fr)",
            "Docs for Developers: An Engineer's Field Guide to Technical Writing"
        ]
    }
]

catalog = {
    "total_skills": len(skills_data),
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

for skill in skills_data:
    skill_id = skill["id"]
    category = skill["category"]
    skill_dir = os.path.join(SKILLS_DIR, skill_id)
    os.makedirs(skill_dir, exist_ok=True)
    
    # Write flat SKILL.md directly inside the skill directory (no subdirectories!)
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    activation_str = "\n".join([f"- {c}" for c in skill["activation_conditions"]])
    knowledge_str = "\n".join([f"- {k}" for k in skill["required_knowledge"]])
    methodology_str = "\n".join([f"- {m}" for m in skill["execution_methodology"]])
    best_practices_str = "\n".join([f"- {b}" for b in skill["best_practices"]])
    common_mistakes_str = "\n".join([f"- {m}" for m in skill["common_mistakes"]])
    validation_str = "\n".join([f"- {v}" for v in skill["validation_criteria"]])
    tools_str = ", ".join(skill["relevant_tools"])
    references_str = "\n".join([f"- {r}" for r in skill["authoritative_references"]])
    
    content = f"""# Skill: {skill["name"]} (`{skill_id}`)

## 1. Purpose
{skill["description"]}

## 2. Activation Conditions
{activation_str}

## 3. Required Knowledge
{knowledge_str}

## 4. Execution Methodology
{methodology_str}

## 5. Best Practices
{best_practices_str}

## 6. Common Mistakes to Avoid
{common_mistakes_str}

## 7. Validation Criteria
{validation_str}

## 8. Relevant Tools
`{tools_str}`

## 9. Authoritative References
{references_str}
"""
    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    catalog["categories"][category].append(skill_id)
    catalog["skills"][skill_id] = {
        "name": skill["name"],
        "category": category,
        "description": skill["description"],
        "path": f".agentic/skills/{skill_id}/SKILL.md"
    }

catalog_path = os.path.join(SKILLS_DIR, "catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2)

print(f"Successfully generated {len(skills_data)} skills and catalog at {catalog_path}")
