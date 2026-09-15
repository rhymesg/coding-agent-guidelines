---
name: run-qa-pass
description: "Use when the user asks for a quality-assurance pass, a QA pass, or this skill by name. Do not start it on your own. Checks tests, cleanliness, runtime, documentation, lint and formatting of a whole project, fixing and committing step by step."
---

# Run a QA Pass

Bring a project through every quality check in one long task and leave each fix committed.

## Setup

- Set up a workplan with the `create-workplan` skill. Its tasks are the steps below, in order.
- Work in a linked worktree of the project.
- Commit each step's changes with the `commit` skill before starting the next step.
- Every fix must leave all tests passing.
- When a finding needs a test change to apply, report it instead of applying it.

## Steps

1. Test guidelines: check that tests exist and cover what the `unit-test-guidelines`, `integration-test-guidelines`, and the project's other test guidelines require. Fix the gaps.
2. Tests: run all tests, unit, integration and regression. Find and fix the cause of each failure until all pass.
3. Clean-up: apply the rules of the `clean-up` skill to the whole codebase, in the project's primary language only. Fix the findings.
4. Runtime optimization: read `docs/runtime-optimization.md` and the commit history. Use the `optimize-runtime` skill on obvious parts only when the document is missing, or when 20 or more commits since its last entry touched the files that entry names as hot paths. Otherwise record that no optimization is due.
5. Documentation: check Doxygen comments and generated documents against the project's Doxygen guidelines and fix the findings. Then review and update the project's documents, usually `README.md` and `docs/`, following the `document-writing-guidelines` and `sync-docs` skills.
6. Format: run the project's formatter.
7. Lint: run the project's linter, for example clang-tidy, and fix the findings.
8. Final verification: run all tests and the project's verification procedures, such as verification skills, make targets or documented checks, when it has them. On a failure, fix it, run `sync-docs` on the touched files, and repeat from step 6.

## Report

- Each step's result, the commits it made, and the suggestions left open.
