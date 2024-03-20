# chess rook.py

class Rook:
    # define the rook
    def __init__(self, color, starting_file):
        self.has_moved = False
        self.color = color
        self.position = (starting_file, 1 if color == "white" else 8)

    # move rule
    def move(self):
        pass

    # capture rule
    def capture(self):
        pass

    # return the sprite of the rook
    def sprite(self):
        white_rook = './pieces_icons/white_rook.png'
        black_rook = './pieces_icons/black_rook.png'

        if self.color == "white":
            return white_rook
        else:
            return black_rook