from datetime import datetime

# Print time stamps to see how long sections
# take to run

# Example 1:

"""
first_name = "Cesar"
print("Task Completed")
print(datetime.now())
print()

for x in range (0,10):
    print(x)
print("Task Completed")
print(datetime.now())
print()


def print_time():
    print("Task Completed")
    print(datetime.now())
    print()

first_name = "Cesar"
print_time()

for x in range (0,10):
    print(x)
print_time

"""

# Example 2:
"""
first_name = input("Enter Your first name: ")
first_name_initial = first_name[0:1]
last_name = input("Enter your last name: ")
last_name_initial = last_name[0:1]

print("Your initials are: " + first_name_initial + last_name_initial)
"""

def get_initial(name):
    initial = name[0:1] # IF initals are wanted in upper case then add .upper() to the end of the brackets.
    return initial

first_name = input("Enter Your first name: ")
first_name_initial = get_initial(first_name)
last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial + last_name_initial)


# How to write user-defined functions.

"""
def function_name(param1, param2, … paramN):
    documentation string
    statement1
    statement2
        ⋮
    statementN
    return value

he first line of a function is called the header or signature, and it includes the following:

the keyword def (which is an abbreviation for "define")
the function name
the parameter list (with the parameters separated by commas)

Here is the header for a function named draw_circle that takes three parameters named x, y, and radius:
def draw_circle(x, y, radius):

You could read the previous line of code as,
“Define a function named draw_circle that takes three parameters named x, y, and radius.”

The function name must start with a letter or the underscore ( _ ). The rest of the name must be made of letters, digits (0–9),
or the underscore. A function name cannot include spaces or other punctuation. 
A function name should be meaningful and should describe briefly what the function does.
Well-named functions often start with a verb.

The statements inside a function are called the body of the function. Just like other block statements in Python,
such as if, else, while, and for, all of which end with a colon (:), you must indent the statements inside the body of a function.
The body of a function should begin with a documentation string which is a triple quoted string that describes the function’s
purpose, parameters and return value. The body of a function may contain as many statements as you wish to write inside of it.
However, it is a good idea to limit functions to less than 20 lines of code.


Example 1 contains a function named print_cylinder_volume() with no parameters that gets two numbers from the user:
radius and height and uses those numbers to compute the volume of a right circular cylinder and then prints the volume
for the user to see.
"""

# Example 1

import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume():
    """Compute and print the volume of a cylinder.
    Parameters: none
    Return: nothing
    """
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

"""
Because the print_cylinder_volume function in example 1 doesn’t accept parameters,
it must be called without any arguments like this:

print_cylinder_volume()


Because the print_cylinder_volume function in example 1 gets input from a user and prints its results to a terminal window,
it can be used only in a program that runs when a user is present.
It cannot be used in a program that runs automatically and gets input from a file or the network or a sensor.
In other words, the print_cylinder_volume function in example 1 is not reusable in other programs.
The most reusable functions are ones that take parameters, perform calculations, and return a result
but do not perform user input and output.

The parameter list in a function’s header contains data stored in variables that the function needs to complete its task.
A parameter is a variable whose value comes from outside the function.
One way to get input into a function is to ask the user for input by calling the built-in Python input function.
Another way to get input into a function is through the function’s parameters.
Getting input through parameters is much more flexible than asking the user for input because the input through parameters
can come from the user or a file on a hard drive or the network or a sensor or even another function.

Example 2 contains another version of the print_cylinder_volume function.
This second version doesn’t get the radius and height from the user.
Instead, it gets input through its two parameters named radius and height.
"""
# Example 2

import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: nothing
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(volume)

"""
Because the second version of the print_cylinder_volume function accepts two parameters,
it must be called with two arguments like this:

print_cylinder_volume(2.5, 4.1)

To return a result from a function, simply type the keyword return followed by whatever result you want returned
to the calling function. Example 3 contains a third version of the cylinder volume function.
Notice that the version in example 3 returns the volume instead of printing it, which makes the function more reusable.
Notice also in example 3 that we changed the name of the function from print_cylinder_volume to compute_cylinder_volume
because this version doesn’t print the volume but instead returns it.

"""

# Example 3

import math

# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
    """Compute and return the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    return volume

"""
Many functions that you’ve used in the past such as input, float, and round, return a result.
When a function returns a result, we usually write code to store that returned result in a
variable to use later in the program like this:

text = input("Please enter your name: ")

Because the compute_cylinder_volume function in example 3 accepts two parameters and returns a result,
it could be called like this:

volume = compute_cylinder_volume(2.5, 4.1)


The main User-Defined Function: 
In all previous Python programs that you wrote in CSE 110 and 111,
you wrote statements that were not in a function like the simple program in example 4.

"""

# Example 4

import math

# Get the radius and height from the user.
radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of a cylinder: "))

# Compute the volume of the cylinder.
volume = math.pi * radius**2 * height

# Print the volume of the cylinder.
print(f"Volume: {volume:.2f}")


"""
In a large program, writing statements outside a function can lead to poor organization.
Professional software developers write statements inside a function whenever possible.
Beginning with this lesson, you will do the following in each program:

