# chess rook.py

class Rook:
    def __init__(self, color, starting_file):
        self.has_moved = False
        self.color = color
        self.position = (starting_file, 1 if color == "white" else 8)

    def move(self):
        pass

    def capture(self):
        white_rook = './pieces_icons/white_rook.png'
        black_rook = './pieces_icons/black_rook.png'

        if self.color == "white":
            return white_rook
        else:
            return black_rook