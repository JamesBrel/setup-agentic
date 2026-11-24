# Skill: Testing and QA (`testing-qa`)

## 1. Purpose
Comprehensive testing pyramid strategy: unit, integration, contract, mutation, and E2E testing.

## 2. Activation Conditions
- Defining test strategy, coverage targets, and test matrices
- Authoring automated test suites across all application layers
- Executing regression tests and evaluating test flakiness

## 3. Required Knowledge
- Testing Pyramid: Many unit tests, moderate integration tests, few E2E tests
- Test Doubles taxonomy: Dummy, Stub, Spy, Mock, Fake (Martin Fowler)
- Test-Driven Development (TDD) Red-Green-Refactor cycle
- Code coverage metrics (Line, Branch, Condition) and mutation testing

## 4. Execution Methodology
- 1. Test Planning: Derive test cases directly from PRD acceptance criteria.
- 2. Unit Testing: Author isolated tests for domain entities, algorithms, and use cases.
- 3. Integration Testing: Test database persistence, API endpoints, and message queues.
- 4. Contract Testing: Verify API consumer/provider contracts with Pact or OpenAPI.
- 5. End-to-End Testing: Automate critical user journey browser tests.
- 6. Quality Gate Verification: Verify test pass rate is 100% and coverage threshold is met.

## 5. Best Practices
- Follow the AAA pattern: Arrange, Act, Assert clearly demarcated in each test.
- Ensure tests are independent and idempotent: running in any order produces identical results.
- Test behaviors, not implementation details; do not mock what you do not own.

## 6. Common Mistakes to Avoid
- Inverted test pyramid: relying almost entirely on slow, brittle E2E tests.
- Writing flaky tests dependent on network timing or uncoordinated sleep() intervals.
- Asserting against mocks instead of validating actual return values or state changes.

## 7. Validation Criteria
- 100% of test suite passes without flaky retries.
- Line coverage >= 80% and branch coverage >= 75% on core domain modules.
- Test suite execution completes within CI time budget.

## 8. Relevant Tools
`Jest, Vitest, Pytest, PHPUnit, Playwright, Stryker Mutation`

## 9. Authoritative References
- xUnit Test Patterns: Refactoring Test Code by Gerard Meszaros
- Working Effectively with Legacy Code by Michael Feathers
