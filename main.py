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

GAME_STATUS = Event.undefined
PAUSED = False
QUIT_MENU_POPPED = False



#Functions ********************************************************************

def render_pause_filter() -> None:
    pass

def ask_quit() -> None:
    global RUNNING
    WINDOW.quit()
    RUNNING = False



#Main Loop ********************************************************************

RUNNING = True
while RUNNING:
    SCREEN.fill((0, 0, 0))

    GAME_STATUS.render_background(SCREEN)

    if PAUSED:
        render_pause_filter()

    if QUIT_MENU_POPPED:
        ask_quit()
        if RUNNING == False:
            break

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            QUIT_MENU_POPPED = True

    #Update Screen ****************************************
    WINDOW.flip()