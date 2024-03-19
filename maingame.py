# maingame.py
import pygame
import sys

# import the subclasses
subclasses = ["pawn", "knight", "bishop", "rook", "queen", "king"]
for subclass in subclasses:
    # create a global variable for each subclass	
    globals()[subclass.capitalize()] = getattr(__import__("subclasses." + subclass, fromlist=[subclass]), subclass.capitalize())

# initialize pygame
from board import Board
from chessmoves import ChessMove
pygame.init()


class MainGame:
    def __init__(self):
        self.chessboard = Board(self.create_pieces())
        self.chessmoves = ChessMove(self.chessboard)


    # return the pieces
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

    def run(self):
        # set game window
        size = (640, 640)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Chess Game")

        # display the chessboard
        self.chessboard.mainloop(screen)

        # run the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    file_index = chr(ord('a') + (x // self.chessboard.square_size))
                    rank_index = 8 - (y // self.chessboard.square_size)
                    
                    self.chessmoves.getPiece(file_index, rank_index)
                    
                # stop the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


# 
if __name__ == "__main__":
    game = MainGame()
    game.run()