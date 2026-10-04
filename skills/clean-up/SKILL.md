---
name: clean-up
description: "Simplifies code and documents while preserving required behavior. Use when the user asks to clean up code or documents."
---

# Clean Up

- Cover the tracked files the project owns; leave out vendored code and data files.

## Workflow

1. Read available plans, design documents, and other relevant project documents alongside the user's requirements, and use them as the basis for cleanup decisions.
2. Before refactoring, ensure tests cover the behavior the cleanup touches, including its edge cases and failure conditions where they exist, and confirm they pass.
3. Review code and commits for abandoned attempts, unused code, duplication, and unnecessary abstractions against the requirements and available documents.
4. Keep every option a user can set, such as public API, parameters, flags, and arguments, even when nothing uses it. Remove code that nothing calls.
5. When another part of the codebase already does the same thing, call it instead, or extend that code to cover the new case.
6. Revert a commit whose whole change is unnecessary instead of editing its content out. Remove remaining unnecessary code and simplify the rest.
7. Remove documents and sections that duplicate other documents or the code, hold temporary information, or record design history or a replaced design. Move still-useful content into the document that owns it first.
8. Remove only what is clearly unneeded. Keep anything that needs a judgment call, and list it in the final report.
9. After cleanup, use the [sync-documents](../sync-documents/SKILL.md) skill and confirm relevant tests and lint pass. Run broader verification procedures when available and report the results.
