"""
W06 Checkpoint: Using Objects:

    Purpose:

        Improve your ability to write object-oriented code.

    Problem Statement:

        There are several types of commands that are commonly found in object oriented programs. 
        These types of commands are so common, that a programmer must be able to recognize and write them. 
        One of these types of commands is calling the methods of an object using the dot operator (.) as shown in this template:
            variable = object.method(arg1, arg2, ...)
        
    
    Assignment:
        Write a small Python program named fruit.py that demonstrates object oriented programming by modifying a list. 
        Do the following:

            1) Open a new blank file in VS Code and save it as fruit.py
            2) Copy and paste this code at the top of your fruit program:
                def main():
                    # Create and print a list named fruit.
                    fruit_list = ["pear", "banana", "apple", "mango"]
                    print(f"original: {fruit_list}")
            3) Add code to reverse and print fruit_list.
            4) Add code to append "orange" to the end of fruit_list and print the list.
            5) Add code to find where "apple" is located in fruit_list and insert "cherry" 
                before "apple" in the list and print the list.
            6) Add code to remove "banana" from fruit_list and print the list.
            7) Add code to pop the last element from fruit_list and print the popped element and the list.
            8) Add code to sort and print fruit_list.
            9) Add code to clear and print fruit_list.
            10) At the bottom of your program write a call to the main function.

            
    Testing Procedure: 

        Verify that your program works correctly by following each step in this testing procedure:

        1) Run your program and ensure that your program’s output is the same as the output shown below.

            > python fruit.py
                original: ['pear', 'banana', 'apple', 'mango']
                reversed: ['mango', 'apple', 'banana', 'pear']
                append orange: ['mango', 'apple', 'banana', 'pear', 'orange']
                insert cherry: ['mango', 'cherry', 'apple', 'banana', 'pear', 'orange']
                remove banana: ['mango', 'cherry', 'apple', 'pear', 'orange']
                pop orange: ['mango', 'cherry', 'apple', 'pear']
                sorted: ['apple', 'cherry', 'mango', 'pear']
                cleared: []

"""

def main():

    # Trying to see if it works 
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        # Reversing Fruit List using .reserse()
        fruit_list.reverse()

        # Printing out the reversed list
        print(f"Reversed: {fruit_list}")

        # Appending Orange to Fruit List
        fruit_list.append("orange")

        # Printing out the appened Fruit List
        print(f"Append Orange: {fruit_list}")

        # Inserting Cherry into Fruit List
        fruit_list.insert(1, "cherry")

        # Printing out the inserted Fruit List
        print(f"Insert Cherry: {fruit_list}")

        # Removing Banana from Fruit List
        fruit_list.remove("banana")

        # Printing out Fruit List with Banana removed
        print(f"Remove Banana: {fruit_list}")

        # Popping out Orange from Fruit List
        fruit_list.pop(4)

        # Printing out Fruit List with Orange Popped out
        print(f"Pop Orange: {fruit_list}")

        # Sorting out Fruit List
        fruit_list.sort()

        # Printing out the sorted Fruit List
        print(f"Sorted: {fruit_list}")

        # Clearing out Fruit list
        fruit_list.clear()

        # Printing out the Cleared List
        print(f"Cleared: {fruit_list}")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")


# If this file is executed like this:
# > python check_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
