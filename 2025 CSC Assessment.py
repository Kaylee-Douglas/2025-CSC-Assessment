# Kaylee Douglas
# 2CSC

# import GUI
import os
import random
import easygui
from easygui import *

# set up game
objective = "blank"
words = {"Māori1":"English1","Māori2":"English2","Māori3":"English3" }
random_item = random.choice(list(words.keys()))  # Selects a random key


# set up areas
# each dictionary contains information for each area, including what is in each direction
# '0' means that there is no room accessable from that point in that direction.
area_1 = {'title':"home", "description":"a small farmhouse to the north of town", "north": 0, "south": 2, "east": 0, "west": 0, "active": False}
area_2 = {'title':"bus stop", "description":"a graffitied old bench. It doesn't appear to have been used for a long while", "north": 1, "south": 0, "east": 3, "west": 0, "active": False}
area_3 = {'title':"sign post", "description":"a muddied board, displaying directions to multiple locations", "north": 0, "south": 4, "east": 0, "west": 2, "active": False}
area_4 = {'title':"empty road", "description":"A road which seems to stretch forever", "north": 3, "south": 6, "east": 0, "west": 0, "active": False}
area_5 = {'title':"translators neighbourhood", "description":"line of neat, regal brick houses with perfectly trimmed grass", "north": 0, "south": 8, "east": 6, "west": 0, "active": False}
area_6 = {'title':"market", "description":"a city of stalls engulfed in swarms of people trying to negotiate the best possible deal", "north": 4, "south": 9, "east": 7, "west": 5, "active": False}
area_7 = {'title':"shop", "description":"stoic old general store", "north": 0, "south": 0, "east": 0, "west": 6, "active": False}
area_8 = {'title':"native bush", "description":"wild and towering landscape made up of great ferns", "north": 5, "south": 0, "east": 9, "west": 0, "active": False}
area_9= {'title':"koro's house", "description":"Home to the player character's Grandfather", "north": 6, "south": 0, "east": 0, "west": 8, "active": False}
locations_list = {1:area_1, 2:area_2, 3:area_3, 4:area_4, 5:area_5, 6:area_6, 7:area_7, 8:area_8, 9:area_9}
# retreives sprites from the sprites folder


#start game
def startgame():
    global running
    print("Welcome, user, to Kōrero.")
    username = input("What is your name?")
    print(f"Nice to meet you, {username}.")

    begin = input('Would you like to start the game? (Yes/No)').strip().title()
    
    while begin not in ["Yes", "No"]:
        print("Please enter either 'Yes' or 'No'.")
        begin = input('Would you like to start the game? (Yes/No)').strip().title()

    if begin == "Yes":
        running = True
        area_1["active"] = True
    elif begin == "No":
        print("Come back when you're ready.")
        quit()
startgame()

