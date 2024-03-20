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

        self.current_player = "white"

        self.pawn = Pawn(self.chessboard, self.chessmoves)
        self.knight = Knight(self.chessboard, self.chessmoves)
        self.bishop = Bishop(self.chessboard, self.chessmoves)
        self.rook = Rook(self.chessboard, self.chessmoves)
        self.queen = Queen(self.chessboard)
        self.king = King(self.chessboard)
        self.pieces = None


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

        self.chessboard.mainloop(screen)
        selected_piece = None

        # initialize the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    file_index = chr(ord('a') + (x // self.chessboard.square_size))
                    rank_index = 8 - (y // self.chessboard.square_size)
                    
                    # select piece or move
                    if selected_piece is None:
                        selected_piece = self.chessmoves.set_piece(file_index, rank_index)
                        print(f"selected piece: {selected_piece}")
                    else:
                        move_results = self.chessmoves.set_move(file_index, rank_index)
                        print(f"selected move: {move_results}")

                        if move_results:
                            self.find_piece(selected_piece[0], selected_piece[1], move_results[1])
                            self.chessboard.mainloop(screen)

                            # switch to the next player
                            self.current_player = "black" if self.current_player == "white" else "white"

                        selected_piece = None

            # stop the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
    # call the correct piece to move
    def find_piece(self, piecename, current_position, new_position):
        for piece in self.chessboard.pieces:
            # move the pawn
            if isinstance(piece, Pawn) and piece.color in piecename:
                print(piece.position)
                if piece.position == tuple(current_position):
                    piece.move(tuple(current_position), tuple(new_position))
                    break
            
            # move the knight
            if isinstance(piece, Knight) and piece.color in piecename:
                if piece.position == tuple(current_position):
                    piece.move(tuple(current_position), tuple(new_position))
                    break

            # move the bishop
            if isinstance(piece, Bishop) and piece.color in piecename:
                if piece.position == tuple(current_position):
                    piece.move(tuple(current_position), tuple(new_position))
                    break

            # move the rook
            if isinstance(piece, Rook) and piece.color in piecename:
                if piece.position == tuple(current_position):
                    piece.move(tuple(current_position), tuple(new_position))
                    break

            # move the queen
            if isinstance(piece, Queen) and piece.color in piecename:
                if piece.position == tuple(current_position):
                    piece.move(tuple(current_position), tuple(new_position))
                    break

            # move the king
            if isinstance(piece, King) and piece.color in piecename:
                if piece.position == tuple(current_position):
                    piece.move(tuple(current_position), tuple(new_position))
                    break

# start the game
if __name__ == "__main__":
    game = MainGame()
    game.run()