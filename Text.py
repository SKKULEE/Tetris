#Built-in Modules *************************************************************

import os, pygame



#Custom Modules ***************************************************************

import Data, Image



#Variables ********************************************************************

try:
    font_image = Image.load(Data.game_folder_path(Data.font))
except:
    try:
        font_image = Image.load(Data.game_folder_path("fonts\LCG_classic.png"))
    except:
        font_image = Image.load(Data.resource_path("images\LCG_classic.png"))
        Data.game_folder_recover()



#Functions ********************************************************************

def draw_text(screen: pygame.Surface, content: str = "", pos: (int, int) = (0, 0), font_size: int = 16, center: str = "top left", align: str = "left") -> None:
    line = content.split('\n')
    clear_field = Image.load(Data.resource_path("images\empty.png"))
    longest = max(len(i) for i in line)
    width = font_size * longest
    height = font_size * len(line)
    base = pygame.transform.scale(clear_field, (width, height))
    
    cursor = [0, -font_size]
    for i in line:
        cursor[0] = font_size * (longest - len(i)) * (1 if align == "middle" else 2 if align == "right" else 0) // 2
        cursor[1] += font_size
        for j in i:
            character_id = ord(j)
            horizontal = character_id % 16 * 16
            vertical = character_id // 16 * 16
            try:
                original_character = font_image.subsurface((horizontal, vertical, 16, 16))
            except:
                original_character = font_image.subsurface((0, 0, 16, 16))
            transformed_character = pygame.transform.scale(original_character, (font_size, font_size))
            base.blit(transformed_character, cursor)
            cursor[0] += font_size

    if center == "top":
        base.center = (width // 2, 0)
    elif center == "top right":
        base.center = (width, 0)
    elif center == "left":
        base.center = (0, height // 2)
    elif center == "center":
        base.center = (width // 2, height // 2)
    elif center == "right":
        base.center = (width, height // 2)
    elif center == "bottom left":
        base.center = (0, height)
    elif center == "bottom":
        base.center = (width // 2, height)
    elif center == "bottom right":
        base.center = (width, height)
    else: #default: center == "top left"
        base.center = (0, 0)

    screen.blit(base, pos)