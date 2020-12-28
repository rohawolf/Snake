import pygame


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# COLORS
RED = 255, 0, 0  # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0  # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255  # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127  # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0  # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127  # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

DIRECTION_ON_KEY = {
    pygame.K_UP: [-1, 0],
    pygame.K_DOWN: [1, 0],
    pygame.K_LEFT: [0, -1],
    pygame.K_RIGHT: [0, 1],
}


def draw_background(screen):
    """ Draw background of pygame screen"""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, BLACK, background)


def draw_block(screen, color, position):
    """Draw block with color at position"""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


def draw_text(screen, text, color, position):
    font = pygame.font.SysFont(None, 48)
    text_img = font.render(text, True, color)
    screen.blit(text_img, position)
