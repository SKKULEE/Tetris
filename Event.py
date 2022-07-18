#Built-in Modules *************************************************************




#Custom Modules ***************************************************************

from main import RUNNING, WINDOW



#Classes **********************************************************************

class event:
    def __init__(self, event_type: str) -> None:
        self.type = event_type

class subevent:
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

def ask_quit_func() -> None:
    WINDOW.quit()
    RUNNING = False



#Class Variables **************************************************************

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

fade_out = subevent("fade_out")
fade_in = subevent("fade_in")
shake = subevent("shake")
ask_quit = subevent("ask_quit")
ask_quit.set_func(ask_quit_func)