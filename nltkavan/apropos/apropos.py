# -*- coding: utf-8 -*-


import nltk
import os
import codecs
from django.template import Template, Context
from django.template import loader
from django.conf import settings


f = codecs.open('../../osp.work.annak.books/AK/Ice/ice-txtonly.txt', "r", encoding="utf-8")
raw = f.read()
f.close()

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)




def plot_proper():
    names = ["Anna", "Dennis", "Helen", "John", "Jorge", "K.", "Luis", "M.", "Owen", "Paul", "Peter", "Philip", "Potter", "S.", "Stone", "Thomas", "William"]
    text.dispersion_plot(names)


def concordance():
    text.concordance('ice')


def similar():
    text.similar('ice')

def common_context():
    text.common_contexts(['Helen', 'Anna'])

def generate():
    text.generate()

def len_statistics():

    ctx = {
        'cc' : len(raw),
        'wc' : len(text),
        'uwc' : len(set(text)),
        'wl' : sorted(set(text))
    }

    return u"""
        <p>
        Ce texte comporte <em>{cc}</em> caractères et <em>{wc}</em> mots, dont <em>{uwc}</em> mots différents.
        </p>
        """.format(**ctx)

def fdist():
    fd = nltk.FreqDist(text)

    ctx = {
        'wl': fd.keys()[:50]
    }

    return u"""
        <p>
        Les mots 50 mots les plus fréquents sont {wl}
        <p>
        """.format(**ctx)

def generate():
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    settings.configure(
        TEMPLATE_DIRS=(os.path.join(PROJECT_DIR, 'templates'),),
    )

    body = u"".join([
        len_statistics(),
        fdist(),
    ])

    t = loader.get_template('apropos.html')
    c = Context({'body': body})
    f = codecs.open(os.path.join(PROJECT_DIR, 'apropos.html'), "w", encoding="utf-8")
    f.write(t.render(c))
    f.close()

if __name__ == '__main__':
    #generate()
    plot_proper()
    concordance()
    similar()
    common_context()

