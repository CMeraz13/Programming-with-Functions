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
        while True:
            option = input("Would you like to start the game (y/n)? ").lower()
            if option == "y":

                os.system('cls' if os.name == 'nt' else 'clear')

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
                print()
                time.sleep(2)
                typingPrint("\nDexterity:")
                time.sleep(2)
                typingPrint("\nDexterity is the second of the stats that will determine how much 'Physical Damage'")
                time.sleep(2)
                print()
                typingPrint("\nIntelligence:")
                time.sleep(2)
                typingPrint("\nIntelligences is one of the stats that will determine how much 'Magic Damage'")
                time.sleep(2)
                print()
                typingPrint("\nFaith:")
                time.sleep(2)
                typingPrint("\nFaith is the stat that will determine how much 'Holy Damage'")
                time.sleep(2)
                print()
                time.sleep(2)
                
                player_char = Character()
                player_char.display_stats()
                print()

                player_char.allocate_stat_points()

                typingPrint("\nGreat! Now your character will need a name.")
                print()
                character_name = input("Please enter a character name: ")

                print()

                typingPrint(f"\n{character_name}")

                player_char.display_stats()
                
                print()
                print()

                break  # Exit the loop once the game starts

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
            stat = input("\nWhich stat would you like improve? ").lower()
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

            os.system('cls' if os.name == 'nt' else 'clear')
    

def beginning_story():
    situation = 1,2,3,4,5
    situation.random()

    if situation == 1:
        typingPrint("\nYou enter the tavern, heads turn in your direction.")
        typingPrint("\nYou head towards a board full of requests of jobs needed to be done.")
        typingPrint("\nGrabbing a sheet off the board you walk over to the counter, placing down infront of")
        typingPrint("\nthe attendant. She looks up at you and asks you to fill out a form before you headout.")
        typingPrint("\nRiding towards the  dungeon, you feel your dagger bounce as you ride along.")
        typingPrint("\nYou hope that it will be enough to keep you alive.")
        typingPrint("\nYou hope...")
    elif situation == 2:
        typingPrint("\nThe wagon shook hard with each bump in the road, suddenly awaking you.")
        typingPrint("\nYou lift yourself up, looking around, you see thick wooden bars.")
        typingPrint("\nLifting your hands up to rub your tired eyes, you feel the hands stop abrubly with the rattling of chains.")
        typingPrint("\nLooking down, you see your hands bound by metal shackles. A Guard slamming on the bars as the wagon stops.")
        typingPrint("\nStartling you, he looks at you, 'We're here. Stick your hands out!' he bellows.")
        typingPrint("\nAs you climb out of the wagon, your clothes and armor is handed to you and a dagger.")
        typingPrint("\nThey inform you that for your punishment you will be handling a dangerous dungeon.")
        typingPrint("\nYour job is to survive, they say with a wicked grin.")
        typingPrint("\nYou hope your skills are good enough to keep you alive.")
        typingPrint("\nYou hope...")
    elif situation == 3:
        typingPrint("\nThe events of the night replay over in your mind as the throbbing from the bump on your head begins again.")
        typingPrint("\nYou see memories of a great fire, the screams of the villagers, and the smell of blood and smoke.")
        typingPrint("\nYou recall the memories of creatures attacking your village, you faught bravely against them.")
        typingPrint("\nAll of a sudden, you remember black as someone or something had struck you in the back of the head.")
        typingPrint("\nVery few survivors were left, and one was able to recall the direction they were heading.")
        typingPrint("\nThe omen of a dangerous dungeon fills your mind, in that direction.")
        typingPrint("\nThey hand you your broken weapon, and your dagger still intact. Grabbing the dagger you set off for the dungeon.")
        typingPrint("\nYou hope you'll be able to avenge the fallen villagers.")
        typingPrint("\nYou hope...")
    elif situation == 4:
        typingPrint("\nThe expedition was a struggle to set up. You worked so hard to make it possible. Everyone called you crazy, but here you are.")
        typingPrint("\nYou wrap bandages around the cut into your leg. The floor collaping under you feet was unexpected. You had expected traps, ")
        typingPrint("\nand creatures. Ancient text, hoards of treasures, and historical relics, but never the floor collapsing and wiping your team out.")
        typingPrint("\nYou stand up, grabbing the dagger that the guard held on to, prying it from his grasp. With no way to turn back, you set forward.")
        typingPrint("\nThe dangerous dungeon that set infront of you. What awaited you, you werent sure anymore.")
        typingPrint("\nYou hope you're knowledge will be able to help you escape.")
        typingPrint("\nYou hope...")
    else:
       typingPrint("\nYou walked through the woods for a few hours. You dont want to admit it to yourself, nor to the creatures of the forest.")
       typingPrint("\nThe day started out fine, you had decided to learn how to be a hunter; to live off of the land. Your group ventured into the ")
       typingPrint("\nforest, your mind ended up wandering. Before you knew it, you were lost, your group gone. After heading in a random direction")
       typingPrint("\nyou found thick stone doors, hidden behind moss and vines. Pushing them in, a cold chill rushed past you, a rumbling rang out.")
       typingPrint("\nYou grab the knife that was prepared for you, you ventured it.")
       typingPrint("\nYou hope your instincts will keep you alive.")
       typingPrint("\nYou hope...")


