---
name: coordinate-sessions
description: "Keeps the agent sessions on a machine informed of each other's progress, dependencies, and share of the machine. Use when the user asks to monitor, report on, or arrange the work of other sessions."
---

# Coordinate Sessions

## Collecting

- Send each session this request and subscribe to its idle notice:

  Status request from the coordinating session <name>: reply with your task, its remaining steps with what each needs, a merge, data, or the machine with its length, the repositories and files you change, your open merge requests, what you run and when it ends, questions for the user, and your uncommitted or unpushed work.

- Verify what the plan depends on, such as merge request state or machine load.
- Ping a session that is idle past its expected end, silent when its turn comes, or missing from the listing. Ask the user to ping it in its chat only when your ping fails.

## Arranging

### Order

- Order steps, not sessions: a step needs a merge, data, or the machine, and a session's independent steps run early.
- Start with the step that unblocks the most others.

### Machine

- One load-sensitive run at a time; no many-core run beside it.
- Queue load-sensitive runs back to back; put many-core runs in the gaps.
- Grant each window; the session that frees the machine notifies the next one directly.

### Messages

- Tell each session only what concerns it.
- Hand a finding, such as a bug or an unowned merge request, to the session working on its area.
- Keep messages short: a dependency, a result, a question, or a user request, marked as coming from the user.

## Reporting

Report in this form, redrawn on an idle notice only when something changed. Link merge requests and files; omit an empty section.

  ## Progress

  - **Session A**: what it finished since the last report.

  | Session | Running | Expected end | Waiting on |
  |---|---|---|---|
  | **Session A** | step, resource held | time | **Your decision** on a question |
  | **Session B** | — | — | **Machine free** or [!number](url) **Merged** |

  ## Work order

  **Session A** →(what passes)→ **Session B**

  ## Suggestions

  1. A model tier for a session whose task calls for a different one.
  2. A work order or conflict that needs the user's decision.
  3. A session the user should open for a finding no session covers, or ping in its chat when your ping failed.

  ## Your decisions

  A question a session asked the user appears only in its Waiting on cell.

  1. Questions from the coordinator on its suggestions or the arrangement, with the evidence.
