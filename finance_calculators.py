# import all math function.
import math 

# Choose either investment or bond.
choose_either = input("'investment' or 'bond' from the new below to proceed:""\n"
                        "investment     - to calculate the amount of interest you will earn on interest" "\n"
                        "bond           - to calculate the amount you'll have to pay on a home loan" "\n").lower()

# Displaying the choosing type. 
print(choose_either)

# If investment, read the amount deposited, the interest rate and the interest duration from the user.
if choose_either == 'investment':
    investment = int(float(input("Enter the amount of money deposited ")))
    interest_rate = float(input("Enter interest rate note you should enter interest rate like (8) not (8%) ")) /100
    year = int(input("Enter number of years "))

    # User should enter either 'simple' or 'compound' they want and store in a variable.
    interest_type = input("Enter either 'simple' or 'compound' interest ""\n")

    # If interest type is 'simple', complete the calculation for the 'simple' interest.
    if interest_type == 'simple':
        total_interest = investment * (1 + interest_rate * year)

        # Displayed the total interest rate of the user.
        print("The simple interest for the number of years is:""\n", total_interest)

        # else if the interest type is 'compound', complete the calculation for the 'compound' interest.
    else:
        total_interest = investment * (math.pow((1 + interest_rate), year))

        # Display the total interest of the user.
        print(round(total_interest, 2))

#If bond, read the value of the header, the interest rate and the interest duration from the user.
elif choose_either == 'bond':
    house_value = float(input("Enter the value of the house: "))
    interest_rate = float( input("Enter interest rate note you should enter interest rate like (8) not (8%) "))/100 / 12
    number_of_months = int((input("Enter the number of months to repay the bond examole (120) ")))

    # compute the calculation for the interest rate for bond.
    repayment = (interest_rate * house_value) / (1 - ((1 + interest_rate) ** (- number_of_months)))
    # Display the total amount to be repaid.
    print(round(repayment, 2))

