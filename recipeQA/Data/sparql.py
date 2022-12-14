from SPARQLWrapper import SPARQLWrapper, JSON, N3
from pprint import pprint


sparql = SPARQLWrapper(endpoint="http://dbpedia.org/resource/")

sparql.setQuery("""
PREFIX : <http://dbpedia.org/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
SELECT ?food 
WHERE {
?food a dbo:Food;
} LIMIT 100
""")
sparql.setReturnFormat(JSON)
response = sparql.query().convert()
pprint(response)
#
# for result in response["results"]["bindings"]:
#     print(result)
# find food by name
"""
select distinct ?food where {
?food a dbo:Food;
dbp:name "Apple crumble"@en.
} LIMIT 100
"""

# food by country
"""
select distinct ?food where {
?food a dbo:Food;
dbp:country "United States"@en.
} LIMIT 100
"""

# main ingredient
"""
select distinct ?food where {
?food a dbo:Food;
dbp:mainIngredient "Carrot"@en.
} LIMIT 100
"""

# Food by course

"""
select distinct ?food where {
?food a dbo:Food;
dbp:course "Dessert"@en.
} LIMIT 100
"""

# Ingredient by object dbr:Meat, dbr:Chicken
"""
select distinct ?food where {
?food a dbo:Food;
dbo:ingredient dbr:Vegetable.
} LIMIT 100
"""

# Food by type
"""
select distinct ?food where {
?food a dbo:Food;
dbo:type dbr:Stew.
} LIMIT 100
"""

# Ingredient type and country
"""
select distinct ?food  where {
?food a dbo:Food;
dbo:ingredient dbr:Vegetable;
dbp:country "United States"@en.
} LIMIT 100
"""

"""select ?food, ?name, ?resource where {
?food a dbo:Food;
dbp:mainIngredient ?name.
?name dbp:name ?resource.
} LIMIT 100"""

"""
select ?food, ?name, ?resource where {
?food a dbo:Food;
dbo:type ?name.
?name dbp:name ?resource.
} LIMIT 100"""

"""
select ?food, ?name, ?resource where {
?food a dbo:Food;
dbp:mainIngredient ?name;
dbp:name ?resource.
} LIMIT 100
"""

"""
select ?food, ?name, ?resource where {
?food a dbo:Food;
dbo:type ?name.
?name dbp:name ?resource;
dbp:name "Stew"@en
} LIMIT 100
"""

"""
select ?food, ?ingredient, ?ingredientName, ?description where {
?food a dbo:Food;
dbp:mainIngredient ?ingredient;
dbo:ingredientName ?ingredientName.
?food dbo:abstract ?description
FILTER (LANG(?description)="en").
} LIMIT 100
"""

"""
select ?food, ?ingredient where {
?food a dbo:Food.
?food dbp:mainIngredient ?ingredient
FILTER REGEX (?ingredient, "Chicken", "i").
} LIMIT 100
"""
