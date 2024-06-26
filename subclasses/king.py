# chess king.py

class King:
    # define the king
    def __init__(self, color):
        self.has_moved = False
        self.color = color

        if self.color == "white":
            self.position = ("e", 1)
        else:
            self.position = ("e", 8)

    # sprite of the king
    def sprite(self):
        white_king = './pieces_icons/white_king.png'
        black_king = './pieces_icons/black_king.png'

        if self.color == "white":
            return white_king
        else:
            return black_king