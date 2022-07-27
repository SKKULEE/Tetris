#!/usr/bin/env python3



#Custom Modules ***************************************************************

import Image



#Default Colors ***************************************************************

I_MINO_COLOR = (140, 255, 251)
J_MINO_COLOR = (255, 127,  39)
L_MINO_COLOR = (255, 127,  39)
O_MINO_COLOR = (255, 242,   0)
S_MINO_COLOR = (147, 255,  14)
T_MINO_COLOR = (184,  61, 186)
Z_MINO_COLOR = (236,  28,  36)



#Initialization Functions *****************************************************

def set_base_color(I, J, L, O, S, T, Z):
    global I_MINO_COLOR, J_MINO_COLOR, L_MINO_COLOR, O_MINO_COLOR, S_MINO_COLOR, T_MINO_COLOR, Z_MINO_COLOR
    I_MINO_COLOR = I
    J_MINO_COLOR = J
    L_MINO_COLOR = L
    O_MINO_COLOR = O
    S_MINO_COLOR = S
    T_MINO_COLOR = T
    Z_MINO_COLOR = Z



#Classes **********************************************************************

class cell:
    def __init__(self, master: Player.board, color: (int, int, int), pos: (int, int, int)) -> None:
        self.master = master
        self.color = color
        self.pos = pos

    def render(self) -> None:
        pass

class piece:
    def __init__(self, master: Player.board, type: str) -> None:
        self.master = master
        self.type = type
        self.color = None #요수정
        self.direction = 0
        self.pos = (4, 23)

    def render(self) -> None:
        pass

    def turn_clockwise(self) -> None:
        pass

    def turn_counterclockwise(self) -> None:
        pass

    def move_left(self) -> None:
        pass

    def move_right(self) -> None:
        pass

    def move_down(self) -> None:
        pass

    def hard_drop(self) -> None:
        pass

    def save(self) -> None:
        pass