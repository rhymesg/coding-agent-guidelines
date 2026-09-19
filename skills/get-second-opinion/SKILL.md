---
name: get-second-opinion
description: "Use when your answer has no clear winner, your conclusion remains uncertain, or a document or code change modifies more than five non-generated lines."
---

# Get a Second Opinion

- Prefer Codex through the `codex:codex-rescue` agent; without it, a fresh general-purpose subagent.

## Asking the Reviewer

### Input

- Pass file paths and the question, not file content.
- Give the user's intent or the goal of the work, relevant constraints, and user-approved decisions.
- Include the additional input for the applicable review type in the table below.
- Present the work neutrally. Do not include your assessment of its quality or suggest a preferred verdict.

### Request

- Include the review focus for the applicable review type in the table below.
- Independently assess whether the proposed answer or changes are the best solution to the user's goal, given the constraints. Challenge assumptions and consider better alternatives.
- Report problems that affect the result. Support agreement or disagreement with evidence.

## Review Types

| Type | Additional input | Review focus |
|---|---|---|
| Decisions | Options and supporting evidence | Tradeoffs, failure cases, recommendation, deciding evidence |
| Documents | Document and applicable [writing rules](../document-writing-guidelines/SKILL.md) | Rule compliance, sentences that can be combined more concisely |
| Code | Diff, expected behavior, design, relevant documentation | Correctness, complexity, test coverage, design alignment |
