def main():
    print("This is a monthly payment loan calculator")
    print("")
    print("")


    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the number of years: "))
    print("")
    print("")

    monthly_interest_rate = apr / 1200
    months_amount = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months_amount))


    print("The monthly payment for this loan is: %.2f" % monthly_payment)

main()