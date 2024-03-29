"""
Purpose:

Prove that you can write a Python program that reads CSV files and creates, populates, and uses a dictionary.

Problem Statement:

A local grocery store subscribes to an online service that enables its customers to order groceries online. 
After a customer completes an order, the online service sends a CSV file that 
contains the customer’s requests to the grocery store. The store needs you to write a program 
that reads the CSV file and prints to the terminal window a receipt that lists the 
purchased items and shows the subtotal, the sales tax amount, and the total.

Assignment:

During this milestone, you will write half of a Python program named receipt.py that 
prints to the terminal window a receipt for a customer’s grocery order. 
Specifically, by the end of this milestone, your program must contain at least these two functions:

    1) main
    2) read_dictionary
and must read and process these two CSV files:

    * The products.csv file is a catalog of all the products that the grocery store sells.
    * The request.csv file contains the items ordered by a customer.

Steps: 

Do the following:

1) Download both of these files: products.csv and request.csv and 
    save them in the same folder where you will save your Python program.
2) Open the products.csv file in VS Code and examine it. Notice that each row in this file 
    contains three values separated by commas: a product number, a product name, and a retail price. 
    Also, notice that each product number in the products.csv file is unique. 
    This means that your program can read the products.csv file into a dictionary and 
    use the product numbers as keys in the dictionary.
3) In VS Code, create a new file and save it as receipt.py in the same folder where you 
    saved the products.csv and request.csv files.
4) In receipt.py, write a function named read_dictionary that will open a CSV file for 
    reading and use a csv.reader to read each row and populate a compound dictionary with the contents of 
    the products.csv file. The read_dictionary function must have this header and documentation string:


    def read_dictionary(filename, key_column_index):
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    

Recall that each item in a dictionary has a key and a value. 
Each item in the products dictionary must have a product number as the key and a list with the product number, 
product name, and price as the value as shown in the following table.


                Products
 Key	            Value
"D150"	["D150", "1 gallon milk", 2.85]
"D083"	["D083", "1 cup yogurt", 0.75]
"D215"	["D215", "1 lb cheddar cheese", 3.35]
"P019"	["P019", "iceberg lettuce", 1.15]
"P020"	["P020", "green leaf lettuce", 1.79]
"P021"	["P021", "butterhead lettuce", 1.83]
"P025"	["P025", "8 oz arugula", 2.19]
"P143"	["P143", "1 lb baby carrots", 1.39]
"W231"	["W231", "32 oz granola", 3.21]
"W112"	["W112", "wheat bread", 2.55]
"C013"	["C013", "twix candy bar", 0.85]
"H001"	["H001", "8 rolls toilet tissue", 6.45]
"H014"	["H014", "facial tissue", 2.49]
"H020"	["H020", "aluminum foil", 2.39]
"H021"	["H021", "12 oz dish soap", 3.19]
"H025"	["H025", "toilet cleaner", 4.50]

5) Open the request.csv file in VS Code and examine it. 
    Notice that each row contains only two values, a product number and a quantity. 
    Notice also that product number D083 appears twice in the file. 
    It appears twice because the customer who created the order in the request.csv file added four 
    yogurts to his order and then later added three more yogurts to his order. 
    Because product numbers may appear multiple times in the request.csv file, 
    your program must not read the contents of request.csv into a dictionary.
6) In your receipt.py program, write another function named main that does the following:
    1) Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
    2) Prints the products_dict.
    3) Opens the request.csv file for reading.
    4) Skips the first line of the request.csv file because the first line contains column headings.
    5) Uses a loop that reads and processes each row from the request.csv file. 
        Within the body of the loop, your program must do the following for each row:
            A) Use the requested product number to find the corresponding item in the products_dict.
            B) Print the product name, requested quantity, and product price.

Because product number D083 appears twice in the request.csv file, 
your program must not read the request.csv file into a dictionary. 
Recall that each key in a dictionary is unique. 
If your program reads the request.csv file into a dictionary, when your program reads line 3 of the 
request.csv file, your program will put a request for four yogurts into the dictionary. 
Then when your program reads line 6 of the request.csv file, your program will replace the 
request for four yogurts with a request for three yogurts. 
In other words, if your program reads the request.csv file into a dictionary, your program will 
think that the customer ordered only three yogurts instead of the seven (4 + 3) that he ordered. 
Therefore, your program must not read the request.csv file into a dictionary but 
should instead read and process each row similar to example 3 in the preparation content for this lesson.

7) At the bottom of your receipt.py file, add a call to the main function. 
Be certain to protect the call to main with an if statement as taught in the preparation content for week 3.

"""

# Imported CSV to be used in code
import csv

# Imported Datetime from Datetime to be used directly later in the code
from datetime import datetime

# Setting a current date and time to the current date and time
current_date_and_time = datetime.now()

# Printing out the current date and time
print(f"{current_date_and_time:%A %I:%M %p}")

