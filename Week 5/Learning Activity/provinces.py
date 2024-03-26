"""
Checkpoint:

Purpose:

Check your understanding of text files and lists by writing a program that 
reads the contents of a text file into a list and then changes some of the values in the list.

Assignment:

You must do the following to setup VS Code so that your program can read from a text file:

1) Download the provinces.txt file and save it in the same folder where you will save your Python program.
2) Using VS Code, open the folder where you saved the provinces.txt file by doing the following:
    * On a computer running the Mac OSX operating system:
        1) Select the File menu, then Open Flder...
        2) Find and select the folder where you saved the provinces.txt file.
        3) Select the Open button.
    # On a computer running the Windows operating system:
        1)Select the File menu, then Open Folder...
        2) Find and select the folder where you saved the provinces.txt file.
        3) Select the Select Folder button.

Now that you have correctly setup VS Code so that your program can read the provinces.txt file, 
open that file in VS Code and examine it. 
Notice that the file contains a list of names of Canadian Provinces. 
Notice also that the file contains "AB" several times which is an abbreviation for Alberta.

Write a Python program named provinces.py that reads the contents of provinces.txt into a list 
and then modifies the list. Your program must do the following:

1) Open the provinces.txt file for reading.
2) Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
3) Print the entire list.
4) Remove the first element from the list.
5) Remove the last element from the list.
6) Replace all occurrences of "AB" in the list with "Alberta".
7) Count the number of elements that are "Alberta" and print that number.

"""

def main():


    print_list = read_list("provinces.txt")
    
    print(print_list)


def read_list(provinces):
    

    print_list = []

    with open(provinces, "rt") as province_text:

        for line in province_text:

            clean_line = line.strip()

            province_text.append(clean_line)

    return print_list



# Call main to start this program.
if __name__ == "__main__":
    main()