#!/usr/bin/env python3



#Built-in Modules *************************************************************

import os, pygame



#Custom Modules ***************************************************************

import Data



#Classes **********************************************************************

class vertex:
    def __init__(self, prop: str) -> None:
        self.prop = prop



#Variables ********************************************************************

default_image = pygame.image.load(Data.resource_path("images\default_image.png")).convert_alpha()



#Class Variables **************************************************************

top_left = vertex("top left")
top_mid = vertex("top middle")
top_right = vertex("top right")
mid_left = vertex("middle left")
center = vertex("center")
mid_right = vertex("middle right")
bot_left = vertex("bottom left")
bot_mid = vertex("bottom middle")
bot_right = vertex("bottom right")



#Functions ********************************************************************

def load(path: str) -> None:
    try: return pygame.image.load(Data.resource_path(path)).convert_alpha()
    except: return default_image

def screenshot(path: str) -> None:
    main_path = Data.game_folder_path()
    if os.path.isdir(main_path):
        screenshot_folder_path = main_path + "\screenshots"
        if not os.path.isdir(screenshot_folder_path):
            os.mkdir(screenshot_forder_path)
        year = time.tm_year
        month = time.tm_month
        day = time.tm_day
        hour = time.tm_hour
        minute = time.tm_min
        second = time.tm_sec
        current_screenshot_name = "screenshot_%s-%s-%s-%s-%s-%s.png" % (year, month, day, hour, minute, second)
        for i in range(2, 2147483647):
            if not os.path.isfile(current_screenshot_name): break
            current_screenshot_name = "screenshot_%s-%s-%s-%s-%s-%s(%d).png" % (year, month, day, hour, minute, second, i)
        pygame.image.save(SCREEN, screenshot_folder_path + "\\" + current_screenshot_name)
        return True
    else:
        Data.game_folder_recover()
        return False

def scale(image: pygame.Surface, target_scale: int or float or (int, int) = 1) -> pygame.Surface:
    if type(target_scale) in (int, float):
        size = image.get_size()
        new_size = tuple(map(int, (size[0] * target_scale, size[1] * target_scale)))
        return pygame.transform.smoothscale(image, new_size)
    else:
        try:
            return pygame.transform.smoothscale(image, target_scale)
        except:
            raise TypeError("scale() expected one of int, float, (int, int), but %s found" % str(type(target_scale)).split('\'')[1])

def draw(screen: pygame.Surface, image: pygame.Surface, pos: (int, int) = (0, 0), vertex: vertex = top_left) -> None:
    rect = image.get_rect()
    if vertex == top_mid:
        rect.midtop = pos
    elif vertex == top_right:
        rect.topright = pos
    elif vertex == mid_left:
        rect.midleft = pos
    elif vertex == center:
        rect.center = pos
    elif vertex == mid_right:
        rect.midright = pos
    elif vertex == bot_left:
        rect.bottomleft = pos
    elif vertex == bot_mid:
        rect.midbottom = pos
    elif vertex == bot_right:
        rect.bottomright = pos
    else: #default: vertex == top_left
        rect.topleft = pos

    screen.blit(image, rect)

def color_swap(surf: pygame.Surface, old_color: (int, int, int), new_color: (int, int, int)) -> pygame.Surface:
    base = pygame.Surface.get_size()
    base.fill(new_color)