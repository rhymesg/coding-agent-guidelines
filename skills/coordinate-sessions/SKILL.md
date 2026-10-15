---
name: coordinate-sessions
description: "Keeps the agent sessions on a machine informed of each other's progress, dependencies, and share of the machine. Use when the user asks to monitor, report on, or arrange the work of other sessions."
---

# Coordinate Sessions

Report in the four sections below, redrawn on an idle notice only when something changed. Link merge requests and files; omit an empty section.

## Progress

- Announce yourself as the coordinator in the first message to each session. Ask for its task, what it runs, when that ends, what it waits on, and its unpushed work; subscribe to its idle notice.
- Verify what the plan depends on, such as merge request state or machine load.
- Re-list a session missing from the listing before its turn. When it is still gone, spawn a subagent in its place with its scratchpad paths and the current order.

  - **Session A**: what it finished since the last report.

  | Session | Running | Expected end | Waiting on |
  |---|---|---|---|
  | **Session A** | step, resource held | time | **Your decision** on a question |
  | **Session B** | — | — | **Machine free** or [!number](url) **Merged** |

## Hand-overs

- Treat the machine as one resource and grant its windows: one real-time run, such as a SITL flight or a dataset replay, at a time, and no many-core build or test run beside it.
- Order steps, not sessions: find what each step needs, a merge, data, or the machine, and let a session's independent steps run early.
- Start with the step that unblocks the most others; queue real-time runs back to back and put builds and tests in the gaps.
- Tell each session only what concerns it; the session that frees a resource or produces data notifies the next one directly.
- Keep messages short: a dependency, a result, a question, or a user request, marked as coming from the user.

  **Session A** →(what passes)→ **Session B**

## Suggestions

1. A model tier for a session whose task calls for a different one, or a better work order.

## Your decisions

1. Questions from the coordinator: its suggestions or the arrangement, with the evidence. A session's own question is only noted: **Session A** needs your decision on the question.
