---
name: write-doc
description: "Use when writing or editing Markdown, other documentation files, or document-style Artifacts such as tech notes and reports — sets the style rules for document content, including README- and skill-specific rules."
---

# Writing a Document

- Order the document as a whole: context first, content next, outcome last. Group content under headings.
- Keep a document under 1000 words unless the user sets another limit.
- Prefer bullet points. One point per bullet, one line per bullet.
- Put parallel items in a list; put compared items in a table.
- Link to the detailed document or source file instead of repeating its content.
- Do not write numbers that change often; point to the source instead.
- Keep paragraphs to two sentences or fewer. One paragraph covers one thing.
- Add a diagram, table, or graph when a picture states the point faster than text.

## Purpose

- State the document's purpose in its first lines. Name another purpose when none below fits.
- Update the document on the trigger for its purpose. Suggest removing it when it has served its purpose or no longer matches the project.

| Purpose | Content | Update when |
|---|---|---|
| Plan | What to do | A decision changes |
| Architecture | How the current system works | The code changes |
| Design | The chosen approach and the alternatives rejected | A decision changes |
| Guide | How to use or set up the system | Behavior or a command changes |
| Progress | What is done and what remains | Work finishes |
| Report | What was found or measured | A correction is needed |
| Review | What is wrong or could improve | A finding is added or resolved |
| Reference | Background knowledge or supporting information | The source changes |
| Note | A fact to recall later | The fact changes |

## Mermaid Diagram

- Draw a two-way relation as two one-directional edges (`-->`, `-.->`), not as `<-->` or `<-.->`.

## README

- Put each command the reader should run in its own fenced bash block.
- Each block must run as-is when copied and pasted.
- State what to do, not why. A README is an outline and a guide.

## Skill

- Write the description as the trigger: "Use when <situation>", with the words seen at trigger time.
- Write rules and guidelines as clear, short bullet points.
- Write workflows as numbered steps, clear and concise, so no step is overlooked.
