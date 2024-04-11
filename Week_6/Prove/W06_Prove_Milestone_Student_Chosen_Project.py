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


def beginning_story():

    situation = random.choice([1, 2, 3, 4, 5])

    if situation == 1:
        typingPrint("\nYou enter the tavern, heads turn in your direction.")
        typingPrint("\nYou head towards a board full of requests of jobs needed to be done.")
        typingPrint("\nGrabbing a sheet off the board you walk over to the counter, placing down infront of")
        typingPrint("\nthe attendant. She looks up at you and asks you to fill out a form before you headout.")
        typingPrint("\nRiding towards the  dungeon, you feel your dagger bounce as you ride along.")
        typingPrint("\nYou hope that it will be enough to keep you alive.")
        typingPrint("\nYou hope...")
        print()
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
        print()
    elif situation == 3:
        typingPrint("\nThe events of the night replay over in your mind as the throbbing from the bump on your head begins again.")
        typingPrint("\nYou see memories of a great fire, the screams of the villagers, and the smell of blood and smoke.")
        typingPrint("\nYou recall the memories of creatures attacking your village, you faught bravely against them.")
        typingPrint("\nAll of a sudden, you remember back as someone or something had struck you in the back of the head.")
        typingPrint("\nVery few survivors were left, and one was able to recall the direction they were heading.")
        typingPrint("\nThe omen of a dangerous dungeon fills your mind, in that direction.")
        typingPrint("\nThey hand you your broken weapon, and your dagger still intact. Grabbing the dagger you set off for the dungeon.")
        typingPrint("\nYou hope you'll be able to avenge the fallen villagers.")
        typingPrint("\nYou hope...")
        print()
    elif situation == 4:
        typingPrint("\nThe expedition was a struggle to set up. You worked so hard to make it possible. Everyone called you crazy, but here you are.")
        typingPrint("\nYou wrap bandages around the cut into your leg. The floor collaping under you feet was unexpected. You had expected traps, ")
        typingPrint("\nand creatures. Ancient text, hoards of treasures, and historical relics, but never the floor collapsing and wiping your team out.")
        typingPrint("\nYou stand up, grabbing the dagger that the guard held on to, prying it from his grasp. With no way to turn back, you set forward.")
        typingPrint("\nThe dangerous dungeon that set infront of you. What awaited you, you werent sure anymore.")
        typingPrint("\nYou hope you're knowledge will be able to help you escape.")
        typingPrint("\nYou hope...")
        print()
    else:
       typingPrint("\nYou walked through the woods for a few hours. You dont want to admit it to yourself, nor to the creatures of the forest.")
       typingPrint("\nThe day started out fine, you had decided to learn how to be a hunter; to live off of the land. Your group ventured into the ")
       typingPrint("\nforest, your mind ended up wandering. Before you knew it, you were lost, your group gone. After heading in a random direction")
       typingPrint("\nyou found thick stone doors, hidden behind moss and vines. Pushing them in, a cold chill rushed past you, a rumbling rang out.")
       typingPrint("\nYou grab the knife that was prepared for you, you ventured it.")
       typingPrint("\nYou hope your instincts will keep you alive.")
       typingPrint("\nYou hope...")
       print()
    




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
                time.sleep(0)
                typingPrint("\nEach individual stat will affect what your character can and cant do.")
                time.sleep(0)
                print()
                typingPrint("\nHealth:")
                time.sleep(0)
                typingPrint("\nHealth indicates how many 'Hit Points' or 'HP' your character has before you get a game over.")
                time.sleep(0)
                typingPrint("\nIf your 'HP' reach 0, its 'Game Over'.")
                time.sleep(0)
                typingPrint("\nDuring the game you will encounter Enemies who will cause you to take damange or get hit")
                time.sleep(0)
                typingPrint("\nSo be sure to always be careful or you will reach 'Game Over'!")
                time.sleep(0)
                print()
                typingPrint("\nStrength:") 
                time.sleep(0)
                typingPrint("\nStrength is one of the stats that will determine where physical strength is required to succeed.")
                print()
                time.sleep(0)
                typingPrint("\nDexterity:")
                time.sleep(0)
                typingPrint("\nDexterity is the second of the stats that will determine where your dexterity is required to succeed.")
                time.sleep(0)
                print()
                typingPrint("\nIntelligence:")
                time.sleep(0)
                typingPrint("\nIntelligences is one of the stats that will determine where intelligence is required to succeed.")
                time.sleep(0)
                print()
                typingPrint("\nFaith:")
                time.sleep(0)
                typingPrint("\nFaith is the stat that will determine the encounters where faith is required to succeed.")
                time.sleep(0)
                print()
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

                typingPrint(f"\n{character_name} \n")

                print(player_char.display_stats())
                time.sleep(3)

                os.system('cls' if os.name == 'nt' else 'clear')
                print()

                break  # Exit the loop once the game starts

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
                os.close()
            else:
               print("Error! Not an option, please try again.")

        print()
        print()
        beginning_story()
        print()
        print()
        encounters()

        player_hp = Character()

        if player_hp.health > 0:
            typingPrint("\nYou stumble out of a hole in the corridor, the bright sun blinding you.")
            typingPrint("\nLooking around you find yourself outside, away from the horrors of the dungeon.")
            typingPrint("\ncleaning yourslef up, you head in a direction, hoping to find civilization.")
            typingPrint("\nHopefully...")
            print()
            print()
            typingPrint("\nTHANK YOU FOR PLAYING FANTASY ADVENTURE!")
            print()
            print()

        elif player_hp.health == 0:
            typingPrint("\nYou died, left in that horrid dungeon with no one ever finding you.")
            typingPrint("\nWell, until the next poor soul stumbles across the dungeon.")
            typingPrint("\nWe hope they do, otherwise the fun will stop.")
            typingPrint("\nWe hope they do...")
            print()
            print()
            typingPrint("\nTHANK YOU FOR PLAYING FANTASY ADVENTURE!")
            print()
            print()

        else:
            typingPrint("\nYou died, left in that horrid dungeon with no one ever finding you.")
            typingPrint("\nWell, until the next poor soul stumbles across the dungeon.")
            typingPrint("\nWe hope they do, otherwise the fun will stop.")
            typingPrint("\nWe hope they do...")
            print()
            print()
            typingPrint("\nTHANK YOU FOR PLAYING FANTASY ADVENTURE!")
            print()
            print()



    except:
        print("F")

    print()

