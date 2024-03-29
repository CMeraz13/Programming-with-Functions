"""
Purpose:

There are a few details about writing and calling functions in Python that, if you understand, 
will help you be a more effective programmer. 
These details include default parameter values and pass by reference. 
As a team during this activity, you will write and call a function that 
demonstrates both default parameter values and pass by reference.

Assignment: 

As a team, write a Python program named random_numbers.py that creates a list of numbers, 
appends more numbers onto the list, and prints the list. 
The program must have two functions named main and append_random_numbers as follows:

1) main
    A) Has no parameters
    B) Creates a list named numbers like this:
        numbers = [16.2, 75.1, 52.3]
    
    C) Prints the numbers list
    D) Calls the append_random_numbers function with only one argument to add one number to numbers
    E) Prints the numbers list
    F) Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    G) Prints the numbers list

2) append_random_numbers
    A) Has two parameters: a list named numbers_list and an integer named quantity. 
        The parameter quantity has a default value of 1
    B) Computes quantity pseudo random numbers by calling the random.uniform function.
    C) Rounds the quantity pseudo random numbers to one digit after the decimal.
    D) Appends the quantity pseudo random numbers onto the end of the numbers_list.

At the bottom of your program, write an if statement that calls the main function. 
Then run your program and verify that your program works correctly.

Core Requirements:

1) Your program includes two functions named main and append_random_numbers. 
    The append_random_numbers function has two parameters named numbers_list and quantity, 
    and quantity has a default value of 1.
2) The main function calls append_random_numbers twice, first with one argument and second with two arguments.
3) The append_random_numbers function includes a loop that appends quantity random numbers at the end of numbers_list.

Stretch Challenges:

If your team finishes the core requirements in less than an hour, complete one or more of these stretch challenges. 
Note that the stretch challenges are optional.

1) Add a function named append_random_words that meets the following criteria:
    A) Has two parameters: a list named words_list and an integer named quantity. The parameter quantity has a default value of 1
    B) Randomly selects quantity words from a list of words and appends the selected words at the end of words_list.

2) Add statements in the main function that create a list of words, call the append_random_words function, 
and then print the list of words.

3) Add something or change something in your program that you think would make your program better, 
easier for the user, more elegant, or more fun. Be creative.

"""
# importing the function random to use later in the code
import random

# Main Function
def main():
    # Creating a list
    numbers = [16.2, 75.1, 52.3]

    # printing the list
    print(numbers)
    
    # Calls append_random_number function and adds a random number
    append_random_numbers(numbers, 1)

    # prints numbers list with the added values
    print(numbers)

    # Calls append_random_number function again and adds a random number
    append_random_numbers(numbers, 3)

    # prints numbers list with the added values
    print(numbers)

    # An empty list used to append random words
    random_words = []

    # Appending 5 random words to the list
    append_random_words(random_words, 5)

    # Printing out the 5 randomly selected words.
    print(random_words)





# Defining append random numbers using numbers list and quantity set to 1
def append_random_numbers(numbers_list, quantity = 1):

    # For loop to get a random generated number
    for num in range(quantity):

        # setting the new number to new number and having it roundly getting 
        #a new number and rounding it to 1 decimal point
        new_number = round(random.uniform(0, 100), 1)
    
        # Appending the new number to numbers list to be called into Main function
        numbers_list.append(new_number)
    

# Defining append random words using words list and quantity set to 1
def append_random_words(words_list, quantity = 1):

    # Creating a list with words that will be randomly pull from
    word_list = ["Computer", "Yellow", "Bus", "Flower", "Barking", "Willingly", "House", "Boat", "Mud", "Butterfly", "Pasta"]

    # For loop used to to randomly pull words from the word list
    for word in range(quantity): 

        # Randomly pulling words from list
        random_word = random.choice(word_list)

        # Appending the random words selected to the empty list in main
        words_list.append(random_word)


# Running main function
if __name__ == "__main__":
    main()

