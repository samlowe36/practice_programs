import random


def dice_roll():
    active_rolling = True
    while active_rolling:
        d4 = random.randint(1, 4)
        d6 = random.randint(1, 6)
        d8 = random.randint(1, 8)
        d10 = random.randint(1, 10)
        d12 = random.randint(1, 12)
        d20 = random.randint(1, 20)
        d100 = random.randint(1, 100)

        print("")
        roll = input("Roll the dice? (yes/no): ")

        if roll.lower() == "yes":
            print("")
            dice_type = input("What kind of die would you like to roll? (d4/d6/d8/d10/d12/d20/d100): ")

            if dice_type.lower() == "d4":
                print("")
                print("Number rolled: {}".format(d4))
            elif dice_type.lower() == "d6":
                print("")
                print("Number rolled: {}".format(d6))
            elif dice_type.lower() == "d8":
                print("")
                print("Number rolled: {}".format(d8))
            elif dice_type.lower() == "d10":
                print("")
                print("Number rolled: {}".format(d10))
            elif dice_type.lower() == "d12":
                print("")
                print("Number rolled: {}".format(d12))
            elif dice_type.lower() == "d20":
                print("")
                print("Number rolled: {}".format(d20))
            elif dice_type.lower() == "d100":
                print("")
                print("Number rolled: {}".format(d100))
            else:
                print("")
                print("Invalid input. Please try again.")

        elif roll.lower() == "no":
            print("")
            print("Goodbye.")
            active_rolling = False
        else:
            print("")
            print("Invalid input. Please try again.")
            print("")


dice_roll()