pass

class Character:

    def __init__(self, health = 100, strength = 1, dexterity = 1, intelligence = 1, faith = 1):
       self.health = health
       self.strength = strength
       self.dexterity = dexterity
       self.intelligence = intelligence
       self.faith = faith
       self.allocate_points = 73

    def display_stats(self):
        stats_str = "Character Stats:\n"
        stats_str += f"Health: {self.health}\n"
        stats_str += f"Strength: {self.strength}\n"
        stats_str += f"Dexterity: {self.dexterity}\n"
        stats_str += f"Intelligence: {self.intelligence}\n"
        stats_str += f"Faith: {self.faith}\n"
        return stats_str

    def allocate_stat_points(self):
        while self.allocate_points > 0:
            typingPrint(f"Points left to allocate: {self.allocate_points}")
            time.sleep(2)
            typingPrint("\nPlease Allocate your points (health, strength, dexterity, intelligence, faith)")
            time.sleep(2)
            stat = input("\nWhich stat would you like improve? ").lower()
            points = int(input("How many points? "))
            print()

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
            print()
            self.allocate_points -= points
            print(self.display_stats())
            time.sleep(3)

            os.system('cls' if os.name == 'nt' else 'clear')
    
    def take_damage(self, damage):
        # Method to reduce character's health by the specified amount of damage
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Ensure health doesn't go below 0

    def health_healed(self, heal):
        # Function used to heal the character's health by the specified amount
        self.health += heal
    
    


