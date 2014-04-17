import csv
import rdflib


ns = {
    'dc': rdflib.Namespace("http://purl.org/dc/elements/1.1/"),
    'bib': rdflib.Namespace("http://purl.org/net/biblio#"),
    'z': rdflib.Namespace("http://www.zotero.org/namespaces/export#")
}

graph = rdflib.Graph()
result = graph.parse("Zotero-AK.rdf")

# Les choses qui peuvent nous interesser sont:
#
# - la dates de publication;
# - la langue (anglais, français ou autre);
# - le type d'outils ou plate-formes (pages web, sites web, forum ou site
#   communautaire, blog, microblogging, réseau social...);
# - le type de document (billet de blog, thèse, article & critique -- journal,
#   magazine, revue --, enregistrement -- audio/vidéo --, interview, page web;
# - le type de contenus (texte, texte avec médias, médias, citation, contenus
#   avec des méta-données);
# - la situation géographique (pays, ville);
# - l'ouvrage concerné (par exemple tous les articles où est mentionné *Ice*);
# - la famille littéraire : relever les références littéraires (à qui l'on
#   compare, associe, confronte Kavan);
# - l'héroïnomètre : relever les liens où il est fait référence à la drogue et/ou
#   son addiction.

# On se contente d'un sous-ensemble pour l'instant

book_list = graph.query("""\
    SELECT DISTINCT ?title ?date ?itemType ?type ?language
    WHERE {
        ?s a bib:Document .
        ?s dc:title ?title .
        ?s dc:date ?date .
        ?s z:itemType ?itemType .
        ?s z:type ?type .
        ?s z:language ?language .
    }""", initNs=ns)


# On écrit le fichier csv

with open('zotero.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    for item in book_list:
        writer.writerow([i.encode('utf-8') for i in item])
