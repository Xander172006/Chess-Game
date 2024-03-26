# Position.py
from board import Board

class Position:
    def __init__(self, file_index, rank_index, color, pieces):
        self.file_index = ord(file_index) - ord('a')
        self.rank_index = rank_index
        self.color = color
        self.pieces = pieces
  
    # return single piece position
    def __str__(self):
        return f"{chr(self.file_index + ord('a'))}{self.rank_index}"
        
            
