#Built-in Modules *************************************************************

import os, pygame



#Custom Modules ***************************************************************

import Data, Image



#Classes **********************************************************************

class pos:
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

top_left = pos("top left")
top_mid = pos("top middle")
top_right = pos("top right")
mid_left = pos("middle left")
center = pos("center")
mid_right = pos("middle right")
bot_left = pos("bottom left")
bot_mid = pos("bottom middle")
bot_right = pos("bottom right")

left = pos("left")
middle = pos("middle")
right = pos("right")



#Functions ********************************************************************

def draw_text(screen: pygame.Surface, content: str = "", pos: (int, int) = (0, 0), font_size: int = 16, origin: str = top_left, align: str = left) -> None:
    line = content.split('\n')
    longest = max(len(i) for i in line)
    field_width = font_size * longest
    field_height = font_size * len(line)
    base = pygame.Surface((field_width, field_height), pygame.SRCALPHA)
    character_width = font_size * 14 // 16
    character_height = font_size
    
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
                original_character = font_image.subsurface((0, 0, 14, 16))
            transformed_character = pygame.transform.scale(original_character, (character_width, character_height))
            base.blit(transformed_character, cursor)
            cursor[0] += character_width

    text_field = base.get_rect()
    if origin == top_mid:
        text_field.midtop = pos
    elif origin == top_right:
        text_field.topright = pos
    elif origin == mid_left:
        text_field.midleft = pos
    elif origin == center:
        text_field.centerx = pos[0]
        text_field.centery = pos[1]
    elif origin == right:
        text_field.midright = pos
    elif origin == bot_left:
        text_field.bottomleft = pos
    elif origin == bot_mid:
        text_field.midbottom = pos
    elif origin == bot_right:
        text_field.bottomright = pos
    else: #default: origin == top_left
        text_field.topleft = pos

    screen.blit(base, text_field)