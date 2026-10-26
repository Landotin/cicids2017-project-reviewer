# CICIDS2017 Project Reviewer

A plain-English, interactive guide to our network-attack classification project. Learn why we conducted it, follow the ML workflow, understand the findings, and practice explaining the decisions.

**[Open the reviewer](https://landotin.github.io/cicids2017-project-reviewer/)** · **[Download the offline HTML](https://landotin.github.io/cicids2017-project-reviewer/CICIDS2017-Project-Reviewer.html)**

## Use it

1. Start with **Our Project and Why**.
2. Follow the eleven steps in **Our ML Workflow**. Each explains the decision, input, output, and a short way to say it aloud.
3. Open **Findings and Meaning**. Its custom-window and official-flow views are separate experiments.
4. Use the twelve answer cards and eight quiz questions in **Practice Explaining**.

Open **[What did we extract and engineer?](https://landotin.github.io/cicids2017-project-reviewer/#project/features)** for the exact workflow stages and a plain-language guide to all 15 original predictors and Model C's four extra values. Filter by traffic type/time, amount/size, direction, or connection signs. Each entry explains what the feature measures and why it may help; these explanations are not measured feature-importance rankings.

Use **Download HTML** to save one file that opens in a browser without internet. Evidence links need internet; the explanations, results, diagrams, and practice tools are embedded in the file. Use **Print all** for a paper or PDF study copy. Any learning progress is stored only in your browser and is optional.

## What the scores describe

- **Frozen custom T1 model:** 85.77% final-test Macro F1 on 499,109 custom conversation-window rows. It was selected using grouped CV before testing and was not refitted on training plus validation.
- **Separate official-flow comparison:** 81.98% mean grouped-CV Macro F1 for 77 official measurements versus 80.42% for 15 official flow analogs, using the same eligible official rows in both arms. These scores do not replace T1's test result or establish superiority over its custom extraction.
- **Heartbleed:** independent held-out scores are N/A. Zero F1 and Not run have different meanings.

The supplied 77 measurements are CICFlowMeter features from the official labelled-flow archive. They are not an expansion of our 15 custom predictors. Prepared-file column counts and model input counts are also different.

## Evidence

Reviewed on **23 October 2026**. The `evidence/` directory contains fourteen small aggregate tables from the existing ML repository. `evidence/provenance.json` records their original paths, source commit, and SHA-256 hashes. The reviewer source links distinguish public aggregate evidence from project-member reports and notebooks that may require permission.

The public repository contains the reviewer, source, aggregate tables, and publishing instructions. The data, saved models, and original project remain in their existing locations.

## Update the reviewer

No framework or package installation is required. Python 3 builds the page using its standard library.

1. Update explanations in `src/content.json`.
2. Update layout and interactions in `src/template.html`.
3. For new measured evidence, review the source results first, replace the relevant aggregate tables, and update their hashes and source revision in `evidence/provenance.json`. Adapt `scripts/build.py` if the measurement definitions changed. Do not type replacement scores into the interface template.
4. Run `python3 scripts/build.py`, then `python3 scripts/build.py --check`.
5. Test the page in a browser, including the downloaded HTML, keyboard navigation, mobile layout, quiz reset, and printing.
6. Commit and push to `main`. The Pages workflow verifies the build and deploys only the reviewer and aggregate evidence.

To preview locally, open `index.html` directly or run `python3 -m http.server 8765` from the repository directory.

## GitHub Pages setup

The dedicated repository is public. Its publishing source is **GitHub Actions**, with the `github-pages` environment. The workflow runs checks on pull requests and publishes passing pushes to `main`; it can also be started manually. Repository contents are readable with `contents: read`, and the deployment job uses `pages: write` and `id-token: write`.

If the page does not update, inspect the **Check and publish reviewer** workflow under Actions. Keep the generated `index.html` committed so users can also download the file from the repository.

See `docs/PROGRESS.md` for implementation and verification status.

## C+T1 follow-up, 26 October 2026

The findings tab now separates the later C+T1 exploratory results from the historical T1 test. [Live model demo](https://cicids2017-model-demo.streamlit.app/) · [Public demo repository](https://github.com/Landotin/cicids2017-model-demo). Mean CV Macro F1 was 72.30% for CT1 versus T1’s 71.43%; CT1 has no independent test result.
