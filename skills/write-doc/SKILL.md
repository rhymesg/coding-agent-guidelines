---
name: write-doc
description: "Use when writing or editing Markdown, other documentation files, or document-style Artifacts such as tech notes and reports — sets the style rules for document content, including README- and skill-specific rules."
---

# Writing a Document

- Order the document as a whole: context first, content next, outcome last. Group content under headings.
- Prefer bullet points. One point per bullet, one line per bullet.
- Put parallel items in a list; put compared items in a table.
- Link to the detailed document or source file instead of repeating its content.
- Do not write numbers that change often; point to the source instead.
- Keep paragraphs to two sentences or fewer. One paragraph covers one thing.
- Add a diagram, table, or graph when a picture states the point faster than text.

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

## Review

- After finishing a document, use the `review-doc` skill.
