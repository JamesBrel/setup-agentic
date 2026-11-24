# Skill: Database Architecture (`database-architecture`)

## 1. Purpose
Relational and NoSQL data modeling, schema migration engineering, indexing, and ACID guarantees.

## 2. Activation Conditions
- Database schema creation or modification
- Writing migration scripts and rollback procedures
- Optimizing slow queries and configuring indices

## 3. Required Knowledge
- Relational normalization (1NF, 2NF, 3NF, BCNF) and deliberate denormalization
- Index architectures (B-Tree, Hash, GIN, GiST) and query execution EXPLAIN plans
- ACID transactions, isolation levels, and optimistic vs pessimistic locking
- Zero-downtime migration patterns (Expand-Contract / Parallel Run)

## 4. Execution Methodology
- 1. Entity-Relationship Modeling: Map entities, cardinality, and referential integrity.
- 2. DDL Drafting: Specify tables, strict column types, NOT NULL defaults, and constraints.
- 3. Indexing Strategy: Create indices for foreign keys and query predicate columns.
- 4. Migration Authoring: Write reversible up() and down() migration scripts.
- 5. Reversibility Verification: Execute migrate -> rollback -> migrate in test environment.
- 6. Query Optimization: Inspect EXPLAIN ANALYZE output to eliminate sequential scans on large tables.

## 5. Best Practices
- Always use UTC timestamps for created_at and updated_at columns.
- Ensure every foreign key has a supporting index to avoid table locks.
- Use transactions inside migrations to ensure atomic schema changes.

## 6. Common Mistakes to Avoid
- Missing down() rollback logic or non-reversible migration statements.
- Over-indexing tables leading to severe write performance degradation.
- Storing unhashed passwords or plain-text PII in database columns.

## 7. Validation Criteria
- Automated test executes migration and complete rollback without errors.
- Zero unindexed foreign keys in relational schema.
- EXPLAIN output confirms index scan utilization for primary query filters.

## 8. Relevant Tools
`PostgreSQL, MySQL, SQLite, Prisma, Doctrine, Eloquent`

## 9. Authoritative References
- Designing Data-Intensive Applications by Martin Kleppmann
- SQL Antipatterns: Avoiding the Pitfalls of Database Programming by Bill Karwin