def encounters():
   
    encounter_options = list(range(1, 11))

    y_encounters = 0
    n_encounters = 0
    succeeded_encounters = 0
    failed_encounters = 0
    
    player = Character()

    while encounter_options:

        if player.health <= 0:
            typingPrint("\nYou Died! Your character ran out of health")
            typingPrint("\nGame Over.")
            return  # End the encounters function if player health is 0

        encounter = random.choice(encounter_options)

        # Check if the encounter has already been encountered
        if encounter in encounter_options:
            encounter_options.remove(encounter)
        else:
            continue  # Skip this iteration if encounter has already been encountered

        if encounter == 1:
            # Sleeping Goblins Encounter
            typingPrint("\nYou walk down a long corridor. Walking deeper, you find a door leading into a small room. Inside you find")
            typingPrint("\nsleeping goblins, as you try to step as forwards you feel something gently scrape the ground.")
            typingPrint("\nThe room of goblins begin to shift, your foot stops, the goblins snore and groan back to sleep. This could be dangerous.")
            print()
            while True:
                goblin_encounter = input("Try to quietly tiptoe around? (y/n) ").lower()
                print()
                if goblin_encounter == 'y':
                    success = roll_for_success(player, 'dexterity')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYour feet, glide around the scattered items and creatures.")
                        typingPrint("\nBefore you know it, your back gently presses against the wooden door.")
                        typingPrint("\nYou slip inside, gently closing and locking the door behind you. Taking a deep breath you continue on your way.")
                        typingPrint("\nYou successfully sneaked past the goblins!")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYour feet, try to glide around the scattered items and creatures.")
                        typingPrint("\nYou stumble, slamming down on a table, launching items and goblins into the air.")
                        typingPrint("\nThe clattering, and scretching filled the room. Quickly standing up, you look around the room.")
                        typingPrint("\nYellow Beady eyes stare back at you. Devilish grins smile back at you. ")
                        typingPrint("\nYou failed, and woke the goblins!")
                        player.take_damage(30)
                        typingPrint("\nYou slam on the door, your body filled with scratches and cuts.")
                        typingPrint("\nYou take 30 damage.")
                        typingPrint("\nYou continue down the long corridor in front of you, trying to get")
                        typingPrint("\nas far as you can from those goblins")
                        print()
                        failed_encounters += 1
                    break
                elif goblin_encounter.lower() == 'n':
                    typingPrint("\nYou slowly step out of the room, quietly closing the door.")
                    typingPrint("\nYou choose to continue down the long corridor ahead of you.") 
                    print()     
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            # Display player's health after each encounter
            typingPrint(f"\nYour current health: {player.health}")
                
        elif encounter == 2:
            # Debris Encounter
            typingPrint("\nWalking down a long hallway, you see some debris blocking a doorway. Behind the debris you see a small shimmering lights.")
            typingPrint("\nYou turn to look down both sides of the hallway to see if there are any dangers awaiting you.")
            typingPrint("\nRubbing your hands together you begin to clear out the debris. You feel something lodged, you try again and still its lodged.")
            typingPrint("\nIts stuck, you will have to use a lot of strength to remove it.")
            print()
            while True:
                debris_encounter = input("Do you wish to try and dislodge the stuck debris? (y/n) ").lower()
                print()

                if debris_encounter == "y":
                    success = roll_for_success(player, 'strength')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou dig your heels down, using your whole body to lift the debris out of the way.")
                        typingPrint("\nYou lift the debris, plopping down next to the doorway, walking through the door you find a small room.")
                        typingPrint("\nIn the small you find a table and some old chairs. At the other end of the room you find another door.")
                        typingPrint("\nWalking through it you find a small corridor, leading to to your right. You step in, walking down a corridor once more.")
                        typingPrint("\nYou succeeded removing the debris!")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou dig your heels down, your stuggle to push the debris out of the way.")
                        typingPrint("\nYour foot slips and you fall down, the debris unmoved and now a sore bump on your behind.")
                        typingPrint("\nYou failed to remove the debris.")
                        typingPrint("\nYou took 10 damage!")
                        print()
                        player.take_damage(10)
                        failed_encounters += 1
                    break
                elif debris_encounter == "n":
                    typingPrint("\nYou turn, continuing down the corridor, deaming it not worth it to try and waste energy on debris.")
                    typingPrint("\nYou head down, hoping to find a way out sooner rather than later.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")

        elif encounter == 3:
            # Intricate Wall Encounter
            typingPrint("\nYou come up to a large wall with intricate designs. To the left you see buttons corresponding")
            typingPrint("\nto the designs on the walls. To your right in another long corridor.")
            typingPrint("\nYou deduce that the buttons when pressed in the correct order will reveal a hidden secret.")
            print()

            while True:
                intricate_wall_encounter = input("Would you like to try and solve the puzzle? (y/n) ").lower()
                print()

                if intricate_wall_encounter == "y":
                    success = roll_for_success(player, 'intelligence')
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
                        print()
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
                        typingPrint("\nYou took 50 damage!")
                        player.take_damage(50)
                        failed_encounters += 1
                        print()
                    break
                elif intricate_wall_encounter == "n":
                    typingPrint("\nYou turn from the wall, not wanting to risk the dangers.")
                    typingPrint("\nYou continue down the long corridor, hoping to find some sort of exit.")
                    typingPrint("\nIf not, at the very least something that wont test your intelligence.")
                    n_encounters += 1
                    print()
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")

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

            while True:
                alter_encounter = input("Would you like to kneel and pray? (y/n) ").lower()
                print()

                if alter_encounter == "y":
                    success = roll_for_success(player, 'faith')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou kneel before the alter, praying to the God above your head.")
                        typingPrint("\nYou feel a small ray of light hit the alter, a warm sensation inside.")
                        typingPrint("\nThe alter begins to rumble. As it rumbles a small golden chalice appears.")
                        typingPrint("\nTaking a sip of the liquid inside you feel warm and stronger.")
                        player.health_healed(50)
                        typingPrint("\nYour faith has proven you worthy!")
                        typingPrint("\nYou healed 50 Health Points!")
                        typingPrint("\nExiting the room, you find another long corridor.")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nNothing happens.")
                        typingPrint("\nYou stand and begin walking away, feeling as if the God is watching you.")
                        typingPrint("\nYour faith has failed you in your time of need.")
                        typingPrint("\nYou walk through the door and find another long corridor.")
                        print()
                        failed_encounters += 1
                    break
                elif alter_encounter == "n":
                    typingPrint("\nYou find a door on the other side of the room. You decide its best not to tempt")
                    typingPrint("\nany God or Devil or whatever rules this place.")
                    typingPrint("\nOpening the doors you find another corridor leading you down intp the path.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")

        elif encounter == 5:
        # Ogre Lair
            typingPrint("\nWalking down the corridor you find a large cave opening. Inside you feel")
            typingPrint("\na small gust of wind. It could be an exit or it could lead into danger.")
            typingPrint("\nVenturing in, you stumble across a large trunk sized arm. Following it to the body")
            typingPrint("\nyou find two large eyes peering back at you. The small gust of wind hitting you in the face.")
            typingPrint("\nAs you jump back the creature doesnt move, it appears to be asleep. Your hand reaches for your")
            typingPrint("\nDagger, sliding it out of it's sheath.")
            print()

            while True:
                ogre_encounter = input("Do you wish to fight the sleeping Ogre? (y/n) ").lower()
                print()

                if ogre_encounter == "y":
                    success = roll_for_success(player, 'strength')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou dash forwards, jumping into the air plunging your dagger deep into")
                        typingPrint("\nits neck, slicing down. The large orge roars in pain as it's suddenly awaken")
                        typingPrint("\nfrom it's slumber. You quickly dash fowards stabbing at its eye.")
                        typingPrint("\nA short battle ensues but you managed to put down the Ogre.")
                        typingPrint("\nYou took 20 damage!")
                        player.take_damage(20)
                        typingPrint("\nYou managed to kill the Ogre!")
                        typingPrint("\nWalking deeper into the cave you come across a door, pushing it open")
                        typingPrint("\nyou enter another long corridor. You chose to walk down it.")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou dash forwards, slashing the Ogre's neck. The cut was shallow.")
                        typingPrint("\nThe Ogre roars, awaken suddenly from its slumber. You quickly")
                        typingPrint("\n dash forwards again, stabbing it in its eye.")
                        typingPrint("\nA long battle ensues but you finally managed to put down the Ogre")
                        typingPrint("\nnot before taking some serious damage.")
                        typingPrint("\nYou failed to kill the Ogre quickly.")
                        typingPrint("\nYou took 70 damage!")
                        player.take_damage(70)
                        typingPrint("\nLimping to the back of the cave you come across a door.")
                        typingPrint("\nPushing it open, you enter another long corridor.")
                        typingPrint("\nYou chose to walk down it, hoping for an exit.")
                        print()
                        failed_encounters += 1
                    break
                elif ogre_encounter == "n":
                    typingPrint("\nYou slowly back up, walking back into the corridor.")
                    typingPrint("\nCarefully walking down the corridor before finding a safe distance")
                    typingPrint("\nto start running. 'How did an Ogre get there you think to yourself?' ")
                    typingPrint("\nas you continue down the corridor.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")

        elif encounter == 6:
        # Cells with skeletons
            typingPrint("\nFinding a door you open it to find some stairs leading down a dark stairway.")
            typingPrint("\nYou walk down the stairs and see a bunch of small empty metal cells.")
            typingPrint("\nLooking around you see the cells have a few skeletons but nothing more.")
            typingPrint("\nSuddenly the rattling of bones startles you.")
            typingPrint("\nSkeletons suddenly start arising from their dark slumber.")
            typingPrint("\nYou see as they begin to stand a door on the other side, it could be a way out.")
            print()

            while True:
                skeleton_encounter = input("Do you wish to fight them and reach the other side? (y/n) ").lower()
                print()

                if skeleton_encounter == "y":
                    success = roll_for_success(player, 'dexterity')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou brandish your dagger, rushing in and attacking the skeletons.")
                        typingPrint("\nYou dagger breaking the weakened skulls, and before long")
                        typingPrint("\nyou managed to defeat the skeletons but not before taking some hits.")
                        typingPrint("\nYou walk past the your broken boned enemies and walk up to the door.")
                        typingPrint("\nYou defeated the Skeletons!")
                        typingPrint("\nYou took 20 damage!")
                        player.take_damage(20)
                        typingPrint("\nPushing the door open you find yourself in another corridor. You ")
                        typingPrint("\nbeing walking down in hopes for an exit.")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou brandish your dagger, rushing in and attacking the skeletons.")
                        typingPrint("\nYour dagger stiking the Skeletons, but didnt manage to break their skulls.")
                        typingPrint("\nYour blade having not been as effective, you managed to strike one down.")
                        typingPrint("\nAfter a long battle you stand above your defeated enemies.")
                        typingPrint("\nYou took a good anount of damage, as you walk towards the doors.")
                        typingPrint("\nYou failed to defeat the Skeletons quickly enough.")
                        typingPrint("\nYou took 60 damage!")
                        player.take_damage(60)
                        typingPrint("\nPushing the door open you find yourself in another corridor. You ")
                        typingPrint("\nbeing walking down in hopes for an exit.")
                        print()
                        failed_encounters += 1
                    break
                elif skeleton_encounter == "n":
                    typingPrint("\nYou turn tail and run up the stairs. The rattling of bones chasing after you.")
                    typingPrint("\nReaching the top of the stairs you slam the door shut, locking it as the ")
                    typingPrint("\nSkeletons pound on the door. You sprint down the corridor not letting those ")
                    typingPrint("\nSkeletons find you if they break the door down.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")

        elif encounter == 7:
        # Maze
            typingPrint("\nYou walk pass a doorway before taking a few steps back.")
            typingPrint("\nYou cant believe your eyes, inside the room you see these large walls, ")
            typingPrint("\nwalls too large to see over but you see the ceiling so high above them.")
            typingPrint("\n'It's a Maze!' you think to yourself. Mazes tend to have an exit.")
            typingPrint("\nMaybe the exit will the way out. ")
            print()

            while True:
                maze_encounter = input("Do you chose to venture into the maze? (y/n) ").lower()
                print()

                if maze_encounter== "y":
                    success = roll_for_success(player, 'intelligence')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou walk around, using little markings to track where you've been and where you have left to go.")
                        typingPrint("\nAfter walking around for about an hour or so, you managed to find you way through this maze.")
                        typingPrint("\nYour tired legs drag you until you see a door at the other side of the room.")
                        typingPrint("\nYou run up to the door, you open it, finding a long corridor.")
                        typingPrint("\nNot wanting to return to the maze, you march on hoping for an exit.")
                        typingPrint("\nCongratulations! You beat the Maze!")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou walk for hours. The maze seeming unchanging yet you find yourself running in circles.")
                        typingPrint("\nThe large walls unable to share a general direction for you to walk into.")
                        typingPrint("\nYour legs grow tired, as you walked in circles for who knows how long.")
                        typingPrint("\nYour final time returning back to where you started you walk out, angered and tired.")
                        typingPrint("\nYou failed to conquer the Maze.")
                        print()
                        failed_encounters += 1
                    break
                elif maze_encounter== "n":
                    typingPrint("\nYou keep going, you have no time for a silly maze.")
                    typingPrint("\nYou keep walking down this endless corridor hoping for an exit.")
                    print()
                    n_encounters
                    break
                else:
                    print("Please enter 'y' or 'n'.")

        elif encounter == 8:
        # Invisible steps in the river
            typingPrint("\nYou come down a path with two directions. On the left is a normal corridor.")
            typingPrint("\nOn the right is a raging river.")
            typingPrint("\nNo sane person would choose to go through a raging river.")
            typingPrint("\nBefore you decided on your path you notice a door on the other side of the river.")
            typingPrint("\nIt could be the way out, you think to yourself.")
            typingPrint("\nWalking up to the river you notice a fish floppin on top of the water, stuck.")
            typingPrint("\nYou bravely take a step to where the fish and notice an invisible square above the water.")
            typingPrint("\nPushing the fish back into the water you notice it swim away, but more importantly")
            typingPrint("\nYou feel as if there is a path for you to come and cross the river.")
            print()

            while True:
                raging_river_encounter = input("Do you try and cross the raging river? (y/n) ").lower()
                print()

                if  raging_river_encounter == "y":
                    success = roll_for_success(player, 'faith')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou take a leap of faith. Jumping to where you feel is right.")
                        typingPrint("\nYou feel your feet hit each soild step as you continue to cross the river.")
                        typingPrint("\nYou eventually land on the other side of the river.")
                        typingPrint("\nOpening the door you find yourself in another long corridor.")
                        typingPrint("\nSuccess! You crossed the Raging River!")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou jump between the soild squares crossing the river.")
                        typingPrint("\nTaking a leap of faith you, splash into the water.")
                        typingPrint("\nThe raging river thrashes you around sending you down stream.")
                        typingPrint("\nYou fling your arms out of the water an catch a soild surface.")
                        typingPrint("\nLifting yourself up you, finding a long corridor ahead of you.")
                        typingPrint("\nYou failed to cross the Raging River.")
                        typingPrint("\nYou took 20 damage!")
                        print()
                        player.take_damage(20)
                        failed_encounters += 1
                    break
                elif raging_river_encounter == "n":
                    typingPrint("\nNo fool would cross a river that strong, you think ")
                    typingPrint("\nto yourself. You turn left continuing down the long corridor.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")

        elif encounter == 9:
        # Cultists
            typingPrint("\nYou notice a passageway on the right, poking your head around the door way")
            typingPrint("\nyou notice a group of hooded figures preforming a ritual.")
            typingPrint("\nThey seem distracted, and you notice a door on the other side of the room.")
            typingPrint("\nYou could take out the cultists and enter the other door, hoping for a way out.")
            print()

            while True:
                cultists_encounter = input("Do you wish to try and take out the cultists? (y/n) ").lower()
                print()

                if cultists_encounter == "y":
                    success = roll_for_success(player, 'faith')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou pray you can defeat these cultists, carefully tip toeing inside.")
                        typingPrint("\nYour prayers were heard, as you managed to stealthly take out each cultists ")
                        typingPrint("\nwithout injury. You dust yourslef off, and walk to the door, opening it and ")
                        typingPrint("\nseeing a long corridor in front of you. You continue down the path hoping for an exit.")
                        typingPrint("\nSuccess! You managed to beat the cultists!")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou make your way in, trying to stealthly take them out.")
                        typingPrint("\nYour prayers were turned away from you as they were quickly alerts.")
                        typingPrint("\nA sudden brawl rages and you managed to make it out alive but not before")
                        typingPrint("\ncatching cuts and bruises. You walk up to the door and find yourself in another corridor.")
                        typingPrint("\nYou took 40 damage!")
                        print()
                        player.take_damage(40)
                        failed_encounters += 1
                    break
                elif cultists_encounter == "n":
                    typingPrint("\nNo way, you would try and fight those scary hooded figures,")
                    typingPrint("\nYou think to yourself as you continue walking down the long corridor.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            typingPrint(f"\nYour current health: {player.health}")
                
        else:
        # The lone Commander Knight
            typingPrint("\nYou walk past a large arch way, inside you notice large stone pillars.")
            typingPrint("\nAt the other end of the room you notice a Lone Knight sitting on a throne.")
            typingPrint("\nHis blade pointed down, he looks to be resting or waiting, you cant tell which.")
            typingPrint("\nBehind him you noticed the slight image of a what could be a door.")
            typingPrint("\nHopefully this door will be a way out. Hopefully.")
            print()
            while True:
                lone_knight_encounter = input("Do you wish to enter the throne room, and challenge the knight? (y/n) ").lower()
                print()

                if lone_knight_encounter == "y":
                    success = roll_for_success(player, 'strength')
                    y_encounters += 1
                    if success:
                        typingPrint("\nYou ready your dagger, and walk up to the knight. He stands, readying his sword.")
                        typingPrint("\nYou dart toward each other, a flurry of calculated swings filling the empty space.")
                        typingPrint("\nEach swing was almost like a dance, one making a move and the other would react.")
                        typingPrint("\nOne misstep and it could be devestating. But you managed to land a critical strike.")
                        typingPrint("\nThe Lone Knight fell to his knees, his blade, barely holding him up.")
                        typingPrint("\nHe falls over and you noticed a small golden badge under his cape.")
                        typingPrint("\nIt read, Commander Knight. You managed to defeat a Commander Knight.")
                        typingPrint("\nYou walk behind the throne and noticed a door, you were right.")
                        typingPrint("\nWalking through the door, you find yourself in another corridor.")
                        typingPrint("\nCongratulations! You managed to defeat the Lone Commander Knight!")
                        print()
                        succeeded_encounters += 1
                    else:
                        typingPrint("\nYou dash forwards, you blades clashing. He clearly outclasses you in terms")
                        typingPrint("\nof combat experiences and skills. The fighting was hard, you felt overwhelmed but managed")
                        typingPrint("\nto somehow win. As his body falls before you, you breathe heavily. Dropping to your knees.")
                        typingPrint("\nThe battle left you with many wounds, you tended to. Walking behind the throne you see the door.")
                        typingPrint("\nWalking through it you find youself in another corridor.")
                        typingPrint("\nYou failed to kill the Lone Knight quickly.")
                        typingPrint("\nYou took 100 damage!")
                        print()
                        player.take_damage(100)
                        failed_encounters += 1
                    break
                elif lone_knight_encounter == "n":
                    typingPrint("\nYou are no fighter. You would rather keep walking then to have some sort")
                    typingPrint("\nof confrontation with someone in full metal armor.")
                    typingPrint("\nYou continue walking down the long corridor hoping you find a way out.")
                    print()
                    n_encounters += 1
                    break
                else:
                    print("Please enter 'y' or 'n'.") 
            typingPrint(f"\nYour current health: {player.health}")

        break
    print()
    print("Encounters completed!")
    print("Total successful encounters:", succeeded_encounters)
    print("Total failed encounters:", failed_encounters)
    print("Total encounters where the player chose to continue:", n_encounters)
    print("Total encounters where the player chose to attempt the encounter:", y_encounters)
    print()

# Function called Roll for Success to see if character will succeed in an action
def roll_for_success(character,required_stat):
   
    # Dictionary to map the stat value to the bonus
    stat_bonus = {10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3,17:3, 18:4, 19:4, 20:5}

    required_value = random.randint(1, 20)

    # Simulate a roll, for simplicity let's say it's between 1 and 20
    roll = random.randint(1, 20)
    #encounter_difficulty_roll = random.randomint(1,15)

    bonus = stat_bonus.get(getattr(character, required_stat), 0)

    # Showing what the player rolled and what was required
    print(f"Rolled: {roll}, Required: {required_value} Stat Bonus: +{bonus}")

    modified_roll = roll + bonus

    # Compare the roll to the required stat value
    if modified_roll >= required_value:
        print("Success!")
        return True
    else:
        print("Failed.")
        return False
        
        
def character_health(health, encounters_result):
    if health > 0:
        return encounters_result
    else:
        return "You Died", "Thank you for playing Fantasy Adventure!"

def clearScreen():
  os.system("clear")
    


if __name__ == "__main__":
    main()