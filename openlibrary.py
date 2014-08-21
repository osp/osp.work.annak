# Prints a list of Open Library pages (related to Anna Kavan) to index

import requests
import json

# key for Anna Kavan
author_key = 'OL200810A'


print('https://openlibrary.org/authors/OL200810A/Anna_Kavan')

r1 = requests.get('http://openlibrary.org/authors/%s/works.json' % author_key)

works = r1.json()

for work in works['entries']:
    print('https://openlibrary.org%s.rdf' % work['key'])

    r2 = requests.get('http://openlibrary.org%s/editions.json' % work['key'])

    editions = r2.json()

    for edition in editions['entries']:
        print('https://openlibrary.org%s.rdf' % edition['key'])
