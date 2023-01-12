import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    try:
        password_length = int(input("How long will the password be? "))
        random.shuffle(characters)
        password = []

        for x in range(password_length):
            password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)
        print("Here is your new password: " + password)
    except ValueError:
        print("Invalid. Please enter a whole number for password length.")
        print("")
        print("")
        call_generator()


def call_generator():
    option = input("Would you like to generate a password? (yes/no) ")

    if option.lower() == "yes" or option.upper() == "YES":
        generate_password()
    elif option.lower == "no" or option.upper() == "NO":
        print("Program ended. Goodbye.")
        quit()
    else:
        print("Invalid input. please enter yes or no")
        print("")
        print("")
        call_generator()


call_generator()
