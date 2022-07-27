#!/usr/bin/env python3



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



#Window Settings **************************************************************

WINDOW = pygame.display
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode(RESOLUTION)
pygame.mouse.set_visible(False)



#Custom Modules ***************************************************************

import Data, Event, Image, Text



#Global Variables *************************************************************

GAME_STATUS = Event.starting
FULL_SCREEN = False
PAUSED = False
QUIT_MENU_POPPED = False
CURSOR_IMAGE = Image.load("images\cursor.png")



#Game Data Preset *************************************************************

GAME_DATA_FILE_INTEGRITY = True
INTEGRITY_WARN = False
GAME_DATA = {}
for i in Data.game_file_read().split('\n'):
    cur = i.strip()
    if cur[0] == '#': continue
    try:
        key, value = cur.split(':')
        GAME_DATA[key] = value
    except:
        GAME_DATA_FILE_INTEGRITY = False

try:
    RESOLUTION = tuple(map(int, GAME_DATA["RESOLUTION"].strip("()").split(", ")))
except:
    GAME_DATA_FILE_INTEGRITY = False
try:
    cur = GAME_DATA["FULLSCREEN"].strip()
    FULL_SCREEN = True if cur == "True" else False
    if cur != "True" and cur != "False": GAME_DATA_FILE_INTEGRITY = False
except:
    GAME_DATA_FILE_INTEGRITY = False
try:
    I_MINO_COLOR = tuple(map(int, GAME_DATA["I-mino color"].strip("()").split(", ")))
    J_MINO_COLOR = tuple(map(int, GAME_DATA["J-mino color"].strip("()").split(", ")))
    L_MINO_COLOR = tuple(map(int, GAME_DATA["L-mino color"].strip("()").split(", ")))
    O_MINO_COLOR = tuple(map(int, GAME_DATA["O-mino color"].strip("()").split(", ")))
    S_MINO_COLOR = tuple(map(int, GAME_DATA["S-mino color"].strip("()").split(", ")))
    T_MINO_COLOR = tuple(map(int, GAME_DATA["T-mino color"].strip("()").split(", ")))
    Z_MINO_COLOR = tuple(map(int, GAME_DATA["Z-mino color"].strip("()").split(", ")))
    Piece.set_base_color(I_MINO_COLOR, J_MINO_COLOR, L_MINO_COLOR, O_MINO_COLOR, S_MINO_COLOR, T_MINO_COLOR, Z_MINO_COLOR)
except:
    GAME_DATA_FILE_INTEGRITY = False

if GAME_DATA_FILE_INTEGRITY == False: INTEGRITY_WARN = True



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

    #Run Events *******************************************
    GAME_STATUS.run_events()

    #Test *************************************************
    cur_fps = int(CLOCK.get_fps())
    Text.draw_text(SCREEN, "FPS: %d" % cur_fps)

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