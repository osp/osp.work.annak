# -*- coding: utf-8 -*-

import rdflib
import os
from collocations import collocations
from count import count


BOOKS = {
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
}


EBOOKS_BASE_PATH = "/home/aleray/work/osp.work.annak/osp.work.annak.books/ebooks/txt/"


if __name__ == '__main__':
    graph = rdflib.Graph()

    ns_stats = rdflib.Namespace("http://kavan.land/vocab/stats#")
    graph.namespace_manager.bind('stats', ns_stats)

    for url, filename in BOOKS.items():
        subject = rdflib.URIRef(url)
        path = os.path.join(EBOOKS_BASE_PATH, filename)

        # generate bigrams
        bigrams = collocations(path)

        for bigram in bigrams:
            graph.add((subject, ns_stats.bigram, rdflib.Literal(" ".join(bigram))))

        # generate stats
        stats = count(path)

        graph.add((subject, ns_stats.hasCharacterCount, rdflib.Literal(stats['cc'])))
        graph.add((subject, ns_stats.hasWordCount, rdflib.Literal(stats['wc'])))
        graph.add((subject, ns_stats.hasUniqueWordCount, rdflib.Literal(stats['uwc'])))
        graph.add((subject, ns_stats.hasDiversityIndice, rdflib.Literal(stats['idx'])))

    print(graph.serialize(format="turtle"))
