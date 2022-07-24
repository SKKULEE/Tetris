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
CLOCK = pygame.time.Clock()



#Window Setting ***************************************************************

WINDOW = pygame.display
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode(RESOLUTION)
pygame.mouse.set_visible(False)



#Custom Modules ***************************************************************

import Data, Event, Image, Text



#Global Variables *************************************************************

DICT = {}
GAME_STATUS = Event.starting
PAUSED = False
QUIT_MENU_POPPED = False
CURSOR_IMAGE = Image.load("images\cursor.png")



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
    #Set Clock ********************************************
    CLOCK.tick(FPS)

    #Default Background ***********************************
    SCREEN.fill((0, 127, 255))

    #Current Background ***********************************
    #GAME_STATUS.render_background()

    #Test *************************************************
    Text.draw_text(SCREEN, "Tetris", font_size = 16 * MAGNIFYING_RATE, pos = (0, 0))
    print(CLOCK.get_fps())

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
        NEW_IMAGE = Image.scale(CURSOR_IMAGE, MAGNIFYING_RATE)
        Image.draw(SCREEN, NEW_IMAGE, pygame.mouse.get_pos(), Image.center)

    #Key Input ********************************************
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            QUIT_MENU_POPPED = True

    #Update Screen ****************************************
    WINDOW.flip()