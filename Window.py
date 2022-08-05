#!/usr/bin/env python3



#Built-in Modules *************************************************************

import pygame


#Custom_Modules ***************************************************************

import Image, Text



#Classes **********************************************************************

class window:
    def __init__(self, caption: str = ""):
        self.caption = caption

    def set_size(self, size: (int, int) = (320, 180)):
        self.size = size

    def set_pos(self, pos: (int, int) = (0, 0)):
        self.pos = pos

    def set_vertex(self, vertex: Image.vertex):
        self.vertex = vertex

    def set_icon(self, icon: pygame.Surface):
        self.icon = icon

    def set_content(self, content: str = ""):
        self.content = content