#while program is running
while running:
    #move between areas
    def travel():
        # Dictionary to map directions to their corresponding keys
        direction_map = {"North": "north","South": "south","East": "east","West": "west"}
        # Finds the currently active area by checking every area in the area list
        current_area = None 
        for area in locations_list.values(): 
            if area["active"]:
                current_area = area
                break # immediatly stops the loop, meaning once it comes across an active area it will stop checking.

        if current_area is None: # if no areas are active
            print("No areas are active. Something is probably broken.") # inform user
            return # immediatly exits the 'travel()' function

        direction = input("What direction would you like to travel? ").strip().title()

        if direction in direction_map:
            next_area_number = current_area[direction_map[direction]]  # Get the corresponding area number by searching the area's dictionary

            if next_area_number > 0:  # If there is something in this direction
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # Print movement so user knows what's happening
            
                current_area["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("Hm, there doesn't appear to be anything this way. Maybe try another direction?")
                travel()
        else:
            print("Enter an actual direction - North, South, East, or West.") # if this occurs user entered an invalid input.
            travel()
    
    # area one
    if area_1["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        if objective == "blank":
            print(f"You wake up in {area_1['description']}. This place is familar to you - it's your {area_1['title']}.")
            print("'Username!'") # this text will be a different color.
            print("Another familar sound - it's your mother. She enters the room, looking worried.")
            print("There you are, Username. I promised your Koro that i'd bring him some things from the shop today, but i've forgotten what they were.") #color
            acceptquest = input("Could you stop by and ask him? (Yes/No)").strip().title()
            while acceptquest not in ["Yes", "No"]:
                print("Please enter either 'Yes' or 'No'.")
                acceptquest = input("Could you stop by and ask him? (Yes/No)").strip().title()

            if acceptquest == "Yes":
                print("yay!")
            elif acceptquest == "No":
                confirm = input("Are you sure? This option will end the game. (Yes/No)").strip().title()
                while confirm not in ["Yes", "No"]:
                    print("Please enter either yes or no")
                    confirm = input("Are you sure you don't want to help? (Yes/No)")
                if confirm == "Yes":
                    quit()
            objective = "find koro"
            print("Objective gained: find your Koro.")
            print("Travel south to leave your home and begin your journey.")
            print("You walk outside, ready to begin your journey.")
            travel()
        else:
            print("What are you doing here? Head south and follow the road.")
            travel()
        
    # area two
    if area_2["active"]:
        
        print(f"You find yourself at a {area_2['title']}, which could be more accuratly described as {area_2['description']}.")
        print("There doesn't appear to be anything to do here, but the road extends to the east.")
        travel() 

    # area three
    if area_3["active"]: 
        
        #anything occuring in area 4 happens here
        print(f"Your travels brings you to {area_3['description']}. This {area_3['title']} could be useful!")
        inspect = input('Inspect? (Yes/No)').strip().title()
        while inspect not in ["Yes", "No"]:
            print("Please enter either 'Yes' or 'No'.")
            inspect = input("Inspect (Yes/No)").strip().title()
        if inspect == "Yes":
            print('''The sign post contains some useful information! 
            To get to the shop you must continue south to the market, then travel east. 
            To get to your Koro's neighbourhood, you must travel directly south. 
            Another neighbourhood can be found to the west of the market.''')
            travel()
        elif inspect == "No":
            print("You ignore the sign post. The road extends southwards before you.")
            travel()
        
    # area four
    if area_4["active"]: 
        
        print(f'''Before you lies {area_4["description"]}. This {area_4['title']} is non descript - but in the distance to the south, you can clearly make out the shapes of a town.''')
        travel()

    # area five

    if area_5["active"]:
        print(f"You find yourself in front of a {area_5['description']}.")
        if objective == "find koro":
            print("This doesn't seem like Koro's neighbourhood - you can't spot his house. You should keep looking.")
            travel()
        if objective == "find shop":
            print("Huh. No shops here. You should keep looking. The same pair of friends are chatting by the gate.")
            talk = input("Do you want to talk to them again? (Yes/No)").strip().title()
            while talk not in ["Yes", "No"]:
                print("Please enter either 'Yes' or 'No'.")
                talk = input("Do you want to talk to them again? (Yes/No)")
            if talk == "Yes":
                print("Once again, the pair welcome you to their conversation with open arms.")
                ask = input("Ask them to translate something? (Yes/No)").strip().title()
                while ask not in ["Yes", "No"]:
                    print("Please enter either 'Yes' or 'No'.")
                    ask = input("Ask them to translate something? (Yes/No)").strip().title()
                if ask == "Yes":
                    print("They agree once again, and ask what you'd like to learn.")
                word_to_translate = input("What word would you like to translate?").strip().title()
                while word_to_translate not in words:
                    if word_to_translate.lower() == "exit":  # Check if user wants to exit
                        print("You politely excuse yourself from the conversation.")
                        travel()  # Calls the travel function to let the user move
                        break  # Exits the loop

                    print("Try asking the word Koro told you. Make sure you remember macrons - if you need to return and ask him again, type 'exit'.")
                    word_to_translate = input("What word would you like to translate?").strip().title()

                if word_to_translate in words:  # Ensures translation only prints if a valid word is entered
                    print(f"Oh, sure! {word_to_translate} means {words[word_to_translate]}.")
                    print(f"Perfect! Now you know what to buy from the store - and what {word_to_translate} means. You thank the pair, and head off.")
                    travel()
                if ask == "No":
                    print("You excuse yourself from the conversation, deciding to continue your journey.")
                    travel()
            if talk == "No":
                print("Been there, done that - you decide to carry on.")
                travel()
        if objective == "translate":
            print("This place seems promising - a couple of friends sit on one of the lawns, speaking in a mix of English and Māori.")
            approach = input("Approach them? (Yes/No)").strip().title()
            while approach not in ["Yes", "No"]:
                print("Please enter either 'Yes' or 'No'.")
                approach = input("Approach them? (Yes/No)").strip().title()
            if approach == "Yes":
                print('You approach the pair, and one of them calls a greeting.')
                print('Kia Ora!') #text colored because someone is speaking.
                ask = input("They seem nice. Do you want to ask them for help? (Yes/No)").strip().title()
                while ask not in ["Yes", "No"]:
                    print("Please enter either 'Yes' or 'No'.")
                    ask = input("Ask them for help? (Yes/No)").strip().title()
                if ask == "Yes":
                    print("You strike up conversation with the pair, and they agree to translate for you.")
                    ask = input("Ask them to translate something? (Yes/No)").strip().title()
                    while ask not in ["Yes", "No"]:
                        print("Please enter either 'Yes' or 'No'.")
                        talk = input("Ask them to translate something? (Yes/No)").strip().title()
                    if ask == "Yes":
                        print("They agree once again, and ask what you'd like to learn.")
                    word_to_translate = input("What word would you like to translate?").strip().title()
                    while word_to_translate not in words:
                        if word_to_translate.lower() == "exit":  # Check if user wants to exit
                            print("You politely excuse yourself from the conversation.")
                            travel()  # Calls the travel function to let the user move
                            break  # Exits the loop

                        print("Try asking the word Koro told you. Make sure you remember macrons - if you need to return and ask him again, type 'exit'.")
                        word_to_translate = input("What word would you like to translate?").strip().title()

                    if word_to_translate in words:  # Ensures translation only prints if a valid word is entered
                        print(f"Oh, sure! {word_to_translate} means {words[word_to_translate]}.")
                        print(f"Perfect! Now you know what to buy from the store - and what {word_to_translate} means. You thank the pair, and head off.")
                        objective = 'find shop'
                        travel()
                    if ask == "No":
                        print("You excuse yourself from the conversation, deciding to continue your journey.")
                        travel()

    # area six
    if area_6["active"]:
        
        #anything occuring in area 6 happens here
        print(f"Finally, you've made your way into a more populated area. The {area_6['title']}, {area_6['description']}")
        if inspect == "Yes":
            print("This must be the market mentioned by the signpost.")
            if objective == "find koro" or "return":
                print("It said that Koro's house was south.")
            if objective == "find shop":
                print("It said that the shop was east.")
            if objective == "translate":
                print("It mentioned a neighbourhood to the west - perhaps someone there can translate?")
        travel()

    # area seven
    if area_7["active"]:
        print(f"This {area_7['description']} must be the {area_7['title']}. You can buy the things Koro needs here.")

        if objective == "find koro":
            print("Hm. You don't know what he wants - better go ask him, then come back.")
            travel()

        elif objective == "find shop":
            print("You make your way over to the counter, and are greeted by a tired-looking salesperson.")
        
            while True:  # Loop until user enters the correct item or exits
                ask = input("Hi. What can I get for you?").strip().title()
            
                if ask.lower() == "exit":  # Allows user to exit the interaction
                    print("You decide to leave and return later.")
                    travel()
                    break
            
                if ask == {words[random_item]}:
                    print(f'Oh, a {words[random_item]}?')
                    print('She nods, and takes your cash for the item. Better return to Koro and give this to him!')
                    objective = 'return'
                    travel()
                    break  # Exit loop after successful transaction

                else:
                    print("Be careful what you ask for - remember, you want to buy the item Koro wanted. If you need to ask him again, type 'exit'.")
        else:
            travel()


    # area eight
    if area_8["active"]:
        
        print(f"In between two modern neighourhoods, a {area_8['description']} lies. {area_8['title']} seems to stretch endlessly into the south and west.")
        travel()

    # area nine
    if area_9["active"]:
        if objective == 'find koro':
            print("In front of you is a familar building - Koro's house.")
            print("You knock on the door and are greeted by a welcoming smile.")
            print("You exchange words of greeting and he ushers you inside.")
            ask = input('Ask him what he needs from the shop? (Yes/No)').strip().title()
            while ask not in ["Yes", "No"]:
                print("Please enter either 'Yes' or 'No'.")
                ask = input("Ask Koro what he needs from the shop? (Yes/No)").strip().title()
            if ask == "Yes":
                print(f"Oh, thank you! I need - uh, {random_item}. I don't know the English name - don't worry, i'm sure you can find someone to help! West of the market, maybe.")
                print('His smile unwavering, Koro hands you the money needed for the purchase and you head away.')
                objective = 'translate'
                travel()
            elif ask == "No":
                print("You maintain polite conversation, before turning to leave. You can always come back later to ask!")
                travel()
        elif objective == 'translate':
            print(f'Forgot what I asked for already? It was {random_item}.')
            print("He shuts the door - huh. Guess he didn't feel like talking.")
            travel()
        elif objective == 'find shop':
            print("Oh, you found the name? Now head to the shop and bring it back!")
            print("He shuts the door - huh. Guess he didn't feel like talking.")
            travel()
        elif objective == 'return':
            print(f"You knock on Koro's door again, and hand him the {random_item}, and he thanks you.")
            words.pop(random_item)
            ask = input('Ask him if he needs anything else (Yes/No)').strip().title()
            while ask not in ["Yes", "No"]:
                print("Please enter either 'Yes' or 'No'.")
                ask = input("Ask him if he needs anything else? (Yes/No)").strip().title()
            if ask == "Yes":
                random_item = random.choice(list(words.keys()))  # Selects a new random key
                print(f"Oh, thank you! I need - uh, {random_item}. I don't know the English name - don't worry, i'm sure you can find someone to help! West of the market, maybe.")
                print('His smile unwavering, Koro hands you the money needed for the purchase and you head away.')
                objective = 'translate'
                travel()
            elif ask == "No":
                print("No worries - You've completed your objective and won the game!")
                print("Thank you for playing.")
                quit()
