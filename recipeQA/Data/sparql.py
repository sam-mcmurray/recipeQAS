from SPARQLWrapper import SPARQLWrapper, JSON


def queryExecutor(query: str):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql/")
    sparql.setQuery(query)
    try:
        sparql.setReturnFormat(JSON)
        ret = sparql.query()
        response = ret.convert()
        return response['results']['bindings']
    except Exception as e:
        print(e)


def wikiQueryExecutor(query: str):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(query)
    try:
        sparql.setReturnFormat(JSON)
        ret = sparql.query()
        response = ret.convert()
        return response['results']['bindings']
    except Exception as e:
        print(e)



#     sparql.wikiQueryExecutor("""SELECT DISTINCT ?item ?itemLabel WHERE {
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
#   {
#     SELECT DISTINCT ?item WHERE {
#       ?item p:P527 ?statement0.
#       ?statement0 (ps:P527/(wdt:P279*)) wd:Q2095.
#     }
#     LIMIT 100
#   }
# }""")