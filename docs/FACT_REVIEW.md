# Public reviewer fact review

**Result: PASS with one wording refinement.** Reviewed `src/content.json` SHA-256 `7877d17627e8d3ea221b35c6d9b72601ae89e6aaa5e547fa596764ca3ec834f3` and `src/facts.json` SHA-256 `635f828b3b1b206292b4bd6f463d0fdc75fdbb12635ae1a4365fa56f7c1b7b0c`. The reviewer contains 12 practice cards, 8 quiz questions, and 11 workflow phases.

The stage descriptions distinguish the documented historical 44-column decoded schema from the checked files: all five annotated packet CSV headers have 47 columns and all five prepared CSV headers have 19. The prepared-row counts reconcile to 2,506,919 total, 2,453,662 sourced-label rows, and 53,257 UNLABELED rows. The 19 prepared columns are 15 baseline predictors plus four metadata fields; Model C uses 19 predictors after adding four calculated inputs, T1 uses the original 15, and the saved split rows have 23 columns.

The saved partition counts are correct: 1,472,712 train, 481,841 validation, and 499,109 test rows. All 15 labels occur in training; 14 have held-out support. The content correctly keeps the 20 custom Heartbleed windows from one conversation and the nine official Heartbleed flows from one group on fitting sides, with held-out Heartbleed scores marked N/A. Macro F1 is described as the equal average over the 14 supported classes.

The model account matches the evidence: T1 ranks first among eligible candidates by full-precision mean grouped-CV Macro F1 (71.43%, sample SD 8.49 points), with a 0.1021-point lead over T3. It was frozen before the reserved test and scored without refitting. The test figures—85.77% supported-class Macro F1, 99.51% accuracy, 2,218 false alarms among 417,513 BENIGN rows, and the cited per-class supports and scores—match the saved CSVs. The text now says balanced weights are recalculated from each CV fitting side; the official-flow median imputer and class weights are also stated to be fitted within each fold's fitting side.

The official comparison is properly scoped to the same filtered official-flow cohort and three saved folds: 15 flow-level analogs averaged 80.42% Macro F1 and 77 official numeric inputs averaged 81.98%, a paired mean difference of 1.56 points. It reports 1,126,067 eligible rows in 536,179 groups, including nine fitting-only Heartbleed flows, and 1,126,058 scored rows. It does not present this as a direct comparison with T1's custom 60-second windows. All eight quiz answer keys and explanations match the evidence.

**Wording refinement:** `project.goal` says “choose one using held-out examples.” This could sound as if the reserved test informed selection. Prefer “choose one using validation and grouped cross-validation results, then score it on the reserved test.” The workflow later explains this correctly; aligning the opening goal would remove the ambiguity. No other factual or unsupported preprocessing issue was found in the reviewed hash.

Evidence checked: `evidence/schema_checks.csv`, `evidence/partition_summary.csv`, `evidence/class_support.csv`, `evidence/custom_ranking.csv`, `evidence/custom_cv_folds.csv`, `evidence/final_test_metrics.csv`, `evidence/final_test_per_class.csv`, `evidence/official_summary.csv`, `evidence/official_paired_folds.csv`, `evidence/official_folds.csv`, and `evidence/official_class_f1.csv`; canonical `DATA_PIPELINE.md`, `MODEL_DEVELOPMENT_REPORT.md`, `FINAL_TEST_ANALYSIS.md`, and `OFFICIAL_FEATURE_RESULTS.md`.

## Supervisor integration review

After the independent review, the supervisor clarified selection using validation and grouped CV before final testing, distinguished zero Heartbleed support from N/A scores, and corrected the feature-experiment chronology. Display facts gained the already verified 991,134 custom linked-group count. No measured score changed.

Final content SHA-256: `0c4b3bcd6979431cd42d09a6f1f09983032de339d280af1d04f85656e235a386`.

Final facts SHA-256: `6859f3320b8367ea5d79a3ea2e324748cbd984f0393a87ecabdc9bdf4ab764ad`.

The supervisor also added plain-English definitions of training, a decision tree, and Random Forest, and explained the model before the A–E settings. The completed reviewer has 26 glossary entries. These teaching changes preserve every measurement and evaluation decision.

## 25 October — feature-guide supervisor review

The added guide was checked against the canonical data dictionary and `reference_models.py`. Initial extraction computes fifteen values from packet windows before training. C's four later calculations and D/E's fitting-only selection are distinct from the W1/T1/T2/T3 settings trials. T1 retains the original fifteen inputs. Whole-frame byte lengths, first-retained-packet direction, packet flag counts, observed duration, and zero-denominator behavior match the implementation. The guide explains why a feature may help without claiming measured importance or diagnosing an attack from one value. The official 77-input representation remains a separate experiment.

Updated content SHA-256: `26b20a5f1c123aa623101b1c0749a49f8c6908ef395aa0624a2e2f287562a369`.

Facts SHA-256 remains `6859f3320b8367ea5d79a3ea2e324748cbd984f0393a87ecabdc9bdf4ab764ad`. No model, split, or measurement changed.
