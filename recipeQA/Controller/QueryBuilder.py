class QueryBuilder:
    def __init__(self):
        self.is_type = False
        self.food_type = ""
        self.is_country = False
        self.country = ""
        self.is_course = False
        self.course = ""
        self.ingredients = 0
        self.ingredients_list = []
        self.recipe_name = ""
        self.is_recipe_name = False

    def setType(self, types: str):
        types_array = types.split("type")[1]
        self.is_type = True
        food_type = ""
        for i in range(len(types_array)):
            if i == 0:
                chars = [char for char in types_array[i]]
                first_char = chars[0]
                chars[0] = first_char.upper()
                string = str(chars)
                food_type = string
            else:
                food_type = food_type + types_array[i]
        self.food_type = food_type

    def getIsType(self) -> bool:
        return self.is_type

    def getFoodType(self) -> str:
        return self.food_type

    def setCountry(self, country_str: str):
        self.is_country = True
        country_array = country_str.split("country")[1]
        country = ""
        for i in range(len(country_array)):
            if i == 0:
                chars = [char for char in country_array[i]]
                first_char = chars[0]
                chars[0] = first_char.upper()
                string = str(chars)
                country = string
            else:
                country = country + country_array[i]
        self.country = country

    def getIsCountry(self) -> bool:
        return self.is_country

    def getCountry(self) -> str:
        return self.country

    def setCourse(self, course_str: str):
        self.is_course = True
        course_array = course_str.split("country")[1]
        course = ""
        for i in range(len(course_array)):
            if i == 0:
                chars = [char for char in course_array[i]]
                first_char = chars[0]
                chars[0] = first_char.upper()
                string = str(chars)
                course = string
            else:
                course = course + course_array[i]
        self.course = course

    def getIsCourse(self) -> bool:
        return self.is_course

    def getCourse(self) -> str:
        return self.course

    def addIngredients(self, ingredients_str: str):
        ingredients_array = ingredients_str.split("ingredients")[1]
        self.ingredients = len(ingredients_array)
        ingredients = []
        for i in range(len(ingredients_array)):
            if i == 0:
                chars = [char for char in ingredients_array[i]]
                first_char = chars[0]
                chars[0] = first_char.upper()
                string = str(chars)
                ingredients.append(string)
            else:
                ingredients.append(ingredients_array[i])
        self.ingredients_list = ingredients

    def getIngredientCount(self) -> int:
        return self.ingredients

    def getIngredientList(self) -> list:
        return self.ingredients_list

    def setRecipeName(self, recipe_str: str):
        self.is_recipe_name = True
        recipe_array = recipe_str.split("country")[1]
        recipe_name = ""
        for i in range(len(recipe_array)):
            if i == 0:
                chars = [char for char in recipe_array[i]]
                first_char = chars[0]
                chars[0] = first_char.upper()
                string = str(chars)
                recipe_name = string
            else:
                recipe_name = recipe_name + recipe_array[i]
        self.recipe_name = recipe_name

    def getIsRecipeName(self) -> bool:
        return self.is_recipe_name

    def getRecipeName(self) -> str:
        return self.recipe_name

    def ingredientQuery(self, ingredient: str) -> str:
        return 'FILTER REGEX (?ingredient, "' + ingredient + '", "i").'
