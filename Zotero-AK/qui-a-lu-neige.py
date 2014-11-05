# -*- coding: utf-8 -*-


import rdflib


# On créé un graph RDF et on charge le contenu de la base de données Zotero
# dans ce graph
g = rdflib.Graph()
g.load('Zotero-AK.rdf')


# On déclare les espaces de noms utilisés dans Zotero
ns = {
    'bib': rdflib.Namespace("http://purl.org/net/biblio#"),
    'z': rdflib.Namespace("http://www.zotero.org/namespaces/export#"),
    'dc': rdflib.namespace.DC,
    'foaf': rdflib.namespace.FOAF
}

#Q =  Qui a lu Neige ?
#tag zotero à mettre en place = #ice #blog #fans
print("--- Qui a lu neige ? ---\n\n")

# NOTE: j'ai remplacé #blog par une requête sur z:itemType = "Blogpost"
#Fill-in-the-blank

qs = """SELECT ?doc ?title ?surname ?date
WHERE {
    ?doc a bib:Document .
    ?doc z:itemType "blogPost" .
    ?doc dc:subject "Ice" .
    ?doc dc:subject "fan" .
    ?doc dc:title ?title .
    ?doc dc:date ?date .

    ?doc bib:authors ?seq .
    ?seq ?seq_index ?seq_bnode .
    ?seq_bnode foaf:surname ?surname .
}
"""
#GROUP BY (month(?date) AS ?year)

results = g.query(qs, initNs=ns)

if results:
    print("""== Liste des blogposts sur Ice ==\n\n""")
    for res in results:
        print(u"* [{0} {1}], par {2} (le {3})".format(res.doc, res.title, res.surname, res.date))
    print("""\n\n""")


#Q =  Qui a chroniqué Neige ?
#tag zotero à mettre en place = #ice #blog #reviews
print("--- Qui a chroniqué Neige ? ---\n\n")

qs = """SELECT ?doc ?title
WHERE {
    ?doc a bib:Document .
    ?doc z:itemType "blogPost" .
    ?doc dc:subject "Ice" .
    ?doc dc:subject "reviews" .
    ?doc dc:title ?title .
}"""

results = g.query(qs, initNs=ns)

if results:
    print("""== Liste des blogposts sur Ice ==\n\n""")
    for res in results:
        print(u"* [{0} {1}]".format(res.doc, res.title))
    print("""\n\n""")

#Q =  Qui a étudié Neige ?
#tag zotero à mettre en place = #ice #blog #thesis #papers
