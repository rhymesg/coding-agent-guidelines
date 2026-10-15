---
name: clean-up
description: "Simplifies code and documents while preserving required behavior. Use when the user asks to clean up code or documents."
---

# Clean Up

- Cover the tracked files the project owns; leave out vendored code and data files.

## Workflow

1. Read available plans, design documents, and other relevant project documents alongside the user's requirements, and use them as the basis for cleanup decisions.
2. Before refactoring, ensure tests cover the behavior the cleanup touches and pass.
3. Review code and commits against the requirements and available documents for:
   - Leftovers: abandoned attempts and unused code. Keep an uncalled function that is public API; remove one that is stale, replaced, or abandoned.
   - Duplication and unnecessary abstractions: the same thing done in several ways, one setting named by several keys, or one job done by two mechanisms.
   - Growth: over-configurability, conditional complexity, and feature creep.
   - Options that choose nothing: nothing sets it, every caller sets it the same way, two switches are always set together, or a flag has one value at every call site.
4. When another part of the codebase already does the same thing, call it instead, or extend that code to cover the new case.
5. Revert a commit whose whole change is unnecessary instead of editing its content out. Remove remaining unnecessary code and simplify the rest.
6. Remove documents and sections that duplicate other documents or the code, or hold temporary information. Move still-useful content into the document that owns it first.
7. Remove only what is clearly unneeded. Keep anything that needs a judgment call, and list it in the final report.
8. After cleanup, use the [sync-documents](../sync-documents/SKILL.md) skill and confirm relevant tests and lint pass. Run broader verification procedures when available and report the results.
