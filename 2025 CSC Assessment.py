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
area_1 = {'title':"home", "description":"Starting point for user", "north": 0, "south": 2, "east": 0, "west": 0, "active": False}
area_2 = {'title':"bus stop", "description":"A bus stop, which doesn't appear to be in use", "north": 1, "south": 0, "east": 3, "west": 0, "active": False}
area_3 = {'title':"sign post", "description":"Can be inspected for directions", "north": 0, "south": 4, "east": 0, "west": 2, "active": False}
area_4 = {'title':"empty road", "description":"A road which seems to stretch forever", "north": 3, "south": 6, "east": 0, "west": 0, "active": False}
area_5 = {'title':"translators home", "descriptions":"The man who lives here can translate between English and Maori", "north": 0, "south": 8, "east": 6, "west": 0, "active": False}
area_6 = {'title':"market", "description":"Food market, navigation point", "north": 4, "south": 9, "east": 7, "west": 5, "active": False}
area_7 = {'title':"shop", "description":"Where goods can be purchased", "north": 0, "south": 0, "east": 0, "west": 0, "active": False}
area_8 = {'title':"native bush", "description":"Untamed native bush past the limits of town", "north": 5, "south": 0, "east": 9, "west": 0, "active": False}
area_9= {'title':"koro's house", "description":"Home to the player character's Grandfather", "North": 6, "South": 0, "East": 0, "West": 8, "active": False}
locations_list = [area_1, area_2, area_3, area_4, area_5, area_6, area_7, area_8, area_9]

# retreives sprites from the sprites folder
BCG_HOME = pygame.image.load(
    os.path.join('Sprites','home_screen.png')) #finds sprite by it's folder and name

#while program is running
while running:
    # check game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if it is identified that pygame has been quit
            running = False # stop & close program
    
    def home_funct():
        win.blit(BCG_HOME, (0, 0)) # place background

    def game_funct():
        win.blit(BCG_HOME, (0, 0)) # place background
        #if () == active:
    # updates screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

# close window
pygame.quit()