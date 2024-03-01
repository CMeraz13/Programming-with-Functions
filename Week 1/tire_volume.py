"""
Problem Statement:

The size of a car tire in the United States is represented with three numbers like this: 205/60R15.
The first number is the width of the tire in millimeters. The second number is the aspect ratio.
The third number is the diameter in inches of the wheel that the tire fits.
The volume of space inside a tire can be approximated with this formula:

v = (pi * w^2 * a (w * a + 2,540 * d)) / 10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Assignment: 

Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire
and computes and outputs the volume of space inside that tire.
"""
# Imported Math to be used later on in the code.
import math
print()
print()

# Getting the inputs (width, aspect ratio and diameter) from user
tire_width_in_mm = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = float(input("Enter the aspect ration of the tire (ex 60): "))
tire_diameter_in_inches = float(input("Enter the diameter of the wheel in inches (ex 15): "))
print()
print()

# Computing the algorthim before displaying it to the user
tire_volume = (math.pi * tire_width_in_mm**2 * tire_aspect_ratio * (tire_width_in_mm * tire_aspect_ratio + 2540 * tire_diameter_in_inches)) / 10000000000


# Displaying the results to the user.
print(f"The approximate volume is: {tire_volume:.2f} liters")


"""
Assignment
The prove milestone required you to write a program named tire_volume.py that
computes the approximate volume of air inside a tire. Add code near the end of that program that does the following:

Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:

1) current date
2) width of the tire
3) aspect ratio of the tire
4) diameter of the wheel
5) volume of the tire

"""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print only the date
# part of the current date and time.
print(f"{current_date_and_time:%Y-%m-%d}")

print()
print()


# Creating a shortcut for the file path.
file_path = "../Programming-with-Functions/Week 1/volumes.txt"


# Running a while statement to ensure the sure answers the question properly.
while True:
    # Asking the user if they would like to purchases tires.
    buy_tires_questions = input("Would you like to purchases tires with the dimentions you entered? Y/N: ")
    print()
    print()
    # Running an if statement to have the option of storing their number or not, and if they didnt asnwer the question.
    if buy_tires_questions.upper() == "Y":
        users_phone_number = input("Please enter your phone number: ")
        with open(file_path, "at") as volume_txt:
            volume_txt.writelines(f"\n{current_date_and_time:%Y-%m-%d}, {tire_width_in_mm:.0f}, {tire_aspect_ratio:.0f}, {tire_diameter_in_inches:.0f}, {tire_volume:.2f}, Phone Number: {users_phone_number}") 
        break
    elif buy_tires_questions.upper() == "N":
        print("")
        with open(file_path, "at") as volume_txt:
            volume_txt.writelines(f"\n{current_date_and_time:%Y-%m-%d}, {tire_width_in_mm:.0f}, {tire_aspect_ratio:.0f}, {tire_diameter_in_inches:.0f}, {tire_volume:.2f}") 
        break
    else:
        print("Please Enter Y or N for your answer.")
        pass

print()
print()
print()