---
name: document-writing-guidelines
description: "Keeps documentation concise and easy to navigate. Use when writing or editing documentation, including READMEs, technical notes, reports, and document-style artifacts."
---

# Document Writing Guidelines

- Order the document as a whole: context first, content next, outcome last. Group content under headings.
- Keep a document under 1000 words unless the user sets another limit. Treat word limits as ceilings, not targets.
- Prefer bullet points. One point per bullet, one line per bullet.
- Put parallel items in a list; put compared items in a table.
- Link to settings, results, and other details in their source document or file instead of repeating them.
- Do not write numbers that change often; point to the source instead.
- Keep paragraphs to two sentences or fewer. One paragraph covers one thing.
- Add a diagram, table, or graph when a picture states the point faster than text.
- Name document files in lowercase with dashes between words, such as `runtime-optimization.md`, not underscores.

## Audience

- For developer- and agent-facing documents, including READMEs, `AGENTS.md`, `CLAUDE.md`, and design documents, use established software engineering terminology rather than everyday substitutes.
- For nontechnical readers, use everyday language and explain necessary technical terms.

## Purpose

- State the document's purpose in its first lines. Name another purpose when none below fits.

| Purpose | Content |
|---|---|
| Plan | What to do |
| Design | The chosen approach and the alternatives rejected |
| Progress | Which tasks are done and which remain |
| Architecture | How the current system works |
| Guide | How to use or set up the system |
| Report | What was found or measured, and what is still open |
| Review | What is wrong or could improve |
| Reference | Background knowledge or supporting information |

## Mermaid Diagram

- Draw a two-way relation as two one-directional edges (`-->`, `-.->`), not as `<-->` or `<-.->`.

## README

- Put each command the reader should run in its own fenced bash block.
- Each block must run as-is when copied and pasted.
- State what the reader runs, sets, or edits, not why. Name the file, parameter, or constant they change.
- Omit background, implementation details, development history, proposed changes, and verification results.