1) Write nearly all statements inside a user-defined function.
2) Write a user-defined function named main, which contains the beginning statements of your program.
3) Write one or more user-defined functions that have parameteters, perform calculations and other useful work,
and return a result to the call point.
4) Write a call to the main function at the bottom of your program.

Example 5 contains the same Python program as example 4
except most of the statements are inside a user-defined function named main.
"""

# Example 5

import math

# Define a function named main.
def main():
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

# Start this program by
# calling the main function.

"""
Notice the call to the main function in example 5 at line 19.
Without that call to the main function, when we run the program, the program will do nothing.
In all of your future programs in CSE 111 you will write a user-defined function
named main and will write a call to main at the bottom of the program.

If you look closely at the code in examples 1 and 5, you will realize that both programs have the same problem,
namely both the print_cylinder_volume function in example 1 and the main function in example 5 are not reusable because
both of them get input from a user and print to a terminal window. A better way to write the program in examples 1 and 5
is to separate the program into two functions, one named main and one named compute_cylinder_volume as shown in example 6.

Example 6 contains a complete program with two functions, the first named main at line 6 and the second named
compute_cylinder_volume at line 20. At line 13, the main function calls the compute_cylinder_volume function.
Notice that the compute_cylinder_volume function gets its input through parameters and returns a result which
makes this function reusable in other programs, including programs that run automatically without a user.

"""

# Example 6

import math

# Define the main function.
def main():
    # Get a radius and a height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Call the compute_cylinder_volume function and store
    # its return value in a variable to use later.
    volume = compute_cylinder_volume(radius, height)

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")


# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    # The returned result will be available wherever
    # this function was called.
    return volume


# Start this program by
# calling the main function.
main()

"""
The most reusable functions are ones that have parameters, perform calculations, and return a result but
do not perform user input and output. In the previous code example, there are two functions named
main and compute_cylinder_volume. The main function is certainly useful in the program, but it is not reusable in other
programs because it gets user input and prints the result for the user to see. The compute_cylinder_volume function is
very reusable in another program because it doesn’t get user input or print output.
Instead, it takes two parameters, performs a calculation, and returns a result to the calling function.
The compute_cylinder_volume function is so reusable that it could be included in a library of functions
that compute the area and volume of 2-D and 3-D geometric shapes.

View "What Happens When the Computer Calls a Function?" Image for next part:

What Happens When the Computer Calls a Function?

Some students have trouble visualizing what happens when the computer calls (executes) a function.
The following diagram contains the same program as example 6.
The circled numbers show the order in which the events happen in the computer.
The green numbers and arrows in the diagram show the order in which the computer executes statements in the program.
The blue numbers and arrows show how data flows from arguments into parameters and from a returned result to a variable.

A computer will execute the statements in the previous diagram in the following order:

A) The statement at (1) is not inside a function, so the computer executes it when the program begins.
The statement at (1) is a call to the main function which causes the computer to begin executing
the statements inside main at (2).

B) At (2), the computer gets two numbers from the user.

C) The statement at (3) is a call to the compute_cylinder_volume function which causes the computer
to copy the values in the arguments r and h into the parameters radius and height respectively and
then begin executing the statements inside the compute_cylinder_volume function at (5).

D) At (5), the computer computes the volume of a cylinder.

E) The statement at (6) is a return statement which causes the computer to stop executing the compute_cylinder_volume function,
to return the computed volume to the call point at (3), and to resume executing statements at the call point.

F) At the call point (3), the computer stores the returned value in the variable named v.

G) At (8), the computer prints the value that is in the volume variable for the user to see.
This is the last statement in the main function, so after executing it,
the computer resumes executing the statements after the call point (1) to main.

H) At (9), there are no more statements after the call to main, so the computer terminates the program.

"""
# Call Graphs

"""
A call graph is a diagram that shows function calls and returns within a program.
A call graph can help you visualize how a program is divided into functions.
Within a call graph, the unfilled circle shows where the computer begins executing a program.
A rounded rectangle represents a function. A solid arrow represents a call from one function to another function.
A dashed arrow represents a value returned from a called function to the calling function.

See "Call Graphs Key" Image for reference.

The call graph below shows the function calls and returns for the program in example 6.
From the call graph, we see that the computer begins executing the program by calling the main function.
While executing the main function, the computer calls the input and float functions.
Then the computer calls the compute_cylinder_volume function. Finally the computer calls the print function.
In the call graph we can see that the main and print functions don’t return a value.
The print function prints results for the user to see, but it doesn’t return anything.

See "Call Graph Prepare" Image for reference.

"""

# Summery

"""
Summary
A function is a group of statements that together perform one task.
A user-defined function is a function written by a programmer like you.
To write a user-defined function, write code that follows this template:


def function_name(param1, param2, … paramN):
    documentation string
    statement1
    statement2
        ⋮
    statementN
    return value
To call a user-defined function, write code that follows this template:


variable_name = function_name(arg1, arg2, … argN)
The most reusable functions are ones that take parameters, perform calculations, and return a result but
do not perform user input and output.
All of your future programs in CSE 111 will have a user-defined function named main and
will have a call to main at the bottom of the program.
"""