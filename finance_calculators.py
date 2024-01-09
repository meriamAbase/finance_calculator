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

