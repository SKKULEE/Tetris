#Built-in Modules *************************************************************

import os, pygame



#pygame Initialization ********************************************************

pygame.init()



#Basic Variables **************************************************************

CAPTION = "Tetris -by.LCG"
ICON = pygame.image.load("images\icon.png")
RESOLUTION = (1440, 810)
FPS = 60
MAGNIFYING_RATE = 1



#Window Setting ***************************************************************

WINDOW = pygame.display
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode(RESOLUTION)
pygame.time.Clock().tick(FPS)
pygame.mouse.set_visible(False)



#Custom Modules ***************************************************************

import Data, Event, Image, Text



#Global Variables *************************************************************

DICT = {}
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
    #Default Background ***********************************
    SCREEN.fill((0, 0, 0))

    #Current Background ***********************************
    GAME_STATUS.render_background(SCREEN)

    #Test *************************************************
    SCREEN.fill((127, 127, 127))
    Text.draw_text(SCREEN, "Tetris", (0, 0), origin = Text.top_left, align = Text.middle)

    #Pause Filter *****************************************
    if PAUSED:
        render_pause_filter()

    #Quit Menu ********************************************
    if QUIT_MENU_POPPED:
        ask_quit()
        if RUNNING == False:
            break

    #Draw Cursor ******************************************
    if pygame.mouse.get_focused():
        cursor_image = Image.load("images\cursor.png")
        SCREEN.blit(cursor_image, pygame.mouse.get_pos())

    #Key Input ********************************************
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            QUIT_MENU_POPPED = True

    #Update Screen ****************************************
    WINDOW.flip()