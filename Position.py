# Position.py

class Position:
    # define the position of the piece
    def __init__(self, file_index, rank_index, piece=None, colors=None):
        self.file_index = file_index
        self.rank_index = rank_index
        self.piece = piece
        self.colors = colors

    # check if the position is valid
    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.file_index == other.file_index and self.rank_index == other.rank_index
    
    # return the position of the piece including its color
    def __str__(self):
        file_letter = chr(self.file_index + ord('a'))
        rank_value = self.rank_index + 1
        
        # return position and color
        return f"{self.colors.capitalize()}-{self.piece.__class__.__name__} on ({file_letter}, {rank_value})"
