# Kaylee Douglas
# 2CSC

# import GUI
#pip install pygame
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
home = {'no':"1", "description":"Starting point for user", "north":"0", "south":"2", "east":"0", "west":"0"}
bus_stop = {'no':"2", "description":"A bus stop, which doesn't appear to be in use", "north":"1", "south":"0", "east":"3", "west":"0"}
sign_posts = {'no':"3", "description":"Can be inspected for directions", "north":"0", "south":"4", "east":"0", "west":"2"}
empty_road = {'no':"4", "description":"A road which seems to stretch forever", "north":"3", "south":"6", "east":"0", "west":"0"}
translators_home = {'no':"5", "descriptions":"The man who lives here can translate between English and Maori", "north":"0", "south":"8", "east":"6", "west":"0"}
market = {'no':"6", "description":"Food market, navigation point", "north":"4", "south":"9", "east":"7", "west":"5"}
shop = {'no':"7", "description":"Where goods can be purchased", "north":"0", "south":"0", "east":"0", "west":"6"}
native_bush = {'no':"8", "description":"Untamed native bush past the limits of town", "north":"5", "south":"0", "east":"9", "west":"0"}
koro_house = {'no':"9", "description":"Home to the player character's Grandfather", "North":"6", "South":"0", "East":"0", "West":"8"}

#while program is running
while running:
    # check game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if it is identified that pygame has been quit
            running = False # stop & close program
   
    #Debug
    x, y = pygame.mouse.get_pos() #get mouse position
    #print mouse position
    # print(x, y)

    # render game
    win.fill("purple") # blank screen - this will be removed

    # updates screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

# close window
pygame.quit()