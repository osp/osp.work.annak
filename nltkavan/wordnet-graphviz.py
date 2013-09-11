from nltk.corpus import wordnet as wn

def draw(synset, fn):
    seen = set()
    graph = {}

    def recurse(s):
        if not s in seen:
            seen.add(s)
            for s1 in fn(s):
                graph[s.name] = s1.name
                recurse(s1)

    recurse(synset)
    return graph


dog = wn.synset('dog.n.01')
graph = draw(dog, lambda s: s.hypernyms())


header = """
digraph {
"""

relations = ""


footer = """
}
"""

for key, value in graph.iteritems():
    relations += '"%s" -> "%s";\n' % (key, value)



print header + relations + footer
