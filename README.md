# CICIDS2017 Project Reviewer

[Open the interactive reviewer](https://landotin.github.io/cicids2017-project-reviewer/) · [Live model demonstration](https://cicids2017-model-demo.streamlit.app/).

The reviewer explains the custom PCAP pipeline, feature extraction and engineering, saved grouped split, Random Forest comparisons and selected 19-input model. Four tabs cover purpose, workflow, findings and practice, with twelve practice cards and eight quizzes. Download the standalone HTML from the page for offline use.

Current selected-model results: **72.30% mean CV Macro F1**, **78.03% validation Macro F1**, **87.31% test Macro F1**, **99.52% test accuracy**, **0.53% benign false alarms**. All 499,109 prediction row identities and 225 matrix cells passed review. The original test was previously examined for T1; this is not fresh independent confirmation. No refitting or tuning used these scores.

The official-flow comparison is excluded from the current study/report/presentation. Its files remain archived in evidence; its results are absent from the active findings and practice content. Original T1 tables remain historical; CT1 test evidence has the ct1_test_ prefix.

Edit `src/content.json` for explanations and `src/template.html` for interface. Add reviewed aggregate tables and their SHA-256 hashes to `evidence/provenance.json`, update `scripts/build.py` when a fact source changes, then run:

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

This regenerates `src/facts.json` and the self-contained `index.html`. GitHub Pages checks and publishes main; its workflow also provides the downloadable offline HTML. No external scripts or network data are required for offline interaction. A published explanation change does not modify or train a model.
