---
name: get-second-opinion
description: "Use when your answer has no clear winner, your conclusion remains uncertain, or a document or code change modifies more than five non-generated lines."
---

# Get a Second Opinion

- Prefer Codex through the `codex:codex-rescue` agent; without it, a fresh general-purpose subagent.
- Pass file paths and the question, not file content.
- Give the context the reviewer cannot infer: the goal, constraints, and user-approved decisions.
- Do not share your own conclusion, including through inherited conversation history.
- Report the reviewer's answer next to your own view and name the differences; adopt neither silently.

## Asking the Reviewer

Put these lines in every request, after the question:

```text
Do not answer "looks good" or "agree".
List at least one problem, with file and line, for example a wrong result, an unhandled input, a missing test, or a broken rule.
Name one different approach and state when it would be better than this one.
If you still agree, write the checks you made and the observation that would change your mind.
```

A reply without file and line references is not a review; send it back with the missing item named.

## Options or Uncertain Conclusion

- Give: the question, each option in one line, the paths to the relevant files.
- Ask for: one case per option where it fails or costs more than the others; a verdict, one of the options or a new one, with the deciding reason; the fact that would settle the question and how to check it.

## Reviewing a Document

- Give: the document path and the rules path `../document-writing-guidelines/SKILL.md`, relative to this skill's directory.
- Ask for: findings against the rules.
- Fixes, when the user asks for them: have the reviewer apply them; with Codex, resume the same thread with `--resume --write`.

## Reviewing Code

- Give: the goal, expected behavior, constraints, non-goals, and user-approved decisions; the diff, branch, or file paths; the plan or design, coding guidelines, and component README.
- Ask for: weaknesses in the logic, unneeded complexity, behavior not covered by unit tests, deviation from the plan or design.
