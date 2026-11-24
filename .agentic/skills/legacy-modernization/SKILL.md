# Skill: Legacy Modernization (`legacy-modernization`)

## 1. Purpose
Techniques for refactoring legacy codebases, adding characterization tests, and reducing technical debt.

## 2. Activation Conditions
- Onboarding existing brownfield repositories with undocumented legacy code
- Refactoring complex legacy functions with high cyclomatic complexity
- Rescuing codebases with zero automated test coverage

## 3. Required Knowledge
- Characterization Testing: Writing tests to capture current system behavior, flaws included
- Sprout Method and Wrap Method refactoring techniques (Michael Feathers)
- Sensing Variables and Seams to isolate untestable dependencies
- Static code smell identification (Shotgun Surgery, Feature Envy, Long Method)

## 4. Execution Methodology
- 1. Discovery & Profiling: Map application entry points and dependency graph without modifying code.
- 2. Seam Identification: Locate insertion points where dependencies can be intercepted.
- 3. Characterization Tests: Author golden master tests capturing exact current input/output pairs.
- 4. Scoped Refactoring: Apply safe, automated refactorings (extract method, rename) under green tests.
- 5. Modern Architecture Introduction: Introduce Clean Architecture interfaces via Strangler Fig.
- 6. Regression Certification: Verify characterization tests remain green after each step.

## 5. Best Practices
- Never change code behavior and structure at the same time; separate refactoring from bug fixes.
- Protect all user uncommitted work; inspect git status before modifying files.
- Use version control commits after every single passing micro-refactoring.

## 6. Common Mistakes to Avoid
- Attempting to rewrite entire modules from scratch without understanding legacy edge cases.
- Fixing 'bugs' in legacy code before verifying if downstream clients rely on that behavior.
- Refactoring without automated characterization tests in place.

## 7. Validation Criteria
- Golden master characterization tests verify zero unintended behavioral divergence.
- Cyclomatic complexity of target modules reduced measurably.
- Existing project build and tests pass without regression.

## 8. Relevant Tools
`ApprovalTests, Michael Feathers Seam Tooling, SonarQube, git`

## 9. Authoritative References
- Working Effectively with Legacy Code by Michael Feathers
- Refactoring: Improving the Design of Existing Code (2nd Edition) by Martin Fowler
