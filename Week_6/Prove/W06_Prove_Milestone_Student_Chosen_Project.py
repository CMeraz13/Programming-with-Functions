"""
W06 Prove Milestone: Student Chosen Program:
    Purpose:
        Prove that you can write a significant Python project that solves a 
        real-world problem and is well organized with functions.

    Assignment:
        Develop the program that you proposed in the project proposal assignment. 
        Your program must include multiple functions that you verify are correct with test functions and pytest.

    Submission:
        At the end of this week, you must submit a description of your work, and your teacher or 
        teaching assistant will grade your work according to the following rubric.

    Project Milestone:
        1) Time—50%: Did you spend at least eight hours on your Python program or test functions during the current week?
        2) Organization—20%:
            A) Is your program organized into multiple functions?
            B) Does each function in your program perform just one task?
        3) Progress—20%: Did you complete some significant part of your program during the current week?
        4) Description—10%: Is the description of your work for this lesson complete and easily understandable? 
        Your description should include the following:
            A) A list of the function names in your program.
            B) A list of the test function names in your test code.
            C) A list of the documentation that you read, the videos that you watched, and the coding experiments that you tried.
            D) A description or list of the work that you finished on your program.

"""

import math
import random
from datetime import datetime

def main():
    
    print("Welcome to Fantasy Adventure: Demo!")


    print()

def Character_Stat():

    # The purpose of this function is to determine what stats the players character will have

    health = 100
    endurance = 10
    mana = 50
    strength = 1
    dexterity = 1
    intelligence = 1
    faith = 1

    

    print(f"Character stats: \nHealth: {health}\nEndurance: {endurance}\nMana: {mana}\nStrength: {strength}\nDexterity: {dexterity}\nIntelligence: {intelligence}\nFaith: {faith}")




Character_Stat()