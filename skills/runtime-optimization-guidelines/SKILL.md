---
name: runtime-optimization-guidelines
description: Use when the user requests execution-time optimization or bottleneck removal.
---

# Runtime Optimization Guidelines

Optimize measured bottlenecks and report the method and before-and-after results.

## Workflow

1. Check for an existing workplan for the same optimization. Use the `workplan` skill to continue it or create one.
2. Inspect the processing flow and existing tests. Define representative workloads, measurement boundaries, and optimization goals.
3. Identify bottlenecks with suitable tools, such as perf for CPU profiling or Cachegrind for instruction counts. Distinguish computation from waiting.
4. Before changing a bottleneck, review regression coverage for the affected behavior. Reuse existing tests and fill coverage gaps. Verify they pass and record repeated timing baselines.
5. Optimize one bottleneck at a time. Run regression tests before and after each change; compare execution time and output quality, then re-profile.
6. Add or update execution-time regression tests without duplication when measurements are stable; otherwise, keep benchmarks and report limitations.

## Guidelines

- Preserve outputs by default. Allow small quality losses for large runtime gains within agreed limits; document tradeoffs and test expectation changes.
- Consider execution on the final deployment computer even when measuring on a desktop.
- Compare on the same machine with only the optimization changed. Repeat measurements and report variability.
- Measure actual completion time separately from profiling overhead. Treat cycle and instruction counts as supporting metrics.

## Report

- Describe the bottleneck, measurement method, optimization, and setup needed to reproduce the comparison.
- Compare baseline and candidate execution time and output quality in a table. Include variability and explain any quality-versus-runtime tradeoff.
- Report correctness and regression checks, goal attainment, and remaining issues or unverified results.
