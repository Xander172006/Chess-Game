# chess bishop.py

class Bishop:
    # define the bishop
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

    # return the sprite of the bishop
    def sprite(self):
        white_bishop = './pieces_icons/white_bishop.png'
        black_bishop = './pieces_icons/black_bishop.png'

        if self.color == "white":
            return white_bishop
        else:
            return black_bishop