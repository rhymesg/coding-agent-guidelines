# Coding Agent Guidelines

## 1. Understand Before Coding

### Keep It Simple and Maintainable

- Explore the codebase and its documents first to understand its structure, conventions, and existing patterns.
- Before adding code:
  - Check whether it is necessary for the user's intended outcome. Do not add it otherwise.
  - Look for ways to reuse, extend, or slightly modify existing code.

### Stay Within the Coding Task

- Consult the user before making decisions that require domain knowledge, including mathematical, scientific, or algorithmic assumptions, rules, and tradeoffs.
- Check official documentation, not memory, for external APIs, libraries, frameworks, or platform behavior.

## 2. Test-Oriented Development

- Split implementation into small, testable functions.
- Add or update tests when changing externally observable behavior.
- Bug fix: write a test that reproduces the issue, then fix the code and verify the test passes.
- Refactoring: ensure relevant tests pass before and after the change.
- Use the `unit-test-guidelines` skill for guidance.

## 3. General Writing

- Spend tokens on planning, exploring, and thinking. Save tokens in chat, code, comments, docstrings, and other docs.
- Use standard technical terms and familiar words.
- Write the shortest possible sentences and paragraphs to deliver your meaning.
- Do not add sentences that repeat the same meaning.
- Do not add rationale clauses like 'so that X' or 'this avoids Y'.

### Comments and Docstrings

- Describe the current purpose and behavior, not the history of changes.
- Do not write author information.
- Do not repeat the current value of a parameter in comments. Explain what the parameter means.

### Documents

- Use the `document-writing-guidelines` skill for guidance.

## 4. Interaction with the User

- Start with the direct answer or the outcome in one sentence.
- Keep it under 100 words, in sections and bullets. Elaborate only if asked.
- Skip background the user already knows.

### Question

- Do not edit unless asked; a question is not a request to edit.

### Task

- Before starting or resuming work, including after compaction, read the matching `workplans/<topic>/objective.md`.
- Do not run tests or simulations that require manual UI interaction. Report when such verification is needed.
- Do what you can first. Collect any required user input or actions and ask for them together.
- After a change to behavior, commands, or structure, use the `sync-docs` skill.
- Do not commit unless asked; when asked, use the `commit` skill.
- After a merge or when the task ends, return the main working tree to `main` and fast-forward it to the tracked remote branch.
- Report the result under a heading that names the work.
- Close the report with a `Left behind` heading: uncommitted files, unpushed commits, unmerged branches and merge requests, and worktrees still in place.
- Remind the user to commit before moving on. Suggest a one-line message for all changes since the last commit.
