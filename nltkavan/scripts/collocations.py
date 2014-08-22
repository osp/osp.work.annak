#! /usr/bin/python2


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
from optparse import OptionParser


def collocations(text, n=20):
    (txt_dir, txt_name) = os.path.split(text)
    corpus = PlaintextCorpusReader(txt_dir, [txt_name])
    n_text = nltk.text.Text(corpus.words(txt_name))

    bigram_measures = nltk.collocations.BigramAssocMeasures()

    # Finds bigrams
    finder = BigramCollocationFinder.from_words(n_text)
    ignored_words = nltk.corpus.stopwords.words('english')
    finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)

    bigrams = finder.nbest(bigram_measures.likelihood_ratio, n)

    for bigram in bigrams:
        print(" ".join(bigram).encode('utf-8'))


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", dest="number", default=20, help="clean cache")
    (options, args) = parser.parse_args()

    collocations(args[0])
