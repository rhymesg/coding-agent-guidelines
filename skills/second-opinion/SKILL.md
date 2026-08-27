---
name: second-opinion
description: "Use when your answer has no clear winner, your conclusion remains uncertain, or a document or code change modifies more than five non-generated lines."
---

# Getting a Second Opinion

- Prefer Codex: delegate through the `codex:codex-rescue` agent.
- Without the codex plugin, delegate to a fresh general-purpose subagent.
- Pass file paths and the question, not copied file content.
- Give the reviewer the context it cannot infer: the goal, the constraints, and prior decisions from the conversation.
- Report the reviewer's answer next to your own view.
- Note where they differ; do not silently adopt either.

## Options or Uncertain Conclusion

1. State the question, the options or the tentative conclusion, and the paths to the relevant files.
2. Ask for a recommendation or a verdict with reasons.

## Reviewing a Document

1. Pass the document path and the rules path `../write-doc/SKILL.md`, relative to this skill's directory.
2. Ask for findings against the rules.
3. When the user asks for fixes, have the reviewer apply them. For Codex: resume the same thread with `--resume --write`.

## Reviewing Code

1. Pass these to the reviewer:
   - The goal, expected behavior, constraints, non-goals, and important prior decisions.
   - The change scope: a diff, branch, or file paths.
   - The related plan or design, coding guidelines, and component README.
2. Ask for findings on:
   - Weaknesses in the logic.
   - Unneeded complexity.
   - Behavior not covered by unit tests.
   - Deviation from the plan or design document.
