
print("Enter question")
question = input(">")

sentence = question.split(" ")

for word in range(len(sentence)):
    if word == "what":
        print("what")


