# maingame.py
import pygame
import sys
import chess

from board import Board
from chessmoves import ChessMove
from chessrules import ChessRules

class MainGame:
    def __init__(self):
        # use other classes
        self.chessboard = Board()
        self.chessmoves = ChessMove(self.chessboard)
        self.chessrules = ChessRules(self.chessboard)

        # set the current player
        self.current_player = "white"

        # hold player interactions
        self.selected_position = None
        self.selected_piece = None
        self.pieces = None

        # game over
        self.game_over = False

    def run(self):
        size = (640, 640)
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        pygame.display.set_caption("Chess Game")

        # setup the game
        self.chessboard.run_board(screen)
        print('\n----- Welcome to Chess! -----')
        print(f"\n\033[1mIt's {self.current_player.capitalize()} to make a move! \033[0m")



        # run the game continuously if no winner
        while True:
            if not self.game_over:
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
                                    if self.current_player == "black":
                                        print(f"It is " + "\033[1;30m`black`\033[0m" + " to make a move!")
                                    else:
                                        print(f"It is " + "\033[1m`white`\033[0m" + " to make a move!")

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

                            # if move is on same position
                            if create_move['current_position'] == create_move['new_position']:
                                print("Invalid move option")
                                self.selected_piece = None
                                continue
                            
                            move_validation = self.chessrules.is_legal_move(create_move)

                            if (move_validation):
                                # castling
                                if (self.chessrules.handle_castling(create_move)):
                                    self.chessboard.castling(create_move)
                                
                                # king is in check
                                if (self.chessrules.board.is_check()):
                                    if self.current_player == "white":
                                        print("\033[1;30mBlack King\033[0m" + "\033[31m is in check!\033[0m")
                                    else:
                                        print("\033[1mWhite King\033[0m" + "\033[31m is in check!\033[0m")

                                # move the piece
                                self.chessboard.move_piece(tuple(create_move['current_position']), tuple(create_move['new_position']))

                                # check for checkmate or stalemate
                                if self.winner():
                                    self.game_over = True
                                    exit()

                                # switch player
                                self.current_player = "black" if self.current_player == "white" else "white"

                                # print current pieces player has captured
                                if self.current_player == "white":
                                    print(f"\033[1;30mBlack's arsenal: \033[0m" + f"{self.chessboard.captured_pieces_black}")
                                else:
                                    print(f"\033[1mWhites arsenal: \033[0m" + f"{self.chessboard.captured_pieces_black}")


                                # reset after move for other player
                                self.selected_piece = None
                                self.chessboard.run_board(screen)

                                # give turn to other player
                                if self.current_player == "black":
                                    print(f"\n\033[1;30mIt's {self.current_player.capitalize()} to make a move! \033[0m")
                                else:
                                    print(f"\n\033[1mIt's {self.current_player.capitalize()} to make a move! \033[0m")

                            else:
                                self.selected_piece = None
                            
                    # stop the game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

    def winner(self):
        # checkmate
        if self.chessrules.is_checkmate():
            if self.current_player == "white":
                print(
                        "\033[1mBlack\033[0m" + 
                        "\033[31m is checkmated!\033[0m"
                    )
                print(f"\033[1m----- {self.current_player.capitalize()}\033[0m" + " wins! -----")
            else:
                print(
                        "\033[1mWhite\033[0m" + 
                        "\033[31m is checkmated!\033[0m"
                    )
                print(f"\033[1;30m----- {self.current_player.capitalize()}\033[0m" + " wins! -----")

            return True
        
        # stalemate
        if self.chessrules.is_stalemate():
            if self.current_player == "white":
                print( 
                        "\033[31m No legal moves for \033[0m" +
                        "\033[1;30mBlack!\033[0m"
                    )
            else:
                print( 
                        "\033[31m No legal moves for \033[0m" +
                        "\033[1mWhite!\033[0m"
                    )
                
            print(f"\033[1m----- Game ends in a Draw -----")
            return True

# start the game
pygame.init()

if __name__ == "__main__":
    game = MainGame()
    game.run()