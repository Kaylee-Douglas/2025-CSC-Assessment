# Kaylee Douglas
# 2CSC

# import models and GUIs used within the code
import os
import random
import easygui
from easygui import *
# set up variables for game
objective = "blank" #set initial objective
words = {"Maori1":"English1","Maori2":"English2","Maori3":"English3" } #the objects that Koro can request and their english translations
random_item = random.choice(list(words.keys()))  # Selects a random key from the words dictionary

# set up areas
# each dictionary contains information for each area.
# 'title' and 'description' describe the area
# 'north', 'south', 'east' and 'west' store whether there is an area in that direction. '0' means there is no area, otherwise numbers reflect area number.
# 'active' states whether the user is currently in the area

area_1 = {'title':"home", "description":"a small farmhouse to the north of town", "north": 0, "south": 2, "east": 0, "west": 0, "active": False}
area_2 = {'title':"bus stop", "description":"a graffitied old bench. It doesn't appear to have been used for a long while", "north": 1, "south": 0, "east": 3, "west": 0, "active": False}
area_3 = {'title':"sign post", "description":"a muddied board, displaying directions to multiple locations", "north": 0, "south": 4, "east": 0, "west": 2, "active": False}
area_4 = {'title':"empty road", "description":"A road which seems to stretch forever", "north": 3, "south": 6, "east": 0, "west": 0, "active": False}
area_5 = {'title':"translators neighbourhood", "description":"line of neat, regal brick houses with perfectly trimmed grass", "north": 0, "south": 8, "east": 6, "west": 0, "active": False}
area_6 = {'title':"market", "description":"a city of stalls engulfed in swarms of people trying to negotiate the best possible deal", "north": 4, "south": 9, "east": 7, "west": 5, "active": True}
area_7 = {'title':"shop", "description":"stoic old general store", "north": 0, "south": 0, "east": 0, "west": 6, "active": False}
area_8 = {'title':"native bush", "description":"wild and towering landscape made up of great ferns", "north": 5, "south": 0, "east": 9, "west": 0, "active": False}
area_9= {'title':"koro's house", "description":"Home to the player character's Grandfather", "north": 6, "south": 0, "east": 0, "west": 8, "active": False}
# Store each area with it's corresponding number as a key
locations_list = {1:area_1, 2:area_2, 3:area_3, 4:area_4, 5:area_5, 6:area_6, 7:area_7, 8:area_8, 9:area_9}

#start game
def startgame(): # create the function 'startgame' which holds the inital set up for the user.
    global username # apply the variable 'global' which is defined in this function, to the rest of the program.
    global running
    msgbox("Welcome, user, to Kōrero.") # print welcome message
    username = enterbox("What is your name?").title() # ask user to input name
    msgbox(f"Nice to meet you, {username}.") # return user's inputed name

    begin = enterbox('Would you like to start the game? (Yes/No)').strip().title() # ask user to type either yes or no to state whether they want to start. .strip removes trailing letters, .title changes cases.
    
    while begin not in ["Yes", "No"]: # if the user entered something that was not Yes or No
        msgbox("Please enter either 'Yes' or 'No'.") # ask them to make a valid entry
        begin = enterbox('Would you like to start the game? (Yes/No)').strip().title()

    if begin == "Yes": # if the user entered yes
        running = True # start main game loop
        area_1["active"] = True # place user in area one.
    elif begin == "No": # if the user entered no
        msgbox("Come back when you're ready.") 
        quit() # close program
startgame() # Call startgame function. this happens once, at the start of the game.

