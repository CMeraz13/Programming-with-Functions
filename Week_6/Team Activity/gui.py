"""
Problem Statement:

    Almost all of the programs that you wrote for this course receive input from and print results to a terminal window. 
    However, most users prefer to interact with a program through a graphical user interface (GUI) 
    that contains icons, text fields, drop-down lists, buttons, etc. Within a GUI, the individual components 
    (icons, text fields, etc.) are called widgets. 
    Most libraries for creating GUIs use object oriented programming because 
    each widget is an object with attributes and methods.

Assignment:

    As a team, write a Python program named gui.py that gets user input from a GUI, 
    performs a simple calculation, and displays the result in a GUI.

Steps:

    Do the following:

        1) Download these two Python files: heart_rate.py and number_entry.py and 
            save them in the same folder where you will save your Python program.
        2) Open the heart_rate.py file in VS Code and run it. 
            Notice how running the program opens a GUI where a user can enter his age and 
            see heart rates for exercising. Experiment with the GUI by entering different ages, 
            seeing the results, and selecting the Clear button.
        3) Read the comments and examine the code in the heart_rate.py program. Notice the following:
            A) To create its GUI, the heart_rate program uses the tkinter module which is imported at line 3.
            B) The main function begins at line 7.
            C) The main function creates a tk.TK root object and uses that object to create the main window for the program.
            D) Beginning at line 49, the populate_main_window function creates labels, text entry boxes, 
                and buttons and places them in a grid.
            E) Inside the populate_main_window function, there are two nested functions named calculate and clear. 
                The calculate function is called each time the user enters a digit in the age text field. 
                The clear function is called each time the user selects the Clear button.
        4) Choose a simple calculation or formula for your program to calculate. You could choose one of these:
            A) Area of a circle:
                a = π r2
            B) Swing time of a pendulum:
                t = 2π
                √
                n
                9.81
            C) Area of a rectangle:
                a = wh
            D) Volume of a tire:
                v =
                π w2 aw a + 2,540 d
                10,000,000,000
        5) Use the heart_rate.py program as a reference (you could even copy and paste parts of it or all of it) 
            and write a Python program with a GUI that calculates the formula that you chose.

    Core Requirements: 

        1) Your program must include a GUI that opens when you run your program.
        2) The GUI must allow a user to enter input.
        3) When the user enters valid input, your program must compute correct results and display those results in the GUI.

        Stretch Challenges:

            If your team finishes the core requirements in less than an hour, complete one or more of these 
            stretch challenges. Note that the stretch challenges are optional.

                1) Add a Clear button to your GUI that clears all inputs and outputs when the user selects it.
                2) Add a label that acts as a status bar at the bottom of your GUI. Your program should display an 
                    error message in the status bar when the user enters invalid input. 
                    Your program should clear the status bar when the user enters valid input.

        Testing Procedure:

            Run your program and enter various inputs, including invalid values. 
            Verify that your program doesn’t crash, behaves as expected, and displays correct results.


"""

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


