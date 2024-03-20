# chessmoves.py
from subclasses.pawn import Pawn


class ChessMove():
    def __init__(self, board):
        self.board = board
        self.pawn = Pawn(self.board, self)

    # return given piece
    def set_piece(self, f_index, r_index):
        coordinates = [f_index, r_index]
        piecename = self.board.get_piece(f_index, r_index)

        return self.format_piece(piecename), coordinates
    
    # return given move
    def set_move(self, f_index, r_index):
        coordinates = [f_index, r_index]
        piecename = self.board.get_piece(f_index, r_index)

        return self.format_piece(piecename), coordinates
    
    # improve formatation
    def format_piece(self, piecename):
        if piecename != 'Empty Square':
            return f"{piecename.color} {piecename.__class__.__name__.lower()}"
        else:
            return 'Empty Square'
        
    # pawns
    def piece_moves(self, piecename, position, move): 
        if piecename == 'white pawn' or piecename == 'black pawn':
            return self.pawn_moves(piecename, position, move)

    def pawn_moves(self, piecename, start_pos, end_pos):
        file_index, rank_index = start_pos
        end_file_index, end_rank_index = end_pos

        for piece in self.board.pieces:
            if isinstance(piece, Pawn) and piece.color in piecename:
                if piece.position == tuple(start_pos):
                    # moves from starting position
                    if not piece.has_moved:
                        return True
                    else:
                        print("cannot move 2 spaces after first move")
                    # moves forward one space
                    if end_rank_index - rank_index == 1 and end_file_index == file_index:
                        return True
                    else:
                        print("can only move forward 1 space")
                    
                    # captures a piece
                    if self.board.get_piece(end_file_index, end_rank_index) != 'Empty Square':
                        piece.capture(piecename, self.board.get_piece(end_file_index, end_rank_index), self.board)
                        return True
                    else:
                        print("cannot capture a empty square")
                    break
