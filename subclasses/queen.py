# chess queen.py

class Queen:
    def __init__(self, color):
        self.has_moved = False
        self.color = color

        # initialize the position of the queen
        if self.color == "white":
            self.position = ("d", 1)
        else:
            self.position = ("d", 8)

    def move(self):
        pass

    def capture(self):
        white_queen = './pieces_icons/white_queen.png'
        black_queen = './pieces_icons/black_queen.png'

        if self.color == "white":
            return white_queen
        else:
            return black_queen