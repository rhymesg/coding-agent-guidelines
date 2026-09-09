# Coding Agent Guidelines

## 1. Understand Before Coding

### Keep It Simple and Maintainable

- Explore the codebase first to understand its structure, conventions, and existing patterns.
- Before creating a new function, check whether existing code can be reused, extended, or slightly modified.
- Use the simplest solution with the minimum necessary code.

### Stay Within the Coding Task

- Consult the user before making decisions that require domain knowledge, including mathematical, scientific, or algorithmic assumptions, rules, and tradeoffs.
- Check official documentation for external APIs, libraries, frameworks, or platform behavior.

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
- No slang, no humor, no metaphor.
- Do not add rationale clauses like 'so that X' or 'this avoids Y'.

### Comments and Docstrings

- Describe the current purpose and behavior, not the history of changes.
- Do not write author information.
- Do not repeat the current value of a parameter in comments. Explain what the parameter means.

### Documents

- Use the `write-doc` skill for guidance.

## 4. Interaction with the User

### Do Not Start Without Request

- Do not edit unless asked; a question is not a request to edit.
- Do not commit unless asked. When asked, use the `commit` skill.

### Long Tasks

- Before starting or resuming work, including after compaction, read the matching `workplans/<topic>/objective.md`.
- When a request will not finish in one session, use the `workplan` skill.

### Answering Questions

- Start with the direct answer or the outcome in one sentence.
- Answer in under 100 words, in sections and bullets. Elaborate only if asked.
- Skip background the user already knows.

### During Work

- Do not run tests or simulations that require manual UI interaction. Report when such verification is needed.
- Do what you can first. Collect any required user input or actions and ask for them together.

### After Work Is Done

- Report the result. Follow [Answering Questions](#answering-questions).
- After a change to behavior, commands, or structure, use the `sync-docs` skill.
- Remind the user to commit before moving on. Suggest a one-line message for all changes since the last commit.
