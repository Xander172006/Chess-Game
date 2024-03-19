import pygame

class Board:
    def __init__(self, pieces):
        # set board size
        self.square_size = 75 
        self.width = 8 * self.square_size
        self.height = 8 * self.square_size

        # set fontsize text
        self.font = pygame.font.Font(None, 18)

        # set the pieces
        self.pieces = pieces

    def mainloop(self, screen):
        # customize the surface and color of the board
        board = pygame.surface.Surface((self.width, self.height))
        board.fill((203, 172, 129))

        # create chessboard
        self.drawBoard(board, screen)

    def drawBoard(self, board, screen):
        # Draw the board squares
        for x in range(0, 8):
            for y in range(0, 8):
                if (x + y) % 2 == 0:
                    color = (249, 220, 186 ) # white
                else:
                    color = (109, 92, 74 ) # black
                pygame.draw.rect(board, color, (x * self.square_size, y * self.square_size, self.square_size, self.square_size))

        # Draw number lines horizontally
        for rank in range(1, 9):
            text_surface = self.font.render(str(rank), True, pygame.Color('#FFFFFF'))
            board.blit(text_surface, (5, (8 - rank) * self.square_size + 0.5 * self.square_size - 12))


        # Draw letter lines vertically
        for file in range(ord('a'), ord('h') + 1):
            text_surface = self.font.render(chr(file), True, pygame.Color('#FFFFFF'))
            board.blit(text_surface, ((file - ord('a')) * self.square_size + 0.5 * self.square_size - 6, self.height - 20))


        # Set piece icons on the board
        for piece in self.pieces:
            piece_icon = pygame.transform.scale(pygame.image.load(piece.capture()), (self.square_size, self.square_size))

            # get the index of the piece
            file_index = ord(piece.position[0]) - ord('a')
            rank_index = 8 - piece.position[1]  
            board.blit(piece_icon, (file_index * self.square_size, rank_index * self.square_size))


        # display the board
        screen.blit(board, (20, 20))
        pygame.display.flip()

    # get the piece on the square
    def get_piece(self, file_index, rank_index):
        for piece in self.pieces:
            if piece.position == (file_index, rank_index):
                return f"{piece.color}_{piece.__class__.__name__.lower()}"

        return 'Empty Square'

