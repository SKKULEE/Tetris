#Built-in Modules *************************************************************

import os, pygame



#Custom Modules ***************************************************************

import Data, Image



#Classes **********************************************************************
"""
class character:
    def __init__(self, content: str, image: "pygame.image", legnth_width_ratio: int) -> None:
        self.content = content
        self.image = image
        self.length_width_ratio = length_width_ratio

    def render(self, screen: pygame.Surface, font_size: int = 10, pos: (int, int) = (0, 0)) -> None:
        screen.blit(pygame.image.transform.scale(self.image, pos))
"""


#Class Variables **************************************************************

#A = character("A", Image.load())



#Functions ********************************************************************

def font_image() -> pygame.image:
    base_path = Data.game_folder_path()
    main_path = os.path.join(base_path, "font_image.png")
    pygame.image.load(main_path)


def draw_text(screen: pygame.Surface, content: str = "", pos: (int, int) = (0, 0), font_size: int = 10, align: str = "top left") -> None:
    pass


#일단 이미지 파일 전체를 불러오는 함수는 만들었는데, 이걸 어떻게 처리할지는 아직 미정...
#모든 글자를 전각으로 처리하면 편하긴 한데 흠...