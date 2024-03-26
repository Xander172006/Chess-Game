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

        self.captured_pieces_white = []
        self.captured_pieces_black = []
        
        self.font = pygame.font.Font(None, 20)
        self.pieces = self.create_pieces()


    # create pieces
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
        board.fill((203, 172, 129))

        # initialize the board position
        self.drawBoard(board)
        self.drawPieces(board)

        # highlight the selected square
        if self.selected_position:
            x = ord(self.selected_position[0]) - ord('a')
            y = 8 - self.selected_position[1]
            rect = pygame.Rect(x * self.square_size, y * self.square_size, self.square_size, self.square_size)
            pygame.draw.rect(board, (255, 0, 0), rect, 3)

        screen.blit(board, (20, 20))
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
                    color = (249, 220, 186)  # white
                else:
                    color = (109, 92, 74)  # black
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

    def all_pieces(self):
        pieces_dict = {}
        for piece in self.pieces:
            # Assuming each piece has a 'position' attribute
            position = piece.position
            pieces_dict[position] = f"{piece.color} {piece.__class__.__name__.lower()}"
        return pieces_dict
    
    def remove_piece(self, position, piece):
        file_index, rank_index = position
        rank_index = int(rank_index)

        for piece in self.pieces:
            if piece.position == (file_index, rank_index):
                self.pieces.remove(piece)
                break

