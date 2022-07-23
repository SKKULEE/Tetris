#Built-in Modules *************************************************************




#Custom Modules ***************************************************************

import Image



#Classes **********************************************************************

class event:
    def __init__(self, event_type: str) -> None:
        self.type = event_type
        self.dict = {}

    def render_background(self, screen: "pygame.display") -> None:
        self.background_rendering_function(screen)

    def set_background_rendering_function(self, func: "function") -> None:
        self.background_rendering_function = func

    def dict_add(self, key: "obj", value: "obj") -> None:
        self.dict[key] = value

    def dict_del(self, key: "obj") -> None:
        del(self.dict[key])

class effect:
    def __init__(self, event_type: str) -> None:
        self.type = event_type
        self.dict = {}

    def set_func(self, func: "function") -> None:
        self.func = func

    def dict_add(self, key: "obj", value: "obj") -> None:
        self.dict[key] = value

    def dict_del(self, key: "obj") -> None:
        del(self.dict[key])



#Functions ********************************************************************

def render_test_screen(screen: "pygame.display") -> None:
    try:
        screen.blit(default_image)
    except:
        default_image = Image.load("images\default_image.png").convert_alpha()
        screen.blit(default_image, (0, 0))


def render_starting_screen(screen: "pygame.display") -> None:
    pass


#Class Variables **************************************************************

undefined = event("undefined")
undefined.set_background_rendering_function(render_test_screen)

starting = event("starting")
title_screen = event("title_screen")
main_lobby = event("main_lobby")
single_lobby = event("single_lobby")
single_challange = event("single_challenge")
single_infinite = event("single_infinite")
single_custom = event("single_custom")
multi_lobby = event("multi_lobby")
multi_challange = event("multi_challenge")
multi_infinite = event("multi_infinite")
multi_custom = event("multi_custom")

fade_out = effect("fade_out")
fade_in = effect("fade_in")
shake = effect("shake")