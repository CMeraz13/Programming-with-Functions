"""
Problem Statement:

A common task for many knowledge workers is to use a number, key, or ID to find information about a person. 
For example, a knowledge worker may use a phone number or e-mail address as 
a key to find (or look up) additional information about a customer. 
During this activity, your team will write a Python program that uses a student’s I-Number to look up the student’s name.

Assignment:

Download the students.csv file and save it in the same folder where you will save your Python program. 
Open the file in VS Code and examine it. 
Notice that the I-Numbers and names in the file are separated by a comma. 
Notice also that the I-Numbers are stored in the file without any dashes between the digits.

As a team, write a Python program named students.py that has at least two functions named main and read_dictionary. 
You must write the read_dictionary function with one of the following two headers and documentation strings. 
Choose the header that makes the most sense to you.

    def read_dictionary(filename):
        Read the contents of a CSV file into a
        dictionary and return the dictionary.
    
        Parameters
            filename: the name of the CSV file to read.
        Return: a dictionary that contains
            the contents of the CSV file.
        
    
    def read_dictionary(filename, key_column_index):
        Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
    
        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
        
    
Core Requirements:

Your program must do the following:

    1) Open the students.csv file for reading, skip the first line of text in the file because it 
        contains only headings, and read the other lines of the file into a dictionary. 
        The program must store each student I-Number as a key and each I-Number name pair 
        or each name as a value in the dictionary.
    2) Get an I-Number from the user, use the I-Number to find the corresponding 
        student name in the dictionary, and print the name.
    3) If a user enters an I-Number that doesn’t exist in the dictionary, 
        your program must print the message, "No such student" (without the quotes).

Stretch Challenges:

If your team finishes the core requirements in less than an hour, complete one or more of these stretch challenges. 
Note that the stretch challenges are optional.

1) Add code to remove dashes from the I-Number that the user enters. 
    This will allow the user to enter I-Numbers with dashes or without dashes and 
    still allow the computer to search in the dictionary.
2) When a user enters an I-Number, your program should ensure it is a valid I-Number.
    A) If there are too few digits in the I-Number, your program should print, 
        "Invalid I-Number: too few digits" (without the quotes).
    B) If there are too many digits in the I-Number, your program should print, 
        "Invalid I-Number: too many digits" (without the quotes).
    C) If the given I-Number contains any characters besides digits and dashes, 
        your program should output "Invalid I-Number" (without the quotes).
3) Add something or change something in your program that you think would make your program better, 
easier for the user, more elegant, or more fun. Be creative.


Testing Procedure:

Verify that your program works correctly by following each step in this testing procedure:

1) Download the test_students.py Python file and save it in the same folder where you saved your students.py program. 
Run the test_students.py file and ensure that the test_read_dictionary function passes. 
If it doesn't pass, there is a mistake in your read_dictionary function. Read the output from pytest, 
fix the mistake, and run the test_students.py file again until the test function passes.

    > python test_students.py
        =================== test session starts ====================
        platform win32--Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy
        rootdir: C:\Users\cse111\week05
        collected 1 item
    
        test_students.py::test_students PASSED                [100%]
    
        ==================== 1 passed in 0.12s =====================

2) Run your program and enter the inputs shown below. Ensure that your program’s output matches the output below.
    > python students.py
        Please enter an I-Number (xxxxxxxxx): 551234151
        No such student
    
        > python students.py
        Please enter an I-Number (xxxxxxxxx): 751766201
        James Smith

3) Run your program and enter this I-Number as input: 00-115-2306 (including the dashes). 
    Many users will want to enter I-Numbers with dashes. 
    How should your program handle the dashes?
4) Run your program and enter an I-Number with too few digits or too many digits. 
    How should your program handle these invalid I-Numbers?
    
"""