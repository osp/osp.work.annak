#! /usr/bin/python

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
from nltk.collocations import BigramCollocationFinder
from json import dumps
import sys

(txt_dir, txt_name) = os.path.split(sys.argv[1])

def collocations(text):
    corpus = PlaintextCorpusReader(txt_dir, [txt_name])
    n_text = nltk.text.Text(corpus.words(text))

    bigram_measures = nltk.collocations.BigramAssocMeasures()

    # Finds bigrams

    finder = BigramCollocationFinder.from_words(n_text)
    ignored_words = nltk.corpus.stopwords.words('english')
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
    bigrams = finder.nbest(bigram_measures.likelihood_ratio, 20)

    for bigram in bigrams:
        print(" ".join(bigram).encode('utf-8'))



    #return dumps ({'name': text, 'bigrams': bigrams})

#print(collocations(txt_name))
collocations(txt_name)
