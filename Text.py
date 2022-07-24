#Built-in Modules *************************************************************

import os, pygame



#Custom Modules ***************************************************************

import Data, Image



#Classes **********************************************************************

class align:
    def __init__(self, prop: str) -> None:
        self.prop = prop



#Variables ********************************************************************

try:
    font_image = Image.load(Data.game_folder_path(Data.font))
except:
    try:
        font_image = Image.load(Data.game_folder_path("fonts\LCG_classic.png"))
    except:
        font_image = Image.load(Data.resource_path("images\LCG_classic.png"))
        Data.game_folder_recover()



#Class Variables **************************************************************

left = align("left")
middle = align("middle")
right = align("right")



#Functions ********************************************************************

def text_to_image(content: str, font_size: int = 16, align: align = left) -> pygame.Surface:
    line = content.split('\n')
    longest = max(len(i) for i in line)
    character_width = font_size * 14 // 16
    character_height = font_size
    field_width = character_width * longest
    field_height = character_height * len(line)
    base = pygame.Surface((field_width, field_height), pygame.SRCALPHA)

    cursor = [0, -font_size]
    for i in line:
        cursor[0] = character_width * (longest - len(i)) * (1 if align == middle else 2 if align == right else 0) // 2
        cursor[1] += character_height
        for j in i:
            character_id = ord(j)
            horizontal = character_id % 16 * 16 + 1
            vertical = character_id // 16 * 16
            try:
                original_character = font_image.subsurface((horizontal, vertical, 14, 16))
            except:
                original_character = font_image.subsurface((1, 0, 14, 16))
            transformed_character = Image.scale(original_character, (character_width, character_height))
            Image.draw(base, transformed_character, cursor)
            cursor[0] += character_width
    return base

def draw_text(screen: pygame.display, content: str, font_size: int = 16, align: align = left, pos: (int, int) = (0, 0), vertex: Image.vertex = Image.top_left) -> None:
    text_image = text_to_image(content, font_size, align)
    Image.draw(screen, text_image, pos, vertex)
