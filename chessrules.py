# chessrules.py

from Position import Position
import chess

class ChessRules:
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.board = chess.Board()

    def convert_to_uci(self, move):
        uci_move = f"{move['current_position'][0]}{move['current_position'][1]}" \
               f"{move['new_position'][0]}{move['new_position'][1]}"
        return uci_move

    
    def is_legal_move(self, move):
        uci_move = self.convert_to_uci(move)

        if chess.Move.from_uci(uci_move) in self.board.legal_moves:
            print(f"moved {move['piecename'].capitalize()} on {move['current_position']} to {move['new_position']}")
            self.board.push(chess.Move.from_uci(uci_move))
            return True
        else:
            print("Invalid move option")
            return False


    def is_check(self, color):
        pass


    def is_checkmate(self, color):
        # Implement logic to check if the specified color is in checkmate
        pass


    def is_stalemate(self, color):
        # Implement logic to check if the specified color is in stalemate
        pass


    def handle_castling(self, color):
        # Implement logic to handle castling for the specified color
        pass

    def handle_en_passant(self):
        # Implement logic to handle en passant
        pass


    def handle_pawn_promotion(self, piece):
        # Implement logic to handle pawn promotion
        pass