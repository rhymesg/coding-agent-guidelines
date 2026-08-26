---
name: review-doc
description: "Use when a documentation file is finished or the user asks to review a Markdown file, another documentation file, or a document-style Artifact — runs an independent review against the write-doc rules."
---

# Reviewing a Document

1. Read `../write-doc/SKILL.md`, relative to this skill's directory. Its rules are the review criteria.
2. Delegate the review to an independent reviewer agent (e.g. Codex via `codex:rescue`) if one is available. Pass the document path and the rules path, not copied rule text.
3. Otherwise, run the review in a fresh agent context (e.g. a general-purpose subagent) whose prompt contains only the two paths and the review request.
4. Report the findings. Apply fixes only when the review is part of a writing task or the user asks.
