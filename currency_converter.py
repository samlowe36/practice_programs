def main():
    print("This program converts US Dollars to British Pounds")
    print("")

    dollars = eval(input("Enter amount in Dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "Pounds.")


convert_to_pounds = lambda dollars: dollars * 0.82

main()