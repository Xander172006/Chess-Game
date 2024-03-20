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
        # fundamentals of the game
        self.chessboard = Board(self.create_pieces())
        self.chessmoves = ChessMove(self.chessboard)

        self.pawn = Pawn(self.chessboard, self.chessmoves)
        self.knight = Knight(self.chessboard, self.chessmoves)
        self.bishop = Bishop(self.chessboard, self.chessmoves)
        self.rook = Rook(self.chessboard, self.chessmoves)
        self.queen = Queen(self.chessboard)
        self.king = King(self.chessboard)

        # set beginning player
        self.current_player = "white"

        # set the selected piece to None
        self.selected_piece = None
        self.pieces = None


    # returns array of pieces
    def create_pieces(self):
        pieces = []

        # 8 pawns
        for color in ["white", "black"]:
            for i in range(8):
                pieces.append(Pawn(color, chr(ord('a') + i)))

        for color in ["white", "black"]:
            # 2 knights
            pieces.append(Knight(color, "b"))
            pieces.append(Knight(color, "g"))

            # 2 bishops
            pieces.append(Bishop(color, "c"))
            pieces.append(Bishop(color, "f"))

            # 2 rooks
            pieces.append(Rook(color, "a" if color == "white" else "h"))
            pieces.append(Rook(color, "a" if color == "black" else "h"))

        for color in ["white", "black"]:
            # 1 queen
            pieces.append(Queen(color))
            # 1 king
            pieces.append(King(color))

        return pieces

    def run(self):
        size = (640, 640)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Chess Game")

        # instantiate the board
        self.chessboard.mainloop(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    file_index = chr(ord('a') + (x // self.chessboard.square_size))
                    rank_index = 8 - (y // self.chessboard.square_size)


                    if self.selected_piece is None:
                        # set the selected piece
                        self.selected_piece = self.chessmoves.set_piece(file_index, rank_index)

                        if self.selected_piece[0] == 'Empty Square':
                            # invalid square
                            print("Please select a piece")
                        else:
                            # highlight the selected piece
                            self.chessboard.highlight_square(file_index, rank_index) 
                            self.chessboard.mainloop(screen)
                            print(f"selected piece: {self.selected_piece}")

                    else:
                        # read selected move
                        move_results = self.chessmoves.set_move(file_index, rank_index)
                        self.chessboard.remove_highlight()
                        print(f"selected move: {move_results}")

                        # validate the move
                        if self.chessmoves.pawn_moves(self.selected_piece[0], self.selected_piece[1], move_results[1]):
                            self.find_piece(self.selected_piece[0], self.selected_piece[1], move_results[1])
                            self.current_player = "black" if self.current_player == "white" else "white"
                        
                        # reset after move
                        self.selected_piece = None
                        self.chessboard.mainloop(screen)

                # stop the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        
    def find_piece(self, piecename, current_position, new_position):
        for piece in self.chessboard.pieces:
            if isinstance(piece, Pawn) and piece.color in piecename:
                # is pawn
                pass
            elif isinstance(piece, Knight) and piece.color in piecename:
                # is knight
                pass
            elif isinstance(piece, Bishop) and piece.color in piecename:
                # is bishop
                pass
            elif isinstance(piece, Rook) and piece.color in piecename:
                # is rook
                pass
            elif isinstance(piece, Queen) and piece.color in piecename:
                # is queen
                pass
            elif isinstance(piece, King) and piece.color in piecename:
                # is king
                pass
            else:
                continue

            # move the piece
            if piece.position == tuple(current_position):
                piece.move(tuple(current_position), tuple(new_position))
                break

# start the game
if __name__ == "__main__":
    game = MainGame()
    game.run()