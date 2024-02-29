# This is a comment.
# Use the '#' to being a comment.

#Variables:

length = 5
time = 7.2
in_flight = True
first_name = "cho"

# Data types: str (string), 
#is any text inside single or double quotes, any text that a user enters, and any text in a text file. For example:
greeting = "Hello"
text = "23"

# bool (Boolean Variable),
# is a variable that stores either True or False.
# A Boolean variable may not store any other value besides True or False. For example:
found = True
var_21390 = False

# int (integer), is a whole number like 14.
# An int may not have a fractional part or digits after the decimal point. For example:
x = 14
a = 2
t = 54

# float (integer with decimals),
# is a number that may have a fractional part or digits after the decimal point like 7.51. For example:
sample = 7.51
sample_2 = 33.3333
sample_3 = 1.234

# lists (how to make lists),
#is a collection of values. Each value in a list is called an element and is stored at a unique index. 
# The primary purpose of a list is to efficiently store many elements.
# In a Python program, we can create a list by using square brackets ([ and ]) and separating the elements with commas (,).
# For example here are two lists named colors and samples:
colors = ["red", "blue", "yellow", "green"]
samples = [6.5, 7.2, 7.0, 8.1, 7.2, 6.8, 6.8]
# dict (dictionary),
# is a collection of items. Each item is a key value pair.

# The primary purpose of a dictionary is to enable a computer to find items very quickly.
# In a Python program, we can create a dictionary by using curly braces ({ and }) and separating the items with commas (,).
# For example:
students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
}

# In a Python program, we use the input()
# function to get input from a user in a terminal window. The input function always returns a string of characters.
# exmaple: text = input("")
text = input("Please Enter Your Name: ")
color = input("What Is Your Favorite Color? ")

# In a Python program, we use the print()
# function to display results to a user. The easiest way to print both text and numbers together is to use a
# formatted string literal (also known as an f-string).
# example: print ("")
# example: print (f"text {data type}")
print(f"students: {students}")




# Example 1

# Create variables of different data types and then
# print the variable names, data types, and values.

a = "Her name is "  # string
b = "Isabella"      # string
c = a + b           # string plus string makes string
print(f"a: {type(a)} {a}")
print(f"b: {type(b)} {b}")
print(f"c: {type(c)} {c}")
print()

d = False  # boolean
e = True   # boolean
print(f"d: {type(d)} {d}")
print(f"e: {type(e)} {e}")
print()

f = 15     # int
g = 7.62   # float
h = f + g  # int plus float makes float
print(f"f: {type(f)} {f}")
print(f"g: {type(g)} {g}")
print(f"h: {type(h)} {h}")
print()

i = "True"   # string because of the surrounding quotes
j = "2.718"  # string because of the surrounding quotes
print(f"i: {type(i)} {i}")
print(f"j: {type(j)} {j}")



# Example 2

# The input function always returns a string.
k = input("Please enter a number: ")        # string
m = input("Please enter another number: ")  # string
n = k + m          # string plus string makes string
print(f"k: {type(k)} {k}")
print(f"m: {type(m)} {m}")
print(f"n: {type(n)} {n}")
print()

# The int and float functions convert a string to a number.
p = int(input("Please enter a number: "))          # int
q = float(input("Please enter another number: "))  # float
r = p + q                     # int plus float makes float
print(f"p: {type(p)} {p}")
print(f"q: {type(q)} {q}")
print(f"r: {type(r)} {r}")




# When we write an arithmetic expression that contains more than one operator,
# the computer executes the operators according to their precedence, also known as the order of operations.
#This table shows the precedence for the arithmetic operators.
# arithmetic operators including power (**), negation (-), multiplication (*), division (/),
# floor division (//), modulo (%), addition (+), and subtraction (-).



# Example 3

# Given the distance that a cable will span and the distance
# it will sag or dip in the middle, this program computes the
# length of the cable.

# Get user input and convert it from
# strings to floating point numbers.
span = float(input("Distance the cable must span in meters: "))
dip = float(input("Distance the cable will sag in meters: "))

# Use the numbers to compute the cable length.
length = span + (8 * dip**2) / (3 * span)

# Print the cable length in the
# console window for the user to see.
print(f"Length of cable in meters: {length:.2f}")



# The Python programming language includes many augmented assignment operators, also known as shorthand operators.
# All the shorthand operators have the same precedence as the assignment operator (=).
# Here is a list of some of the Python shorthand operators:
# **=  *=  /=  //=  %=  +=  -=



# Example 4

# Compute the total price of a pizza.

# The base price of a large pizza is $10.95
price = 10.95

# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))

# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping

# Add the cost of the toppings to the price of the pizza.
price = price + toppings_cost

# Print the price for the user to see.
print(f"Price: ${price:.2f}")


# Example 5

# Compute the total price of a pizza.

# The base price of a large pizza is $10.95
price = 10.95

# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))

# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping

# Add the cost of the toppings to the price of the pizza.
price += toppings_cost

# Print the price for the user to see.
print(f"Price: ${price:.2f}")


# In Python, we use if statements to cause the computer to make decisions;
# if statements are also called selection statements because the computer selects one group of statements
# to execute and skips the other group of statements.


# Example 6

# Get an account balance as a number from the user.
balance = float(input("Enter the account balance: "))

# If the balance is greater than 500, then
# compute and add interest to the balance.
if balance > 500:
    interest = balance * 0.03
    balance += interest

# Print the balance.
print(f"balance: {balance:.2f}")


# If you have written programs in other programming languages such as JavaScript, Java,
# or C++, you always used curly braces to mark the start and end of the body of an if statement.
# However, notice in example 6 that if statements in Python do not use curly braces.
# Instead, we type a colon (:) after the comparison of the if statement as shown on line 8.
# Then we indent all the statements that are in the body of the if statement as shown on lines 9 and 10.
# The body of the if statement ends with the first line of code that is not indented, like line 13.



# Example 7

# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))

# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount

# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")




# Python includes two logic operators which are the keywords and, or that we can use to combine two comparisons.
# Python also includes the logical not operator. Notice in Python that the logical operators are literally the words:
# and, or, not and not symbols as in other programming languages:

driver = 43
passenger = 28

if driver >= 54 or (driver >= 32 and passenger >= 54):
    message = "Enjoy the ride!"
