# -*- coding: utf-8 -*-

# TODO: réécrire en python rdflib


import nltk
import os
import codecs
from django.template import Template, Context
from django.template import loader
from django.conf import settings


books = {
    "http://openlibrary.org/works/OL11334022W/": "ACharmedCircle.txt",
    "http://openlibrary.org/works/OL1740037W/": "AStrangerStill.txt",
    "http://openlibrary.org/works/OL1740040W/": "IAmLazarus.txt",
    "http://openlibrary.org/works/OL11334034W/": "Ice.txt",
    "http://openlibrary.org/works/OL11334025W/": "LetMeAlone.txt",
    "http://openlibrary.org/works/OL1740034W/": "Mercury.txt",
    "http://openlibrary.org/works/OL11334026W/": "MySoulInChina.txt",
    "http://openlibrary.org/works/OL1740047W/": "SleepHasHisHouse.txt",
    "http://openlibrary.org/works/OL16819062W/": "TheHorseSTale.txt",
    "http://openlibrary.org/works/OL1740044W/": "TheParson.txt",
    "http://openlibrary.org/works/OL1740046W/": "WhoAreYou.txt",
    #"http://openlibrary.org/works/OL11334031W/": julia and the bazooka,
    #"http://openlibrary.org/works/OL16818977W/": the dark sisters,
    #"http://openlibrary.org/works/OL16818996W/": rich get rich,
    #"http://openlibrary.org/works/OL1740026W/": change the name,
    #"http://openlibrary.org/works/OL1740029W/": goose cross,
    #"http://openlibrary.org/works/OL1740030W/": guilty,
    #"http://openlibrary.org/works/OL1740035W/": my madness,
    #"http://openlibrary.org/works/OL1740045W/": a scarcity of love,
    #"http://openlibrary.org/works/OL1740048W/": Asylum piece and other stories
    #"http://openlibrary.org/works/OL11334021W/": a bright green field, including 'new and splendid'
    #"http://openlibrary.org/works/OL11334023W/": eagles' nest,
}


ebooks_base_path = "../../osp.work.annak.books/ebooks/txt/"


if __name__ == '__main__':
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    settings.configure(
        TEMPLATE_DIRS=(os.path.join(PROJECT_DIR, 'templates'),),
    )

    output = [
        "@prefix stats: <http://kavan.land/vocab/stats#> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n"]

    for url, filename in books.items():
        path = os.path.join(ebooks_base_path, filename)

        f = codecs.open(path, "r", encoding="utf-8")
        raw = f.read()
        f.close()

        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)

        ctx = {
            'url': url,
            'cc' : len(raw),
            'wc' : len(text),
            'uwc' : len(set(text)),
            'wl' : sorted(set(text)),
        }
        ctx['idx'] = ctx['wc'] / float(ctx['uwc'])

        t = loader.get_template('stats.ttl')
        c = Context(ctx)

        output.append(t.render(c))

    f = codecs.open(os.path.join(PROJECT_DIR, 'stats.ttl'), "w", encoding="utf-8")
    f.write("\n".join(output))
    f.close()
