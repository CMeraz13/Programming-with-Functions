"""
Purpose:

Prove that you can write a Python program that handles exceptions, including FileNotFoundError, PermissionError, and KeyError.

Problem Statement:

A local grocery store subscribes to an online service that enables its customers to order groceries online. 
After a customer completes an order, the online service sends a CSV file that contains the 
customer’s requests to the grocery store. 
The store needs you to write a program that reads the CSV file and prints to the 
terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

Assignment:

During the prove milestone for the previous lesson, you wrote the part of this program that 
reads and processes two CSV files, one named products.csv that contains a catalog of products 
and one named request.csv that contains a customer’s order. 
During this prove assignment, you will add code to finish printing a receipt and 
to handle any exceptions that might occur while your program is running. 
Specifically, your program must do the following:

    1) Print the store name at the top of the receipt.
    2) Print the list of ordered items.
    3) Sum and print the number of ordered items.
    4) Sum and print the subtotal due.
    5) Compute and print the sales tax amount. Use 6% as the sales tax rate.
    6) Compute and print the total amount due.
    7) Print a thank you message.
    8) Get the current date and time from your computer’s operating system and print the current date and time.
    9) Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""