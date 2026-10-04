---
name: document-writing-guidelines
description: "Keeps documentation concise and easy to navigate. Use when planning, writing, or editing documents, including technical notes, reports, and document-style artifacts."
---

# Document Writing Guidelines

- Read neighboring documents with a similar purpose first and follow their writing style and conventions.
- Order the document as a whole: overview first, details next. Group content under headings.
- Keep a document under 1000 words unless the user sets another limit. Treat word limits as ceilings, not targets.
- Put parallel items in a list; put compared items in a table.
- Keep each piece of information in one place and link to it instead of repeating it.
- Do not copy details that change with the code or over time, such as values, counts, signatures, or file lists; point to the source instead.
- One paragraph or bullet covers one thing.
- Do not add sentences that repeat the same meaning.
- Do not add rationale clauses like 'so that X' or 'this avoids Y'.
- Add a diagram, table, or graph when a picture states the point faster than text.
- Name document files in lowercase with dashes between words, such as `runtime-optimization.md`, not underscores.

## Audience

- For developer-facing documents, including READMEs and design documents, use established software engineering terminology rather than everyday substitutes.
- For nontechnical readers, use everyday language and explain necessary technical terms.

## Purpose

- Before writing, decide the document's purpose from the table below. Name another purpose when none fits.
- State the purpose in the document's first lines, then write only what serves it.

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
