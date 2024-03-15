"""
Purpose:

Prove that you can write a Python program and write and 
run test functions to help you find and fix mistakes in your program.

Problem Statement: 

Getting clean water to all buildings in a city is a large and expensive task. 
Many cities will build an elevated water tank, and install a pump that pushes water 
up to the tank where the water is stored. 
In the city, when a thirsty person opens a water faucet, water runs from the tank through pipes to the faucet. 
Earth’s gravity pulling on the water in the elevated tank pressurizes the water and causes it to spray from the faucet.
Before a city builds a water distribution system, 
an engineer must design the system and ensure water will flow to all buildings in the city. 
An engineer must choose the tower height, pipe type, pipe diameter, and pipe path. 
Engineers use software to help them make these choices and design a working water distribtuion system.

Assignment:

Write a Python program that could help an engineer design a water distribution system.
During this prove milestone, you will write three program functions and 
three test functions as described in the Steps section below.

Steps:

Do the following:

1) Using VS Code, create a new file and save it as water_flow.py

2) Create another new file, save it as test_water_flow.py, and copy and paste the following import statements into the file.
    from pytest import approx
    import pytest

3) In your water_flow.py program, write a function named water_column_height that 
calculates and returns the height of a column of water from a tower height and a tank wall height. 
The function must have this header:
    def water_column_height(tower_height, tank_height):
In your function, use the following formula for calculating the water column height.

h = t + ((3w)/4)
where:
* h is height of the water column
* t is the height of the tower
* w is the height of the walls of the tank that is on top of the tower

4) In your test_water_flow.py file, write a test function named test_water_column_height. 
This test function must call water_column_height at least four times to verify that it is working correctly. 
Use the following numbers in your test function:

1) Tower Height: 0.0, 0.0, 25.0, 48.3
2) Tank Wall Height: 0.0, 10.0, 0.0, 12.8
3)Expected Column Height: 0.0, 7.5, 25.0, 57.9

5) In your water_flow.py program, write a function named pressure_gain_from_water_height that 
calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank. 
The function must have this header:
    def pressure_gain_from_water_height(height):
In your function, use the following formula for calculating pressure caused by Earth’s gravity:

P = (p * g * h)/1000

where:
* P is the pressure in kilopascals
* ρ is the density of water 998.2 ( kilogram / meter3) *Just use # in your calculations
* g is the acceleration from Earths gravity 9.80665 (meter / second2) *Just use # in your calculations
* h is the height of the water column in meters

6) In your test_water_flow.py file, write a test function named test_pressure_gain_from_water_height. 
This test function must call pressure_gain_from_water_height at least three times to verify that it is working correctly. 
Use the following numbers in your test function:

1) Height: 0.0, 30.2, 50.0
2) Expected Pressure: 0.000, 295.628, 489.450
3) approx Absolute Tolerance: 0.001, 0.001, 0.001

7) In your water_flow.py program, write a function named pressure_loss_from_pipe that calculates and 
returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through. 
The function must have this header:
    def pressure_loss_from_pipe(pipe_diameter,
            pipe_length, friction_factor, fluid_velocity):
In your function, use the following formula for calculating pressure loss from friction within a pipe:

P = (-f * L * p * v^2)/ (2000 * d)

where:
* P is the lost pressure in kilopascals
* f is the pipe’s friction factor
* L is the length of the pipe in meters
* ρ is the density of water 998.2 (kilogram / meter3) *Just use # in your calculations
* v is the velocity of the water flowing through the pipe in meters / second
* d is the diameter of the pipe in meters


8) In your test_water_flow.py file, write a test function named test_pressure_loss_from_pipe . 
This test function must call pressure_loss_from_pipe at least seven times to verify that it is working correctly. 
Use the following numbers in your test function.

1) Pipe Diameter: 0.048692, 0.048692, 0.048692, 0.048692, 0.048692, 0.286870, 0.286870
2) Pipe Length: 0.00, 200.00, 200.00, 200.00, 200.00, 1000.00, 1800.75
3) Friction Factor: 0.018, 0.00, 0.018, 0.018, 0.018, 0.013, 0.013
4) Fluid Velocity: 1.75, 1.75, 0.00, 1.75, 1.65, 1.65, 1.65
5) Expected Pressure Loss: 0.000, 0.000, 0.000, -113.008, -100.462, -61.576, -110.884
6) approx Absolute Tolerance: 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001

9) Copy and paste the following code at the bottom of your test_water_flow.py file.

"""


def water_column_height(tower_height, tank_height):
    # Used to define the hieght of the water column using tower height and tank height
    column_height_result = tower_height + ((3 * tank_height) / 4)

    return column_height_result

def pressure_gain_from_water_height(height):
    # Function used to define the pressure gain from the water height using height.

    # Constants for calculation
    density_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    
    # Calculate pressure using the provided formula
    pressure_gain_result = (density_water * gravity * height) / 1000

    # Returning the equation as pressure
    return pressure_gain_result


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # Function used to define the pressure lossed from a pipe using the pipes diameter and length
    # As well as a friction factor and fluid velocity

    # Constants for calculation
    density_water = 998.2  # kg/m^3
    pressure_loss_result = (-friction_factor * pipe_length * density_water * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure_loss_result



