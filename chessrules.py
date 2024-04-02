# chessrules.py

from chessrulesbase import ChessRulesBase
import chess 

class ChessRules(ChessRulesBase):
    # check move legality
    def is_legal_move(self, move):
        uci_move = self.convert_to_uci(move)

        # check if move is legal or is from promotion
        if self.board.is_legal(chess.Move.from_uci(uci_move)):
            print(f"moved {move['piecename'].capitalize()} on {move['current_position']} to {move['new_position']}")

            self.capture_piece(move)
            self.handle_castling(move)
            self.handle_en_passant(move)

            self.board.push(chess.Move.from_uci(uci_move))
            return True
        elif chess.square_rank(chess.Move.from_uci(uci_move).to_square) == 0 or chess.square_rank(chess.Move.from_uci(uci_move).to_square) == 7:
            # check if pawn can move forward or capture
            if self.can_promote_pawn(move):
                if int(move['current_position'][1]) + 1 == int(move['new_position'][1]) and move['current_position'][0] == move['new_position'][0]:
                    self.handle_pawn_promotion(move)
                    return True
                else:
                    self.chessboard.remove_piece(move['new_position'], move['piecename'])
                    self.handle_pawn_promotion(move)
                    return True
                
                if int(move['current_position'][1]) - 1 == int(move['new_position'][1]) and move['current_position'][0] == move['new_position'][0]:
                    self.handle_pawn_promotion(move)
                    return True
                else:
                    self.chessboard.remove_piece(move['new_position'], move['piecename'])
                    self.handle_pawn_promotion(move)
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
    def handle_en_passant(self, move):
        check = chess.Move.from_uci(self.convert_to_uci(move))
        if self.board.is_en_passant(check):
            # calculate wich pawn to remove based on the move coordinates
            if move['piecename'] == "white Pawn":
                current_position = move['new_position']
                file_letter = current_position[0]
                rank_number = int(current_position[1]) - 1

                find_coördinates = file_letter + str(rank_number)
                self.chessboard.remove_piece(find_coördinates, move['new_position_piecename'])
            else:
                current_position = move['new_position']
                file_letter = current_position[0]
                rank_number = int(current_position[1]) + 1

                find_coördinates = file_letter + str(rank_number)
                self.chessboard.remove_piece(find_coördinates, move['new_position_piecename'])
        

    def can_promote_pawn(self, move_info):
        current_position = move_info['current_position']
        new_position = move_info['new_position']

        if int(current_position[1]) == 7:
            if int(new_position[1]) == 8:
                
                if abs(ord(current_position[0]) - ord(new_position[0])) > 1:
                    return False
                else: 
                    return True
        elif int(current_position[1]) == 2:
            if int(new_position[1]) == 1:
                if abs(ord(current_position[0]) - ord(new_position[0])) > 1:
                    return False
                else: 
                    return True
    

    # pawn promotion
    def handle_pawn_promotion(self, move):
        print("Choose a piece to promote to: `knight = 1`, `bishop = 2`, `rook = 3`, `queen = 4`")
        promoted_piece = input()

        piece_mapping = {
            '1': 'Knight',
            '2': 'Bishop',
            '3': 'Rook',
            '4': 'Queen'
        }

        promoted_piece_symbol = piece_mapping.get(promoted_piece)

        check = None  # Initialize check variable

        if promoted_piece == '1':
            check = f"{chess.Move.from_uci(self.convert_to_uci(move))}n"
        elif promoted_piece == '2':
            check = f"{chess.Move.from_uci(self.convert_to_uci(move))}b"
        elif promoted_piece == '3':
            check = f"{chess.Move.from_uci(self.convert_to_uci(move))}r"
        elif promoted_piece == '4':
            check = f"{chess.Move.from_uci(self.convert_to_uci(move))}q"

        # Update the internal board representation
        if promoted_piece_symbol and check:
            self.chessboard.change_piece(move, promoted_piece)
            self.board.push(chess.Move.from_uci(check))
            return check
        else:
            print("Invalid input")
