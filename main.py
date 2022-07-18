#Built-in Modules *************************************************************

import os, pygame



#Custom Modules ***************************************************************

import Data, Event, Image



#pygame Initialization ********************************************************

pygame.init()



#Basic Variables **************************************************************

CAPTION = "Tetris -by.LCG"
ICON = Image.load("images\icon.png")
RESOLUTION = (1440, 810)
FPS = 60
MAGNIFYING_RATE = 1



#Window Setting ***************************************************************

WINDOW = pygame.display
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode(RESOLUTION)
pygame.time.Clock().tick(FPS)



#Global Variables *************************************************************

GAME_STATUS = Event.starting



#Main Loop ********************************************************************

RUNNING = True
while RUNNING:
    pass

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            Event.ask_quit.func()