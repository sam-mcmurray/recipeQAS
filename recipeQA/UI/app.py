from pprint import pprint


class Food:
    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.ingredients = ""
        self.country = ""
        self.course = ""
        self.type = ""
        self.url = url

    def setCountry(self, country: str):
        self.country = country

    def getCountry(self) -> str:
        return self.country

    def setCourse(self, course: str):
        self.course = course

    def getCourse(self) -> str:
        return self.course

    def setType(self, food_type: str):
        self.type = food_type

    def getType(self) -> str:
        return self.type

    def getDescription(self) -> str:
        return self.description

    def getName(self) -> str:
        return self.name

    def getUrl(self) -> str:
        return self.url

    def getIngredients(self) -> str:
        return self.ingredients

    def setIngredients(self, ingredients: str):
        self.ingredients = ingredients


menu = ["h: Help", "q: Exit"]


def printMenu():
    print("Welcome to RecipeQAS")
    print("*" * 50)
    for i in range(len(menu)):
        print(menu[i])
    print("Ask Question")


def printHelp():
    print("Help:")
    print("> To find a recipe by name")
    print("ex.(recipeName chicken curry;)")
    print("> To find a recipe by type")
    print("ex.(type curry;)")
    print("> To find a recipe by country")
    print("ex.(country indian subcontinent;)")
    print("> To find a recipe by course")
    print("ex.(course main course;)")
    print("> To find a recipe by ingredients")
    print(">ex.(ingredients chicken onions garlic chili peppers;")
    print("> A search can be preformed with any combination of features")
    print("ex.(recipe name chicken curry; type curry;country indian subcontinent;)")
    print("> Please note not every recipe has all information available...")
    print("> The more complex a question the more likely it is to return nothing")


def printFood(food: Food):
    print("Name: ", food.getName())
    descr = "Description: " + food.getDescription()
    pprint(descr)
    print("URL: ", food.getUrl())
    if food.getType() != "":
        print("Type: ", food.getType())
    if food.getIngredients() != "":
        print("Ingredients: ", food.getIngredients())
    if food.getCountry() != "":
        print("Country: ", food.getCountry())
    if food.getCourse() != "":
        print("Course: ", food.getCourse())


def setResults(results):
    food_list = []
    for i in range(len(results)):
        food = Food(results[i]['recipeName']['value'], results[i]['description']['value'], results[i]['food']['value'])
        try:
            food.setCountry(results[i]['country']['value'])
        except Exception as e:
            food.setCountry("")
        try:
            food.setCourse(results[i]['course']['value'])
        except Exception as e:
            food.setCourse("")
        try:
            food.setType(results[i]['course']['value'])
        except Exception as e:
            food.setType("")
        try:
            food.setIngredients(results[i]['ingredient']['value'])
        except Exception as e:
            food.setType("")
        food_list.append(food)

    for i in range(len(food_list)):
        printFood(food_list[i])
