import pygame
from datetime import datetime, timedelta

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
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    """Draw block with color at position"""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    LAST_POSITION = [0, 0]
    LAST_DELTA = [0, 1]
    LAST_MOVED_TIME = datetime.now()

    playing = True
    while playing:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                playing = False

            elif event.type == pygame.KEYDOWN:
                if event.key in DIRECTION_ON_KEY:
                    LAST_DELTA = DIRECTION_ON_KEY[event.key]

        next_pos = LAST_POSITION
        if datetime.now() - LAST_MOVED_TIME >= timedelta(seconds=1):
            next_pos = tuple(sum(pos) for pos in zip(LAST_POSITION, LAST_DELTA))
            LAST_MOVED_TIME = datetime.now()
            LAST_POSITION = next_pos

        draw_background(screen)
        draw_block(screen, GREEN, next_pos)
        pygame.display.update()


run()
