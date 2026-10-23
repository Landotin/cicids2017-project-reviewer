# Reviewer verification — 23 October 2026

## Content and measurements

- Two Luna Max implementation workers handled content and interface separately. A third independently reviewed the new content and display facts. The supervisor reviewed and integrated their work.
- All fourteen copied aggregate tables match their recorded SHA-256 hashes. Display numbers are generated from these tables; scores remain unrounded fractions until formatting.
- Required counts passed: five data stages, eleven lifecycle phases, five project gap cards, twelve oral-practice cards, eight four-option quiz questions, and twenty-six glossary terms.
- Dataset counts, saved partitions, final-test supports, supported-class Macro F1, ranking, official paired differences, and N/A/Not run distinctions passed build checks.
- Source scope is preserved: custom-window T1 and official-flow comparison are separate experiments. The original data, split, models, and test outcome were not changed.

## Browser checks

Forty interaction checks passed in Chromium. They covered all top-level tabs, all data stages and workflow phases, the two illustrative examples, glossary search, progress marks/reset, custom/official views, displayed results, Heartbleed N/A, unperformed CV, quiz scoring at 8/8 and 0/8, reset, print expansion/restoration, and lack of required network resources.

Keyboard Arrow Right, Home, and End moved the active tab and focus correctly. Wide tables have focusable labelled scroll regions.

At widths **320, 360, 768, and 1440 pixels**, none of the four tabs caused full-page horizontal overflow. Wide tables retain their own scroll regions. Desktop and phone screenshots were visually inspected.

The automated accessibility checker reported **zero violations** in project, workflow, custom findings, official findings, and practice, including expanded detail content. This is one automated browser check, not a claim of accessibility certification or testing in every browser.

## Download and printing

The Download HTML control produced a single HTML file. That downloaded file opened with the browser set offline; its eleven phases and quiz worked, with all correct answers producing 8/8 and no required HTTP resources or browser errors.

The complete print view was checked through a browser-generated PDF. Text extraction confirmed every lifecycle phase, all twelve practice questions and answers, the headline results, and quiz answer explanations. Print preparation expands details and illustrative answers, then restores reading state afterward. Temporary quiz score messages are omitted from the print handout.

Evidence links require internet; original project reports and notebooks may also require member access. The embedded explanations, measurements, and study tools work offline.

## Publishing

The dedicated public repository is `Landotin/cicids2017-project-reviewer`. GitHub Pages is configured to use Actions. The workflow checks the reproducible build before publishing the HTML and aggregate evidence. Live deployment verification is recorded in [progress](PROGRESS.md).
