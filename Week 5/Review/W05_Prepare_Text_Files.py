"""
Concepts:

Broadly speaking, there are two types of files: text files and binary files. 
A text file stores words and numbers as human readable text. 
A binary file stores pictures, diagrams, sounds, music, movies, and other media as 
numbers in a format that is not directly readable by humans.

Text Files:

In order to read data from a text file, the file must exist on one of the computer’s drives, 
and your program must do these three things:

    1) Open the file for reading text
    2) Read from the file, usually one line of text at a time
    3) Close the file

The built-in open function opens a file for reading or writing. 
Here is an excerpt from the official documentation for the open function:

    open(filename, mode="rt")

    Open a file and return a corresponding file object.

    filename is the name of the file to be opened.

    mode is an optional string that specifies the mode in which the file will be opened. 
    It defaults to "rt" which means open for reading in text mode. 
    Other common values are "wt" for writing a text file (truncating the file if it already exists), 
    and "at" for appending to the end of a text file.


Example 1 contains a program that opens a text file named plants.txt for reading at line 26. 
At line 30 there is a for loop that reads the text in the file one line at a time and repeats 
the body of the for loop once for each line of text in the file. 
In the body of the for loop at lines 32–38, the code removes surrounding white space, 
if there is any, from each line of text and then stores each line of text in a list.

"""

# Example 1

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("plants.txt")

    # Print the entire list.
    print(text_list)


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()

"""
> python example_1.py
['baobab', 'kangaroo paw', 'eucalyptus', 'heliconia', 'tulip',
'chupasangre cactus', 'prickly pear cactus', 'ginkgo biloba']

After the body of a for loop that reads from a file, we can write a call to the file.close method. 
However, when calling the open function, most programmers use a with block as shown in 
example 1 at line 26 and nest the for loop inside the with block as shown at lines 30–38. 
When the with block ends, the computer will automatically close the file, 
so that the programmer doesn’t have to write a call to the file.close method.


CSV Files:

Many computer systems import and export data in CSV files. 
CSV is an acronym for comma separated values. 
A CSV file is a text file that contains tabular data with each row on a 
separate line of the file and each cell (column) separated by a comma. 
The following example shows the contents of a CSV file named hymns.csv that stores data about religious songs. 
Notice that the first row of the file contains column headings, 
the next four rows contain data about four hymns, and each row contains three columns separated by commas.

    Title,Author,Composer
    O Holy Night,John Dwight,Adolphe Adam
    Away in a Manger,Anonymous,William Kirkpatrick
    Joy to the World,Isaac Watts,George Handel
    With Wondering Awe,Anonymous,Anonymous

Python has a standard module named csv that includes functionality to read from and write to CSV files. 
The program in example 2 shows how to open a CSV file and use the csv module to 
read the data and print it to a terminal window. 
In example 2 at line 8, there is a call to the Python built-in open function, which opens the hymns.csv file for reading. 
At line 12, the program creates a csv.reader object that will read from the hymns.csv file. 
Within the for loop at lines 16 and 17 the csv.reader reads and prints each row from the CSV file.
"""

# Example 2

import csv

def main():
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open("hymns.csv", "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            print(row_list)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""
> python example_2.py
['Title', 'Author', 'Composer']
['O Holy Night', 'John Dwight', 'Adolphe Adam']
['Away in a Manger', 'Anonymous', 'William Kirkpatrick']
['Joy to the World', 'Isaac Watts', 'George Handel']
['With Wondering Awe', 'Anonymous', 'Anonymous']


"""