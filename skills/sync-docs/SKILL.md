---
name: sync-docs
description: "Use when a finished task changed behavior, commands, or structure — checks the comments and documents touched by the change and updates the stale ones."
---

# Sync Docs

Bring the documents in line with the current state of the code.

## Workflow

1. Check the comments in the code changed by the task. Update descriptions that no longer match the behavior.
2. List the names the task touched: files, functions, commands, and settings. Grep the documents across the project for them.
3. Compare each matching document against the current code and configuration.
4. Update the stale parts, using the `write-doc` skill.

When asked to sync everything, run steps 2 to 4 on every document instead of only the matches.

## Rules

- Describe the current purpose and behavior, not the history of changes or bug fixes.
- Prefer updating an existing point over adding a new one.
- If a plan document no longer matches the code, report it to the user and confirm before changing it.
