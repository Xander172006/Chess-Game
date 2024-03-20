# chess queen.py

class Queen:
    # define the queen
    def __init__(self, color):
        self.has_moved = False
        self.color = color

        # initialize the position of the queen
        if self.color == "white":
            self.position = ("d", 1)
        else:
            self.position = ("d", 8)

    # move rule
    def move(self, current_position, new_position):
        if self.position == current_position:
            self.position = new_position
            self.has_moved = True
            print(self.position, new_position)

        print(f"move has been made")

    # capture rule
    def capture(self):
        pass

    # return the sprite of the queen    
    def sprite(self):
        white_queen = './pieces_icons/white_queen.png'
        black_queen = './pieces_icons/black_queen.png'

        if self.color == "white":
            return white_queen
        else:
            return black_queen