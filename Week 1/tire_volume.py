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

import math

print()
print()
tire_width_in_mm = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = float(input("Enter the aspect ration of the tire (ex 60): "))
tire_diameter_in_inches = float(input("Enter the diameter of the wheel in inches (ex 15): "))
print()
print()

tire_volume = (math.pi * tire_width_in_mm**2 * tire_aspect_ratio * (tire_width_in_mm * tire_aspect_ratio + 2540 * tire_diameter_in_inches)) / 10000000000

print(f"The approximate volume is: {tire_volume:.2f} liters")