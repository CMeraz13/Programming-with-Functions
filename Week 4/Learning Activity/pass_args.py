"""
Purpose:

Reinforce your understanding that numbers are passed to a function by value and lists are passed to a function by reference.

Problem Statement:

Within a Python program, when a number is passed as an argument to a function, 
the computer copies the number from the argument into the parameter. 
In other words, the parameter gets a copy of the value that is in the argument. 
However, when a list is passed as an argument to a function, the computer does not copy the list. 
Instead, the computer copies a reference to the list into the parameter. 
This means the argument and parameter refer to the same list. 
If a called function changes a list that was passed to the function, 
this will change the list in both the calling and called functions because both the argument 
and parameter refer to the same list.

Assignment:

During this checkpoint, you will examine and run a Python program that passes both a number and a list to function. 
Do the following:




1) Download and save the pass_args.py Python file and then open it in VS Code.
2) Run the pass_args.py program on your computer. 
Examine the code and the output and answer the following three questions:
    A) In main, there are two local variables named x and lx. 
    At line 14, both of these local variables are passed to the modify_args function. 
    After the call to modify_args finished, which of main’s two local variables did the modify_args function change?
        A-1) x
        B-2) lx
        C-3) both of them
        D-4) neither of them
    B) Why is the modify_args function NOT able to change main’s local variable x?
        A-1) Because x is a number and therefore passed to a function by value
        B-2) Because x is a list and therefore passed to a function by reference
    C) Why is the modify_args function able to change main’s local variable lx?
        A-1) Because lx is a number and therefore passed to a function by value
        B-2) Because lx is a list and therefore passed to a function by reference


Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("    modify_args(n, alist)")
    print(f"        Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"        After changing n and alist:  n {n}  alist {alist}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
