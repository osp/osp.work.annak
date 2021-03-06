#! /usr/bin/python

import os
import sys
import nltk

#LOCAL_PATH = sys.argv[1]
#PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#TEXT_DIR = PROJECT_DIR + "/" + "/".join(LOCAL_PATH.split("/")[1:-1]) + "/"
#text =  LOCAL_PATH.split("/")[-1]

(txt_dir, txt_name) = os.path.split(sys.argv[1])

corpus = nltk.corpus.PlaintextCorpusReader(txt_dir, [txt_name])
n_text = nltk.text.Text(corpus.words(txt_name))

stopwords = nltk.corpus.stopwords.words("english")

# What are the unusual words?
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    #print text_vocab
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]

output = diff(unusual_words(n_text), stopwords)

print( "\n".join(output)).encode("utf-8")
