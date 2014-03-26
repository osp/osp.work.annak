import rdflib
from rdflib.namespace import RDF

import os
import codecs
from django.template import Template, Context
from django.template import loader
from django.conf import settings


DC = rdflib.Namespace("http://purl.org/dc/elements/1.1/")
BIB = rdflib.Namespace("http://purl.org/net/biblio#")
Z = rdflib.Namespace("http://www.zotero.org/namespaces/export#")


rdflib.plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')

rdflib.plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')


graph = rdflib.Graph()
result = graph.parse("Zotero-AK.rdf")

book_list = graph.query("""\
    SELECT DISTINCT ?title ?date ?language
    WHERE {
        ?s a bib:Document .
        ?s dc:title ?title .
        ?s dc:date ?date .
        ?s dc:date ?date .
        ?s z:language ?language .
    }""", initNs=dict(bib=BIB, dc=DC, z=Z))


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
settings.configure(
    TEMPLATE_DIRS=(os.path.join(PROJECT_DIR, 'templates'),),
)
t = loader.get_template('gallery.html')
c = Context({
    'namespace_list': {'dc': DC, 'bib': BIB, 'rdf': RDF, 'z': Z},
    'book_list': book_list
})

f = codecs.open(os.path.join(PROJECT_DIR, 'gallery.html'), "w", encoding="utf-8")
f.write(t.render(c))
f.close()


