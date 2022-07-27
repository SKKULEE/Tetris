#!/usr/bin/env python3



#Built-in Modules *************************************************************

import functools, os, pygame, sys



#Custom Modules ***************************************************************

import Data, Image, Text



#Initialization Functions *****************************************************

main = sys.modules["__main__"]
try:
    SCREEN = main.SCREEN
except:
    raise NameError("To use 'Event' module, '__main__' module must have initialized 'pygame.display' object named 'SCREEN'")
RESOLUTION = main.RESOLUTION
FPS = main.FPS



#Classes **********************************************************************

class event:
    def __init__(self, name: str, condition: "function", action: "function") -> None:
        self.name = name
        self.condition = condition
        self.action = action
        
class status:
    def __init__(self, name: str) -> None:
        self.name = name
        self.dict = {}
        self.event = []
        self.init = lambda: None

    def set_init_function(self, func: "function") -> None:
        self.init = functools.partial(func, self)

    def dict_append(self, key: "obj", value: "obj") -> None:
        self.dict[key] = value

    def dict_del(self, key: "obj") -> None:
        del(self.dict[key])

    def event_append(self, ev: event) -> None:
        self.event.append(ev)

    def event_del(self, index: int) -> None:
        del(self.event[index])

    def event_remove(self, ev: event) -> None:
        self.event.remove(ev)

    def run_events(self) -> None:
        for e in self.event:
            if e.condition(self):
                e.action(self)



#Sample Conditions ************************************************************
always = lambda s: True
never = lambda s: False

#Sample Actions ***************************************************************
idling = lambda s: None



#Statuses *********************************************************************

#Undefined ********************************************************************
undefined = status("undefined")
undefined_event = event("undefined_event", always, idling)
undefined.set_init_function(lambda u: u.event_append(undefined_event))
undefined.init()

#Starting *********************************************************************
starting = status("starting")

def starting_init(st: status) -> None:
    st.event_append(starting_background_event)
    st.event_append(starting_fade_in_event)

def starting_background_action(st: status) -> None:
    base = pygame.Surface((SCREEN.get_size()), pygame.SRCALPHA)
    base.fill((0, 0, 0))
    
    logo = Image.load("images\logo.png")
    logo = Image.scale(logo, 4)

    Image.draw(base, logo, base.get_rect().center, Image.center)
    Image.draw(SCREEN, base)

def starting_fade_in_action(st: status) -> None:
    if "fade_in_counter" not in st.dict:
        st.dict_append("fade_in_counter", FPS*2)

    cur_alpha = 255 * st.dict["fade_in_counter"] // (FPS*2)

    curtain = pygame.Surface(SCREEN.get_size(), pygame.SRCALPHA)
    curtain.fill((0, 0, 0))
    curtain.set_alpha(cur_alpha)

    Image.draw(SCREEN, curtain)

    st.dict["fade_in_counter"] -= 1

    if st.dict["fade_in_counter"] < 0:
        st.dict_del("fade_in_counter")
        st.event_del(1)
        st.event_append(starting_wait_event)

def starting_wait_action(st: status) -> None:
    if "wait_counter" not in st.dict:
        st.dict_append("wait_counter", FPS*2)

    st.dict["wait_counter"] -= 1

    if st.dict["wait_counter"] < 0:
        st.dict_del("wait_counter")
        st.event_del(1)
        st.event_append(starting_fade_out_event)

def starting_fade_out_action(st: status) -> None:
    if "fade_out_counter" not in st.dict:
        st.dict_append("fade_out_counter", FPS*2)

    cur_alpha = 255 - 255 * st.dict["fade_out_counter"] // (FPS*2)

    curtain = pygame.Surface(SCREEN.get_size(), pygame.SRCALPHA)
    curtain.fill((0, 0, 0))
    curtain.set_alpha(cur_alpha)

    Image.draw(SCREEN, curtain)

    st.dict["fade_out_counter"] -= 1

    if st.dict["fade_out_counter"] < 0:
        st.dict_del("fade_out_counter")
        main.GAME_STATUS = undefined

starting_background_event = event("starting_background_event", always, starting_background_action)
starting_fade_in_event = event("starting_fade_in_event", always, starting_fade_in_action)
starting_wait_event = event("starting_wait_event", always, starting_wait_action)
starting_fade_out_event = event("starting_fade_out_event", always, starting_fade_out_action)

starting.set_init_function(starting_init)
starting.init()






#Class Variables **************************************************************

#Events ***********************************************************************


#Statuses *********************************************************************
