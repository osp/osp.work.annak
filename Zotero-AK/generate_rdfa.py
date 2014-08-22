import rdflib
from rdflib.namespace import RDF

import os
import codecs
from django.template import Template, Context
from django.template import loader
from django.conf import settings


ns = {
    'dc': rdflib.Namespace("http://purl.org/dc/elements/1.1/"),
    'bib': rdflib.Namespace("http://purl.org/net/biblio#"),
    'z': rdflib.Namespace("http://www.zotero.org/namespaces/export#")
}


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
    }""", initNs=ns)


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
settings.configure(
    TEMPLATE_DIRS=(os.path.join(PROJECT_DIR, 'templates'),),
)
t = loader.get_template('gallery.html')
c = Context({
    'namespace_list': ns,
    'book_list': book_list
})

f = codecs.open(os.path.join(PROJECT_DIR, 'gallery.html'), "w", encoding="utf-8")
f.write(t.render(c))
f.close()


