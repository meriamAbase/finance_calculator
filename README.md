# Capstone Proejct - Finance Calculator
For this project, I will show you how to create a program that allows users to access two different financial calculators: an investment calculator and a home calculator.

First, import math.

Then, use a while-loop to avoid calculator terminating upon invalid input.
Greet the user and ask which financial investment they require. 
Convert this variable into lowercase.

Print out an appropriate error message in case the first input was incorrect.
This will loop back to the start of the finance calculator.

Using an if-statement, for 'investment', we will ask the user for the following: 
The amount of money they are depositing ('deposit').
The interest rate ('interest') as a number only. This will then be divided by
100 for our calculations later.
The number of years they plan on investing ('num_of_years').

Next, this is optional, add a friendly message thanking the user for their
input so far.

Use a nested while-loop to avoid starting at the beginning again.
Find out if the users interest is a 'simple' interest or a 'compound' interest.
again, convert this variable into lowercase.

Create a nested if-statment and do the following:
if simple interest, use the following formulae to work out the total earnings:
simple_total = deposit*(1 + interest*num_of_years).
Make sure to round this digit up to the 2nd decimal point using the 'round'
function.
Print out a sentence saying how much the user will save after num_of_years.

Else, if compound interest, use the following formulae to
work out the total earnings:
compound_total = deposit * math.pow((1+interest),num_of_years).
Make sure to round this up as well. 
Print out a sentence saying how much the user will save after num_of_years.  

add an else-statement to print n error message if the input is invalid.
This will loop back to the simple/compound choice question. 


Going back to the first if-statment, if the user chooses a home calculator
(bond), ask the user for the following:
The present value of their house ('house').
The interest rate in a number only ('interest_rate').
The number of months they plan to take to repay the bond ('num_of_months').

Use the following formulae to work out the total money they will need to repay each month:
repayment = (interest_rate*house)/(1-(1+interest_rate)**(-num_of_months)).
Do not forget to round this up the the 2nd decimal point.

Print out how much they will have to pay back a month.

And finally, again optional(but advised), add an appropriate thank you 
message for the user.

