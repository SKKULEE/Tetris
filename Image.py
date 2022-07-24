#Built-in Modules *************************************************************

import os, pygame, time



#Custom Modules ***************************************************************

import Data



#Functions ********************************************************************

def load(path: str) -> None:
    try: return pygame.image.load(Data.resource_path(path)).convert_alpha()
    except: return pygame.image.load(Data.resource_path("images\default_image.png")).convert_alpha()

def screenshot(image: pygame.Surface, path: str) -> None:
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
        pygame.image.save(image, screenshot_folder_path + "\\" + current_screenshot_name)
        return True
    else:
        Data.game_folder_recover()
        return False

def scale(image: pygame.Surface, target_size: (int, int)) -> pygame.Surface:
    return pygame.transform.smoothscale(image, target_size)