# Function defining the main purpose of the code
def main():

    try:
        # Setting Prodcut Dict to the function read dictionary
        product_dict = read_dictionary("products.csv", 0)

        # Printing out Product Dict
        print(product_dict)

        # Setting the variable Number of Items to 0 to be used later
        number_of_items = 0

        # Setting a variable for Subtotal to 0 to be added to later
        subtotal = 0.00

        # Setting the variable Tax to be used in the code later
        tax = 0.06

        # Setting the Discount Percent Variable to 10 percent to be used later
        discount_percent = 0.10

        # Opening the Request.csv and turning it to the variable Request Text
        with open("request.csv", "rt") as request_text:

            # Reading the CSV file, Request text and putting it into Reader variable
            reader = csv.reader(request_text)

            # Calling reader to skip the first line of the csv
            next(reader)

            # Printing empty space for formatting
            print()
            print()
            print()

            # Printing the name of the store for the receipt
            print("General Store Inc. ")

            # Using a For Loop that will iterate through each Line in Reader
            for line in reader:

                # Setting the Product Number to the first index within Line
                product_number = line[0]

                # Setting the quantity to the first index within Line and making it into an integer
                quantity = int(line[1])

                # Creating a variable to add each quantity of items into Number of Items to be used later
                number_of_items += quantity

                # If statement used to check the Product Number in the Product Dict
                if product_number in product_dict:

                    # Variable Product info set to the Product Dict index of Product Number
                    product_info = product_dict[product_number]

                    # Variable Product Name set to the Product Info index of One
                    product_name = product_info[1]

                    # Variable Price set to a float value from Product Info index of Two
                    product_price = float(product_info[2])

                    # Creating a variable of Subtotal that adds each quantity multiplied by their price
                    # for each iteration
                    subtotal += quantity * product_price

                    # Printing out the Product Name with their Quanatities and their Price
                    print(f"{product_name}: {quantity} @ ${product_price:.2f}")
                    
            # Setting Variable Day of The Week to the Current Date and Time with method Weekday
            day_of_the_week = current_date_and_time.weekday()

            # Printing an empty space for formatting
            print()

            # If statement to check if its a Tuesday or Wednesday
            if day_of_the_week == 1 or day_of_the_week == 2:

                # Printing out the Number of Items
                print(f"Number of Items: {number_of_items}")

                # Rounding the Subtotal to the second decimal point
                subtotal = round(subtotal, 2)

                # Printing the Subtotal
                print(f"Subtotal: {subtotal}")

                # Setting Sales Tax equal to Subtotal * Tax
                sales_tax = subtotal * tax

                # Rounding the Sales Tax to the second decimal point
                sales_tax = round(sales_tax,2)

                # Printing out the Sales Tax
                print(f"Sales Tax: {sales_tax}")

                # Setting Discount to a rounded total of the Subtotal multiplied by Discount Percent
                # and setting it to the second decimal point
                discount = round(subtotal * discount_percent, 2)

                # Printing out the Discount
                print(f"Discount: {discount}")
                
                # Subtracting the discount from the subtotal
                subtotal -= discount

                # Setting Total equal to the Subtotal plus the Sales Tax
                total = subtotal + sales_tax

                # Rounding out Total to second decimal point
                total = round(total, 2)

                # Printing out the Total
                print(f"Total: {total}")

                # Printing out an empty space for formatting
                print()

            # Else statement if the Day of The Week isnt Tuesday or Wednesday
            else:

                # Printing out the Number of Items
                print(f"Number of Items: {number_of_items}")

                # Rounding the Subtotal to the second decimal point
                subtotal = round(subtotal, 2)

                # Printing the Subtotal
                print(f"Subtotal: {subtotal}")

                # Setting Sales Tax equal to Subtotal * Tax
                sales_tax = subtotal * tax

                # Rounding the Sales Tax to the second decimal point
                sales_tax = round(sales_tax,2)

                # Printing out the Sales Tax
                print(f"Sales Tax: {sales_tax}")

                # Setting the Total equal to Subtotal plus the Sales Tax
                total = subtotal + sales_tax

                # Rounding Total to the second decimal point
                total = round(total, 2)

                # Printing out the Total
                print(f"Total: {total}")

                # Printing out an empty space for formatting
                print()

            # Printing out end message
            print("Thank you for shopping at General Store Inc.")

            # Printing out the Current Date and Time
            print(f"{current_date_and_time:%a %b %m %I:%M:%S %p %G}")

            # Printing out an empty space for formatting
            print()

    except KeyError as value_not_found_err:


        print(type(value_not_found_err).__name__, value_not_found_err, sep=": ")
        print()

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {product_dict} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {product_dict}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

    except IndexError as index_err:
        # This code will be executed if the user enters a valid
        # integer for the line number, but the integer is greater
        # than the number of lines in the file.
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        length = len(product_dict)
        if product_dict < 0:
            print(f"{product_dict} is a negative integer.")
        else:
            print(f"{product_dict} is greater than the number" \
                    f" of lines in {product_dict}.")
            print(f"There are only {length} lines in {product_dict}.")
        print(f"Run the program again and enter a line number" \
                f" between 1 and {length}.")
                
    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")

        
# Function defining read dictionary
def read_dictionary(filename, key_column_index):
    """ Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Creating an empty dictionary to be used later
    products = {}

    # Opening the filename set to Products Text
    with open(filename, "rt") as products_text:

        # Setting a Product Reader to read the CSV File of Product Text
        product_reader = csv.reader(products_text)
        
        # Setting Product Reader to skip the first line
        next(product_reader)

        # A For Loop that iterates each Line in Product reader
        for line in product_reader:

            # Setting the Variable Key to Line with Key Column Index
            key = line[key_column_index]

            # Setting Product Key equal to Line and storing them in Products dictionary
            products[key] = line
            
    # Returns Prodcuts
    return products

# If this file was executed like this:
# > python receipt_prove.py
# then call the main function. However if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()