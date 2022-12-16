from UI import app
from Controller import question_controller
from Data import sparql

if __name__ == "__main__":
    while True:
        app.printMenu()
        user_input = input(">>")
        if user_input.lower() == "h":
            app.printHelp()
        if user_input.lower() == "q":
            exit(0)
        elif len(user_input) > 2:
            query = question_controller.sentenceDeconstruction(user_input)
            results = sparql.queryExecutor(query)
            app.setResults(results)
