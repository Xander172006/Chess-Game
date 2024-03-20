import pygame
from subclasses.pawn import Pawn
from Position import Position

class Board:
    def __init__(self, pieces):
        self.square_size = 75 
        self.width = 8 * self.square_size
        self.height = 8 * self.square_size
        
        self.font = pygame.font.Font(None, 20)
        self.pieces = pieces


    # instantiate the board
    def mainloop(self, screen):
        board = pygame.surface.Surface((self.width, self.height))
        board.fill((203, 172, 129))

        # initialize the board position
        self.drawBoard(board)
        self.drawPieces(board)

        # create chessboard
        screen.blit(board, (20, 20))
        pygame.display.flip()
        

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

            # return the current position from getPosition
            str(Position(file_index, rank_index, piece, piece.color))

    # get the piece
    def get_piece(self, file_index, rank_index):
        for piece in self.pieces:
            if piece.position == (file_index, rank_index):
                return piece
            
        return "Empty Square"