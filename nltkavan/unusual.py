#! /usr/bin/python2

import os
import sys
import nltk

PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEXT_DIR = PROJECT_DIR + sys.argv[1]
text = sys.argv[2]

corpus = nltk.corpus.PlaintextCorpusReader(TEXT_DIR, [text])
n_text = nltk.text.Text(corpus.words(text))

# What are the unusual words?
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    #print text_vocab
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)
print( "\n".join(unusual_words(n_text)))
