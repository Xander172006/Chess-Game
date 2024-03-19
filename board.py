import pygame

class Board:
    def __init__(self, pieces):
        self.square_size = 75  # Adjust the size of the squares
        self.width = 8 * self.square_size
        self.height = 8 * self.square_size
        self.pieces = pieces
        self.font = pygame.font.Font(None, 24)  # Choose your desired font size

    # Main loop
    def mainloop(self, screen):
        board = pygame.surface.Surface((self.width, self.height))
        board.fill((203, 172, 129))

        self.drawBoard(board, screen)

    # Draw the board
    def drawBoard(self, board, screen):
        # Draw the board squares
        for x in range(0, 8):
            for y in range(0, 8):
                if (x + y) % 2 == 0:
                    color = (50, 29, 11)
                else:
                    color = (203, 172, 129)
                pygame.draw.rect(board, color, (x * self.square_size, y * self.square_size, self.square_size, self.square_size))

        # Draw rank numbers (1 to 8)
        for rank in range(1, 9):
            text_surface = self.font.render(str(rank), True, pygame.Color('#FFFFFF'))
            board.blit(text_surface, (5, (8 - rank) * self.square_size + 0.5 * self.square_size - 12))

        # Draw file letters (a to h)
        for file in range(ord('a'), ord('h') + 1):
            text_surface = self.font.render(chr(file), True, pygame.Color('#FFFFFF'))
            board.blit(text_surface, ((file - ord('a')) * self.square_size + 0.5 * self.square_size - 6, self.height - 20))

        # Blit piece icons on the board
        for piece in self.pieces:
            piece_icon = pygame.transform.scale(pygame.image.load(piece.capture()), (self.square_size, self.square_size))
            file_index = ord(piece.position[0]) - ord('a')
            rank_index = 8 - piece.position[1]  # Adjust for 0-based indexing
            board.blit(piece_icon, (file_index * self.square_size, rank_index * self.square_size))

        screen.blit(board, (20, 20))
        pygame.display.flip()
