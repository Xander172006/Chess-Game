# maingame.py
import pygame
import sys
import os

# import subclasses
from subclasses.Pawn import Pawn
from subclasses.Knight import Knight
from subclasses.Bishop import Bishop
from subclasses.Rook import Rook
from subclasses.Queen import Queen
from subclasses.King import King

# initialize pygame
from board import Board
from chessmoves import ChessMove
from chessrules import ChessRules

import chess
pygame.init()


class MainGame:
    def __init__(self):
        self.chessboard = Board()
        self.chessmoves = ChessMove(self.chessboard)
        self.chessrules = ChessRules(self.chessboard)

        # set beginning player
        self.current_player = "white"

        # set the selected piece to None
        self.selected_piece = None
        self.pieces = None

    def run(self):
        size = (640, 640)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Chess Game")

        # instantiate the board
        self.chessboard.run_board(screen)
        print(f"It's {self.current_player.capitalize()} to make a move!")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    # mouse position
                    x, y = pygame.mouse.get_pos()
                    file_index = chr(ord('a') + (x // self.chessboard.square_size))
                    rank_index = 8 - (y // self.chessboard.square_size)


                    # set the turn
                    if self.current_player == "black":
                        self.chessrules.board.turn = chess.BLACK
                    else:
                        self.chessrules.board.turn = chess.WHITE


                    # select a piece
                    if self.selected_piece is None:
                        self.selected_piece = self.chessmoves.chess_piece_information(file_index, rank_index)

                        # empty square
                        if self.selected_piece[0] == 'Empty Square':
                            print("Please select a piece!")
                            self.selected_piece = None
                        else:                         
                            # not other players piece
                            color, piece = self.selected_piece[0].split()

                            if color != self.current_player:
                                print(f"It is `{self.current_player}` to make a move!")
                                self.selected_piece = None
                            else:
                                # highlighting
                                self.chessboard.highlight_square(file_index, rank_index) 
                                self.chessboard.run_board(screen)

                    # move the piece
                    else:
                        move_results = self.chessmoves.chess_piece_information(file_index, rank_index)
                        self.chessboard.remove_highlight()

                        # validation
                        create_move = self.chessmoves.create_move(self.selected_piece, move_results)
                        move_validation = self.chessrules.is_legal_move(create_move)

                        if (move_validation):
                            self.chessboard.move_piece(tuple(create_move['current_position']), tuple(create_move['new_position']))
                            self.current_player = "black" if self.current_player == "white" else "white"

                            # reset after move for other player
                            self.selected_piece = None
                            self.chessboard.run_board(screen)

                            print(f"It's {self.current_player.capitalize()} to make a move!")
                        else:
                            self.selected_piece = None



                # stop the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

# start the game
if __name__ == "__main__":
    game = MainGame()
    game.run()