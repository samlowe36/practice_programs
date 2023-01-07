quiz = {
    "Question1": {
        "Question": "What is the capital of France?",
        "Answer": "Paris"
    },
    "Question2": {
        "Question": "What is the capital of Germany?",
        "Answer": "Berlin"
    },
    "Question3": {
        "Question": "What is the capital of Italy?",
        "Answer": "Rome"
    },
    "Question4": {
        "Question": "What is the capital of Spain?",
        "Answer": "Madrid"
    },
    "Question5": {
        "Question": "What is the capital of The United States?",
        "Answer": "Washington DC"
    },
    "Question6": {
        "Question": "What is the capital of England?",
        "Answer": "London"
    },
    "Question7": {
        "Question": "What is the capital of Greece?",
        "Answer": "Athens"
    },
}

score = 0

for key, value in quiz.items():
    print(value["Question"])
    answer = input("Answer? ")

    if answer.lower() == value["Answer"].lower():
        print("Correct")
        score += 1
        print("Your Current Score is: " + str(score))
        print("")
    else:
        print("Wrong!")
        print("The answer is: " + value["Answer"])
        print("Your current score is: " + str(score))
        print("")

print("You got " + str(score) + " out of 7 questions correct!")
print("Your percentage is " + str(int(score/7 * 100)) + "%")