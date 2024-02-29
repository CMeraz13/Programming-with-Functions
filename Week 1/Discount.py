"""
Problem Statement:
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days.
On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

Assignment:
Work as a team to write a Python program named discount.py that gets a customer’s subtotal as
input and gets the current day of the week from your computer’s operating system.
Your program must not ask the user to enter the day of the week.
Instead, it must get the day of the week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal.
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal.
Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

Core Requirements: 
1) Your program asks the user for the subtotal but does not ask the user for the day of the week. 
Your program gets the day of the week from your computer’s operating system.
2) Your program correctly computes and prints the discount amount if applicable.
3) Your program correctly computes and prints the sales tax amount and the total amount due.
"""
"""
# Importing datetime to be used in code.
from datetime import datetime

# Calling forth
todays_date = datetime.now(tz=None)
datetime.isoweekday()
print(todays_date)
"""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
day_of_week = 1
# Print the day of the week for the user to see.
print(day_of_week)

discount_amount = 0.10
sales_tax_amount = 0.06

subtotal = float(input("Please enter the subtotal: "))
# print(sales_tax)

if (day_of_week == 1 or day_of_week == 2):
    discount = round(subtotal * discount_amount, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

sales_tax = round(subtotal * sales_tax_amount,2)
print(f"Sales Tax amount: {sales_tax:.02f}")

total = subtotal + sales_tax

print(f"Total: {total:.02f}")