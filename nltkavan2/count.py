# -*- coding: utf-8 -*-

# TODO: réécrire en python rdflib


import nltk
import codecs


def count(path):
    f = codecs.open(path, "r", encoding="utf-8")
    raw = f.read()
    f.close()

    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

    ctx = {
        'cc' : len(raw),
        'wc' : len(text),
        'uwc' : len(set(text)),
        'wl' : sorted(set(text)),
    }
    ctx['idx'] = ctx['wc'] / float(ctx['uwc'])
    return ctx
