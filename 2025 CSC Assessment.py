# Kaylee Douglas
# 2CSC

# import GUI
import pygame
import os

# set up GUI
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Korero : Play')
running = True

# set up areas
# each dictionary contains information for each area, including what is in each direction
# '0' means that there is no room accessable from that point in that direction.
area_1 = {'title':"home", "description":"Starting point for user", "north": 0, "south": 2, "east": 0, "west": 0, "active": True}
area_2 = {'title':"bus stop", "description":"A bus stop, which doesn't appear to be in use", "north": 1, "south": 0, "east": 3, "west": 0, "active": False}
area_3 = {'title':"sign post", "description":"Can be inspected for directions", "north": 0, "south": 4, "east": 0, "west": 2, "active": False}
area_4 = {'title':"empty road", "description":"A road which seems to stretch forever", "north": 3, "south": 6, "east": 0, "west": 0, "active": False}
area_5 = {'title':"translators home", "descriptions":"The man who lives here can translate between English and Maori", "north": 0, "south": 8, "east": 6, "west": 0, "active": False}
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
     # Dictionary to map directions to their corresponding keys
    direction_map = {"North": "north","South": "south","East": "east","West": "west"}
    
    # area one
    if area_1["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 1 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_1[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_1["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area two
    if area_2["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 2 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_2[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_2["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area three
    if area_3["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 4 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_3[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_3["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area four
    if area_4["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 4 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_4[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_4["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area five
    if area_5["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 2 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_5[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_5["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area six
    if area_6["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 6 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_6[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_6["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area seven
    if area_7["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 7 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_7[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_7["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area eight
    if area_8["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 8 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_8[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_8["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    # area nine
    if area_9["active"]: #Because value is a boolean, it isn't required to specify what you're checking for
        
        #anything occuring in area 9 happens here
        
        direction = input("What direction? ").title()
        if direction in direction_map:  # Check if user input is a valid direction
            next_area_number = area_9[direction_map[direction]]  # Get the corresponding area number

            if next_area_number > 0:  # Ensure valid movement
                next_area = locations_list[next_area_number]  # Find correct area dictionary
            
                print(f"Moving to: {next_area['title']}")  # print movement
            
                area_9["active"] = False  # Deactivate current area
                next_area["active"] = True  # Activate new area
            else:
                print("There are no areas this way.")
        else:
            print("Enter an actual direction.")
    
    
    # win.blit(BCG_HOME, (0, 0)) # place background

    # updates screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

# close window
pygame.quit()