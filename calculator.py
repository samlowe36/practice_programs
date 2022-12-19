def add(x, y):
    answer = x + y
    print("Answer: " + str(answer) + "\n")


def subtract(x, y):
    answer = x - y
    print("Answer: " + str(answer) + "\n")


def multiply(x, y):
    answer = x * y
    print("Answer: " + str(answer) + "\n")


def divide(x, y):
    answer = x / y
    print("Answer: " + str(answer) + "\n")


def exponent(x, y):
    answer = x ** y
    print("Answer: " + str(answer) + "\n")

while True:
    print("""
Available Options:
Addition "+"
Subtraction "-"
Multiplication "*"
Division "/"
Exponents "^"
Exit "X"
""")

    choice = input("input your choice: ")

    if choice == "+":
        print("Addition")
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        add(x, y)
    elif choice == "-":
        print("Subtraction")
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        subtract(x, y)
    elif choice == "*":
        print("Multiplication")
        x = int(input("Input first number: "))
        y = int(input("Input second number: "))
        multiply(x, y)
    elif choice == "/":
        try:
            print("Division")
            x = int(input("Input first number: "))
            y = int(input("Input second number: "))
            divide(x, y)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
    elif choice == "^":
        print("Exponents")
        x = int(input("Input first number: "))
        y = int(input("Input the power: "))
        exponent(x, y)
    elif choice == "x" or choice == "X":
        print("Program Ended")
        quit()
    else:
        print("Invalid Operator. Please try again!")
