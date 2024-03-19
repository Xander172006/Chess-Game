# chess pawn.py

class Pawn:
    def __init__(self, color, starting_rank):
        self.has_moved = False
        self.color = color
        self.position = (starting_rank, 2) if color == "white" else (starting_rank, 7)


    def move(self):
        pass

    def capture(self):
        white_pawn = './pieces_icons/white_pawn.png'
        black_pawn = './pieces_icons/black_pawn.png'

        if self.color == "white":
            return white_pawn
        else:
            return black_pawn