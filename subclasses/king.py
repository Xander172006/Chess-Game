# chess king.py

class King:
    def __init__(self, color):
        self.has_moved = False
        self.color = color

        # initialize the position of the king
        if self.color == "white":
            self.position = ("e", 1)
        else:
            self.position = ("e", 8)

    def move(self):
        pass

    def capture(self):
        white_king = './pieces_icons/white_king.png'
        black_king = './pieces_icons/black_king.png'

        if self.color == "white":
            return white_king
        else:
            return black_king