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

#while program is running
while running:
    # check game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if exit button is pressed
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