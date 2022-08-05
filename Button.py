#!/usr/bin/env python3



#Built-in Modules *************************************************************

import pygame


#Custom_Modules ***************************************************************

import Image, Text



#Classes **********************************************************************

#Button Status ********************************************
class status:
    def __init__(self, name):
        self.name = name

idling = status("Idling")
mouse_on = status("mouse_on")
clicked = status("clicked")

just_mouse_in = status("get_mouse_in")
just_mouse_out = status("get_mouse_out")
just_clicked = status("get_clicked")
just_declicked = status("get_declicked")

#Button ***************************************************
class button:
    def __init__(self, text: str) -> None:
        self.text = text
        self.image = {"default": Image.load(None)}
        self.pos = [0, 0]
        self.vertex = Image.top_left
        self.stat = idling
        self.disabled = False

    def set_default_image(self, img: pygame.Surface) -> None:
        self.image[idling] = img
        for i in self.image:
            self.image[i] = Image.scale(self.image[i], self.image[idling].get_size())

    def set_mouse_on_image(self, img: pygame.Surface) -> None:
        self.image[mouse_on] = Image.scale(img, image[idling].get_size())

    def set_clicked_image(self, img: pygame.Surface) -> None:
        self.image[clicked] = Image.scale(img, image[idling].get_size());

    def set_just_mouse_in_image(self, img: pygame.Surface) -> None:
        self.image[just_mouse_in] = Image.scale(img, image[idling].get_size());

    def set_just_mouse_out_image(self, img: pygame.Surface) -> None:
        self.image[just_mouse_out] = Image.scale(img, image[idling].get_size());
        
    def set_just_clicked_image(self, img: pygame.Surface) -> None:
        self.image[just_clicked] = Image.scale(img, image[idling].get_size());
        
    def set_just_declicked_image(self, img: pygame.Surface) -> None:
        self.image[just_declicked] = Image.scale(img, image[idling].get_size());

    def set_disabled_image(self, img: pygame.Surface) -> None:
        self.image[disabled] = Image.scale(img, image[default].get_size())

    def set_pos(self, pos: [int, int]) -> None:
        self.pos = pos

    def set_size(self, size: (int, int)) -> None:
        for i in self.image:
            self.image[i] = Image.scale(self.image[i], size)

    def set_vertex(self, vertex: "Image.vertex") -> None:
        self.vertex = vertex

    def set_disabled(self) -> None:
        self.disabled = True

    def set_activated(self) -> None:
        self.disabled = False

    def update(self) -> None:
        rect = pygame.rect(pos, size)
        if self.vertex == Image.top_mid:
            rect.midtop = pos
        elif self.vertex == Image.top_right:
            rect.topright = pos
        elif self.vertex == Image.mid_left:
            rect.midleft = pos
        elif self.vertex == Image.center:
            rect.center = pos
        elif self.vertex == Image.mid_right:
            rect.midright = pos
        elif self.vertex == Image.bot_left:
            rect.bottomleft = pos
        elif self.vertex == Image.bot_mid:
            rect.midbottom = pos
        elif self.vertex == Image.bot_right:
            rect.bottomright = pos
        else: #default: self.vertex == Image.top_left
            rect.topleft = pos

        if rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if self.stat == clicked:
                    return
                elif self.stat == just_clicked:
                    self.stat = clicked
                else:
                    self.stat = just_clicked
            else:
                if self.stat == mouse_on:
                    return
                elif self.stat == just_mouse_in:
                    self.stat = mouse_on
                else:
                    self.stat = just_mouse_in
        else:
            if self.stat == idling:
                return
            elif self.stat == just_mouse_out:
                self.stat = idling
            else:
                self.stat = just_mouse_out

    def get_status(self):
        self.update()
        return self.stat

    def render(self, screen: pygame.Surface):
        try:
            img = self.image[self.stat]
            Image.draw(screen, img, self.pos, self.vertex)
        except:
            pass