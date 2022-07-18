#Custom Modules ***************************************************************

import Image



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