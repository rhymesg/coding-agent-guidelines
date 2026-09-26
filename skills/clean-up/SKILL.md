---
name: clean-up
description: "Simplifies code while preserving required behavior. Use when unmerged changes add more than 100 lines of non-generated source code since the last cleanup or relative to the base branch."
---

# Clean Up

## Workflow

1. Read available plans, design documents, and other relevant project documents alongside the user's requirements, and use them as the basis for cleanup decisions.
2. Before refactoring, ensure tests verify the required behavior across normal cases, edge cases, and failure conditions, and confirm they pass.
3. Review code and commits for abandoned attempts, unused code, duplication, and unnecessary abstractions against the requirements and available documents.
4. Among the unused code, separate the options the public API offers to a library user from the stale code no caller reaches. Keep the options, remove the stale code.
5. When another part of the codebase already does the same thing, call it instead, or extend that code to cover the new case.
6. Drop wholly unnecessary commits. Remove remaining unnecessary code and simplify the rest.
7. After cleanup, use the [sync-documents](../sync-documents/SKILL.md) skill and confirm relevant tests and lint pass. Run broader verification procedures when available and report the results.
8. When the user requests a commit, use the [commit](../commit/SKILL.md) skill to commit verified changes.
