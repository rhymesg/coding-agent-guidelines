---
name: report-writing-guidelines
description: "Makes technical findings and evidence clear to readers. Use when writing or editing a report on engineering work that is not tracked in a repository, such as a workplan or run report."
---

# Report Writing Guidelines

Use the [human-deliverable-guidelines](../human-deliverable-guidelines/SKILL.md) skill for document structure, presentation, and delivery.

A report tracked in a repository follows the [document-writing-guidelines](../document-writing-guidelines/SKILL.md) skill, with the purpose Report.

## Layout

- Default the Body to Introduction, Method, Results, and Conclusion, as in a technical paper. Adapt the sections when the work needs another structure.

## Body

- Write for engineers unfamiliar with the work.
- State the data, the code branch or commit, and the command that reproduces each result.
- Give every number its unit, and every statistic its sample, such as the number of runs or seeds.
- State measured or code-backed facts; mark estimates and open points as such.
- Give each section one topic, such as one quantity or one question.
- Open each section with its context, give the content, and end with its conclusion.
- When presenting results, pose the question, show the evidence, and state the answer.
- Keep the argument moving in one direction, and word headings at the same level in parallel.
- Use at most three heading levels, and give each subsection at least one sibling.
- Number the body sections, and refer to them by number.
- End the body by answering the goal from the results, then stating the limits and open points.
- Put non-essential material, such as raw data or derivations, in appendices referenced from the text.

## Captions

- Number figures and tables in order of appearance: "Figure 1." for diagrams and graphs, "Table 1." for tables. Put figure captions below the figure and table captions above the table.
- Open each caption with a short bold title: a phrase naming what is shown, not a sentence and not the axis labels restated. Follow it with the conclusion it supports, if any.
- Make each caption readable without the text: define abbreviations beyond the field's standard ones, and state the sample, such as the number of runs.
- Do not restate values the figure or table shows.

## Terminology

- Use the standard terms of the report's field instead of invented or everyday words.
- Define each quantity at its first use, such as "p95: the 95th percentile of the error".
- Use one term per concept across text, tables, and figure labels.

## References

- Body: [Ten simple rules for structuring papers](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619), [KU Leuven report structure](https://eng.kuleuven.be/en/study/engineering-essentials/reporting/structure-content).
- Captions: [SCU figure caption tips](https://www.scu.edu/provost/writingcenter/resources/subject-specific-writing/figure-caption-tips/), [International Science Editing](https://www.internationalscienceediting.com/how-to-write-a-figure-caption/).
