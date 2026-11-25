# <Topic>: Tasks

> Execution checklist, progress, and evidence.

Choose the grouping and detail to fit the task.

- List concrete tasks in the order they can be done, and keep their status current.
- Link to relevant plan sections instead of repeating the plan.
- Note dependencies or blockers when needed.
- Check a task off only with a one-line `evidence:` from the real result: a command and its output, a measured value, or a link to a log, report, merge request, or pipeline.
- Keep a task you choose not to do in the list with a one-line `skip: <reason>`.
- Under each task, record the attempts that failed, the results, and the open questions the next session needs. Label unverified ideas.
- Keep current notes easy to find. Shorten older details, keeping failures, evidence, and reasons for decisions.

Example:

```markdown
- [x] 2.1 Add the usage log ([plan](plan.md#logging))
  - evidence: `python3 -m unittest discover -s ci` passed; [pipeline](<link>) green.
  - Tried one shared helper in `ci/`; the scripts keep their own copies.
- [ ] 2.2 Measure a week of logs
  - skip: the user estimates cost from the review count instead.
```
