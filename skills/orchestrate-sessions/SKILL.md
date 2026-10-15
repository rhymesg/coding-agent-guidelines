---
name: orchestrate-sessions
description: "Orchestrates the other agent sessions on a machine: collects their status, arranges their order and machine use, and reports to the user. Use when the user asks to orchestrate, monitor, or arrange the work of other sessions."
---

# Orchestrate Sessions

## Collecting

- Send each session this request and subscribe to its idle notice:

  Status request from the orchestrator session <name>: reply with your task, its remaining steps with what each needs, a merge, data, or the machine with its length, the repositories and files you change, your open merge requests, what you run and when it ends, questions for the user, and your uncommitted or unpushed work.

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
- Tell a waiting session to keep a background wait running, then send the hand-over as a message.
- Hand a finding, such as a bug or an unowned merge request, to the session working on its area.
- Keep messages short: a dependency, a result, a question, or a user request, marked as coming from the user.

## Reporting

Re-list the sessions before each report. Report in this form; on an idle notice that changes nothing, say nothing. Link merge requests and files; omit an empty section.

  ## Progress

  | Session | Running | Expected end | Waiting on |
  |---|---|---|---|
  | **Session A** | step, resource held | time | **Your decision** on a question |
  | **Session B** | — | — | **Machine free** or [!number](url) **Merged** |

  - **Expected end:** when the last step of all sessions finishes.
  - **Done today:** one bullet per finished task across sessions, its goal and result for a reader outside the project: no steps, file, tool, or merge names; name only how the result was verified.

  ## Work order

  **Session A** →(what passes)→ **Session B**

  ## Suggestions

  1. A work order or conflict that needs the user's decision.
  2. A session the user should open for a finding no session covers, or ping in its chat when your ping failed.

  ## Your decisions

  A question a session asked the user appears only in its Waiting on cell.

  1. Questions from the orchestrator on its suggestions or the arrangement, with the evidence.
