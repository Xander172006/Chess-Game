# chess knight.py

class Knight:
    def __init__(self, color, starting_file):
        self.has_moved = False
        self.color = color
        self.position = (starting_file, 1 if color == "white" else 8)

    def move(self):
        pass

    def capture(self):
        white_knight = './pieces_icons/white_knight.png'
        black_knight = './pieces_icons/black_knight.png'

        if self.color == "white":
            return white_knight
        else:
            return black_knight