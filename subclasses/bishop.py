# chess bishop.py

class Bishop:
    def __init__(self, color, starting_file):
        self.has_moved = False
        self.color = color
        self.position = (starting_file, 1 if color == "white" else 8)

    def move(self):
        pass

    def capture(self):
        white_bishop = './pieces_icons/white_bishop.png'
        black_bishop = './pieces_icons/black_bishop.png'

        if self.color == "white":
            return white_bishop
        else:
            return black_bishop