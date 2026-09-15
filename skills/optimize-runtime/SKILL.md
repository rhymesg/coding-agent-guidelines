---
name: optimize-runtime
description: Use when the user requests execution-time optimization or bottleneck removal.
---

# Optimize Runtime

Optimize measured bottlenecks and report the method and before-and-after results.

## Workflow

1. Inspect the processing flow and existing tests. Define representative workloads, measurement boundaries, and optimization goals.
2. Measure each part with suitable tools, such as perf for CPU profiling or Cachegrind for instruction counts. Distinguish computation from waiting.
3. Build the nominal-run table: each part's calls per unit of operation (for example 400 propagations and 20 image updates per second), its time, and its share of the total. The largest shares are the bottlenecks and set the order of work.
4. Before changing a bottleneck, review regression coverage for the affected behavior. Reuse existing tests and fill coverage gaps. Verify they pass and record repeated timing baselines.
5. Optimize one bottleneck at a time. Run regression tests before and after each change; compare execution time and output quality, then re-profile.
6. For successful optimizations, add or update execution-time regression tests without duplication when measurements are stable; otherwise, keep benchmarks and report limitations.
7. Commit each successful optimization and its related tests using the `commit` skill, then update `docs/runtime-optimization.md` with the measured before-and-after code hashes.

## Guidelines

- Preserve outputs by default. Allow small quality losses for large runtime gains within agreed limits; document tradeoffs and test expectation changes.
- Consider the target execution environment when measuring elsewhere.
- Compare in the same execution environment with only the optimization changed. Repeat measurements and report variability.
- Measure actual completion time separately from profiling overhead. Treat cycle and instruction counts as supporting metrics.

### Report

- Create or update `docs/runtime-optimization.md` in the repository being optimized with a [results table](templates/runtime-optimization.md). Integrate findings into relevant sections while preserving historical comparisons.
- Put the nominal-run table first, with the after column and shares filled in and the overall improvement of the nominal run under it; the per-part and per-change tables follow.
- Reference the measured code commits, not report commits. Keep uncommitted measurements provisional until that exact code is committed; remeasure if it changes.
- Cover bottlenecks, environment, performance measurement methods, quality tradeoffs, and useful unsuccessful attempts.
