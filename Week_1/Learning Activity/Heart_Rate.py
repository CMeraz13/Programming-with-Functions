
"""
Purpose:
# Write a Python program that gets input from a user, uses variables, performs arithmetic,
# and displays results for the user to see.

# Problem Statement:

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# Asking User for an imput of their age.
heart_rate = int(input("Please Enter Your Age: "))
print()

# Calculatijng the low heart rate and high heart rate to create a range
maximum_heart_rate = 220 - heart_rate
high_heart_rate = maximum_heart_rate * .85
low_heart_rate = maximum_heart_rate * .65

# Printing out the results for the user.
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {low_heart_rate:.0f} and {high_heart_rate:.0f} beats per minute.")
print()
print()
print()
