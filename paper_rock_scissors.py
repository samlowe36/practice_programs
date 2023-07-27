import random


exit_game = False
user_points = 0
computer_points = 0

while exit_game == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ")
    computer_input = random.choice(options)

    if user_input.upper() == "EXIT":
        print("Game ended. Thanks for playing!")
        print("User Points: " + str(user_points))
        print("Computer Points: " + str(computer_points))

        if user_points > computer_points:
            print("A winner is you!")
        elif computer_points > user_points:
            print("Better luck next time!")
        elif computer_points == user_points:
            print("The game ended in a draw!")

        exit_game = True

    elif user_input.upper() == "ROCK":
        if computer_input == "rock":
            print("Your input is rock.")
            print("Computer input is rock.")
            print("It's a tie!")
        elif computer_input == "paper":
            print("Your input is rock.")
            print("Computer input is paper.")
            print("You lose!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock.")
            print("Computer input is scissors")
            print("You win!")
            user_points += 1

    elif user_input.upper() == "PAPER":
        if computer_input == "rock":
            print("Your input is paper.")
            print("Computer input is rock.")
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper.")
            print("Computer input is paper.")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("Your input is paper.")
            print("Computer input is scissors")
            print("You lose!")
            computer_points += 1

    elif user_input.upper() == "SCISSORS":
        if computer_input == "rock":
            print("Your input is scissors.")
            print("Computer input is rock.")
            print("You lose!")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors.")
            print("Computer input is paper.")
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors.")
            print("Computer input is scissors")
            print("It's a tie!")

    elif user_input.upper() != "ROCK" or user_input.upper() != "PAPER" or user_input.upper() != "SCISSORS" \
            or user_input.upper() != "EXIT":
        print("Invalid response. Please try again!")