#! /usr/bin/env python

# Finds proper names in a text
#
# USAGE
#
# python collocations.py TEXT_PATH_FROM_PROJECT_ROOT
# python collocations.py "file.txt"     # if text is in current directory
# python collocations.py "../books-AK/Ice/Ice.txt"     # text folder from project directory

import re
import os
import sys


LOCAL_PATH = sys.argv[1]
PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
text = PROJECT_DIR + LOCAL_PATH.strip(".")

f = open(text, "r")
text = f.readlines()
f.close()

tmp = open("/tmp/proper.txt", "w")


from nltk import DefaultTagger, UnigramTagger, BigramTagger
from nltk.corpus import brown
# This section is recompiled from the Natural Language Processing Book: http://nltk.googlecode.com/svn/trunk/doc/book/book.html
brown_news_tagged = brown.tagged_sents(categories='news') # Automatic tagging of a sentence, based on Brown News corpus
size = int(len(brown_news_tagged) * 0.9)
brown_news_train = brown_news_tagged[:size]
unigram_tagger = UnigramTagger(brown_news_train)
# Uses BigramTagger -- if it fails, it uses the UnigramTagger -- if it fails, it uses DefaultTagger
t0 = DefaultTagger('NN')
t1 = UnigramTagger(brown_news_train, backoff=t0)
tagger = BigramTagger(brown_news_train, backoff=t1)


for line in text:
    tagged =  tagger.tag(line.split(" "))
    is_np = re.compile(r"NP")
    for w in tagged:
        if (is_np.match(w[1])):
            #print w[0]
            tmp.write(w[0] + "\n")

tmp.close()

# Sort list and remove duplicates
os.system("cat /tmp/proper.txt | sort | uniq") 

