---
name: human-deliverable-guidelines
description: "Makes standalone documents clear at a glance through figures, diagrams, tables, brief text, and bold keywords. Use when creating or editing a standalone document for human readers, such as a report, guide, or proposal."
---

# Human Deliverable Guidelines

Use the [document-writing-guidelines](../document-writing-guidelines/SKILL.md) skill for shared writing rules. The prose and length rules below override its defaults.

## Format and Delivery

- Default to self-contained HTML; use another format when the user or destination requires it.
- Embed images and fonts as data URIs. Keep videos as separate files linked from the document.
- Link other documents, code, and repositories only by global URLs, such as a file's GitHub or GitLab page at a commit. Do not use local file paths.
- Default to `outputs/<topic>/` under the working folder, outside Git. Follow another location when specified by the user, repository, or calling skill.
- Check the rendered document in a browser screenshot before delivery.

## Structure

- Default to one readable page with a Summary section. Add a detailed Body only when the user asks.
- Keep the Summary well below 400 words whenever possible. Shorten the content to fit the page; do not shrink the text.
- When a Body is requested, use it for supporting detail and keep the Summary consistent with it.

## Presentation

- Title: name the subject in at most eight words.
- Open the Summary with the central figure, diagram, or table, and let the text follow it. Make the message clear at a glance through visuals, with only the text needed to interpret them.
- Use headings such as Summary, Key finding, and Conclusion where useful.
- Bold the keywords and short phrases that carry the message; avoid bolding whole paragraphs.
- Show the key evidence and numbers in the visuals, then state the recommendation or decision needed. Do not repeat what the visuals already show.
- Show results as graphs and methods or structures as diagrams.
- In diagrams, show where inputs and processing steps act.
- Explain colours, markers, and lines with labels and legends in the figure.

## References

- Conclusion first: [Minto pyramid principle](https://untools.co/minto-pyramid/), [USC executive summary guide](https://libguides.usc.edu/writingguide/executivesummary), [NPS executive summaries](https://nps.edu/web/gwc/executive-summaries-and-abstracts).
