# chessmoves.py
from Position import Position

class ChessMove():
    def __init__(self, board):
        self.board = board
        self.color = None
        self.selected_position = None

    def chess_piece_information(self, f_index, r_index):
        piece = self.board.get_piece(f_index, r_index)

        if piece == 'Empty Square':
            position = Position(f_index, r_index, 'Empty', 'Square')
        else:
            position = Position(f_index, r_index, piece[0], piece[1])

        return piece, position


    # create move instance
    def create_move(self, current_position, new_position):
        move_dict = {}
        move_dict['piecename'] = current_position[0]
        move_dict['current_position'] = str(current_position[1])

        move_dict['new_position_piecename'] = new_position[0]
        move_dict['new_position'] = str(new_position[1])

        return move_dict