# maingame.py
import pygame
import sys
import os

# import the subclasses
from subclasses.pawn import Pawn
from subclasses.knight import Knight
from subclasses.bishop import Bishop
from subclasses.rook import Rook
from subclasses.queen import Queen
from subclasses.king import King

# initialize pygame
from board import Board
from chessmoves import ChessMove
pygame.init()


class MainGame:
    def __init__(self):
        self.chessboard = Board(self.create_pieces())
        self.chessmoves = ChessMove(self.chessboard)

        self.pawn = Pawn(self.chessboard, self.chessmoves)
        self.knight = Knight(self.chessboard, self.chessmoves)
        self.bishop = Bishop(self.chessboard, self.chessmoves)
        self.rook = Rook(self.chessboard, self.chessmoves)
        self.queen = Queen(self.chessboard)
        self.king = King(self.chessboard)


    # return the pieces
    def create_pieces(self):
        pieces = []

        # add 8 pawns
        for color in ["white", "black"]:
            for i in range(8):
                pieces.append(Pawn(color, chr(ord('a') + i)))

        # add 2 knights
        for color in ["white", "black"]:
            pieces.append(Knight(color, "b"))
            pieces.append(Knight(color, "g"))

        # add 2 bishops
        for color in ["white", "black"]:
            pieces.append(Bishop(color, "c"))
            pieces.append(Bishop(color, "f"))

        # add 2 rooks
        for color in ["white", "black"]:
            pieces.append(Rook(color, "a" if color == "white" else "h"))
            pieces.append(Rook(color, "a" if color == "black" else "h"))

        # add 1 queens
        for color in ["white", "black"]:
            pieces.append(Queen(color))

        # add 1 kings
        for color in ["white", "black"]:
            pieces.append(King(color))

        return pieces

    def run(self):
        size = (640, 640)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Chess Game")

        # display the chessboard
        self.chessboard.mainloop(screen)

        # initialize the game
        while True:
            for event in pygame.event.get():
                pass

            # stop the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# start the game
if __name__ == "__main__":
    game = MainGame()
    game.run()