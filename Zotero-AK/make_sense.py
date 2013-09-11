import RDF
from urlparse import urlparse

RDF_STORAGE_DIR = "."
RDF_STORAGE_NAME = "store"

options = "hash-type='bdb', contexts='yes', dir='%s'" % RDF_STORAGE_DIR
storage = RDF.HashStorage(RDF_STORAGE_NAME, options=options)


RDF_MODEL = RDF.Model(storage)


def list_associated_tags(tag):
    """
    List the tags associated the given one
    """
    query = """
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    SELECT DISTINCT ?s ?tags
    WHERE {
        ?s dc:subject "%s" .
        ?s dc:subject ?tags .
    }
    """ % tag

    results = RDF.Query(query, query_language='sparql').execute(RDF_MODEL)

    ret = []
    for r in results:
        ret.append('%s %s' % (r['s'], r['tags']))

    print("\n".join(ret))


def list_people_names():
    query = """
    SELECT DISTINCT ?name
    WHERE {
        ?s a <http://xmlns.com/foaf/0.1/Person> ;
           <http://xmlns.com/foaf/0.1/surname> ?name.
    }
    """

    results = RDF.Query(query, query_language='sparql').execute(RDF_MODEL)

    ret = []
    for r in results:
        ret.append('%s' % (r['name']))

    print("\n".join(ret))


def construct_graph_of_names():
    query = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    CONSTRUCT {
        ?s foaf:name ?name .
    }
    WHERE {
        ?s a foaf:Person ;
           foaf:surname ?name.
    }
    """

    new_graph = RDF.Query(query, query_language='sparql').execute(RDF_MODEL)

    print(new_graph.to_string())


def is_there_more_books_than_blogposts():
    """
    Is there more books than blog posts?
    """
    query = """
    PREFIX z: <http://www.zotero.org/namespaces/export#> 
    ASK
    {
        ?books z:itemType "book" .
        ?blogposts z:itemType "blogPost" .
        FILTER(?books > ?blogposts) .
    }
    """

    answer = RDF.Query(query, query_language='sparql').execute(RDF_MODEL)
    print(answer)


def tell_me_whatever_about(title):
    query = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    DESCRIBE ?something
    WHERE {
        ?something dc:title "%s" .
    }
    """ % title
    answer = RDF.Query(query, query_language='sparql').execute(RDF_MODEL)
    print(answer)


def select_title(title):
    query = """
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    select ?something 
    WHERE {
        ?something dc:title "%s" .
    }
    """ % title
    results = RDF.Query(query, query_language='sparql').execute(RDF_MODEL)
    ret = []
    for r in results:
        ret.append('%s' % r['something'])

    print("\n".join(ret))


if __name__ == "__main__":
    #list_associated_tags("blog")
    #list_people_names()
    #construct_graph_of_names()
    is_there_more_books_than_blogposts()
    #tell_me_whatever_about("AK")
    #select_title("AK")
