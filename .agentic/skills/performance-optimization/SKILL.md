# Skill: Performance Optimization (`performance-optimization`)

## 1. Purpose
Profiling, bottleneck identification, algorithmic optimization, memory leak resolution, and caching.

## 2. Activation Conditions
- Application response latency exceeds TRD SLA thresholds
- High CPU or memory consumption detected under load
- Optimizing slow database queries and computational loops

## 3. Required Knowledge
- Big-O algorithmic time and space complexity
- CPU profiling, flame graphs, and memory heap dump analysis
- Caching hierarchies: L1 in-memory, L2 distributed (Redis), HTTP edge (CDN)
- Database query optimization, index tuning, and connection pooling

## 4. Execution Methodology
- 1. Benchmark Baseline: Establish statistically sound latency and memory baselines.
- 2. Profiling: Collect flame graphs and allocation traces to pinpoint hotspots.
- 3. Root Cause Analysis: Distinguish between I/O bottlenecks, lock contention, and algorithmic complexity.
- 4. Targeted Optimization: Optimize critical paths (add index, vectorize loop, cache query).
- 5. Re-benchmarking: Run identical load test to measure percentage performance improvement.
- 6. Regression Guard: Add performance benchmark assertions into automated test suite.

## 5. Best Practices
- Never optimize without first measuring; profile production-like workloads.
- Target the largest bottleneck first (Amdahl's Law).
- Always verify that optimization preserves 100% of functional test correctness.

## 6. Common Mistakes to Avoid
- Premature optimization of non-critical code paths.
- Introducing complex concurrency that causes race conditions or deadlocks.
- Relying on micro-benchmarks that do not reflect real-world memory access patterns.

## 7. Validation Criteria
- Benchmark shows measurable latency reduction meeting TRD requirement.
- All functional unit and integration tests remain 100% passing.
- Memory heap analysis confirms zero dangling references or leaks after load cycle.

## 8. Relevant Tools
`clinic.js, py-spy, pprof, Apache Bench, k6, Redis`

## 9. Authoritative References
- Systems Performance: Enterprise and the Cloud by Brendan Gregg
- High Performance Browser Networking by Ilya Grigorik
