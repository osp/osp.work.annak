# -*- coding: utf-8 -*-


import rdflib
import subprocess
import sys
import codecs


sys.stdout = codecs.getwriter("utf-8")(sys.stdout)


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

qs = """SELECT ?doc ?title
WHERE {
    ?doc a bib:Document .
    ?doc z:itemType "blogPost" .
    ?doc dc:title ?title .
}
"""

results = g.query(qs, initNs=ns)

for res in results:
    sys.stdout.write(u"%s\t%s\n" % (res.doc[7:], res.title))
    #cmd = u"webtocon %s screenshots/%s.png 1280 1024" % (res.doc, res.title)
    #p1 = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    #(stdout_data, stderr_data) = p1.communicate()
