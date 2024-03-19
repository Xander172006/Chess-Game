# maingame.py
from board import Board
import pygame
import sys
from subclasses.pawn import Pawn
from subclasses.knight import Knight
from subclasses.bishop import Bishop
from subclasses.rook import Rook
from subclasses.queen import Queen
from subclasses.king import King

pygame.init()

class MainGame:
    def __init__(self):
        self.chessboard = Board(self.create_pieces())

    def create_pieces(self):
        pieces = []

        # add pawns
        for color in ["white", "black"]:
            for i in range(8):
                pieces.append(Pawn(color, chr(ord('a') + i)))

        # add knights
        for color in ["white", "black"]:
            pieces.append(Knight(color, "b"))
            pieces.append(Knight(color, "g"))

        # add bishops
        for color in ["white", "black"]:
            pieces.append(Bishop(color, "c"))
            pieces.append(Bishop(color, "f"))

        # add rooks
        for color in ["white", "black"]:
            pieces.append(Rook(color, "a" if color == "white" else "h"))
            pieces.append(Rook(color, "a" if color == "black" else "h"))

        # add queens
        for color in ["white", "black"]:
            pieces.append(Queen(color))

        # add kings
        for color in ["white", "black"]:
            pieces.append(King(color))

        return pieces


    # Run the game
    def run(self):
        size = (640, 640)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Chess Game")

        # display the chessboard
        self.chessboard.mainloop(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    game = MainGame()
    game.run()