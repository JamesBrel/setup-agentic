# Skill: Java Engineering (`java-engineering`)

## 1. Purpose
Enterprise Java development with Spring Boot, JPA/Hibernate, Gradle/Maven, and JUnit 5.

## 2. Activation Conditions
- Building enterprise Java services, Spring Boot applications, or Kafka consumers
- Authoring JPA entities, repositories, and transactional services
- Enforcing code style with Checkstyle, SpotBugs, and SonarQube

## 3. Required Knowledge
- Modern Java (Java 17 / 21 LTS: records, sealed interfaces, virtual threads)
- Spring Boot 3 ecosystem (Spring Data JPA, Spring Security, Actuator)
- JPA lifecycle, entity relationships, and second-level caching
- JUnit 5, Mockito, and Testcontainers for integration testing

## 4. Execution Methodology
- 1. Project Scaffolding: Configure build.gradle.kts or pom.xml with dependencies.
- 2. Domain Model: Define JPA entities with proper equals/hashCode on immutable identifiers.
- 3. Repositories: Implement Spring Data repositories with explicit query methods.
- 4. Service Layer: Implement transactional use cases with @Transactional(readOnly = true).
- 5. Controller Layer: Implement REST endpoints with OpenAPI annotations and bean validation.
- 6. Verification: Execute gradle test check or mvn verify with Testcontainers.

## 5. Best Practices
- Use Java records for immutable Data Transfer Objects (DTOs).
- Use Testcontainers for authentic database and message queue integration tests.
- Explicitly define fetch = FetchType.LAZY on all @ManyToOne and @OneToOne JPA mappings.

## 6. Common Mistakes to Avoid
- Using default FetchType.EAGER causing massive unintended join queries.
- Calling transactional methods from within the same class (bypassing Spring proxies).
- Catching Throwable or generic Exception.

## 7. Validation Criteria
- Gradle / Maven build compiles with zero warnings.
- Checkstyle and SpotBugs report zero violations.
- All unit and Testcontainers integration tests pass.

## 8. Relevant Tools
`Gradle, Maven, Spring Boot, Testcontainers, JUnit 5, SpotBugs`

## 9. Authoritative References
- Effective Java (3rd Edition) by Joshua Bloch
- Spring Framework Documentation (spring.io)
