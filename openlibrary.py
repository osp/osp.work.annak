import requests
import json

# key for Anna Kavan
author_key = 'OL200810A'


#r = requests.get('http://openlibrary.org/query.json?type=/type/edition&authors=/authors/%s' % author_key)

#data = r.json()

#for i in data:
    #print(i)

r1 = requests.get('http://openlibrary.org/authors/%s/works.json' % author_key)

works = r1.json()

#print(json.dumps(data, sort_keys=True, indent=2))

for work in works['entries']:
    print('https://openlibrary.org%s.rdf' % work['key'])

    r2 = requests.get('http://openlibrary.org%s/editions.json' % work['key'])

    editions = r2.json()

    for edition in editions['entries']:
        print('https://openlibrary.org%s.rdf' % edition['key'])
