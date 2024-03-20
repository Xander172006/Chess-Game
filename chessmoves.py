# chessmoves.py

class ChessMove():
    def __init__(self, board):
        self.board = board

    def get_piece(self, f_index, r_index):
        coordinates = [f_index, r_index]
        piecename = self.board.get_piece(f_index, r_index)

        return piecename, coordinates
    
    def move_piece(self, f_index, r_index):
        coordinates = [f_index, r_index]
        piecename = self.board.get_piece(f_index, r_index)

        
        return piecename, coordinates
