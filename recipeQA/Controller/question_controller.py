from QueryBuilder import QueryBuilder


# type, ingredients, course, country, recipe name
def sentenceDeconstruction(sentence: str) -> QueryBuilder:
    query_builder = QueryBuilder()
    subjects = sentence.split(";")
    for i in range(len(subjects)):
        words = subjects[i].split(" ")
        for word in words:
            if word.lower() == "type":
                query_builder.setType(subjects[i])
            if word.lower() == "ingredients":
                query_builder.addIngredients(subjects[i])
            if word.lower() == "recipe name":
                query_builder.setRecipeName(subjects[i])
            if word.lower() == "course":
                query_builder.setCourse(subjects[i])
            if word.lower() == "country":
                query_builder.setCountry(subjects[i])
    return query_builder

