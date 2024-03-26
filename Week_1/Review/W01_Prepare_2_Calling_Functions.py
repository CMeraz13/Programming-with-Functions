"""
Python includes many built-in functions such as: input, int, float, str, len, range, abs, round, list, dict, open, and print.
These are called built-in functions because you don’t have to import any module to use them.
They are simply a built-in part of the Python language. 

A programmer uses a function by calling it (also known as invoking it).
To call (or invoke) a function means to write code that causes the computer to execute the code that is inside that function.
Regardless of the type of function (built-in, standard, third-party, or user-defined),
a function is called by writing its name followed by a set of parentheses ( ).

"""

# During CSE 110 and 111, you often wrote code that called the built-in input and print functions like this:
name = input("Please enter your name: ")
print(f"Hello {name}")

"""
To call a function you must know the following three things:

The name of the function
The parameters that the function accepts
What the function does

"""

# These three pieces of information are normally available in online documentation.
# For example, from the online Python reference for the input function, we read this:
# input(prompt)

"""
The name of the function is input.
The function accepts one parameter named prompt.
The function writes the prompt to a terminal window and then reads user input from the terminal and 
returns that input to the calling function.


A parameter is a piece of data that a function needs in order to complete its task.
In the online reference for the input function, we see that the input function has one parameter named prompt.

An argument is the value that is passed through a parameter into a function.
In other words, parameters are listed in a function’s documentation, and arguments are listed in a call to a function.

Type a new variable name and use the assignment operator (=) to assign a value to the variable.
Type the name of the function followed by a set of parentheses.
Between the parentheses, type arguments that the computer will pass into the function through its parameters.

For example, the following code calls the built-in input function and passes the string
"Please enter your name: " as the argument for the prompt parameter.

"""

name = input("Please enter your name: ")

"""
When a function has more than one parameter and a programmer writes code to call that function,
the programmer nearly always writes the arguments in the same order as the parameters.
Consider the description of the built-in round function:

"""
# round(number, ndigits)

"""
Return number rounded to ndigits precision after the decimal point.
If ndigits is omitted or is None, round returns the nearest integer to number.

Now consider this Python code that gets a number from a user, rounds that number to two digits after the decimal,
and then prints the rounded number.

"""

n = float(input("Please enter a number: "))
r = round(n, 2)
print(r)

"""
The code on line 1 causes the computer to call the built-in input function and then call the built-in float function.
Line 2 causes the computer to call the built-in round function and pass two arguments.
Notice that the order of the arguments matches the order of the parameters. Specifically,
the number to be rounded (n) is the first argument, and the number of digits after the decimal point (2) is the second argument.
Line 3 causes the computer to call the built-in print function to print the rounded number.

From the description, we read that the second argument is optional.
If the programmer doesn’t type a second argument, the value in the number parameter will be rounded to an integer.

"""
n = float(input("Please enter a number: "))
r = round(n)
print(r)

"""
For some optional arguments, we must pass a named argument,
which is an argument that is preceded by the name of its matching parameter.
For example, here is an excerpt from the documentation for the print function:
"""
"""
# print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)
# Print objects to the text stream file, separated by sep and followed by end.
# sep, end, file and flush, if present, must be given as named arguments.

Notice from the excerpt that the print function can take many objects that will be printed.
Optionally, it can take parameters named sep, end, file, and flush that must be named when they are used.
For example, this code calls the print function to print three words all separated by a vertical bar (|).
Notice the named arguments sep and flush.

"""
x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=True)


"""
A Python module is a collection of related functions.
The Python standard library includes many modules which have more functions, such as the math module—which includes the floor,
ceil, and sqrt functions and the random module—which includes the randint, choice, and shuffle functions.
Consider the description of the sqrt function that is in the standard math module:
"""

# math.sqrt(x)
# Return the square root of x.

"""
The name of the containing module is math.
The name of the function is sqrt.
The function accepts one parameter named x.
The function computes and returns the square root of the number that is in x.


To use any code that is in a module, you must import the module into your program and
precede the function name with the module name. For example,
if you wish to call the math.sqrt function, you must first import the math module and then type math.
in front of sqrt like this:

"""
import math

r = math.sqrt(71)
print(r)

"""
In the above example, 71 is the argument that will be passed through the parameter x into the math.sqrt function.
The math.sqrt function will compute the square root of 71 and
return the computed value that will then be stored in the variable r.
"""
#------------------------------------------------------------------------------------------------------------------------

"""
Python is an object-oriented language and includes many classes and objects.
A method is a function that belongs to a class or object.
Even though classes and objects are not part of this course (CSE 111),
calling a method in Python is so common and so easy that you should know how to do it.
A method is a kind of function, so calling a method is similar to calling a function.
The difference is that to call a method we must type the name of the object and a period (.) in front of the method name.

Consider the program in example 6 that gets a string of text from a user and prints the number of
characters in the string and prints the string in all upper case characters.

"""

# Example 6

# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get
# the number of characters in the text.
length = len(text1)

# Call the string upper method to convert
# the quote to upper case characters.
text2 = text1.upper()

# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
print(length, text2)

"""
To call the len function, we type the name of the function followed by a list of arguments inside parentheses.
To call the upper method, we type the name of the object (text1) and a period, then the method name (upper),
and then a list of arguments inside parentheses.

However, in example 6 at line 12, there are no arguments passed to the upper method, so the parentheses are empty.
In order for the computer to call the upper method, a programmer must type the empty parentheses. In other words,
if you write a line of code to call the upper method but don’t type the empty parentheses, like this:
"""
text2 = text1.upper  # Does NOT call the upper method

"""
the computer will not call the upper method.
Instead the computer will assign a reference to the upper method to the text2 variable.
You don’t want the computer to do this because assigning a function reference won’t make
sense to you until you study functional programming.

All the previous examples in this preparation content use the assignment operator (=)
to store the value returned from a function in a variable. For example:
"""

text = input("Enter a motivational quote: ")



# Example 7

import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and
# immediately print its return value.
print( math.sqrt(number) )

# Call the math.sqrt function again and
# use its return value in an if statement.
if math.sqrt(number) < 100:
    print(f"The square root is less than 100.")
elif math.sqrt(number) > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")

"""
Notice in example 7, there are three statements that call the math.sqrt function, one at line 10 to print the square root,
another at line 14 to check if the square root is less than 100, and yet another at line 16 to check if the square root is
greater than 100. Every time the computer calls a function, the computer will execute the code that is inside that function.
In example 7, because the argument is the same at lines 10, 14 and 16, the returned result will be the same in all three cases.
So it would be faster to save the result in a variable and reuse the variable instead, as shown in example 8 at lines
10, 12, 14, and 16.
"""

# Example 8

import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and store its
# return value in a variable to use later.
root = math.sqrt(number)

print(f"The square root is {root:.2f}")

if root < 100:
    print(f"The square root is less than 100.")
elif root > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")


# To call a built-in function, write code that follows this template:
# variable_name = function_name(arg1, arg2, … argN)

# To call a function from a module, import the module and write code that follows this template:
# import module_name
# variable_name = module_name.function_name(arg1, arg2, … argN)
    
# To call a method, write code that follows this template:
# variable_name = object_name.method_name(arg1, arg2, … argN)