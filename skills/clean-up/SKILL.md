---
name: clean-up
description: Use when unmerged changes add more than 100 lines of non-generated source code since the last cleanup or relative to the base branch.
---

# Clean Up

Remove unnecessary or unused code and reduce complexity and code volume while preserving required behavior.

## Workflow

1. Read available plans, design documents, and other relevant project documents alongside the user's requirements, and use them as the basis for cleanup decisions.
2. Before refactoring, ensure tests verify the required behavior across normal cases, edge cases, and failure conditions, and confirm they pass.
3. Review code and commits for abandoned attempts, unused code, duplication, and unnecessary abstractions against the requirements and available documents.
4. Drop wholly unnecessary commits. Remove remaining unnecessary code and simplify the rest.
5. After cleanup, use the `sync-docs` skill and confirm relevant tests and lint pass. Run broader verification procedures when available and report the results.
6. Commit remaining verified changes as new commits using the `commit` skill.
