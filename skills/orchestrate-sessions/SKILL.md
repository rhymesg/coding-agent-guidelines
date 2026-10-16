---
name: orchestrate-sessions
description: "Acts as a mid-level manager between the user and the other agent sessions on a machine: collects their status, arranges their order and machine use, and reports to the user. Use when the user asks to orchestrate, monitor, report, check, or arrange the work of other sessions."
---

# Orchestrate Sessions

## Collect

- Send each session this request and subscribe to its idle notice:

  Status request from the orchestrator session <name>: reply with your task, its remaining steps with what each needs, a merge, data, or the machine with its length, the repositories and files you change, your open merge requests, what you run and when it ends, questions for the user, and your uncommitted or unpushed work.

- Rearrange when a session reports a finished run or a merge.
- Verify what the plan depends on, such as merge request state or machine load.
- Read each routine session's last run to identify what it left unfinished: an open merge request, a question or approval waiting on the user, or a failure.
- Ask a session again when its report is overdue or it is missing from the listing; if it still does not answer, ask the user to ping it in its chat.

## Arrange

### Order

- Order steps, not sessions: a step needs a merge, data, or the machine, and a session's independent steps run early.
- Start with the step that unblocks the most others.
- After a merge, have each session whose work depends on it rebase before its load-sensitive run.

### Machine

- One load-sensitive run at a time; no many-core run beside it.
- Queue load-sensitive runs back to back; put many-core runs in the gaps.
- Grant each window when the previous run ends.

### Messages

- Tell each session only what concerns it.
- Send each hand-over to the waiting session as a message.
- Hand a finding, such as a bug or an unowned merge request, to the session working on its area.
- Keep messages short: a dependency, a result, a question, or a user request, marked as coming from the user.

## Report

Re-list the sessions before each report. Report in this form; on an idle notice that changes nothing, say nothing. Link each session as `[title](#sessionId)` with the id from the session list, and link merge requests and files; omit an empty section.

  ## Progress

  | Session | Running | Expected end | Waiting on |
  |---|---|---|---|
  | **[Session A](#sessionId)** | step, resource held | time | **Your decision** on a question |
  | **[Session B](#sessionId)** | — | — | **Machine free** or [!number](url) **Merged** |
  | **[Routine C](#sessionId)** | — | next run | **Your review** of [!number](url) |

  - **Expected end:** when the last step of all sessions finishes.
  - **Waiting on:** a routine's unfinished item goes in its cell.
  - **Done today:** in every report, one bullet per finished task across sessions, routine runs since the last report included, its goal and result for a reader outside the project: no steps, file, tool, or merge names; name only how the result was verified.

  ## Work order

  **[Session A](#sessionId)** →(what passes)→ **[Session B](#sessionId)**

  ## Suggestions

  1. A work order or conflict that needs the user's decision.
  2. A session the user should open for a finding no session covers, or ping in its chat when your ping failed.

  ## Your decisions

  A question a session asked the user appears only in its Waiting on cell.

  1. Questions from the orchestrator on its suggestions or the arrangement, with the evidence.
