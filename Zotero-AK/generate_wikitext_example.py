import rdflib

DC = rdflib.Namespace("http://purl.org/dc/elements/1.1/")
Z = rdflib.Namespace("http://www.zotero.org/namespaces/export#")

graph = rdflib.Graph()
result = graph.parse("/home/aleray/work/osp.work.annak/Zotero-AK/Zotero-AK.rdf")

book_list = graph.query("""\
    SELECT DISTINCT ?title ?lang
    WHERE {
        ?book z:itemType "book" .
        ?book dc:title ?title .
        ?book z:language ?lang .
    }""", initNs=dict(z=Z, dc=DC))

wikitext = ["== Bibliographie ==", ""]

for r in book_list:
    wikitext.append(u"* ''[[{0}]]'', ({1})".format(*r))

print('\n'.join(wikitext))
