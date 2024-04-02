# board.py
import pygame

from subclasses.Pawn import Pawn
from subclasses.Knight import Knight
from subclasses.Bishop import Bishop
from subclasses.Rook import Rook
from subclasses.Queen import Queen
from subclasses.King import King

class Board:
    def __init__(self):
        self.square_size = 75
        self.width = 8 * self.square_size
        self.height = 8 * self.square_size
        self.selected_position = None

        # store the pieces each player has captured
        self.captured_pieces_white = []
        self.captured_pieces_black = []
        
        self.font = pygame.font.Font(None, 20)
        self.pieces = self.create_pieces()


    # create pieces for white and black
    def create_pieces(self):
        pieces = []

        for color in ["white", "black"]:
            for i in range(8):
                pieces.append(Pawn(color, chr(ord('a') + i)))

        for color in ["white", "black"]:
            pieces.append(Knight(color, "b"))
            pieces.append(Knight(color, "g"))
            pieces.append(Bishop(color, "c"))
            pieces.append(Bishop(color, "f"))
            pieces.append(Rook(color, "a" if color == "white" else "h"))
            pieces.append(Rook(color, "a" if color == "black" else "h"))

        for color in ["white", "black"]:
            pieces.append(Queen(color))
            pieces.append(King(color))

        return pieces

   # run the board
    def run_board(self, screen):
        board = pygame.surface.Surface((self.width, self.height))

        # draw the board and pieces
        self.drawBoard(board)
        self.drawPieces(board)

        # highlight the selected square
        if self.selected_position:
            x = ord(self.selected_position[0]) - ord('a')
            y = 8 - self.selected_position[1]
            rect = pygame.Rect(x * self.square_size, y * self.square_size, self.square_size, self.square_size)
            pygame.draw.rect(board, (220, 183, 19), rect, 3)

        # draw the board on the screen at the center
        screen.blit(board, ((screen.get_width() - self.width) // 2, (screen.get_height() - self.height) // 2))
        pygame.display.flip()


    def highlight_square(self, file_index, rank_index):
        self.selected_position = file_index, rank_index
    
    def remove_highlight(self):
        self.selected_position = None
        

    # draw the board
    def drawBoard(self, board):
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    color = (242, 240, 221)  # white
                else:
                    color = (54, 117, 4)  # black
                pygame.draw.rect(board, color, (x * self.square_size, y * self.square_size, self.square_size, self.square_size))

        # number lines horizontally
        for rank in range(1, 9):
            text_surface = self.font.render(str(rank), True, pygame.Color('black'))
            board.blit(text_surface, (5, (8 - rank) * self.square_size + 0.25 * self.square_size - 12))

        # letter lines vertically
        for file in range(ord('a'), ord('h') + 1):
            text_surface = self.font.render(chr(file), True, pygame.Color('black'))
            board.blit(text_surface, ((file - ord('a')) * self.square_size + 0.15 * self.square_size - 6, self.height - 20))


    # draw the pieces
    def drawPieces(self, board):
        for piece in self.pieces:
            # get the position of the piece
            position = piece.position
            file_index = ord(position[0]) - ord('a')
            rank_index = 8 - position[1]

            # place the piece on the board
            piece_sprite = pygame.image.load(piece.sprite())
            piece_sprite = pygame.transform.scale(piece_sprite, (self.square_size, self.square_size))
            board.blit(piece_sprite, (file_index * self.square_size, rank_index * self.square_size))


    # get piece
    def get_piece(self, file_index, rank_index):
        for piece in self.pieces:
            if piece.position == (file_index, rank_index):
                return f"{piece.color} {piece.__class__.__name__}"
        return "Empty Square"


    # move piece
    def move_piece(self, current_position, new_position):
        current_file, current_rank = current_position
        new_file, new_rank = new_position

        current_rank = int(current_rank)
        new_rank = int(new_rank)

        for piece in self.pieces:
            if piece.position == (current_file, current_rank):
                piece.position = (new_file, new_rank)
                break

        size = (640, 640)
        screen = pygame.display.set_mode(size)
        self.run_board(screen)
    
    def remove_piece(self, position, piece):
        file_index, rank_index = position
        rank_index = int(rank_index)


        for piece in self.pieces:
            if piece.position == (file_index, rank_index):
                self.pieces.remove(piece)
                # add captured piece to the list
                if piece.color == "white":
                    self.captured_pieces_white.append(piece.__class__.__name__.lower())
                else:
                    self.captured_pieces_black.append(piece.__class__.__name__.lower())
                break

    def change_piece(self, move, piece):
        coördinates = (move['current_position'][0], int(move['current_position'][1]))

        for piece_obj in self.pieces:
            if piece_obj.position == coördinates:
                # change to a knight
                if int(piece) == 1:
                    piece_obj.__class__ = Knight
                    print(f"pawn promoted to Knight")

                # change to a bishop
                if int(piece) == 2:
                    piece_obj.__class__ = Bishop
                    print(f"pawn promoted to Bishop")

                # change to a rook
                if int(piece) == 3:
                    piece_obj.__class__ = Rook
                    print(f"pawn promoted to Rook")

                if int(piece) == 4:
                    piece_obj.__class__ = Queen
                    print(f"pawn promoted to Queen")
                break
