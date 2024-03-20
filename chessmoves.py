# chessmoves.py

class ChessMove():
    def __init__(self, board):
        self.board = board

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
