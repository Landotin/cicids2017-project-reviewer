#!/usr/bin/env python3
"""Build the offline HTML from reviewed aggregate evidence and readable source files."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]


def rows(name):
    with (ROOT / 'evidence' / name).open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))


def number(value):
    return float(value) if value not in (None, '') else None


def make_facts():
    """Scores stay as fractions; only the display layer rounds them."""
    provenance = json.loads((ROOT / 'evidence/provenance.json').read_text())
    for item in provenance['files']:
        actual = hashlib.sha256((ROOT / 'evidence' / item['file']).read_bytes()).hexdigest()
        if actual != item['sha256']:
            raise ValueError('Evidence changed without a reviewed provenance update: ' + item['file'])
    validation = {r['model']: r for r in rows('custom_validation.csv')}
    ranking = {r['model']: r for r in rows('custom_ranking.csv')}
    configurations = [
        ('A', 15, 'Original 15 predictors', 'None', 12, 2),
        ('B', 15, 'Original 15 predictors', 'Balanced', 12, 2),
        ('C', 19, '15 original predictors + 4 calculated values', 'Balanced', 12, 2),
        ('D', 8, '8 selected from the original 15', 'Balanced', 12, 2),
        ('E', 12, '12 selected from the expanded 19', 'Balanced', 12, 2),
        ('W1', 15, 'Original 15 predictors', 'Square root of balanced', 12, 2),
        ('T1', 15, 'Original 15 predictors', 'Balanced', 20, 2),
        ('T2', 15, 'Original 15 predictors', 'Balanced', 12, 1),
        ('T3', 15, 'Original 15 predictors', 'Balanced', 20, 1),
    ]
    models = []
    for name, count, description, weight, depth, leaf in configurations:
        v, cv = validation[name], ranking.get(name, {})
        models.append(dict(name=name, features=count, featureDescription=description,
                           weight=weight, depth=depth, leaf=leaf,
                           validationMacroF1=number(v['validation_macro_f1']),
                           validationAccuracy=number(v['validation_accuracy']),
                           validationFalseAlarmRate=number(v['validation_false_alarm_rate']),
                           cvMacroF1=number(cv.get('cv_macro_f1_mean')),
                           cvSd=number(cv.get('cv_macro_f1_std')), selected=name == 'T1',
                           notes='CV Not run: this trial was not shortlisted.' if name in ('W1', 'T2')
                           else 'All models use 80 trees and seed 42.'))
    metrics = rows('final_test_metrics.csv')[0]
    test = dict(model='T1', rows=499109, date='2026-10-21',
                macroF1=number(metrics['supported_class_macro_f1']), accuracy=number(metrics['accuracy']),
                precision=number(metrics['supported_class_macro_precision']),
                recall=number(metrics['supported_class_macro_recall']), kappa=number(metrics['kappa']),
                falseAlarms=int(metrics['benign_false_alarms']), benignRows=int(metrics['benign_rows']),
                falseAlarmRate=number(metrics['benign_false_alarm_rate']),
                perClass=[dict(label=r['label'], support=int(r['support']), precision=number(r['precision']),
                               recall=number(r['recall']), f1=number(r['f1'])) for r in rows('final_test_per_class.csv')])
    official_arms = []
    for r in rows('official_summary.csv'):
        official_arms.append(dict(id=r['arm'], title='15 official flow analogs' if r['arm'] == 'flow_analogs_15'
                                  else '77 official traffic measurements', features=15 if r['arm'] == 'flow_analogs_15' else 77,
                                  macroF1=number(r['mean_macro_f1']), sd=number(r['sample_sd_macro_f1']),
                                  falseAlarmRate=number(r['mean_fold_false_alarm_rate']), accuracy=number(r['mean_accuracy']),
                                  kappa=number(r['mean_kappa']), fitSeconds=number(r['total_fit_seconds']),
                                  predictionSeconds=number(r['median_of_fold_prediction_medians']),
                                  falseAlarms=int(float(r['pooled_false_alarms'])), errors=int(float(r['pooled_errors']))))
    rare_labels = {'Infiltration', 'Web Attack – Sql Injection', 'Heartbleed', 'Web Attack – XSS'}
    official = dict(eligibleRows=1126067, scoredRows=1126058, groups=536179, heartbleedFlows=9,
                    arms=official_arms, gain=official_arms[1]['macroF1'] - official_arms[0]['macroF1'],
                    pairedFoldGains=[number(r['fuller_minus_analogs_macro_f1']) for r in rows('official_paired_folds.csv')],
                    correctedErrors=3107, introducedErrors=177,
                    rareClasses=[dict(label=r['label'], support=int(r['held_out_rows']), f1=number(r['fuller_official']))
                                 for r in rows('official_class_f1.csv') if r['label'] in rare_labels],
                    notes=[
                        'Both feature sets use the same eligible official flow records and three saved training folds.',
                        'Fixed T1 settings: 80 trees, depth 20, minimum leaf size 2, balanced weights, seed 42, two CPU workers.',
                        'Median imputation and class weights are fitted using only the current fitting side.',
                        'The 15 flow analogs approximate our design on official flows; they are different inputs from T1’s custom windows.',
                        'Three folds show a consistent direction here; they do not establish statistical certainty.',
                        'The cohort is filtered. Its scores describe retained records, not the complete official dataset.',
                        'No replacement model was selected and the frozen T1 final test was not repeated.',
                        'False-alarm rates shown here are unweighted fold means; counts below are pooled across folds.',
                        'Prediction time includes imputation, uses three repeats after a warm-up, and excludes loading, feature construction, and scoring.',
                    ])
    support = [dict(label=r['class'], train=int(r['train']), validation=int(r['validation']), test=int(r['test']))
               for r in rows('class_support.csv')]
    return dict(
        dataset=dict(preparedRows=2506919, labeledRows=2453662, unlabeledRows=53257,
                     trainingClasses=15, evaluatedClasses=14, rawColumns=47, preparedColumns=19,
                     baselinePredictors=15, splitColumns=23, heartbleedWindows=20,
                     baselineFeatures=['protocol', 'duration_seconds', 'packet_count', 'total_bytes',
                                       'mean_packet_bytes', 'min_packet_bytes', 'max_packet_bytes',
                                       'forward_packet_count', 'backward_packet_count', 'forward_bytes',
                                       'backward_bytes', 'syn_count', 'ack_count', 'fin_count', 'rst_count']),
        split=dict(id='split_68ab64fbdd2b', folds=3, groups=991134,
                   parts=[dict(name=r['partition'], rows=int(r['rows']), share=float(r['actual_share_pct']) / 100)
                          for r in rows('partition_summary.csv')],
                   heartbleedPolicy='All 20 custom Heartbleed windows belong to one conversation and stay on fitting sides. Independent validation/test scores are N/A.'),
        models=models, test=test, official=official, classSupport=support,
        provenance=dict(sourceRevision=provenance['source_revision'], reviewedDate=provenance['reviewed_date'],
                        sourceRepository=provenance['source_repository']))


def validate(content, facts, template):
    schema = rows('schema_checks.csv')
    assert len(schema) == 10 and all(r['status'] == 'PASS' for r in schema)
    assert sum(r['stage'] == 'annotated_packet' and r['actual_columns'] == '47' for r in schema) == 5
    assert sum(r['stage'] == 'prepared_window' and r['actual_columns'] == '19' for r in schema) == 5
    assert len(content['workflow']) == 11, 'Need 11 lifecycle phases'
    assert len({p['id'] for p in content['workflow']}) == 11
    assert len(content['practice']) == 12, 'Need 12 oral practice cards'
    assert len(content['quiz']) == 8, 'Need eight multiple-choice questions'
    for q in content['quiz']:
        assert len(q['options']) == 4 and 0 <= q['correct'] <= 3 and q['explanation']
    assert len(content['stages']) == 5 and len(content['project']['gaps']) == 5
    assert len(content['glossary']) >= 20
    guide = content['featureGuide']
    assert len(guide['baseline']) == 15
    assert {r['key'] for r in guide['baseline']} == set(facts['dataset']['baselineFeatures'])
    assert len(guide['engineered']) == 4
    assert {r['key'] for r in guide['engineered']} == {'forward_backward_packet_ratio', 'forward_backward_byte_ratio', 'forward_packet_share', 'no_backward_packets'}
    assert len(guide['where']) == 3
    for row in guide['baseline'] + guide['engineered']:
        assert all(row.get(k) for k in ('key', 'title', 'group', 'meaning', 'why'))
    for row in guide['where']:
        assert row['link'].startswith('#workflow/')
        assert row['link'].split('/')[-1] in {p['id'] for p in content['workflow']}
    for phase in content['workflow']:
        assert all(phase.get(k) for k in ('id', 'title', 'plain', 'what', 'why', 'input', 'output', 'finding', 'spoken'))
    assert sum(p['rows'] for p in facts['split']['parts']) == facts['dataset']['labeledRows']
    assert facts['dataset']['labeledRows'] + facts['dataset']['unlabeledRows'] == facts['dataset']['preparedRows']
    assert sum(p['support'] for p in facts['test']['perClass']) == facts['test']['rows']
    assert len(facts['test']['perClass']) == facts['dataset']['trainingClasses']
    assert sum(r['support'] > 0 for r in facts['test']['perClass']) == facts['dataset']['evaluatedClasses']
    heart = next(p for p in facts['test']['perClass'] if p['label'] == 'Heartbleed')
    assert heart['support'] == 0 and heart['f1'] is None
    assert next(m for m in facts['models'] if m['selected'])['name'] == 'T1'
    assert [m['name'] for m in facts['models'] if m['cvMacroF1'] is None] == ['W1', 'T2']
    assert math.isclose(facts['test']['macroF1'], sum(r['f1'] for r in facts['test']['perClass'] if r['support']) / 14)
    assert facts['official']['scoredRows'] + facts['official']['heartbleedFlows'] == facts['official']['eligibleRows']
    assert all(g > 0 for g in facts['official']['pairedFoldGains'])
    assert math.isclose(sum(facts['official']['pairedFoldGains']) / 3, facts['official']['gain'])
    assert template.count('<!-- REVIEWER_DATA -->') == 1
    assert not re.search(r'<(?:script|iframe)\b[^>]*\bsrc\s*=', template, re.I), 'No external scripts/frames'
    assert not re.search(r'\bfetch\s*\(', template), 'Offline content must not need fetch'
    assert not re.search(r'@import\b|url\([\s\"\x27]*https?://', template), 'No network fonts/styles'
    return 'PASS: evidence hashes, 11 phases, 5 stages, 12 cards, 8 quiz questions, metrics, supports, offline dependencies'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Check outputs without rewriting them')
    parser.add_argument('--facts-only', action='store_true')
    args = parser.parse_args()
    facts = make_facts()
    facts_text = json.dumps(facts, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    if args.facts_only:
        (ROOT / 'src/facts.json').write_text(facts_text, encoding='utf-8')
        print('Prepared reviewed display facts from 14 aggregate evidence tables.')
        return
    content = json.loads((ROOT / 'src/content.json').read_text(encoding='utf-8'))
    template = (ROOT / 'src/template.html').read_text(encoding='utf-8')
    result = validate(content, facts, template)
    data = '<script>\nwindow.REVIEWER_CONTENT = ' + json.dumps(content, ensure_ascii=False, allow_nan=False).replace('</', '<\\/')
    data += ';\nwindow.REVIEWER_FACTS = ' + json.dumps(facts, ensure_ascii=False, allow_nan=False).replace('</', '<\\/') + ';\n</script>'
    html = template.replace('<!-- REVIEWER_DATA -->', data)
    for relative, expected in [('src/facts.json', facts_text), ('index.html', html)]:
        path = ROOT / relative
        if args.check:
            assert path.exists() and path.read_text(encoding='utf-8') == expected, relative + ' needs rebuilding'
        else:
            path.write_text(expected, encoding='utf-8')
    print(result)
    print('Standalone reviewer: index.html (' + str(len(html.encode('utf-8'))) + ' bytes).')


if __name__ == '__main__':
    main()
