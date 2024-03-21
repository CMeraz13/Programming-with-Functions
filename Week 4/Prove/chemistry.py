"""
Purpose: 

Prove that you can write a Python program that creates and uses a compound list.

Problem Statement:

In chemistry, a mole is a very large, fixed quantity, specifically 602,214,076,000,000,000,000,000 
(usually written as 6.02214076 × 1023). 
The molar mass of a substance is the mass in grams of one mole of the substance (grams / mole). 
A molar mass calculator is a program that computes the molar mass of a substance and the number of moles 
of a sample of that substance. To use a molar mass calculator, a chemist enters two inputs:

    * The formula for a molecule, such as H2O (water) or C6H12O6 (glucose)
    * The mass in grams of a sample of the substance, such as 3.71


The calculator computes the molar mass of the molecule and the number of moles in the sample and 
then prints both of those numbers.

Table of Elements:

There are 94 chemical elements known to occur naturally on earth. 
The symbol, name, and atomic mass of all 94 elements are shown in the following table.

Symbol: "Ac", "Ag", "Al", "Ar", "As", "At", "Au", "B", "Ba", "Be", "Bi",
Name: "Actinium", "Silver",
Atomic Mass: 227, 107.8682

Symbol: Name:       Atomic Mass:
"Ac",	"Actinium",	227
"Ag",	"Silver",	107.8682
"Al",	"Aluminum",	26.9815386
"Ar",	"Argon",	39.948
"As",	"Arsenic",	74.9216
"At",	"Astatine",	210
"Au",	"Gold",	196.966569
"B",	"Boron",	10.811
"Ba",	"Barium",	137.327
"Be",	"Beryllium",	9.012182
"Bi",	"Bismuth",	208.9804
"Br",	"Bromine",	79.904
"C",	"Carbon",	12.0107
"Ca",	"Calcium",	40.078
"Cd",	"Cadmium",	112.411
"Ce",	"Cerium",	140.116
"Cl",	"Chlorine",	35.453
"Co",	"Cobalt",	58.933195
"Cr",	"Chromium",	51.9961
"Cs",	"Cesium",	132.9054519
"Cu",	"Copper",	63.546
"Dy",	"Dysprosium",	162.5
"Er",	"Erbium",	167.259
"Eu",	"Europium",	151.964
"F",	"Fluorine",	18.9984032
"Fe",	"Iron",	55.845
"Fr",	"Francium",	223
"Ga",	"Gallium",	69.723
"Gd",	"Gadolinium",	157.25
"Ge",	"Germanium",	72.64
"H",	"Hydrogen",	1.00794
"He",	"Helium",	4.002602
"Hf",	"Hafnium",	178.49
"Hg",	"Mercury",	200.59
"Ho",	"Holmium",	164.93032
"I",	"Iodine",	126.90447
"In",	"Indium",	114.818
"Ir",	"Iridium",	192.217
"K",	"Potassium",	39.0983
"Kr",	"Krypton",	83.798
"La",	"Lanthanum",	138.90547
"Li",	"Lithium",	6.941
"Lu",	"Lutetium",	174.9668
"Mg",	"Magnesium",	24.305
"Mn",	"Manganese",	54.938045
"Mo",	"Molybdenum",	95.96
"N",	"Nitrogen",	14.0067
"Na",	"Sodium",	22.98976928
"Nb",	"Niobium",	92.90638
"Nd",	"Neodymium",	144.242
"Ne",	"Neon",	20.1797
"Ni",	"Nickel",	58.6934
"Np",	"Neptunium",	237
"O",	"Oxygen",	15.9994
"Os",	"Osmium",	190.23
"P",	"Phosphorus",	30.973762
"Pa",	"Protactinium",	231.03588
"Pb",	"Lead",	207.2
"Pd",	"Palladium",	106.42
"Pm",	"Promethium",	145
"Po",	"Polonium",	209
"Pr",	"Praseodymium",	140.90765
"Pt",	"Platinum",	195.084
"Pu",	"Plutonium",	244
"Ra",	"Radium",	226
"Rb",	"Rubidium",	85.4678
"Re",	"Rhenium",	186.207
"Rh",	"Rhodium",	102.9055
"Rn",	"Radon",	222
"Ru",	"Ruthenium",	101.07
"S",	"Sulfur",	32.065
"Sb",	"Antimony",	121.76
"Sc",	"Scandium",	44.955912
"Se",	"Selenium",	78.96
"Si",	"Silicon",	28.0855
"Sm",	"Samarium",	150.36
"Sn",	"Tin",	118.71
"Sr",	"Strontium",	87.62
"Ta",	"Tantalum",	180.94788
"Tb",	"Terbium",	158.92535
"Tc",	"Technetium",	98
"Te",	"Tellurium",	127.6
"Th",	"Thorium",	232.03806
"Ti",	"Titanium",	47.867
"Tl",	"Thallium",	204.3833
"Tm",	"Thulium",	168.93421
"U",	"Uranium",	238.02891
"V",	"Vanadium",	50.9415
"W",	"Tungsten",	183.84
"Xe",	"Xenon",	131.293
"Y",	"Yttrium",	88.90585
"Yb",	"Ytterbium",	173.054
"Zn",	"Zinc",	65.38
"Zr",	"Zirconium",	91.224

Assignment: 

During this prove milestone and the next prove assignment, 
you will write and test a molar mass calculator named chemistry.py. 
During this milestone, you will complete part of the calculator by writing a function named 
make_periodic_table and the main function. 
The make_periodic_table function must create and return a compound list that contains 
data for all 94 naturally occuring elements.

Steps:

Do the following:

1) Using VS Code, create a new file and save it as chemistry.py
2) In the chemistry.py file, write a function named make_periodic_table that takes no parameters and 
creates and returns a compound list. 
The compound list must contain all the data in the table of elements shown in the Table of Elements section above. 
The data within the compound list must be organized like this:

periodic_table_list = [
        # [symbol, name, atomic_mass]
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
          ⋮
    ]

    A) We strongly recommend that you do not type the data in the table of elements but instead that you copy and 
    paste the data from this assignment into your program. 
    If you don’t know how to use copy and paste to help you quickly write the make_periodic_table function, 
    ask a fellow student, a tutor, a teaching assistant, or your teacher for help.

    B) After you copy and paste the periodic table data into your program, you must add square brackets ([ and ]) and 
    commas (,) so that the data is organized in a compound list. 
    If you’re using VS Code as your text editor, you can use multi-line editing to quickly add 
    all the necessary square brackets and commas.

3) In the chemistry.py file, write the main function that takes no parameters and returns nothing. 
The main function should do the following:
    A) Get a chemical formula for a molecule from the user.
    B) Get the mass of a chemical sample in grams from the user.
    C) Call the make_periodic_table function and store the returned list in a variable.
    D) Print the name and atomic mass for each chemical element on a separate line. 
        Do not print the chemical element symbols.

4) At the bottom of your chemistry.py file, add a call to the main function. 
Be certain to protect the call to main with an if statement as taught in the preparation content for week 03.

Call Graph:

The following call graph shows the user-defined functions and function calls and returns as you should 
write them in your chemistry.py program. 
From this call graph we see the following function calls:

    A) The computer starts executing the chemistr.py program by calling the main function.
    B) While executing the main function, the computer calls the input, 
        float make_periodic_table, and print functions.
        
"""


