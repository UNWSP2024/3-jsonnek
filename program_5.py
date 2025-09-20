# Jonathan Sonnek
# Sept 19th 2025
# Hot Dog Cost Program

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

# Defining Variables
cost = 0.0
Hot_Dog = 3.50
Chili_Dog = 4.50
Cheese = 0.50
Peppers = 0.75
Grilled_Onions = 1.00

# Selecting Hot Dog
hotdog = input("Enter type of Hotdog, (Chili or Normal): ")
if str.lower(hotdog) == "chili":
    cost = Chili_Dog
elif str.lower(hotdog) == "normal":
    cost = Hot_Dog
else:
    print("Invalid entry!")
    exit()

# Ask For Cheese
toppings = input("Enter cheese if you want cheese on your hotdog: ")
if str.lower(toppings) == "cheese":
    cost += Cheese

# Ask for Peppers
toppings = input("Enter pepper if you want peppers on your hotdog: ")
if str.lower(toppings) == "peppers":
    cost += Peppers

# Ask for onions
toppings = input("Enter onions if you want grilled onions on your hotdog: ")
if str.lower(toppings) == "onions":
    cost += Grilled_Onions

# Calculate 7% tax and Total
Sales_Tax = cost * 0.07
Total = cost + Sales_Tax

#Display Cost of Hot Dog, Sales Tax, and Total
print('\n\tSubtotal  =\t', f'{cost:.2f}')
print('\tSales Tax =\t', f'{Sales_Tax:.2f}')
print('\t\tTotal = ', f'{Total:.2f}')