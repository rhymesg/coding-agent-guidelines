---
name: second-opinion
description: "Use when your answer contains several options without a clear winner, when your conclusion is uncertain or rests on claims you could not verify, or when reviewing a finished document or code change — gets an independent pass from a reviewer agent."
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

1. Pass the change scope: a diff, a branch, or file paths.
2. Pass the paths of related documents: the plan or design document the change follows, the coding guidelines, and the README of the touched component.
3. Ask for these findings:
   - Weaknesses in the logic.
   - Unneeded complexity.
   - Behavior not covered by unit tests.
   - Deviation from the plan or design document.
