# Reviewer content contract

Build a self-contained static reviewer, simple English, with four top-level tabs: project, workflow, findings, practice. Source templates and content are composed by `scripts/build.py` into `index.html`.

`src/template.html` must contain exactly one `<!-- REVIEWER_DATA -->` marker. The build replaces it with one inline script assigning `window.REVIEWER_CONTENT` and `window.REVIEWER_FACTS`. No fetch, external resources, fonts, framework, backend, or network dependency. All content must be embedded for file:// operation. The UI can assume data exists by the time its main script runs.

## content.json (prose worker owns)

- meta: {title, subtitle, reviewedDate}.
- project: {headline, intro, goal, pitch, gaps:[{title, observed, question, action, learned}], boundaries:[string]}.
- stages: [{id, title, countLabel, rowMeaning, explanation, detail}] in PCAP, decoded44, annotated47, prepared19, split23 order. Explain 15 predictors plus metadata; C's 19 inputs are different.
- workflow: exactly 11 [{id, title, plain, what, why, input, output, finding, spoken, details:[string]}]. All non-array fields are strings. Correct sequence: problem, gathering, understanding, preparation, extraction, splitting, baseline training, feature/settings experiments, selection/test, official feature comparison, interpretation/reporting.
- glossary: [{term, plain, detail}]. Include accuracy, precision, recall, F1, Macro F1, false alarm, fold, variation/SD, class weights, feature, predictor, support, T1, conversation, window, flow, leakage, hyperparameter, validation, test, N/A, Not run, zero.
- practice: exactly 12 [{question, answer, say}].
- quiz: exactly 8 [{question, options:[string,string,string,string], correct:integer 0..3, explanation}].
- sources: [{title, url, access, why}], access is public or project. Link public dataset/reviewer aggregate tables plus member-access original reports/Doc/notebook. Explicitly label private/project evidence links.
- featureGuide: {intro, where:[{title,stage,what,link}], baseline:[{key,title,group,meaning,why}], engineered:[{key,title,group,meaning,why,formula}], note, official}. The baseline lists all 15 fixed predictors; the engineered list describes C's four derived values. The guide distinguishes extraction (Step5), C engineering before A–E fits (Step7), and settings tuning without new inputs (Step8). It also explains the separate official analog calculations in Step10. Relevance descriptions explain possible use, not measured importance.

## facts.json (supervisor owns)

All scores are fractions 0..1, not percentages. Use percent(value, digits=2), null -> N/A; CV null -> Not run for W1/T2. Display standard deviations as percentage points. Integers use locale formatting.

- dataset: {preparedRows,labeledRows,unlabeledRows,trainingClasses,evaluatedClasses,rawColumns,preparedColumns,baselinePredictors,splitColumns,heartbleedWindows,baselineFeatures:[string]}.
- split: {id,parts:[{name,rows,share}],folds,heartbleedPolicy}.
- models: [{name,features,featureDescription,weight,depth,leaf,validationMacroF1,validationAccuracy,cvMacroF1,cvSd,validationFalseAlarmRate,selected,notes}]. A-E, W1,T1,T2,T3 in that order.
- test: {model,rows,macroF1,accuracy,precision,recall,kappa,falseAlarms,benignRows,falseAlarmRate,perClass:[{label,support,precision,recall,f1}],date}.
- official: {eligibleRows,scoredRows,groups,heartbleedFlows,arms:[{id,title,features,macroF1,sd,falseAlarmRate,accuracy,kappa,fitSeconds,predictionSeconds,falseAlarms,errors}],gain,pairedFoldGains:[number],correctedErrors,introducedErrors,rareClasses:[{label,support,f1}],notes:[string]}.
- provenance: {sourceRevision,reviewedDate,sourceRepository}.

## Interface requirements

Warm paper/off-white palette, dark navy/ink, coral and teal accents; system sans body and serif headings, no external fonts. Editorial, spacious and legible. Four accessible tabs with hash/deep links, a clickable 11-phase workflow, clickable data stages, clearly separate custom/official result views, model comparison details, metric glossary, 12 answer-reveal cards and an 8-question scored quiz with explanations/reset. Two illustrative interactive examples: packets -> one summary and grouped splitting. Use unmistakable 'illustrative example' labels. Keep 15 official analogs distinct from actual T1 inputs. Include false alarm rates and rare-class supports. Include Print all and Download HTML controls; download must work using a Blob from self-contained document, no fetch. Print all content, including every phase/hidden tab/revealed answer; exclude interactive controls in print. Keyboard focus and ARIA, accessible chart labels, reduced motion, responsive at 360px, 768px, 1440px. No horizontal page overflow. Optional local progress must gracefully handle denied storage.

Use no raw rows/IP addresses/packet records in this public reviewer. Aggregate evidence is in evidence/. Dataset and model results remain unchanged. All official numbers come from the 23 October reviewed cohort; custom T1 result is the frozen 21 October final test. Do not put their scores on a shared ranking chart.
