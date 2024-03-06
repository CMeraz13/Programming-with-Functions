
"""
Purpose:

Strengthen your understanding of user-defined functions, parameters, arguments, 
and local variable scope by writing a program that has three or more functions.

Problem Statement:

In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. 
There are many different sizes of steel cans. 
The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can. 
Some sizes of cans require a lot of steel to store a small amount of food. 
Other sizes of cans require less steel and store more food. 
A can size with a large storage efficiency is considered more friendly to the environment than a can size with
a small storage efficiency.

The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.

storage_efficiency =
volume
surface_area

In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. 
The formulas for the volume and surface area of a cylinder are:

volume = π*radius**2 height
surface_area = 2π*radius*(radius + height)
- π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
- radius is the radius of the cylinder
- height is the height of the cylinder

Assignment:

Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each 
of the following 12 steel can sizes. 
Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”

If you separate your program into functions, 
this problem will be much easier to solve than if you don’t separate it into functions. 
You are free to write any functions that you choose in your program, 
but we strongly suggest that your program include at least these three functions:

- main
- compute_volume
- compute_surface_area

"""

import math

def main():
    name = "#1 Picnic"
    radius_cm = 6.83
    height_cm = 10.16
    cost_us_dollar = 0.28
    volume = compute_volume(radius_cm, height_cm)
    surface_area = compute_surface_area(radius_cm, height_cm)
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#1 Tall"
    radius_cm = 6.83
    height_cm = 7.78
    cost_us_dollar = 0.43
    volume = compute_volume(radius_cm, height_cm)
    surface_area = compute_surface_area(radius_cm, height_cm)
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#2"
    radius_cm = 8.73
    height_cm = 11.59
    cost_us_dollar = 0.45
    volume = compute_volume(radius_cm, height_cm)
    surface_area = compute_surface_area(radius_cm, height_cm)
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#2.5"
    radius_cm = 10.32
    height_cm = 11.91
    cost_us_dollar = 0.61
    volume = compute_volume(radius_cm, height_cm)
    surface_area = compute_surface_area(radius_cm, height_cm)
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#3 Cylinder"
    radius_cm = 10.79
    height_cm = 17.78
    cost_us_dollar = 0.86
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#5"
    radius_cm = 13.02
    height_cm = 14.29
    cost_us_dollar = 0.83
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "6Z"
    radius_cm = 5.40
    height_cm = 8.89
    cost_us_dollar = 0.22
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "8Z short"
    radius_cm = 6.83
    height_cm = 7.62
    cost_us_dollar = 0.26
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#10"
    radius_cm = 15.72
    height_cm = 17.78
    cost_us_dollar = 1.53
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#211"
    radius_cm = 6.83
    height_cm = 12.38
    cost_us_dollar = 0.34
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#300"
    radius_cm = 7.62
    height_cm = 11.27
    cost_us_dollar = 0.38
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#303"
    radius_cm = 8.10
    height_cm = 11.11
    cost_us_dollar = 0.42
    volume = compute_volume(radius_cm, height_cm)
    surface_area = volume / surface_area
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")
    

    pass


def compute_volume(radius_cm, height_cm):
    volume = math.pi * radius_cm **2 * height_cm
    return volume


def compute_surface_area(radius_cm, height_cm):
    surface_area =  2 * math.pi * radius_cm * (radius_cm + height_cm)
    return surface_area

main()