def encounters():
   
    encounter_options = 1,2,3,4,5,6,7,8,9,10
    encounter = random.choice(encounter_options)

    y_encounters = 0
    n_encounters = 0
    succeeded_encounters = 0
    failed_encounters = 0
    
    if encounter == 1:
        # Sleeping Goblins Encounter
        typingPrint("\nWalking inside the dungeon, you feel an eerie gust of wind. Walking deeper, you step into a small room. Inside you find")
        typingPrint("\nsleeping goblins, as you try to step as forwards you feel something gently scrape the ground.")
        typingPrint("\nThe room of goblins begin to shift, your foot stops, the goblins snore and groan back to sleep. This could be dangerous.")
        print()
        goblin_encounter = input("Try to quietly tiptoe around? (y/n) ")
        print()
        if goblin_encounter.lower() == 'y':
            success = roll_for_success(Character, 'dexterity')
            y_encounters += 1
            if success:
                typingPrint("\nYour feet, glide around the scattered items and creatures.")
                typingPrint("\nBefore you know it, your back gently presses against the wooden door.")
                typingPrint("\nYou slip inside, gently closing and locking the door behind you. Taking a deep breath you continue on your way.")
                typingPrint("\nYou successfully sneaked past the goblins!")
                succeeded_encounters += 1
            else:
                typingPrint("\nYour feet, try to glide around the scattered items and creatures.")
                typingPrint("\nYou stumble, slamming down on a table, launching items and goblins into the air.")
                typingPrint("\nThe clattering, and scretching filled the room. Quickly standing up, you look around the room.")
                typingPrint("\nYellow Beady eyes stare back at you. Devilish grins smile back at you. ")
                typingPrint("\nYou failed, and woke the goblins!")
                Character.health - 30
                typingPrint("\nYou slam on the door, your body filled with scratches and cuts.")
                typingPrint("\nYou take 30 damage.")
                failed_encounters += 1
        else:
            typingPrint("\nYou slowly step out of the room, quietly closing the door.")
            typingPrint("\nYou choose to continue down the long corridor ahead of you.")      
            n_encounters += 1    
    elif encounter == 2:
        # Debris Encounter
        typingPrint("\nWalking down a long hallway, you see some debris blocking a doorway. Behind the debris you see a small shimmering lights.")
        typingPrint("\nYou turn to look down both sides of the hallway to see if there are any dangers awaiting you.")
        typingPrint("\nRubbing your hands together you begin to clear out the debris. You feel something lodged, you try again and still its lodged.")
        typingPrint("\nIts stuck, you will have to use a lot of strength to remove it.")
        print()
        debris_encounter = input("Do you wish to try and dislodge the stuck debris? (y/n) ")
        print()

        if debris_encounter.lower() == "y":
            success = roll_for_success(Character, 'strength')
            y_encounters += 1
            if success:
                typingPrint("\nYou dig your heels down, using your whole body to lift the debris out of the way.")
                typingPrint("\nYou lift the debris, plopping down next to the doorway, walking through the door you find a small room.")
                typingPrint("\nIn the small you find a table and some old chairs. At the other end of the room you find another door.")
                typingPrint("\nWalking through it you find a small corridor, leading to to your right. You step in, walking down a corridor once more.")
                typingPrint("\nYou succeeded removing the debris!")
                succeeded_encounters += 1
            else:
                typingPrint("\nYou dig your heels down, your stuggle to push the debris out of the way.")
                typingPrint("\nYour foot slips and you fall down, the debris unmoved and now a sore bump on your behind.")
                typingPrint("\nYou failed to remove the debris.")
                Character.health - 10
                failed_encounters += 1
        else:
            typingPrint("\nYou turn, continuing down the corridor, deaming it not worth it to try and waste energy on debris.")
            typingPrint("\nYou head down, hoping to find a way out sooner rather than later.")
            n_encounters += 1

    elif encounter == 3:
        # Intricate Wall Encounter
        typingPrint("\nYou come up to a large wall with intricate designs. To the left you see buttons corresponding")
        typingPrint("\nto the designs on the walls. To your right in another long corridor.")
        typingPrint("\nYou deduce that the buttons when pressed in the correct order will reveal a hidden secret.")
        print()
        intricate_wall_encounter = input("Would you like to try and solve the puzzle? (y/n) ")
        print()

        if intricate_wall_encounter.lower() == "y":
            success = roll_for_success(Character, 'intelligence')
            y_encounters += 1
            if success:
               typingPrint("\nLooking at the wall, you push a button you think would correctly correspond to the image")
               typingPrint("\non the wall. As you do the button suddenly sinks in, causing you to flinch.")
               typingPrint("\nTo your relief nothing happens. You continue to push buttons carefully to each image.")
               typingPrint("\nEach button sinks, clicking into place, and as the last one sinks in the wall begins to shake.")
               typingPrint("\nYou take a step back, as the wall begins to slowly rotate, revealing a hidden path.")
               typingPrint("\nStepping inside, the wall closes behind you. You hear the clicking from the buttons being undone.")
               typingPrint("\nThe dark room suddenly lights up, as torches begin to light doing down the hall.")
               typingPrint("\nWith no where else to go, you press forwards.")
               typingPrint("\nYou successfully decoded the wall!")
               succeeded_encounters += 1
            else:
               typingPrint("\nYou push the button on the wall with the one you think it corresponds to.")
               typingPrint("\nYou hear harsh clanking behind the wall. As you take a step back, nothing happens.")
               typingPrint("\nStepping closer, you reach for another button. Before your fingers reach the buttons")
               typingPrint("\nyou feel weightless. The floor opened up below you and you begin to fall.")
               typingPrint("\nYou land in a small river violently thrashing you around.")
               typingPrint("\nYou managed to grab onto a ledge and pull yourself up.")
               typingPrint("\nTaking deep breaths, you managed to get on your feet and walk down another long corridor")
               typingPrint("\nYou failed to decode the wall.")
               Character.health - 50
               failed_encounters += 1
        else:
           typingPrint("\nYou turn from the wall, not wanting to risk the dangers.")
           typingPrint("\nYou continue down the long corridor, hoping to find some sort of exit.")
           typingPrint("\nIf not, at the very least something that wont test your intelligence.")
           n_encounters += 1

    elif encounter == 4:
       # Alter
        typingPrint("\nWalking down the Corridor you find two large wooden doors. With golden words inscripted on the walls.")
        typingPrint("\nYou can't understand the inscriptions, but decide to try and open the doors anyway.")
        typingPrint("\nInside you see a large room with circular pillars, torches lining the walls. In the center")
        typingPrint("\nyou see, an alter. Walking up to it, you look around, rows of pews facing the center. ")
        typingPrint("\nAbove you, is a large trompe l'oeil, the image looking like a God watching down on you.")
        typingPrint("\nYou feel an eerie feeling, but when you arrive to the Alter you feel compelled to pray")
        typingPrint("\nto the God above you.")
        print()
        alter_encounter = input("Would you like to kneel and pray? (y/n) ")
        print()

        if alter_encounter == "y":
            success = roll_for_success(Character, 'faith')
            y_encounters += 1
            if success:
                typingPrint("\nYou kneel before the alter, praying to the God above your head.")
                typingPrint("\nYou feel a small ray of light hit the alter, a warm sensation inside.")
                typingPrint("\nThe alter begins to rumble. As it rumbles a small golden chalice appears.")
                typingPrint("\nTaking a sip of the liquid inside you feel warm and stronger.")
                Character.health + 50
                typingPrint("\nYour faith has proven you worthy!")
                typingPrint("\nExiting the room, you find another long corridor.")
                succeeded_encounters += 1
            else:
                typingPrint("\nNothing happens.")
                typingPrint("\nYou stand and begin walking away, feeling as if the God is watching you.")
                typingPrint("\nYour faith has failed you in your time of need.")
                typingPrint("\nYou walk through the door and find another long corridor.")
                failed_encounters += 1
        else:
            typingPrint("\nYou find a door on the other side of the room. You decide its best not to tempt")
            typingPrint("\nany God or Devil or whatever rules this place.")
            typingPrint("\nOpening the doors you find another corridor leading you down intp the path.")
            n_encounters += 1

    elif encounter == 5:
       # Ogre Lair
        typingPrint("\nWalking down the corridor you find a large cave opening. Inside you feel")
        typingPrint("\na small gust of wind. It could be an exit or it could lead into danger.")
        typingPrint("\nVenturing in, you stumble across a large trunk sized arm. Following it to the body")
        typingPrint("\nyou find two large eyes peering back at you. The small gust of wind hitting you in the face.")
        typingPrint("\nAs you jump back the creature doesnt move, it appears to be asleep. Your hand reaches for your")
        typingPrint("\nDagger, sliding it out of it's sheath.")
        print()
        ogre_encounter = input("Do you wish to fight the sleeping Ogre? (y/n) ")
        print()

        if ogre_encounter == "y":
            success = roll_for_success(Character, 'strength')
            y_encounters += 1
            if success:
                typingPrint("\nYou dash forwards, jumping into the air plunging your dagger deep into")
                typingPrint("\nits neck, slicing down. The large orge roars in pain as it's suddenly awaken")
                typingPrint("\nfrom it's slumber. You quickly dash fowards stabbing at its eye.")
                typingPrint("\nA short battle ensues but you managed to put down the Ogre.")
                Character.health - 20
                typingPrint("\nYou managed to kill the Ogre!")
                typingPrint("\nWalking deeper into the cave you come across a door, pushing it open")
                typingPrint("\nyou enter another long corridor. You chose to walk down it.")
                succeeded_encounters += 1
            else:
                typingPrint("\nYou dash forwards, slashing the Ogre's neck. The cut was shallow.")
                typingPrint("\nThe Ogre roars, awaken suddenly from its slumber. You quickly")
                typingPrint("\n dash forwards again, stabbing it in its eye.")
                typingPrint("\nA long battle ensues but you finally managed to put down the Ogre")
                typingPrint("\nnot before taking some serious damage.")
                typingPrint("\nYou failed to kill the Ogre quickly.")
                Character.health - 70
                typingPrint("\nLimping to the back of the cave you come across a door.")
                typingPrint("\nPushing it open, you enter another long corridor.")
                typingPrint("\nYou chose to walk down it, hoping for an exit.")
                failed_encounters += 1
        else:
            typingPrint("\nYou slowly back up, walking back into the corridor.")
            typingPrint("\nCarefully walking down the corridor before finding a safe distance")
            typingPrint("\nto start running. 'How did an Ogre get there you think to yourself?' ")
            typingPrint("\nas you continue down the corridor.")
            n_encounters += 1

    elif encounter == 6:
       # Cells with skeletons
        typingPrint("\nFinding a door you open it to find some stairs leading down a dark stairway.")
        typingPrint("\nYou walk down the stairs and see a bunch of small empty metal cells.")
        typingPrint("\nLooking around you see the cells have a few skeletons but nothing more.")
        typingPrint("\nSuddenly the rattling of bones startles you.")
        typingPrint("\nSkeletons suddenly start arising from their dark slumber.")
        typingPrint("\nYou see as they begin to stand a door on the other side, it could be a way out.")
        print()
        encounter = input("Do you wish to fight them and reach the other side? (y/n) ")
        print()

        if encounter == "y":
            success = roll_for_success(Character, 'dexterity')
            y_encounters += 1
            if success:
                typingPrint("\nYou brandish your dagger, rushing in and attacking the skeletons.")
                typingPrint("\nYou dagger breaking the weakened skulls, and before long")
                typingPrint("\nyou managed to defeat the skeletons but not before taking some hits.")
                typingPrint("\nYou walk past the your broken boned enemies and walk up to the door.")
                typingPrint("\nYou defeated the Skeletons!")
                Character.health - 20
                typingPrint("\nPushing the door open you find yourself in another corridor. You ")
                typingPrint("\nbeing walking down in hopes for an exit.")
                succeeded_encounters += 1
            else:
                typingPrint("\nYou brandish your dagger, rushing in and attacking the skeletons.")
                typingPrint("\nYour dagger stiking the Skeletons, but didnt manage to break their skulls.")
                typingPrint("\nYour blade having not been as effective, you managed to strike one down.")
                typingPrint("\nAfter a long battle you stand above your defeated enemies.")
                typingPrint("\nYou took a good anount of damage, as you walk towards the doors.")
                typingPrint("\nYou failed to defeat the Skeletons quickly enough.")
                Character.health - 60
                typingPrint("\nPushing the door open you find yourself in another corridor. You ")
                typingPrint("\nbeing walking down in hopes for an exit.")
                failed_encounters += 1
        else:
            typingPrint("\nYou turn tail and run up the stairs. The rattling of bones chasing after you.")
            typingPrint("\nReaching the top of the stairs you slam the door shut, locking it as the ")
            typingPrint("\nSkeletons pound on the door. You sprint down the corridor not letting those ")
            typingPrint("\nSkeletons find you if they break the door down.")
            n_encounters += 1
    elif encounter == 7:
       # Maze
        typingPrint("\nYou walk pass a doorway before taking a few steps back.")
        typingPrint("\nYou cant believe your eyes, inside the room you see these large walls, ")
        typingPrint("\nwalls too large to see over but you see the ceiling so high above them.")
        typingPrint("\n'It's a Maze!' you think to yourself. Mazes tend to have an exit.")
        typingPrint("\nMaybe the exit will the way out. ")
        print()
        maze_encounter = input("Do you chose to venture into the maze? (y/n) ")
        print()

        if maze_encounter== "y":
            success = roll_for_success(Character, 'intelligence')
            y_encounters += 1
            if success:
                typingPrint("\n")
                succeeded_encounters += 1
            else:
                typingPrint("\n")
                failed_encounters += 1
        else:
            typingPrint("\n")
            n_encounters
    elif encounter == 8:
       # Invisible steps in the river
        typingPrint("\n")
        print()
        encounter = input("")
        print()

        if encounter == "y":
            success = roll_for_success(Character, 'faith')
            y_encounters += 1
            if success:
                typingPrint("\n")
                succeeded_encounters += 1
            else:
                typingPrint("\n")
                failed_encounters += 1
        else:
            typingPrint("\n")
            n_encounters += 1
    elif encounter == 9:
       # Cultists
        typingPrint("\n")
        print()
        encounter = input("")
        print()

        if encounter == "y":
            success = roll_for_success(Character, 'faith')
            y_encounters += 1
            if success:
                typingPrint("\n")
                succeeded_encounters += 1
            else:
                typingPrint("\n")
                failed_encounters += 1
        else:
            typingPrint("\n")
            n_encounters += 1
    else:
       # The lone Commander Knight
        typingPrint("\n")
        print()
        encounter = input("")
        print()

        if encounter == "y":
            success = roll_for_success(Character, 'faith')
            y_encounters += 1
            if success:
                typingPrint("\n")
                succeeded_encounters += 1
            else:
                typingPrint("\n")
                failed_encounters += 1
        else:
            typingPrint("\n")
            n_encounters += 1

# Function called Roll for Success to see if character will succeed in an action
def roll_for_success(character,required_stat):
   
    if hasattr(character, required_stat):
        required_value = getattr(character, required_stat)
    else:
        print(f"Error: '{required_stat}' is not a valid stat.")
        return False

    # Simulate a roll, for simplicity let's say it's between 1 and 20
    roll = random.randint(1, 20)
    encounter_difficulty_roll = random.randomint(1,15)

    # Showing what the player rolled and what was required
    print(f"Rolled: {roll}, Required: {required_value}")

    # Compare the roll to the required stat value
    if roll <= required_value:
        print("Success!")
        return True
    else:
        print("Failed.")
        return False
        
        


def clearScreen():
  os.system("clear")
    



main()