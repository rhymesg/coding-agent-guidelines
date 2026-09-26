---
name: sync-documents
description: "Updates comments and documents to match the code. Use when a finished task changed behavior, commands, or structure."
---

# Sync Documents

## Workflow

1. Check the comments in the code changed by the task. Update descriptions that no longer match the behavior.
2. List the names the task touched: files, functions, commands, and settings. Grep the documents across the project for them.
3. Compare each matching document against the current code and configuration.
4. Use the [document-writing-guidelines](../document-writing-guidelines/SKILL.md) skill to update stale documentation.

## Rules

- Describe the current purpose and behavior, not the history of changes or bug fixes.
- Prefer updating an existing point over adding a new one.
- If a plan document no longer matches the code, report it to the user and confirm before changing it.
