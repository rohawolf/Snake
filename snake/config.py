import pygame

class Screen:
    BLOCK_SIZE = 20
    WIDTH = BLOCK_SIZE * 20
    HEIGHT = BLOCK_SIZE * 20
    

class Colors:
    RED = 255, 0, 0  # R 255, G 0, B 0
    GREEN = 0, 255, 0  # R 0, G 5, B 0
    BLUE = 0, 0, 255  # R 0, G 0, B 255
    PURPLE = 127, 0, 127  # R 127, G 0, B 127
    BLACK = 0, 0, 0  # R 0, G 0, B 0
    GRAY = 127, 127, 127  # R 127, G 127, B 127
    WHITE = 255, 255, 255  # R 255, G 5, B 255

class Controller:
    DIRECTION_ON_KEY = {
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0),
    }
