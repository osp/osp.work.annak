# -*- coding: utf-8 -*-


import rdflib
from itertools import groupby


# On créé un graph RDF et on charge le contenu de la base de données Zotero
# dans ce graph
g = rdflib.Graph()
g.load('Zotero-AK.rdf')


# On déclare les espaces de noms utilisés dans Zotero
ns = {
    'bib': rdflib.Namespace("http://purl.org/net/biblio#"),
    'z': rdflib.Namespace("http://www.zotero.org/namespaces/export#"),
    'dc': rdflib.namespace.DC,
    'dcterms': rdflib.namespace.DCTERMS,
    'foaf': rdflib.namespace.FOAF
}

def who_read_ice():
    """
    Who has read 'Ice' and written something about it on-line?
    """
    qs = """SELECT DISTINCT ?doc ?title ?date ?surname ?abstract
    WHERE {
        ?doc a bib:Document .
        ?doc z:itemType "blogPost" .
        ?doc dc:subject "Ice" .
        ?doc dc:title ?title .
        ?doc dc:date ?date .
        ?doc dcterms:abstract ?abstract .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .
    } ORDER BY ?date
    """

    results = g.query(qs, initNs=ns)

    if results:
        print("<p>Here is a recollection of enthusiastic and critical blogposts about 'Ice' published by bloggers since 2000:</p>")

        for res in results:
            #print(u"* [{} {}], par {} (le {})\n\n{}\n\n".format(res.doc, res.title, res.surname, res.date, res.abstract))
            print(u"""<article><header><p>le <time>{}</time>, par <span>{}</span></p><h1><a href="{}">{}</a></h1><blockquote>{}</blockquote></article>\n\n""".format(res.date, res.surname, res.doc, res.title, res.abstract).encode('utf-8'))
        print("""\n\n""")


def chatty():
    """
    Who is chatty about her life?
    """
    qs = """SELECT DISTINCT ?doc ?title ?date ?surname ?abstract
    WHERE {
        ?doc a bib:Document .
        ?doc z:itemType "blogPost" .
        ?doc dc:subject "sensational life" .
        ?doc dc:title ?title .
        ?doc dc:date ?date .
        ?doc dcterms:abstract ?abstract .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .
    } ORDER BY ?date
    """

    results = g.query(qs, initNs=ns)

    if results:
        print("<p>Her sensational life has often been in front page</p>")

        for res in results:
            print(u"""<article><header><p>le <time>{}</time>, par <span>{}</span></p><h1><a href="{}">{}</a></h1><blockquote>{}</blockquote></article>\n\n""".format(res.date, res.surname, res.doc, res.title, res.abstract).encode('utf-8'))
        print("""\n\n""")


def drug_addict():
    """
    Anna Kavan, a hero(in)?
    """
    qs = """SELECT DISTINCT ?doc ?title ?date ?surname ?abstract
    WHERE {
        ?doc a bib:Document .
        ?doc z:itemType "blogPost" .
        ?doc dc:subject "drug addict" .
        ?doc dc:title ?title .
        ?doc dc:date ?date .
        ?doc dcterms:abstract ?abstract .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .
    } ORDER BY ?date
    """

    results = g.query(qs, initNs=ns)

    if results:
        print("<p>All those who know about her life-long heroin addiction:</p>")

        for res in results:
            print(u"""<article><header><p>le <time>{}</time>, par <span>{}</span></p><h1><a href="{}">{}</a></h1><blockquote>{}</blockquote></article>\n\n""".format(res.date, res.surname, res.doc, res.title, res.abstract).encode('utf-8'))
        print("""\n\n""")


def scotland_yard():
    """
    What did say Scotland Yard when they found Kavan on 5th december 1968?
    """
    qs = """SELECT DISTINCT ?doc ?title ?date ?surname ?abstract
    WHERE {
        ?doc a bib:Document .
        ?doc z:itemType "blogPost" .
        ?doc dc:subject "enough heroin" .
        ?doc dc:title ?title .
        ?doc dc:date ?date .
        ?doc dcterms:abstract ?abstract .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .
    } ORDER BY ?date
    """

    results = g.query(qs, initNs=ns)

    if results:
        print("<p>Even if there was enough heroin to kill the whole street, still her death has been interpretated in various ways...</p>")

        for res in results:
            print(u"""<article><header><p>le <time>{}</time>, par <span>{}</span></p><h1><a href="{}">{}</a></h1><blockquote>{}</blockquote></article>\n\n""".format(res.date, res.surname, res.doc, res.title, res.abstract).encode('utf-8'))
        print("""\n\n""")


def like():
    """
    Who are the writers often recalled when writing about Kavan ?
    """
    qs = """SELECT *
    WHERE {
        ?doc a bib:Document .
        ?doc z:itemType "blogPost" .
        ?doc dc:subject ?tag .
        ?doc dc:title ?title .
        ?doc dc:date ?date .
        ?doc dcterms:abstract ?abstract .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .

        FILTER(STRSTARTS(?tag, 'like ')) .
    }
    ORDER BY ?tag ?title
    """

    results = g.query(qs, initNs=ns)

    if results:
        print("<p>If it has been said that she was Kafka's sister, wider filiations are opened by her readers.</p>")


    for group in groupby(results.bindings, lambda x: x['?tag']):
        print("<p><strong>{}</strong></p>".format(group[0]))
        for res in group[1]:
            print(u"""<article><header><p>le <time>{}</time>, par <span>{}</span></p><h1><a href="{}">{}</a></h1><blockquote>{}</blockquote></article>\n\n""".format(res['?date'], res['?surname'], res['?doc'], res['?title'], res['?abstract']).encode('utf-8'))
        print("""\n\n""")


def self_portrait():
    """
    Beyond her books, who does mention her paintings?
    """
    qs = """SELECT ?doc ?title ?date ?surname ?abstract
    WHERE {
        ?doc a bib:Document .
        ?doc z:itemType "blogPost" .
        ?doc dc:subject "self-portrait" .
        ?doc dc:title ?title .
        ?doc dc:date ?date .
        ?doc dcterms:abstract ?abstract .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .
    } ORDER BY ?date
    """

    results = g.query(qs, initNs=ns)

    if results:
        print("<p>Where Anna Kavan's paintings re-appeared on-line whereas in the physical world museal institutions newly acquired her works or exhibited them in galleries.</p>")

        for res in results:
            print(u"""<article><header><p>le <time>{}</time>, par <span>{}</span></p><h1><a href="{}">{}</a></h1><blockquote>{}</blockquote></article>\n\n""".format(res.date, res.surname, res.doc, res.title, res.abstract).encode('utf-8'))
        print("""\n\n""")








if __name__ == "__main__":
    #who_read_ice()
    #chatty()
    #drug_addict()
    #scotland_yard()
    #like()
    self_portrait()
