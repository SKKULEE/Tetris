#!/usr/bin/env python3



#Built-in Modules *************************************************************

import os, pygame, sys



#pygame Initialization ********************************************************

pygame.init()



#Basic Variables **************************************************************

CAPTION = "Tetris -by.LCG"
ICON = pygame.image.load(os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))), "images\icon.png"))

RESOLUTION = (1280, 720)
FPS = 144
MAGNIFYING_RATE = 1
CLOCK = pygame.time.Clock()
MOUSE = pygame.mouse



#Window Settings **************************************************************

WINDOW = pygame.display
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode(RESOLUTION)
MOUSE.set_visible(False)



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
    Text.draw_text(SCREEN, "FPS: %d" % cur_fps, font_size = 16 * MAGNIFYING_RATE, color = (255, 255, 255))
    Text.draw_text(SCREEN, "GAME_STATUS: %s" % GAME_STATUS.name, font_size = 16 * MAGNIFYING_RATE, pos = SCREEN.get_size(), vertex = Image.bot_right, color = (255, 255, 255))

    #Pause Filter ***************************************** This and...
    if PAUSED:
        render_pause_filter()

    #Quit Menu ******************************************** This and...
    if QUIT_MENU_POPPED:
        ask_quit()
        if RUNNING == False:
            break

    #Draw Cursor ****************************************** This will be changed to be under control of 'Event' module
    if MOUSE.get_focused() and GAME_STATUS != Event.starting:
        NEW_IMAGE = Image.scale(CURSOR_IMAGE, MAGNIFYING_RATE)
        Image.draw(SCREEN, NEW_IMAGE, MOUSE.get_pos(), Image.center)

    #Key Input ********************************************
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            QUIT_MENU_POPPED = True

    #Update Screen ****************************************
    WINDOW.flip()
