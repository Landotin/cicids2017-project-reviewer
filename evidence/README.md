# Aggregate evidence

These are small, already reviewed result tables for the reviewer. They contain aggregate measurements, not the training dataset or packet records.

`provenance.json` records the source repository commit, original paths, and SHA-256 hashes. The build verifies the hashes before generating display facts. Scores in source tables are fractions unless a column explicitly says percent or percentage points. The display rounds scores only for reading.

## Read the right comparison

- `custom_validation.csv`: validation results for A–E, W1, T1, T2, and T3.
- `custom_ranking.csv`: original grouped-CV ranking of eligible models. W1/T2 were not shortlisted and have no CV measurement.
- `custom_cv_folds.csv`: the three saved grouped CV results for T1/T3.
- `final_test_metrics.csv` and `final_test_per_class.csv`: the frozen T1 custom-window test, completed 21 October 2026. Empty Heartbleed scores mean N/A, with zero test support.
- `official_summary.csv`, `official_folds.csv`, `official_paired_folds.csv`, and `official_class_f1.csv`: the separate two-arm official-flow experiment, reviewed 23 October 2026. These concern a filtered, aligned cohort and cannot be ranked against the custom-window final test.
- `partition_summary.csv` and `class_support.csv`: the unchanged saved custom-data split.
- `schema_checks.csv`: completed checks of five annotated packet headers (47 columns) and five prepared headers (19 columns).
- `v1_validation.csv` and `v1_cv.csv`: historical first-version measurements.

The original research dataset is [CICIDS2017 from the Canadian Institute for Cybersecurity, University of New Brunswick](https://www.unb.ca/cic/datasets/ids-2017.html). The reviewer identifies its own custom extraction separately from the dataset's supplied CICFlowMeter measurements.