#while program is running
while running:
    #move between areas
    def travel(): # create the function 'travel' which allows the user to move between areas when called
        # Connects map directions to their corresponding dictionary keys
        direction_map = {"North": "north","South": "south","East": "east","West": "west"}
        # Finds the currently active area by checking every area in the area list
        current_area = None 
        for area in locations_list.values(): # loops for every area in locations_list dictionary
            if area["active"]: # until it finds an active area
                current_area = area # then defines this area as the current area
                break # stops running the loop, as only one area will be active at once so continuing after one if found isn't needed.

        if current_area is None: # if no areas are active
            msgbox("No areas are active. Something is probably broken.") # inform user
            return # immediatly exits the 'travel()' function

        direction = enterbox("What direction would you like to travel? (North/South/East/West)").strip().title() # ask user where they want to go

        if direction in direction_map: # if the direction exists
            next_area_number = current_area[direction_map[direction]]  # Get the corresponding area number by searching the area's dictionary

            if next_area_number > 0:  # If there is something in this direction
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                #msgbox(f"Moving to: {next_area['title']}")
            
                current_area["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else: # if there is nothing in the direction entered
                msgbox("Hm, there doesn't appear to be anything this way. Maybe try another direction?") # ask user.
                travel()
        else: # if the entered direction does not exist
            msgbox("Enter an actual direction - North, South, East, or West.") # ask user to enter a valid input
            travel()
    
    # area one
    if area_1["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        if objective == "blank": # if the users current goal is undefined
            msgbox(f"You wake up in {area_1['description']}. This place is familar to you - it's your {area_1['title']}.") # print area description
            msgbox(f"'{username}!'") # print speech
            msgbox("Another familar sound - it's your mother. She enters the room, looking worried.") # print text
            msgbox(f"'There you are, {username}. I promised your Koro that i'd bring him some things from the shop today, but i've forgotten what they were.'") #color
            acceptquest = enterbox("Could you stop by and ask him? (Yes/No)").strip().title() # asks user if they will accept the quest. .strip removes trailing letters and .title capitalises first letter.
            while acceptquest not in ["Yes", "No"]: # while user has not entered yes or no
                msgbox("Please enter either 'Yes' or 'No'.")
                acceptquest = enterbox("Could you stop by and ask him? (Yes/No)").strip().title() # re ask question
            if acceptquest == "No": # if the user does not accept the quest
                confirm = enterbox("Are you sure? This option will end the game. (Yes/No)").strip().title() # ask for confirmation
                while confirm not in ["Yes", "No"]: # while user has not entered yes or no
                    msgbox("Please enter either yes or no")
                    confirm = enterbox("Are you sure you don't want to help? (Yes/No)") # ask again
                if confirm == "Yes": # if user confirms that they want to quit
                    quit() # quit code.
            objective = "find koro" # set 'objective'
            # print instructions
            msgbox("Objective gained: find your Koro.") 
            msgbox("You walk outside, Ready to travel south and begin your journey.")
            travel()
        else: # if you return to the house after receiving the objective
            msgbox("'What are you doing here? Head south and follow the road.'")
            travel()
        
    # area two
    if area_2["active"]: # if 'active' key in area_2 dictionary is true (if this area is active)
        
        msgbox(f"You find yourself at a {area_2['title']}, which could be more accuratly described as {area_2['description']}.") # print description
        msgbox("There doesn't appear to be anything to do here, but the road extends to the east.") # tell direction
        travel() # call travel function to allow user to continue

    # area three
    if area_3["active"]: # if 'active' key in area_3 dictionary is true (if this area is active)

        msgbox(f"Your travels brings you to {area_3['description']}. This {area_3['title']} could be useful!") # print area description
        inspect = enterbox(f"Inspect {area_3['title']}? (Yes/No)").strip().title() # ask if user wants to view signpost
        while inspect not in ["Yes", "No"]: # while user hasn't entered yes or no
            msgbox("Please enter either 'Yes' or 'No'.") 
            inspect = enterbox("Inspect (Yes/No)").strip().title() # re ask question
        if inspect == "Yes": # if user entered yes
            msgbox('''The sign post contains some useful information! 
            To get to the shop you must continue south to the market, then travel east. 
            To get to your Koro's neighbourhood, you must travel directly south. 
            Another neighbourhood can be found to the west of the market.''') # print info
            travel() # call travel function, which allows user to move.
        elif inspect == "No": # if user entered no
            msgbox("You ignore the sign post. The road extends southwards before you.")
            travel() # call travel function, which allows user to move.
        
    # area four
    if area_4["active"]: # if 'active' key in area_4 dictionary is true (if this area is active)
        
        msgbox(f'''Before you lies {area_4["description"]}. This {area_4['title']} is non descript - but in the distance to the south, you can clearly make out the shapes of a town.''') #print area description
        travel() # call travel function, which allows user to move.

    # area five
    if area_5["active"]: # if 'active' key in area_5 dictionary is true (if this area is active)
        msgbox(f"You find yourself in front of a {area_5['description']}.") # print area description
        if objective == "find koro": # if user's current objective is to find koro
            msgbox("This doesn't seem like Koro's neighbourhood - you can't spot his house. You should keep looking.") # prompt for user
            travel() # call travel function, allowing user to travel.
        if objective == "find shop": # if user's current objective is to find the shop
            msgbox("Huh. No shops here. You should keep looking. The same pair of friends are chatting by the gate.") 
            talk = enterbox("Do you want to talk to them again? (Yes/No)").strip().title() # allows interaction with the translators again - this may be useful if user has forgotten translation.
            while talk not in ["Yes", "No"]: # while the user has not entered yes or no
                msgbox("Please enter either 'Yes' or 'No'.")
                talk = enterbox("Do you want to talk to them again? (Yes/No)") # re ask question
            if talk == "Yes": # if the user entered yes
                msgbox("Once again, the pair welcome you to their conversation with open arms.")
                ask = enterbox("Ask them to translate something? (Yes/No)").strip().title()
                while ask not in ["Yes", "No"]: # while the user has not entered yes or no
                    msgbox("Please enter either 'Yes' or 'No'.")
                    ask = enterbox("Ask them to translate something? (Yes/No)").strip().title() # re ask question
                if ask == "Yes":
                    msgbox("They agree once again, and ask what you'd like to learn.")
                word_to_translate = enterbox("What word would you like to translate?").strip().title()
                while word_to_translate not in words: # while the user has not entered yes or no
                    if word_to_translate.lower() == "exit":  # Check if user wants to exit
                        msgbox("You politely excuse yourself from the conversation.")
                        travel()  # Calls the travel function to let the user move
                        break  # Exits the loop

                    msgbox("Try asking the word Koro told you. Make sure you remember macrons - if you need to return and ask him again, type 'exit'.")
                    word_to_translate = enterbox("What word would you like to translate?").strip().title()

                if word_to_translate in words:  # Ensures translation only prints if a valid word is entered
                    msgbox(f"Oh, sure! {word_to_translate} means {words[word_to_translate]}.")
                    msgbox(f"Perfect! Now you know what to buy from the store - and what {word_to_translate} means. You thank the pair, and head off.")
                    travel()
                if ask == "No":
                    msgbox("You excuse yourself from the conversation, deciding to continue your journey.")
                    travel()
            if talk == "No":
                msgbox("Been there, done that - you decide to carry on.")
                travel()
        if objective == "translate":
            msgbox("This place seems promising - a couple of friends sit on one of the lawns, speaking in a mix of English and Māori.")
            approach = enterbox("Approach them? (Yes/No)").strip().title()
            while approach not in ["Yes", "No"]:
                msgbox("Please enter either 'Yes' or 'No'.")
                approach = enterbox("Approach them? (Yes/No)").strip().title()
            if approach == "Yes":
                msgbox('You approach the pair, and one of them calls a greeting.')
                msgbox('Kia Ora!') #text colored because someone is speaking.
                ask = enterbox("They seem nice. Do you want to ask them for help? (Yes/No)").strip().title()
                while ask not in ["Yes", "No"]:
                    msgbox("Please enter either 'Yes' or 'No'.")
                    ask = enterbox("Ask them for help? (Yes/No)").strip().title()
                if ask == "Yes":
                    msgbox("You strike up conversation with the pair, and they agree to translate for you.")
                    ask = enterbox("Ask them to translate something? (Yes/No)").strip().title()
                    while ask not in ["Yes", "No"]:
                        msgbox("Please enter either 'Yes' or 'No'.")
                        ask = enterbox("Ask them to translate something? (Yes/No)").strip().title()
                    if ask == "Yes":
                        msgbox("They agree once again, and ask what you'd like to learn.")
                    word_to_translate = enterbox("What word would you like to translate?").strip().title()
                    while word_to_translate not in words:
                        if word_to_translate.lower() == "exit":  # Check if user wants to exit
                            msgbox("You politely excuse yourself from the conversation.")
                            travel()  # Calls the travel function to let the user move
                            break  # Exits the loop

                        msgbox("Try asking the word Koro told you. Make sure you remember macrons - if you need to return and ask him again, type 'exit'.")
                        word_to_translate = enterbox("What word would you like to translate?").strip().title()

                    if word_to_translate in words:  # Ensures translation only prints if a valid word is entered
                        msgbox(f"Oh, sure! {word_to_translate} means {words[word_to_translate]}.")
                        msgbox(f"Perfect! Now you know what to buy from the store - and what {word_to_translate} means. You thank the pair, and head off.")
                        objective = 'find shop'
                        travel()
                    if ask == "No":
                        msgbox("You excuse yourself from the conversation, deciding to continue your journey.")
                        travel()
        travel()

    # area six
    if area_6["active"]: # if 'active' key in area_6 dictionary is true (if this area is active)
        
        msgbox(f"Finally, you've made your way into a more populated area. The {area_6['title']}, {area_6['description']}") # print area description
        if inspect == "Yes": # if user inspected the sign post earlier
            msgbox("This must be the market mentioned by the signpost.") # prompt remembered information from sign post
            # find objective and give relevant information from the sign post 
            if objective == "find koro" or "return": 
                msgbox("It said that Koro's house was south.")
            if objective == "find shop":
                msgbox("It said that the shop was east.")
            if objective == "translate":
                msgbox("It mentioned a neighbourhood to the west - perhaps someone there can translate?")
        travel()

    # area seven
    if area_7["active"]: # if 'active' key in area_7 dictionary is true (if this area is active)

        msgbox(f"This {area_7['description']} must be the {area_7['title']}. You can buy the things Koro needs here.") # print area description

        if objective == "find koro": # if current objective is to find koro
            msgbox("Hm. You don't know what he wants - better go ask him, then come back.") 
            travel() # allow user to travel again

        elif objective == "find shop": # if current objective is find shop
            
            # start shop interaction.
            msgbox("You make your way over to the counter, and are greeted by a tired-looking salesperson.")
            while True:  # Loop until user enters the correct item or exits
                ask = enterbox("Hi. What can I get for you?").strip().title()
            
                if ask.lower() == "exit":  # Allows user to exit the interaction
                    msgbox("You decide to leave and return later.")
                    travel()
                    break
            
                if ask == words[random_item]: # check if user input is the thing Koro needs
                    msgbox("Oh, a "+words[random_item]+'!') # print confirmation
                    msgbox('She nods, and takes your cash for the item. Better return to Koro and give this to him!') 
                    objective = 'return' # change objective to return, because item has been purchased.
                    travel() # calls travel function, allowing user to move.
                    break  # Exit loop after successful transaction

                else: # if user entered something other than what koro wanted
                    msgbox("Be careful what you ask for - remember, you want to buy the item Koro wanted. If you need to ask him again, type 'exit'.")
        else:
            travel()


    # area eight
    if area_8["active"]: # if 'active' key in area_8 dictionary is true (if this area is active)
        
        msgbox(f"In between two modern neighourhoods, a {area_8['description']} lies. {area_8['title']} seems to stretch endlessly into the south and west.") #print description
        travel() # call travel function, which allows user to move

    # area nine
    if area_9["active"]: # if 'active' key in area_9 dictionary is true (if this area is active)
        if objective == 'find koro':
            msgbox("In front of you is a familar building - Koro's house.")
            msgbox("You knock on the door and are greeted by a welcoming smile.")
            msgbox("You exchange words of greeting and he ushers you inside.")
            ask = enterbox('Ask him what he needs from the shop? (Yes/No)').strip().title()
            while ask not in ["Yes", "No"]: # loop until user has entered yes or no
                msgbox("Please enter either 'Yes' or 'No'.")
                ask = enterbox("Ask Koro what he needs from the shop? (Yes/No)").strip().title() # re ask question
            if ask == "Yes":
                msgbox(f"Oh, thank you! I need - uh, {random_item}. I don't know the English name - don't worry, i'm sure you can find someone to help! West of the market, maybe.")
                msgbox('His smile unwavering, Koro hands you the money needed for the purchase and you head away.')
                objective = 'translate' # change user objective to translate
                travel() # call travel function, allowing user to move.
            elif ask == "No":
                msgbox("You maintain polite conversation, before turning to leave. You can always come back later to ask!")
                travel() # call travel function, allowing user to move.
        elif objective == 'translate': # if current objective is to translate
            msgbox(f'Forgot what I asked for already? It was {random_item}. Find someone to translate west of the market.') # remind user of what is needed.
            msgbox("He shuts the door - huh. Guess he didn't feel like talking.")
            travel() # call travel function, allowing user to move.
        elif objective == 'find shop': # if objective is to find shop
            msgbox("Oh, you found the name? Now head to the shop and bring it back!") # remind user what they need to be doing
            msgbox("He shuts the door - huh. Guess he didn't feel like talking.")
            travel() # call travel function, allowing user to move.
        elif objective == 'return': # if objective is to return to koro
            msgbox(f"You knock on Koro's door again, and hand him the {random_item}, and he thanks you.")
            words.pop(random_item) # remove retrieved item from items dictionary
            ask = enterbox('Ask him if he needs anything else (Yes/No)').strip().title()
            while ask not in ["Yes", "No"]:
                msgbox("Please enter either 'Yes' or 'No'.")
                ask = enterbox("Ask him if he needs anything else? (Yes/No)").strip().title()
            if ask == "Yes":
                random_item = random.choice(list(words.keys()))  # Selects a new random item (by selecting a key from list)
                msgbox(f"Oh, thank you! I need - uh, {random_item}. I don't know the English name - don't worry, i'm sure you can find someone to help! West of the market, maybe.")
                msgbox('His smile unwavering, Koro hands you the money needed for the purchase and you head away.')
                objective = 'translate'
                travel()
            elif ask == "No":
                msgbox("No worries - You've completed your objective and won the game!")
                msgbox("Thank you for playing.")
                quit() # quit code.
