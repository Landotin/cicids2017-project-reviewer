# Reviewer progress

## 23 October 2026

- Approved: simple English, four tabs, eleven lifecycle phases, twelve oral-practice cards, eight quiz questions, downloadable offline HTML, separate public repository and GitHub Pages.
- Reviewed sources: canonical data pipeline, model report, frozen T1 test analysis, and the completed official-flow comparison.
- Prepared: fourteen aggregate evidence tables and their hashes, display facts generated from those tables, reproducible HTML build and Pages workflow.
- Complete: plain-English content and interface by separate Luna Max workers; independent content review and supervisor integration.
- Complete: 40 interaction checks, five automated accessibility views with zero violations, four responsive widths, keyboard navigation, offline download, and complete print content. See [verification](VERIFICATION.md).
- Configured: the dedicated public repository and GitHub Pages using Actions.
- Complete: GitHub Pages deployment and live-link verification. The home page, downloadable HTML, and fourteen aggregate evidence tables returned HTTP200 and matched the committed hashes. The latest teaching update was also checked on the live page.
- Live reviewer: https://landotin.github.io/cicids2017-project-reviewer/
- Passing deployment: https://github.com/Landotin/cicids2017-project-reviewer/actions/runs/39973255564
- This artifact is complete. It supports project review and practice; the separate slide-deck task remains outside this deliverable.

## Content decisions

- The project gap cards describe problems observed in this project, with evidence and limitations.
- Packet summaries are already feature extraction. The workflow places that step before splitting/training and shows later feature experiments as a return to the feature design.
- File columns, model predictors, and the meaning of each row are explained separately.
- Use the completed 23 October raw-header audit: all five actual annotated headers have 47 columns, and all five prepared headers have 19.
- Keep custom-window T1 findings and the official-flow comparison in separate views.
- The official comparison retained 1,126,067 rows; nine Heartbleed flow rows always fit, and 1,126,058 other rows received held-out predictions per feature set.
- Unsupported scores remain N/A; unperformed CV is Not run; measured zero F1 remains zero.
- The reviewer introduces no new fit, data split, or test prediction.

## 25 October 2026 — feature explanations

- Added a feature guide in the Project tab, linked from Findings: [open the guide](https://landotin.github.io/cicids2017-project-reviewer/#project/features).
- Distinguished initial packet-to-window extraction in Step 5, Model C engineering and D/E selection in Step 7, and settings-only trials in Step 8.
- Added plain-language meanings and potential relevance for the fifteen original predictors and four C extras, with filters and optional formulas.
- Checked whole-frame bytes, first-retained-packet direction, window duration, flag counts, and zero-denominator handling against the implementation. Relevance explanations are explicitly not measured importance rankings.
- Preserved T1's fifteen inputs, all measured results, and the separate origin and scope of the official 77-input comparison.
- Focused browser checks covered filters, feature-set controls, workflow links, phone/desktop layout, accessibility, deep linking, and all nineteen printed feature definitions. See [verification](VERIFICATION.md).
