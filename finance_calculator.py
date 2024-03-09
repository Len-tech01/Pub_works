import math
""" This program works in VScode terminal but vanishes part -way through
when it does the calculations for investment or bond
if you just fire finance_calculator.py from file directory - any reason?"""


# output of the opening screen
print("""\n\n\t\t Finance Calculator 
\t\t ------------------
Investment - to calculate the amount of interest earned 
             on your investment \n
Bond       - to calculate the amount you will have to pay 
             on a home loan
          
\t Please Enter 'investment' or 'bond'  """)


# initialise variables
invalid_choice = True

# get user choice

while invalid_choice:
  user_select = input("Please enter your choice: ")
  selection = user_select.lower()  # standardise input to lower case
  if (selection == "investment"  or selection == "bond") :
     invalid_choice = False
   
  else:
    print (f"You typed {user_select}. \n Please type 'investment' or 'bond." )
    continue

print("\t valid selection")     

# calculation for investment
if selection  == "investment":
    deposit = input ("Plaese enter how much are you depositing in £:")
    deposit = deposit.strip("£")
    deposit = float(deposit)
    interest = input ("Please enter the percetage interest rate % : ") 
    interest = interest.strip("%")
    interest = float(interest)
    years = input("Please enter length of time of your investment in years: ")
    years = years.strip("years")     # incomplete validataion
    years = float(years)             #  will allow decimal years  - expect 2.5 = two and half
    print("*"*50)
    print (f"Your capital is £ {deposit}." )
    print(f"The proposed interest rate is : {interest} %")
    print(f"The investment is for {years} year(s)" )
    print("*"*50 + "\n")
    print("please enter if you want 'simple' or 'compound' interest")
    interest_type = True
    while interest_type :                # checking for valid entry
       int_type_pick = input("Enter 'simple' or 'compound' :  ")
       int_type_pick = int_type_pick.lower()
       if (int_type_pick == "simple") or (int_type_pick == "compound"):
          interest_type = False
       else: 
          print(f"you typed {int_type_pick} . Please enter 'simple' or 'compound'. ")
          continue            
    # calculate simple interest of investment
    # initialise Interest calculation variables
    amount = 0.00
    p = deposit
    r = interest/100       #  convert interest into r of simple interest formula
    t = years 
    # calculate simple interest of investment
    if int_type_pick == 'simple': 
       print("*"*79) 
       print (f"\t Beginning {int_type_pick} interest calculation ")
       amount = p * (1 +r*t)
    # display the simple interest output   
       print(f"\n\n Your investment of {p} for {t} years at {interest} % will end up as  £ {round(amount,2)}. ")
       print("*"*79) 
    if int_type_pick == 'compound':
       print("*"*50) 
       print (f"\t Beginning {int_type_pick} interest calculation ")
       amount = p * math.pow((1+r), t)
    # display the compound interest output
       print(f"\n\n Your investment of {p} for {t} years at {interest} % will end up as  £ {round(amount,2)}")
       print("*"*79)    
# calculation for bond
if selection == "bond":
    house_value = input("Please enter the present value of the house in  £: ") 
    house_value = house_value.strip("£")
    house_value = float(house_value)
    bond_int = input ("Please enter the annual bond interest rate % : ") 
    bond_int = bond_int.strip("%")
    bond_int = float(bond_int)
    months = input("Please enter repayment  of time of your bond  in months: ")
    months = months.strip("months")     # incomplete validataion assume months is the only addendum
    if type(months) == float:
        months = int(months)
    else:
        months = float(months)             #  more likely to be an integer
    print("*"*50)
    print (f"The present value of the house is  £ {round(house_value, 2)} -" )
    print(f"The proposed annual bond  rate is : {bond_int} %")
    print(f"The repayment will be over  {months} month(s)" )
    print("*"*50 + "\n")
# As there is only once choice for bond calculation - proceed directly to calculation
    # calculate bond 
    amount = 0.00
    p = house_value
    i = bond_int/100/12       #  convert annual interest into i the monthly interest rate
    n = months 
    print("*"*50) 
    print(f"\t  {selection.capitalize()}  calculation ")
    print("\t ----------------") 
    amount = (i * p)/(1 - (1+i)**(-n))
    # output the bond information
    print(f"For a bond over {int(n)} months at annual interest {bond_int} % ")
    print(f"will have a monthly payment of  £ {round(amount,2)}")
    print("*"*50)    

print(" \n  \n  ***** Thank you for using this finance_calculator ***** \n\n")


