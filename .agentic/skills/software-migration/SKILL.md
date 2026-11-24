# Skill: Software Migration (`software-migration`)

## 1. Purpose
Database migrations, framework upgrades, language migrations, and backward-compatible data evolution.

## 2. Activation Conditions
- Upgrading major framework or runtime versions (e.g., Python 3.9 -> 3.12, Node 18 -> 22)
- Migrating monolithic database schemas or switching database engines
- Replacing deprecated third-party libraries across a codebase

## 3. Required Knowledge
- Strangler Fig pattern for incremental component replacement
- Expand-Contract (Parallel Run) database migration pattern
- Semantic Versioning (SemVer) and deprecation analysis
- Automated AST refactoring tools (jscodeshift, OpenRewrite, Bowler)

## 4. Execution Methodology
- 1. Dependency Audit: Inspect lockfiles and release notes to map all breaking changes.
- 2. Baseline Establishment: Run full test suite on pre-migration codebase to establish green baseline.
- 3. Dual-Read / Dual-Write: Implement dual-adapter layer to support both legacy and new contracts.
- 4. Incremental Migration: Migrate individual modules or endpoints behind feature flags.
- 5. Verification: Execute regression suites and compare output equivalence.
- 6. Decommissioning: Remove legacy code paths and deprecation shims once cutover is certified.

## 5. Best Practices
- Never attempt a big-bang rewrite; migrate incrementally with continuous verification.
- Keep migration PRs small, isolated, and reversible.
- Maintain comprehensive regression test suites that run against both old and new implementations.

## 6. Common Mistakes to Avoid
- Upgrading multiple major dependencies simultaneously making root cause analysis impossible.
- Failing to plan for rollbacks if the new runtime fails under production load.
- Deleting legacy database columns before all client versions have stopped querying them.

## 7. Validation Criteria
- 100% of baseline regression tests pass on the migrated system.
- Zero deprecated API warnings emitted during build or runtime.
- Rollback plan documented and verified in staging environment.

## 8. Relevant Tools
`OpenRewrite, jscodeshift, git diff, AST Grep`

## 9. Authoritative References
- Monolith to Microservices by Sam Newman
- Refactoring Databases: Evolutionary Database Design by Scott Ambler & Pramod Sadalage
