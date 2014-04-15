#! /usr/bin/env python

# Finds bigrams (word couples) in a text
#
# USAGE
#
# python collocations.py TEXT
# python collocations.py "file.txt"     # if text is in current directory
# python collocations.py "../books-AK/Ice/Ice.txt"     # text folder from project directory


import os
import nltk
from nltk.corpus import PlaintextCorpusReader
from json import dumps
import sys


LOCAL_PATH = sys.argv[1]
PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#TEXT_DIR = PROJECT_DIR + sys.argv[1]
TEXT_DIR = PROJECT_DIR + "/" + "/".join(LOCAL_PATH.split("/")[1:-1]) + "/"
text =  LOCAL_PATH.split("/")[-1]

def collocations(text):
    text = '%s' % text
    corpus = PlaintextCorpusReader(TEXT_DIR, [text])
    n_text = nltk.text.Text(corpus.words(text))

    bigram_measures = nltk.collocations.BigramAssocMeasures()

    # Finds bigrams
    from nltk.collocations import BigramCollocationFinder
    
    finder = BigramCollocationFinder.from_words(n_text)
    ignored_words = nltk.corpus.stopwords.words('english')
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
    bigrams = finder.nbest(bigram_measures.likelihood_ratio, 20)

    #return template('templates/split', text=source, word_list=foo)
    return dumps ({'name': text, 'bigrams': bigrams})

print collocations(text)
