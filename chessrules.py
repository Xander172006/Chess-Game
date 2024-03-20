# chessrules.py

class ChessRules:
    def __init__(self, chessboard):
        self.chessboard = chessboard

    def is_legal_move(self, piece, start_pos, end_pos):
        # Implement logic to check if the move is legal for the given piece
        pass

    def is_check(self, color):
        # Implement logic to check if the specified color is in check
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