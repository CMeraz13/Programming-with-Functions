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

        print("Fantasy Adventure: Demo")
        option = input("Would you like to start the game (y/n)? ").lower
        option_answer = True
        while option_answer == True:
            if option == "y":
                print()
                print()


                typingPrint("Welcome to Fantasy Adventure: Demo!")
                time.sleep(2)
                typingPrint("\nBefore we begin, you will need a character!")
                typingPrint("\nLets take a look at the Stats!")
                time.sleep(2)
                print()

                #display_standard_stats = Character_Stat()
                #print(display_standard_stats)

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
                print()
                time.sleep(2)
                typingPrint("\nDexterity:")
                time.sleep(2)
                typingPrint("\nDexterity is the second of the stats that will determine how much 'Physical Damage'")
                time.sleep(2)
                typingPrint("\nyour character will do and how much 'Physical Resistances' protect you from 'Physical Damage'.")
                time.sleep(2)
                print()
                typingPrint("\nIntelligence:")
                time.sleep(2)
                typingPrint("\nIntelligences is one of the stats that will determine how much 'Magic Damage'")
                time.sleep(2)
                typingPrint("\nyour character will do and how much 'Magic Resistance' will protect you from 'Magic Damage'.")
                time.sleep(2)
                print()
                typingPrint("\nFaith:")
                time.sleep(2)
                typingPrint("\nFaith is the stat that will determine how much 'Holy Damage'")
                time.sleep(2)
                typingPrint("\nyour character will do and how much 'Holy Resistance' will protect you from 'Holy Damage'.")
                time.sleep(2)
                print()
                time.sleep(2)
                
                player_char = Character()
                player_char.display_stats()
                print()

                player_char.allocate_stat_points()

                print("great")
                print()

                player_char.display_stats()
                
                print()
                print()



                option_answer = False
            elif option == "n":
                print("Closing the game.")
                time.sleep(1)
                typingPrint("\n3...")
                time.sleep(1)
                typingPrint("\n2...")
                time.sleep(1)
                typingPrint("\n1...")
                time.sleep(1)
                typingPrint("\nBye bye!")
                option_answer = False
                os.close()
            else:
               print("Error! Not an option, please try again.")






    except:
        print()

    print()


class Character:

    def __init__(self, health = 100, strength = 1, dexterity = 1, intelligence = 1, faith = 1):
       self.health = health
       self.strength = strength
       self.dexterity = dexterity
       self.intelligence = intelligence
       self.faith = faith
       self.allocate_points = 27

    def display_stats(self):
        typingPrint(f"Character Stats:\nHealth: {self.health}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nIntelligence: {self.intelligence}\nFaith: {self.faith}\n")

    def allocate_stat_points(self):
        while self.allocate_points > 0:
            typingPrint(f"Points left to allocate: {self.allocate_points}")
            time.sleep(2)
            typingPrint("\nPlease Allocate your points (health, strength, dexterity, intelligence, faith)")
            time.sleep(2)
            stat = input("Which stat would you like improve? ").lower()
            points = int(input("How many points? "))

            if points > self.allocate_points:
               typingPrint("You dont have enough points.")
               continue

            if stat == "health":
               self.health += points * 10
            elif stat == "strength":
               self.strength += points
            elif stat == "dexterity":
               self.dexterity += points
            elif stat == "intelligence":
               self.intelligence += points
            elif stat == "faith":
               self.faith += points
            else:
               print("Invalid Stat. Please try again.")
               continue

            self.allocate_points -= points
            self.display_stats()

        
        


def clearScreen():
  os.system("clear")
    



main()