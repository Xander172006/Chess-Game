from abc import ABC, abstractmethod
import chess

class ChessRulesBase(ABC):
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.board = chess.Board()

    def convert_to_uci(self, move):
        uci_move = f"{move['current_position'][0]}{move['current_position'][1]}" \
                   f"{move['new_position'][0]}{move['new_position'][1]}"
        return uci_move

    @abstractmethod
    def is_legal_move(self, move):
        pass

    @abstractmethod
    def is_check(self, color):
        pass

    @abstractmethod
    def is_checkmate(self, color):
        pass

    @abstractmethod
    def is_stalemate(self, color):
        pass

    @abstractmethod
    def handle_castling(self, color):
        pass

    @abstractmethod
    def handle_en_passant(self):
        pass

    @abstractmethod
    def handle_pawn_promotion(self, piece):
        pass