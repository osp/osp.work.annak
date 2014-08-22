#! /usr/bin/env python2


import codecs
import sys
import nltk
from optparse import OptionParser


def dispersion(text, words):
    tokens = nltk.word_tokenize(text)
    text = nltk.Text(tokens)
    text.dispersion_plot(words)


if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()

    f = codecs.open(args[0], "r", encoding="utf-8")
    text = f.read()
    f.close()

    f = codecs.open(args[1], "r", encoding="utf-8")
    words = f.read()
    f.close()

    words = words.splitlines()
    print(words)

    dispersion(text, words)
