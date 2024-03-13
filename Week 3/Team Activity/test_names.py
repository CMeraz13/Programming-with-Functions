"""
Purpose: 

Writing and running test functions often help a software developer find mistakes in code. 
During this assignment, you will write three test functions. 
Then use pytest to run the test functions and use the output of pytest to help you find and 
fix errors in some program functions.

Problem Statement:

Most people around the world today have at least two names, a family name and a given name. 
In the United States, we usually write a person’s given name followed by his family name. 
However, when a computer lists names in alphabetical order, it is convenient to list the family name first and 
then the given name like this:

* Toussaint; Marie
* Toussaint; Olivier
* Washington; George
* Washington; Martha

When writing a program that alphabetizes names, it is often helpful to have the following three functions.

make_full_name
    Combines a person’s given name and family name into one string with the family name first
extract_family_name
    Extracts a person’s family name from his full name
extract_given_name
    Extracts a person’s given name from his full name

A programmer has already written those three functions. However, 
there are mistakes in at least two of the three functions.

Assignment: 

As a team, write three test functions named test_make_full_name, test_extract_family_name, and test_extract_given_name. 
Each of the test functions will test one of three previously written program functions. 
Use pytest to run the test functions and find and fix the mistakes, if any, that are in program functions.



Steps:

Do the following:

1) Download the names.py Python file and save it in the same folder where you will save your Python test program. 
Then open the downloaded file in VS Code. 
Notice that the downloaded file contains three small functions named: make_full_name, extract_family_name, 
and extract_given_name. Notice also that each function has a documentation string 
(a triple quoted string immediately below the function header) that describes what the function does. 
Read the documentation strings for all three functions. The code in the functions may contain some mistakes.

2) Using VS Code, open a new Python file and copy and paste the following import statements at the top of the file.
from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

Save the file with the name test_names.py in the same folder where you downloaded and saved the names.py file.

3) In test_names.py, write a function named test_make_full_name that takes no parameters. 
Write assert statements inside this function to test the value returned from the make_full_name function. 
If you are not sure what the make_full_name function does or how to test it, read the documentation string 
that is at the top of the make_full_name function in the names.py file.

4) In test_names.py write a function named test_extract_family_name that takes no parameters. 
Write assert statements inside this function to test the value returned from the extract_family_name function.

5) In test_names.py write a function named test_extract_given_name that takes no parameters. 
Write assert statements inside this function to test the value returned from the extract_given_name function.

6) At the bottom of your test_names.py file, write a call to the pytest.main function like this:

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

7) Save your test_names.py file and run it by clicking the green run icon in VS Code.

8) Read the output from pytest and use the output to help you find and fix any errors that are in your test functions 
or the make_full_name, extract_family_name, and extract_given_name functions.

9) Repeat steps 7 and 8 until you have found and fixed all the mistakes and your three test functions pass.

Core Requirements:

1) Write test_make_full_name so that it tests make_full_name with various names, including long names, short names, 
and hyphenated names. Fix the mistake in the make_full_name function.

2) Write test_extract_family_name so that it tests extract_family_name with various names, including long names, 
short names, and hyphenated names.

3) Write test_extract_given_name so that it tests extract_given_name with various names, including long names, 
short names, and hyphenated names. Fix the mistake in the extract_given_name function.

"""

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Cesar", "Meraz") == "Meraz; Cesar"
    return

def extract_family_name():
    assert extract_family_name("Meraz; Cesar") == "Meraz"
    return

def test_extract_given_name ():
    assert extract_family_name("Meraz; Cesar") == "Cesar"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])