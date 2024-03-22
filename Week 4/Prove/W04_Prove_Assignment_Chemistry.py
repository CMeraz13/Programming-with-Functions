"""
Problem Statement:

In chemistry, a mole is a very large, fixed quantity, specifically 602,214,076,000,000,000,000,000 
(usually written as 6.02214076 × 1023). 
The molar mass of a substance is the mass in grams of one mole of the substance (grams / mole). 
A molar mass calculator is a program that computes the molar mass of a substance and the 
number of moles of a sample of that substance. To use a molar mass calculator, a chemist enters two inputs:

* The formula for a molecule, such as H2O (water) or C6H12O6 (glucose)
* The mass in grams of a sample of the substance, such as 3.71

The calculator computes the molar mass of the molecule by doing the following for each element in the formula:

1) Sum the number of atoms of each element in the formula
2) Find the atomic mass of each element
3) Multiply the number of atoms by their atomic mass
4) Add the product into the molar mass of the molecule

Then the calculator computes the number of moles in the sample with this formula:

number_of_moles = sample_mass / molar_mass

Finally, the calculator prints two results for the chemist to see:

* the molar mass
* the number of moles

Example:

As an example, consider a sample of glucose (C6H12O6) with a mass of 12.37 grams. 
To use a molar mass calculator, a chemist enters

* C6H12O6
* 12.37

The calculator computes the molar mass of glucose by doing the following:

1) Sum the number of atoms of each element in the formula for glucose:
    6 carbon atoms
    12 hydrogen atoms
    6 oxygen atoms

2) Find the atomic mass of each element:


Symbol	Name	Atomic Mass
C	Carbon	12.0107
H	Hydrogen	1.00794
O	Oxygen	15.9994

3) Multiply the number of atoms by their atomic mass:


6	×	12.0107	=	72.0642
12	×	1.00794	=	12.09528
6	×	15.9994	=	95.9964

4) Add the results of the multiplications to get the molar mass of glucose:
    72.0642 + 12.09528 + 95.9964 = 180.15588 grams/mole

Then the calculator divides the mass of the sample of glucose by the molar mass of glucose which results in the number of moles in the sample:

12.37 grams / 180.15588 grams/mole = 0.06866 moles


The calculator prints two results for the chemist to see:

* the molar mass of glucose: 180.15588 grams/mole
* the number of moles in the sample: 0.06866 moles


Assignment:

During this assignment, you will write and test the remaining parts of the molar mass calculator 
that you started writing in the previous lesson’s prove milestone. 
When you are finished with this prove assignment, your chemistry.py program must 
contain at least three functions named as follows:

1) main
2) make_periodic_table
3) compute_molar_mass



Steps:

Do the following:

1) Download the formula.py Python file and save it in the same folder where you saved your 
chemistry.py program from the previous prove milestone. 
The formula.py file includes a FormulaError class and a function named parse_formula. 
Both of them are complete and work correctly, and you should not change them.

2) Open the formula.py file in VS Code and read the triple quoted string at the top of the parse_formula function. 
As the triple quoted string states, the parse_formula function converts a chemical formula for a molecule, 
such as "C13H16N2O2" (melatonin), into a compound list, such as [["C", 13], ["H", 16], ["N", 2], ["O", 2]]. 
This compound list is known as a symbol_quantity_list because it contains the 
symbols of chemical elements and the quantity of atoms of each element that appear in a chemical formula.

3) Copy and paste the following import statement into your chemistry.py program at the top of your program. 
This statement will import the parse_formula function from the formula.py file into 
your chemistry.py program so that you can call the parse_formula function in your program.

from formula import parse_formula

4) In your chemistry.py program, change the compound list that is in your 
make_periodic_table function to a compound dictionary. 
Each item in the dictionary should have a chemical symbol as the key and 
the chemical name and atomic mass in a list as the value, like this:

 periodic_table_dict = {
        # symbol: [name, atomic_mass]
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
          ⋮
    }

We strongly recommend that you use find and replace or multi-line editing in VS Code to quickly 
change the periodic table to a compound dictionary. 
If you don't know how to use find and replace or multi-line editing, ask a fellow student, 
a tutor, a teaching assistant, or your teacher for help.

5) Copy and paste the following Python code into your chemistry.py program. 
Be certain not to paste the code inside an existing function.

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.

    # Return the total molar mass.
    return

    
The code that you pasted includes the header and documentation string for a function named compute_molar_mass. 
Read the docstring and comments in the compute_molar_mass function and write the code for that function. 
Note that you can complete the compute_molar_mass function by writing ten or fewer lines of code.


6) Modify the main function in your chemistry.py program so that it does the following:

def main():
    # Get a chemical formula for a molecule from the user.

    # Get the mass of a chemical sample in grams from the user.

    # Call the make_periodic_table function and
    # store the periodic table in a variable.

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.

    # Compute the number of moles in the sample.

    # Print the molar mass.

    # Print the number of moles.

    
Call Graph:

The following call graph shows the user-defined functions and function 
calls and returns as you should write them in your chemistry.py program. 
From this call graph we see the following function calls:

1) The computer starts executing the chemistry.py program by calling the main function.
2) While executing the main function, the computer calls the input and float functions.
3) While still executing the main function, the computer calls the make_periodic_table, 
parse_formula, and compute_molar_mass functions.
4) Finally, while still executing the main function, the computer calls the print function.


"""