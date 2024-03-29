# chess king.py

class King:
    # define the king
    def __init__(self, color):
        self.has_moved = False
        self.color = color

        # initialize the position of the king
        if self.color == "white":
            self.position = ("e", 1)
        else:
            self.position = ("e", 8)

    # move rule
    def move(self, current_position, new_position):
        if self.position == current_position:
            self.position = new_position
            self.has_moved = True
            print(self.position, new_position)

        print(f"move has been made")

    # castle rule
    def castle(self):
        pass

    # return the sprite of the king
    def sprite(self):
        white_king = './pieces_icons/white_king.png'
        black_king = './pieces_icons/black_king.png'

        if self.color == "white":
            return white_king
        else:
            return black_king