# chessmoves.py

class ChessMove():
    def __init__(self, board):
        self.board = board

    def getPiece(self, file_index, rank_index):
        # get the selected piece
        coordinates = [file_index, rank_index]
        piecename = self.board.get_piece(file_index, rank_index)

        print(piecename, coordinates)

        return piecename, coordinates
    
    def movePiece(self, piecename, coordinates):
        # move the piece
        pass