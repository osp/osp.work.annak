# Prints a list of Open Library pages (related to Anna Kavan) to index

import requests
import json
import rdflib

graph = rdflib.Graph()

ns_stats = rdflib.Namespace("http://kavan.land/vocab/stats#")
graph.namespace_manager.bind('stats', ns_stats)

# key for Anna Kavan
author_key = 'OL200810A'
r1 = requests.get('http://openlibrary.org/authors/%s/works.json' % author_key)

works = r1.json()

for work in works['entries']:
    r2 = requests.get('https://openlibrary.org%s.json' % work['key'])

    data = r2.json()

    if data.has_key('subject_people'):
        subject = rdflib.URIRef('https://openlibrary.org%s/' % work['key'])

        for people in data['subject_people']:
            graph.add((subject, ns_stats.hasCharacter, rdflib.Literal(people)))

print(graph.serialize(format="turtle"))
