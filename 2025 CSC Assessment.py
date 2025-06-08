# Kaylee Douglas
# 2CSC

# import GUI
import pygame
import os

# set up GUI
pygame.init()
clock = pygame.time.Clock()
# win = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Korero : Play')
running = True

# set up areas
# each dictionary contains information for each area, including what is in each direction
# '0' means that there is no room accessable from that point in that direction.
area_1 = {'title':"home", "description":"a small farmhouse to the north of town", "north": 0, "south": 2, "east": 0, "west": 0, "active": False}
area_2 = {'title':"bus stop", "description":"a graffitied old bench. It doesn't appear to have been used for a long while.", "north": 1, "south": 0, "east": 3, "west": 0, "active": False}
area_3 = {'title':"sign post", "description":"Can be inspected for directions", "north": 0, "south": 4, "east": 0, "west": 2, "active": False}
area_4 = {'title':"empty road", "description":"A road which seems to stretch forever", "north": 3, "south": 6, "east": 0, "west": 0, "active": False}
area_5 = {'title':"translators home", "description":"The man who lives here can translate between English and Maori", "north": 0, "south": 8, "east": 6, "west": 0, "active": False}
area_6 = {'title':"market", "description":"Food market, navigation point", "north": 4, "south": 9, "east": 7, "west": 5, "active": False}
area_7 = {'title':"shop", "description":"Where goods can be purchased", "north": 0, "south": 0, "east": 0, "west": 6, "active": False}
area_8 = {'title':"native bush", "description":"Untamed native bush past the limits of town", "north": 5, "south": 0, "east": 9, "west": 0, "active": False}
area_9= {'title':"koro's house", "description":"Home to the player character's Grandfather", "north": 6, "south": 0, "east": 0, "west": 8, "active": False}
locations_list = {1:area_1, 2:area_2, 3:area_3, 4:area_4, 5:area_5, 6:area_6, 7:area_7, 8:area_8, 9:area_9}
# retreives sprites from the sprites folder
BCG_HOME = pygame.image.load(
    os.path.join('Sprites','home_screen.png')) #finds sprite by it's folder and name


#while program is running
while running:
    # check game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if it is identified that pygame has been quit
            running = False # stop & close program
    #startgame
    def startgame():
        print("Welcome, user, to Kōrero.")
        username = input("What is your name?")
        print(f"Nice to meet you, {username}.")

        begin = input('Would you like to start the game? (Yes/No)').strip().title()
    
        while begin not in ["Yes", "No"]:
            print("Please enter either 'Yes' or 'No'.")
            begin = input('Would you like to start the game? (Yes/No)').strip().title()

        if begin == "Yes":
            area_1["active"] = True
        elif begin == "No":
            print("Come back when you're ready.")
            quit()

    def travel():
        # Dictionary to map directions to their corresponding keys
        direction_map = {"North": "north","South": "south","East": "east","West": "west"}
        # Find the currently active area
        current_area = None
        for area in locations_list.values():
            if area["active"]:
                current_area = area
                break

        if current_area is None:
            print("No active area found. Something might be wrong.")
            return

        direction = input("What direction would you like to travel? ").strip().title()

        if direction in direction_map:
            next_area_number = current_area[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # Print movement
            
                current_area["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("No area is active - something is wrong.")
        else:
            print("Enter an actual direction - North, South, East, or West.")
    
    # area one
    if area_1["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
               
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
        print("Objective gained: find your Koro.")
        print("Travel south to leave your home and begin your journey.")
        print("You walk outside, ready to begin your journey.")
        travel()
        
    # area two
    if area_2["active"]:
        
        print(f"You find yourself at a {area_2['title']}, which could be more accuratly described as {area_2['description']}.")
        print("There doesn't appear to be anything to do here, but the road extends to the east.")
        travel() 

    # area three
    if area_3["active"]: 
        
        #anything occuring in area 4 happens here
        print('area_3')
        travel()
        
    # area four
    if area_4["active"]: 
        
        #anything occuring in area 4 happens here
        print('area four')
        travel()

    # area five
    if area_5["active"]:
        
        #anything occuring in area 2 happens here
        print('area five')
        travel()

    # area six
    if area_6["active"]:
        
        #anything occuring in area 6 happens here
        print("area six")
        travel()

    # area seven
    if area_7["active"]:
        
        #anything occuring in area 7 happens here
        print("area seven")
        travel()

    # area eight
    if area_8["active"]:
        
        #anything occuring in area 8 happens here
        print("area eight")
        travel()

    # area nine
    if area_9["active"]:
        
        #anything occuring in area 9 happens here
        print("area nine")
        travel()

    else:
        startgame()
    
    # win.blit(BCG_HOME, (0, 0)) # place background

    # updates screen
    #pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

# close window
pygame.quit()