# Function defining how to make a periodic table
def make_periodic_table():

    # Making a list with the elements inside
    periodic_table_list = [
        ["Ac",	"Actinium",	227],
        ["Ag",	"Silver",	107.8682],
        ["Al",	"Aluminum",	26.9815386],
        ["Ar",	"Argon",	39.948],
        ["As",	"Arsenic",	74.9216],
        ["At",	"Astatine",	210],
        ["Au",	"Gold",	196.966569],
        ["B",	"Boron",	10.811],
        ["Ba",	"Barium",	137.327],
        ["Be",	"Beryllium",	9.012182],
        ["Bi",	"Bismuth",	208.9804],
        ["Br",	"Bromine",	79.904],
        ["C",	"Carbon",	12.0107],
        ["Ca",	"Calcium",	40.078],
        ["Cd",	"Cadmium",	112.411],
        ["Ce",	"Cerium",	140.116],
        ["Cl",	"Chlorine",	35.453],
        ["Co",	"Cobalt",	58.933195],
        ["Cr",	"Chromium",	51.9961],
        ["Cs",	"Cesium",	132.9054519],
        ["Cu",	"Copper",	63.546],
        ["Dy",	"Dysprosium",	162.5],
        ["Er",	"Erbium",	167.259],
        ["Eu",	"Europium",	151.964],
        ["F",	"Fluorine",	18.9984032],
        ["Fe",	"Iron",	55.845],
        ["Fr",	"Francium",	223],
        ["Ga",	"Gallium",	69.723],
        ["Gd",	"Gadolinium",	157.25],
        ["Ge",	"Germanium",	72.64],
        ["H",	"Hydrogen",	1.00794],
        ["He",	"Helium",	4.002602],
        ["Hf",	"Hafnium",	178.49],
        ["Hg",	"Mercury",	200.59],
        ["Ho",	"Holmium",	164.93032],
        ["I",	"Iodine",	126.90447],
        ["In",	"Indium",	114.818],
        ["Ir",	"Iridium",	192.217],
        ["K",	"Potassium",	39.0983],
        ["Kr",	"Krypton",	83.798],
        ["La",	"Lanthanum",	138.90547],
        ["Li",	"Lithium",	6.941],
        ["Lu",	"Lutetium",	174.9668],
        ["Mg",	"Magnesium",	24.305],
        ["Mn",	"Manganese",	54.938045],
        ["Mo",	"Molybdenum",	95.96],
        ["N",	"Nitrogen",	14.0067],
        ["Na",	"Sodium",	22.98976928],
        ["Nb",	"Niobium",	92.90638],
        ["Nd",	"Neodymium",	144.242],
        ["Ne",	"Neon",	20.1797],
        ["Ni",	"Nickel",	58.6934],
        ["Np",	"Neptunium",	237],
        ["O",	"Oxygen",	15.9994],
        ["Os",	"Osmium",	190.23],
        ["P",	"Phosphorus",	30.973762],
        ["Pa",	"Protactinium",	231.03588],
        ["Pb",	"Lead",	207.2],
        ["Pd",	"Palladium",	106.42],
        ["Pm",	"Promethium",	145],
        ["Po",	"Polonium",	209],
        ["Pr",	"Praseodymium",	140.90765],
        ["Pt",	"Platinum",	195.084],
        ["Pu",	"Plutonium",	244],
        ["Ra",	"Radium",	226],
        ["Rb",	"Rubidium",	85.4678],
        ["Re",	"Rhenium",	186.207],
        ["Rh",	"Rhodium",	102.9055],
        ["Rn",	"Radon",	222],
        ["Ru",	"Ruthenium",	101.07],
        ["S",	"Sulfur",	32.065],
        ["Sb",	"Antimony",	121.76],
        ["Sc",	"Scandium",	44.955912],
        ["Se",	"Selenium",	78.96],
        ["Si",	"Silicon",	28.0855],
        ["Sm",	"Samarium",	150.36],
        ["Sn",	"Tin",	118.71],
        ["Sr",	"Strontium",	87.62],
        ["Ta",	"Tantalum",	180.94788],
        ["Tb",	"Terbium",	158.92535],
        ["Tc",	"Technetium",	98],
        ["Te",	"Tellurium",	127.6],
        ["Th",	"Thorium",	232.03806],
        ["Ti",	"Titanium",	47.867],
        ["Tl",	"Thallium",	204.3833],
        ["Tm",	"Thulium",	168.93421],
        ["U",	"Uranium",	238.02891],
        ["V",	"Vanadium",	50.9415],
        ["W",	"Tungsten",	183.84],
        ["Xe",	"Xenon",	131.293],
        ["Y",	"Yttrium",	88.90585],
        ["Yb",	"Ytterbium",	173.054],
        ["Zn",	"Zinc",	65.38],
        ["Zr",	"Zirconium",	91.224]
    ]

    # Returing function as periodic table list
    return periodic_table_list

# Function defining the main purpose of the code
def main():

    # Indexing values that will be used in the code
    symbols = 0
    name = 1
    atomic_mass = 2

    # Getting user input for later
    chemical_fomula = str(input("Please enter the Chemical Formula for the Molecule: "))
    mass_of_chemical_sample = float(input("Please enter the Mass of the Chemical Sample (Grams): "))

    # Creating the variable that will hold the function make periodic table
    periodic_table = make_periodic_table()

    # For loop used to print out the intented values
    for molecule in periodic_table:

        # Grabbing the indexed information to use in print statment.
        name_index = molecule[name]
        weight_index = molecule[atomic_mass]

        # Printing the indexed information formated
        print(f"{name_index}: {weight_index}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()