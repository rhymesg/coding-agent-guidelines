---
name: readme-writing-guidelines
description: "Structures a README so the reader quickly grasps the project and can easily work with it. Use when planning, writing, or editing a README."
---

# README Writing Guidelines

- Use the [document-writing-guidelines](../document-writing-guidelines/SKILL.md) skill for general writing rules.
- In a repository's top-level README, use the sections below in this order. Include a section only when it has content; add others after them. A sub-folder README uses the sections its content needs.

| Section | Content |
|---|---|
| Overview | One sentence on what the repository does. A diagram of its architecture or of its interaction with other modules, when needed |
| Installation | Set-up steps in the reader's workflow order |
| Usage | Run steps in the reader's workflow order, with the default command per step |
| Development | Build, test, lint, and CI commands |

- Give a folder its own README when it holds several items of one kind, such as datasets or profiles. A README covers what is common at its level and links each sub-folder's README instead of repeating its details.
- Put each command the reader should run in its own fenced bash block. Each block must run as-is when copied and pasted.
- State what the reader runs, sets, or edits, not why, and name the file, parameter, or constant.
- Move detailed settings, background, implementation details, development history, proposed changes, and verification results to a separate section after the main ones or to a separate file. Link to them where they matter.
