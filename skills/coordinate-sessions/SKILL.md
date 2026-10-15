---
name: coordinate-sessions
description: "Keeps the agent sessions on a machine informed of each other's progress, dependencies, and share of the machine. Use when the user asks to monitor, report on, or arrange the work of other sessions."
---

# Coordinate Sessions

## Status

- Announce yourself as the coordinator in the first message to each session. Ask for its task, what is done, what it waits on, and its unpushed work; subscribe to its idle notice.
- Verify what the plan depends on, such as merge request state or machine load, before relying on it.
- Re-list a session missing from the listing before its turn. When it is still gone, spawn a subagent in its place with its scratchpad paths and the current order.

## Arranging

- Treat the machine as one resource and grant its windows: one real-time run, such as a SITL flight or a dataset replay, at a time, and no many-core build or test run beside it.
- Sequence sessions that share files, data, or a merge target; let the rest run in parallel.
- Tell each session only what concerns it; the session that frees a resource or produces data notifies the next one directly.
- Keep messages short: a dependency, a result, a question, or a user request, marked as coming from the user.

## Reporting

- Keep one picture in this form, redrawn on an idle notice only when something changed. Link merge requests and files inside the cells.

  **Order:**

  **Session A** →(hand-over)→ **Session B**

  | Session | Running | Expected end | Waiting on | Next |
  |---|---|---|---|---|
  | **Session A** | step, resource held | time | **Your decision** on a question | steps |
  | **Session B** | — | — | **Machine free** or [!number](url) **Merged** | steps |

- Recommend a model tier for a session when its current task calls for a different one.
