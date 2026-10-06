---
name: technical-report-guidelines
description: "Makes technical findings and evidence clear to readers. Use when the user requests a technical report."
---

# Technical Report Guidelines

Use the [human-deliverable-guidelines](../human-deliverable-guidelines/SKILL.md) skill for document structure, presentation, and delivery.

A report tracked in a repository follows the [document-writing-guidelines](../document-writing-guidelines/SKILL.md) skill, with the purpose Report.

## Layout

- Include a Summary and a detailed Body instead of the one-page default.
- State the sample in the Summary, such as runs and configurations, and compare the key metric in numbers, with one chart of it.
- Default the Body to Introduction, Method, Results, and Conclusion, as in a technical paper. Adapt the sections when the work needs another structure.
- Keep each Body section to a few bullets or lines; put detail in figures, tables, and appendices.

## Evidence

Apply these rules throughout the report.

- Claims: Support claims with measurements or code references. Distinguish verified findings from estimates, assumptions, and open questions.
- Measurements: Give quantities their units and statistics their sample sizes.
- Tables: Carry the decision metric and its worst case; put secondary measures in an appendix.
- Reproducibility: Identify the data, code revision, and commands needed to reproduce results in the Method section or an appendix.

## Body

- Audience: Write for engineers unfamiliar with the work.
- Sections: Give each section one topic and a descriptive heading. Keep headings at the same level parallel.
- Findings: Lead with the finding, support it with evidence, and explain what it means.
- Conclusion: Answer the goal from the results, then state limitations and open points.
- Supporting detail: Put raw data and derivations in referenced appendices.

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
