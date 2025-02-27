#Quinn Dickey
#5th hour
#ai playground


import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]]   # L
]

SHAPE_COLORS = [CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE]

# Class for the game
class Tetris:
    def __init__(self):
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.game_over = False
        self.current_shape = None
        self.current_pos = None
        self.score = 0

    def new_shape(self):
        shape_index = random.randint(0, len(SHAPES) - 1)
        self.current_shape = SHAPES[shape_index]
        self.shape_color = SHAPE_COLORS[shape_index]
        self.current_pos = [0, SCREEN_WIDTH // BLOCK_SIZE // 2 - len(self.current_shape[0]) // 2]

    def rotate_shape(self):
        self.current_shape = [list(x) for x in zip(*self.current_shape[::-1])]

    def move_left(self):
        self.current_pos[1] -= 1
        if self.check_collision():
            self.current_pos[1] += 1

    def move_right(self):
        self.current_pos[1] += 1
        if self.check_collision():
            self.current_pos[1] -= 1

    def move_down(self):
        self.current_pos[0] += 1
        if self.check_collision():
            self.current_pos[0] -= 1
            self.place_shape()
            self.clear_lines()
            if self.game_over:
                return False
            self.new_shape()
        return True

    def check_collision(self):
        for i, row in enumerate(self.current_shape):
            for j, block in enumerate(row):
                if block:
                    x = self.current_pos[0] + i
                    y = self.current_pos[1] + j
                    if x >= len(self.board) or y < 0 or y >= len(self.board[0]) or self.board[x][y]:
                        return True
        return False

    def place_shape(self):
        for i, row in enumerate(self.current_shape):
            for j, block in enumerate(row):
                if block:
                    x = self.current_pos[0] + i
                    y = self.current_pos[1] + j
                    self.board[x][y] = self.shape_color

    def clear_lines(self):
        full_lines = [i for i, row in enumerate(self.board) if all(cell for cell in row)]
        for line in full_lines:
            del self.board[line]
            self.board.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
            self.score += 100

    def draw(self):
        SCREEN.fill(BLACK)
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(SCREEN, cell, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        for i, row in enumerate(self.current_shape):
            for j, block in enumerate(row):
                if block:
                    pygame.draw.rect(SCREEN, self.shape_color, ((self.current_pos[1] + j) * BLOCK_SIZE, (self.current_pos[0] + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        self.new_shape()

        while not self.game_over:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.move_right()
                    elif event.key == pygame.K_DOWN:
                        self.move_down()
                    elif event.key == pygame.K_UP:
                        self.rotate_shape()

            if not self.move_down():
                break

            self.draw()

# Start the game
if __name__ == "__main__":
    game = Tetris()
    game.run()
    pygame.quit()