# chess pawn.py
import pygame

class Pawn:
    # define the pawn
    def __init__(self, color, starting_rank):
        self.has_moved = False
        self.color = color
        self.position = (starting_rank, 2) if color == "white" else (starting_rank, 7)

    # move rule
    def move(self, new_position):
        self.position = new_position
        self.has_moved = True

    # capture rule
    def capture(self):
        pass

    # return the sprite of the pawn
    def sprite(self):
        white_pawn = './pieces_icons/white_pawn.png'
        black_pawn = './pieces_icons/black_pawn.png'

        if self.color == "white":
            return white_pawn
        else:
            return black_pawn