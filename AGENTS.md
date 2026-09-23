# Coding Agent Guidelines

## 1. Understand Before Coding

### Keep It Simple and Consistent

- Explore the codebase, its documents, and neighboring projects of the same kind first. Follow their conventions.
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
- Use the [unit-test-guidelines](skills/unit-test-guidelines/SKILL.md) skill for test guidance.

## 3. Writing Guidelines

### Comments and Docstrings

- Keep each file header and in-line comment to two lines at most. This does not apply to Doxygen comments.
- Put design, algorithm, and background details in a separate document, and link it from the comment if needed.
- Do not write author information.
- Do not repeat the current value of a parameter in comments. Explain what the parameter means.

### Documents and Instructions

- A document is written content that explains, guides, or reports, in any format: Markdown, HTML, PDF, or another artifact. Use the [document-writing-guidelines](skills/document-writing-guidelines/SKILL.md) skill.
- For a README, use the [readme-writing-guidelines](skills/readme-writing-guidelines/SKILL.md) skill.
- For skills, use the [skill-writing-guidelines](skills/skill-writing-guidelines/SKILL.md) skill.

## 4. Interaction with the User

- Start with the direct answer or the outcome in one sentence.
- Keep it under 100 words, in sections and bullets. Elaborate only if asked.
- Skip background the user already knows.

### Question

- Do not edit unless asked; a question is not a request to edit.

### Task

#### Working

- Before starting or resuming work, including after compaction, read the matching `workplans/<topic>/objective.md`.
- Do not run tests or simulations that require manual UI interaction. Report when such verification is needed.
- Do what you can first. Collect any required user input or actions and ask for them together.

#### Finishing

- After a change to behavior, commands, or structure, use the [sync-docs](skills/sync-docs/SKILL.md) skill for related documentation updates.
- Do not commit unless asked; when asked, use the [commit](skills/commit/SKILL.md) skill for committing changes.
- After a merge or when the task ends, return the main working tree to `main` and fast-forward it to the tracked remote branch.

#### Reporting

- Report the result under a heading that names the work.
- Close the report with a `Left behind` heading when something remains: uncommitted files, unpushed commits, unmerged branches and merge requests, or worktrees still in place. Omit the heading when nothing does.
- When work performed through a skill produces a potentially reusable script or other artifact, suggest incorporating it into that skill.
- Remind the user to commit before moving on. Suggest a one-line message for all changes since the last commit.
