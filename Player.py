#!/usr/bin/env python3



#Classes **********************************************************************

class player:
    def __init__(self, name: str, slot: int) -> None:
        self.name = name
        self.board = [[None for i in range(10)] for j in range(20)]
        self.combo = 0
        self.back_to_back = False
        self.score = 0
        self.gravity = 0
        self.drop_delay = 0
        self.decision_delay = 0
        self.piece = None