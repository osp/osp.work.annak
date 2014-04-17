# -*- coding: utf-8 -*-


import rdflib


# On créé un graph RDF et on charge le contenu de la base de données Zotero
# dans ce graph
g = rdflib.Graph()
g.load('Zotero-AK.rdf')


# On déclare les espace de noms utilisés dans Zotero
ns = {
    'bib': rdflib.Namespace("http://purl.org/net/biblio#"),
    'z': rdflib.Namespace("http://www.zotero.org/namespaces/export#"),
    'dc': rdflib.namespace.DC,
    'foaf': rdflib.namespace.FOAF
}

# L'oeuvre Neige a-t-elle inspirée de nouvelles créations ?
# tag zotero à mettre en place = #ice #remix ou  #iceremix
print("--- L'oeuvre Neige a-t-elle inspirée de nouvelles créations ? ---\n\n")

# Il y a t-il des documents avec pour étiquettes "Ice" et "remix" ?
qs = """ASK {
    ?doc a bib:Document .
    ?doc dc:subject "Ice" .
    ?doc dc:subject "remix" .
}"""

answer = g.query(qs, initNs=ns).askAnswer

if answer:
    print("Oui, l'oeuvre Neige a inspiré d'autres créations\n\n")

    # NOTE: les noms des auteurs sont dans une liste RDF. Pour accéder aux membres
    # de la liste, voir
    # <http://stackoverflow.com/questions/4702518/how-to-access-members-of-an-rdf-list-with-rdflib-or-plain-sparql>
    # La solution employée ici va créer dédoubler les entrées si plusieurs auteurs
    # sont listés pour un résultat (ce cas ne se présente cependant pas.

    qs = """SELECT ?doc ?title ?surname
    WHERE {
        ?doc a bib:Document .
        ?doc dc:subject "Ice" .
        ?doc dc:subject "remix" .
        ?doc dc:title ?title .

        ?doc bib:authors ?seq .
        ?seq ?seq_index ?seq_bnode .
        ?seq_bnode foaf:surname ?surname .
    }"""

    print("""== Liste des remix de Ice ==\n\n""")
    for res in g.query(qs, initNs=ns):
        print(u"* [{0} {1}], par {2}".format(res.doc, res.title, res.surname))
    print("""\n\n""")
else:
    print("Non, l'oeuvre Neige n'a inspiré personne\n\n")

#Q = L'oeuvre Neige a-t-elle fait l'objet de ré-éditions ?
#tag zotero à mettre en place = #ice #bookcover  #reprint

print("--- L'oeuvre Neige a-t-elle fait l'objet de ré-éditions ? ---\n\n")
# TODO: infos non-taguées, le faire avec Zotero ou autre?

qs = """SELECT ?doc ?title
WHERE {
    ?doc a bib:Document .
    ?doc dc:subject "Ice" .
    ?doc dc:subject "bookcover" .
    ?doc dc:title ?title .
}"""

results = g.query(qs, initNs=ns)

if results:
    print("""== Liste des réeditions de Ice ==\n\n""")
    for res in results:
        print("* [{0} {1}]".format(res.doc, res.title))
    print("""\n\n""")

#Q = L'oeuvre Neige a-t-elle été traduites ?
#tag zotero à mettre en place = #ice #bookcover  #lang
print("--- L'oeuvre Neige a-t-elle été traduite ? ---\n\n")

qs = """SELECT ?doc ?title
WHERE {
    ?doc a bib:Document .
    ?doc dc:subject "Ice" .
    ?doc dc:subject "lang" .
    ?doc dc:title ?title .
}"""

results = g.query(qs, initNs=ns)

if results:
    print("""== Liste des traductions de Ice ==\n\n""")
    for res in results:
        print("* [{0} {1}]".format(res.doc, res.title))
    print("""\n\n""")

#Q = Oracle, donnes moi une citation ?
#tag zotero à mettre en place = #ice #quote

#Q =  Qui a lu Neige ?
#tag zotero à mettre en place = #ice #blog #fans
print("--- Qui a lu neige ? ---\n\n")

# NOTE: j'ai remplacé #blog par une requête sur z:itemType = "Blogpost"

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
