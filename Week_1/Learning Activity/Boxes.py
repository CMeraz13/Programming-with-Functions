
"""
Problem Statement
In our modern world economy, many items are manufactured in large factories,
then packed in boxes and shipped to distribution centers and retail stores.
A common question for employees who pack items is “How many boxes do we need?”


Assignment
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping.
Write a Python program named boxes.py that asks the user for two integers:

1. The number of manufactured items
2. The number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number.
Note that the last box may be packed with fewer items than the other boxes.
"""

# Importing Math.
import math

print ()

# Getting the user's imput for the number of items and items per box.
number_of_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Calculating how many boxes the user will need.
boxes_needed = math.ceil(number_of_items / items_per_box)
print()

# Printing out the results for the user.
print(f"For {number_of_items}, packing {items_per_box} items in each box, you will need {boxes_needed} boxes.")
print()