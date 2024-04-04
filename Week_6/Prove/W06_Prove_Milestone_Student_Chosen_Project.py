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

import math, random, time, sys, os
from datetime import datetime

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def main():
    try:
        print()
        print()

        typingPrint("Welcome to Fantasy Adventure: Demo!")
        time.sleep(2)
        typingPrint("\nBefore we begin, you will need a character!")
        typingPrint("\nLets take a look at the Stats!")
        time.sleep(2)
        print()

        display_standard_stats = Character_Stat()
        print(display_standard_stats)

        typingPrint("\nEach character has 5 individual stats.")
        time.sleep(2)
        typingPrint("\nEach individual stat will affect what your character can and cant do.")
        time.sleep(2)
        print()
        typingPrint("\nHealth:")
        time.sleep(2)
        typingPrint("\nHealth indicates how many 'Hit Points' or 'HP' your character has before you get a game over.")
        time.sleep(2)
        typingPrint("\nIf your 'HP' reach 0, its 'Game Over'.")
        time.sleep(2)
        typingPrint("\nDuring the game you will encounter Enemies who will cause you to take damange or get hit")
        time.sleep(2)
        typingPrint("\nSo be sure to always be careful or you will reach 'Game Over'!")
        time.sleep(2)
        print()
        typingPrint("\nStrength:") 
        time.sleep(2)
        typingPrint("\nStrength is one of the stats that will determine how much 'Physical Damage'")
        time.sleep(2)
        typingPrint("\nyour character will do and how much 'Physical Resistances' protect you from 'Physical Damage'.")
        time.sleep(2)
        typingPrint("\nStrength:")
        time.sleep(2)
        typingPrint("\nDexterity:")
        time.sleep(2)
        typingPrint("\nDexterity is the second of the stats that will determine how much 'Physical Damage'")
        time.sleep(2)
        typingPrint("\nyour character will do and how much 'Physical Resistances' protect you from 'Physical Damage'.")
        time.sleep(2)
        typingPrint("\nIntelligence:")
        time.sleep(2)
        typingPrint("\nIntelligences is one of the stats that will determine how much 'Magic Damage'")
        time.sleep(2)
        typingPrint("\nyour character will do and how much 'Magic Resistance' will protect you from 'Magic Damage'.")
        time.sleep(2)
        typingPrint("\nFaith:")
        time.sleep(2)
        typingPrint("\nFaith is the stat that will determine how much 'Holy Damage'")
        time.sleep(2)
        typingPrint("\nyour character will do and how much 'Holy Resistance' will protect you from 'Holy Damage'.")
        time.sleep(2)
        typingPrint("\nLets take a look at the Level 1: Character Stats!")
        time.sleep(2)
        health = 100
        # player_health = health * (allocated_health_points * 10)

        #mana = 50
        #player_mana = mana * (allocated_mana_points * 3.2)

        strength = 1
        #player_strength = strength + allocated_strength_points

        dexterity = 1
        #player_dexterity = dexterity + allocated_dexterity_points

        intelligence = 1
        #player_intelligence = intelligence + allocated_intelligence_points

        faith = 1
        #player_faith = faith + allocated_faith_points
        
        print()
        print(f"Character stats: \nHealth: {health}\nStrength: {strength}\nDexterity: {dexterity}\nIntelligence: {intelligence}\nFaith: {faith}")

        print()
        print()






    except:
        print()

    print()

def Character_Stat():

    allocate_points = 37

    while allocate_points != 0 or allocate_points = 37:
        

def clearScreen():
  os.system("clear")
    



main()