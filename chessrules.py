# chessrules.py

from chessrulesbase import ChessRulesBase
import chess 

class ChessRules(ChessRulesBase):
    # check move legality
    def is_legal_move(self, move):
        uci_move = self.convert_to_uci(move)

        if chess.Move.from_uci(uci_move) in self.board.legal_moves:
            print(f"moved {move['piecename'].capitalize()} on {move['current_position']} to {move['new_position']}")
            self.capture_piece(move)
            self.handle_castling(move)
            self.board.push(chess.Move.from_uci(uci_move))
            return True
        else:
            print("Invalid move option")
            return False


    # capture piece
    def capture_piece(self, move):
        new_pos = move['new_position']
        file_index = ord(new_pos[0]) - ord('a')  
        rank_index = int(new_pos[1]) - 1  

        if self.board.piece_at(chess.square(file_index, rank_index)):
            self.board.remove_piece_at(chess.square(file_index, rank_index))
            self.chessboard.remove_piece(new_pos, move['new_position_piecename'])
            print(f"Captured {move['new_position_piecename']} at {move['new_position']}")


    # king is in check
    def is_check(self):
        if self.board.is_check():
            return True
        else:
            return False

    # king is checkmated
    def is_checkmate(self):
        if self.board.is_checkmate():
            return True
        else:
            return False

    # king is in stalemate
    def is_stalemate(self):
        if self.board.is_stalemate():
            return True
        else:
            return False

    # king has castled
    def handle_castling(self, move):
        check = chess.Move.from_uci(self.convert_to_uci(move))
        if self.board.is_kingside_castling(check) or self.board.is_queenside_castling(check):
            # kingside castling white
            if move['current_position'] == "e1" and move['new_position'] == "g1":
                self.chessboard.move_piece(("h", 1), ("f", 1))
            # queenside castling white
            elif move['current_position'] == "e1" and move['new_position'] == "c1":
                self.chessboard.move_piece(("a", 1), ("d", 1))
            # kingside castling black
            elif move['current_position'] == "e8" and move['new_position'] == "g8":
                self.chessboard.move_piece(("h", 8), ("f", 8))
            # queenside castling black
            elif move['current_position'] == "e8" and move['new_position'] == "c8":
                self.chessboard.move_piece(("a", 8), ("d", 8))

            print(move['piecename'].capitalize() + " has castled")


    # en passant
    def handle_en_passant(self):
        pass

    # pawn promotion
    def handle_pawn_promotion(self, piece):
        pass