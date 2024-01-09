
# For this project, I will show you how to create a program that allows users 
# to access two different financial calculators: 
# an investment calculator and a home calculator.

# First, import math.

# Then, use a while-loop to avoid calculator terminating upon invalid input.
# Greet the user and ask which financial investment they require. 
# Convert this variable into lowercase.

# Print out an appropriate error message in case the first input was incorrect.
#This will loop back to the start of the calculator. 

# Using an if-statement, for 'investment', we will ask the user for the 
# following: the amount of money they are depositing ('deposit').
# The interest rate ('interest') as a number only. This will then be divided by
# 100 for our calculations later.
# The number of years they plan on investing ('num_of_years').

# Next, this is optional, add a friendly message thanking the user for their
# input so far.

# Use a nested while-loop to avoid starting at the beginning again.
# Find out if the users interest is a 'simple' interest or a 'compound' interest.
# again, convert this variable into lowercase.

# Create a nested if-statment and do the following:
# if simple interest, use the following formulae to work out the total earnings:
# simple_total = deposit*(1 + interest*num_of_years).
# Make sure to round this digit up to the 2nd decimal point using the 'round'
# function.
# Print out a sentence saying how much the user will save after num_of_years.

# Else, if compound interest, use the following formulae to
# work out the total earnings:
# compound_total = deposit * math.pow((1+interest),num_of_years).
# Make sure to round this up as well. 
# Print out a sentence saying how much the user will save after num_of_years.  

# add an else-statement to print n error message if the input is invalid.
#This will loop back to the simple/compound choice question.

# Going back to the first if-statment, if the user chooses a home calculator
# (bond), ask the user for the following:
# The present value of their house ('house').
# The interest rate in a number only ('interest_rate').
# The number of months they plan to take to repay the bond ('num_of_months').

# Use the following formulae to work out the total money they will need to repay
# each month:
# repayment = (interest_rate*house)/(1-(1+interest_rate)**(-num_of_months)).
# Do not forget to round this up the the 2nd decimal point.

# Print out how much they will have to pay back a month.

# And finally, again optional(but advised), add an appropriate thank you 
# message for the user.


import math

while True:
    calculator = input("Welcome! Which financial calculator do you require? Investment, or bond?: ").lower()

    if calculator == "investment":
        deposit = float(input("How much money will you be depositing? £"))
        interest = float(input("What percent will the interest rate be? Please enter a number only: "))
        interest = interest/100
        num_of_years = float(input("How many years do you plan on investing?: "))
        
        print("Thank you! We're nearly there!")
        
        while True:
            interest_type = (input("Which interest type will you be using, simple, or compound?: ")).lower()
            
            if interest_type == "simple":
                simple_total = round(deposit*(1 + interest*num_of_years),2)
                print(f"After {num_of_years} years, you will make £{simple_total}!")
                break
                
            elif interest_type == "compound":
                compound_total = round(deposit * math.pow((1+interest),num_of_years),2)
                print(f"After {num_of_years} years, you will make £{compound_total}!")
                break
                
            else:
                print("Error, match not found. Please try again. Tip: Make sure it is spelt correctly and please try again without any special characters.")    
        break    
            
    elif calculator == "bond":
        house = float(input("What is the present value of your house? £"))  
        interest_rate = float(input("What percent will the interest rate be? Please enter a number only: "))
        interest_rate = (interest_rate/100)/12
        num_of_months = float(input("How many months will you repay the bond by?: "))
        
        repayment = round((interest_rate*house)/(1-(1+interest_rate)**(-num_of_months)),2)
        print(f"You will have to pay £{repayment} a month.")
        break

    else:
        print("Error, match not found. Please try again. Tip: Make sure it is spelt correctly and please try again without any special characters.") 
    
print("Thank you for using our services :)")       
     