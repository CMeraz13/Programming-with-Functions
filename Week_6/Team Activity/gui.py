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
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle:")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_radius = Label(frm_main, text="Radius:")

    # Create an integer entry box where the user will enter her age.
    ent_radius = IntEntry(frm_main, width=4, lower_bound=12, upper_bound=90)

    # Create a label that displays "years"
    #lbl_age_units = Label(frm_main, text="years")

    # Create a label that displays "Area:"
    lbl_rates = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_radius = Label(frm_main, width=3)
    lbl_fast = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="(pi x r^2)")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    ent_radius.grid(      row=0, column=1, padx=3, pady=3)
   # lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_rates.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_radius.grid(      row=1, column=1, padx=3, pady=3)
    lbl_fast.grid(      row=1, column=2, padx=3, pady=3)
    lbl_rate_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            Radius = ent_radius.get()

            # Compute the user's maximum heart rate.
            #max_rate = 220 - age

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            #slow = max_rate * 0.65
            #fast = max_rate * 0.85
            
            area = (math.pi * (Radius**2))

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            #lbl_slow.config(text=f"{slow:.0f}")
            #lbl_fast.config(text=f"{fast:.0f}")

            

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_radius.config(text="")
            lbl_fast.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_age.clear()
        lbl_radius.config(text="")
        lbl_fast.config(text="")
        ent_age.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_age.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_age.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
