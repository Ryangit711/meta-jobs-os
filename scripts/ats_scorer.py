#!/usr/bin/env python3
"""
ATS Scorer — Pure-Python TF-IDF Cosine Similarity
Compares resume against job description using a corpus of past JDs.
Returns score (0-1) with keyword breakdown.

Usage:
  python3 scripts/ats_scorer.py --resume resume.txt --jd jd.txt
  python3 scripts/ats_scorer.py --resume resume.txt --jd jd.txt --corpus-dir data/jd_corpus/
"""

import argparse
import json
import math
import os
import re
import sys
from collections import Counter
from glob import glob


def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = text.split()
    stopwords = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
        'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
        'would', 'could', 'should', 'may', 'might', 'shall', 'can', 'need',
        'this', 'that', 'these', 'those', 'it', 'its', 'we', 'our', 'you',
        'your', 'they', 'their', 'he', 'she', 'his', 'her', 'i', 'me', 'my',
        'not', 'no', 'nor', 'so', 'if', 'then', 'than', 'too', 'very', 'just',
        'about', 'above', 'after', 'again', 'all', 'also', 'any', 'because',
        'before', 'between', 'both', 'each', 'few', 'more', 'most', 'much',
        'other', 'some', 'such', 'only', 'own', 'same', 'into', 'over', 'up',
        'out', 'off', 'down', 'here', 'there', 'when', 'where', 'why', 'how',
        'what', 'which', 'who', 'whom', 'while', 'during', 'through', 'until',
        'against', 'within', 'without', 'along', 'around', 'among', 'across',
        'under', 'above', 'below', 'between', 'behind', 'beyond', 'via'
    }
    return [t for t in tokens if t not in stopwords and len(t) > 1]


class TfidfVectorizer:
    def __init__(self):
        self.idf = {}
        self.vocab = set()
        self.n_docs = 0

    def fit(self, documents):
        self.n_docs = len(documents)
        doc_freq = Counter()
        for doc in documents:
            tokens = set(tokenize(doc))
            for t in tokens:
                doc_freq[t] += 1
        self.vocab = set(doc_freq.keys())
        self.idf = {}
        for term, df in doc_freq.items():
            self.idf[term] = math.log((self.n_docs + 1) / (df + 1)) + 1
        return self

    def transform(self, document):
        tokens = tokenize(document)
        tf = Counter(tokens)
        total = len(tokens) if tokens else 1
        features = {}
        for term in set(tokens):
            if term in self.idf:
                tf_val = tf[term] / total
                features[term] = tf_val * self.idf[term]
        return features

    def cosine_similarity(self, vec_a, vec_b):
        terms = set(vec_a.keys()) & set(vec_b.keys())
        dot = sum(vec_a[t] * vec_b[t] for t in terms)
        norm_a = math.sqrt(sum(v * v for v in vec_a.values()))
        norm_b = math.sqrt(sum(v * v for v in vec_b.values()))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def top_terms(self, vec, n=10):
        return sorted(vec.items(), key=lambda x: -x[1])[:n]

    def matched_terms(self, vec_a, vec_b):
        common = set(vec_a.keys()) & set(vec_b.keys())
        return {t: (vec_a[t], vec_b[t]) for t in sorted(common, key=lambda t: -vec_b[t])[:20]}

    def missing_terms(self, vec_a, vec_b, n=10):
        a_only = set(vec_a.keys()) - set(vec_b.keys())
        b_only = set(vec_b.keys()) - set(vec_a.keys())
        return {
            'resume_not_in_jd': sorted(a_only, key=lambda t: -vec_a.get(t, 0))[:n],
            'jd_not_in_resume': sorted(b_only, key=lambda t: -vec_b.get(t, 0))[:n]
        }


def load_corpus(corpus_dir):
    documents = []
    paths = glob(os.path.join(corpus_dir, '*.txt')) + glob(os.path.join(corpus_dir, '*.md'))
    for path in paths:
        try:
            with open(path, 'r') as f:
                documents.append(f.read())
        except:
            pass
    return documents


def main():
    parser = argparse.ArgumentParser(description='ATS TF-IDF Scorer')
    parser.add_argument('--resume', required=True, help='Path to resume text file')
    parser.add_argument('--jd', required=True, help='Path to job description text file')
    parser.add_argument('--corpus-dir', default=None, help='Directory of past JDs for IDF corpus')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    if not os.path.exists(args.resume):
        print(f"Error: resume file not found: {args.resume}")
        sys.exit(1)
    if not os.path.exists(args.jd):
        print(f"Error: JD file not found: {args.jd}")
        sys.exit(1)

    with open(args.resume) as f:
        resume_text = f.read()
    with open(args.jd) as f:
        jd_text = f.read()

    corpus = []
    if args.corpus_dir and os.path.isdir(args.corpus_dir):
        corpus = load_corpus(args.corpus_dir)

    if not corpus:
        corpus = [jd_text]

    vectorizer = TfidfVectorizer()
    vectorizer.fit(corpus + [jd_text])

    resume_vec = vectorizer.transform(resume_text)
    jd_vec = vectorizer.transform(jd_text)

    score = vectorizer.cosine_similarity(resume_vec, jd_vec)
    top_jd = vectorizer.top_terms(jd_vec)
    matched = vectorizer.matched_terms(resume_vec, jd_vec)
    missing = vectorizer.missing_terms(resume_vec, jd_vec)

    result = {
        'score': round(score, 4),
        'score_pct': round(score * 100, 1),
        'top_jd_terms': dict(top_jd[:10]),
        'matched_terms': list(matched.keys())[:15],
        'jd_not_in_resume': missing['jd_not_in_resume'][:10],
        'resume_not_in_jd': missing['resume_not_in_jd'][:10],
        'corpus_size': len(corpus)
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(f"\n{'='*50}")
    print(f"ATS SCORE: {result['score_pct']}% (corpus: {result['corpus_size']} docs)")
    print(f"{'='*50}")
    print(f"\nTop JD Keywords (by weight):")
    for term, weight in top_jd[:10]:
        bar = '#' * int(weight * 20)
        print(f"  {term:<20} {bar} {weight:.3f}")
    print(f"\nMatched terms (resume ∩ JD): {len(matched)}")
    for term in list(matched.keys())[:15]:
        rw, jw = matched[term]
        print(f"  ✓ {term:<20} resume={rw:.3f}  jd={jw:.3f}")
    print(f"\n⚠ JD terms MISSING from resume ({len(missing['jd_not_in_resume'])}):")
    for t in missing['jd_not_in_resume'][:10]:
        print(f"  ✗ {t} (jd weight: {jd_vec.get(t, 0):.3f})")
    print()


if __name__ == '__main__':
    main()
