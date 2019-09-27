from datetime import datetime, timedelta
from snake.settings import *


def draw_background(screen, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    """ Draw background of pygame screen"""
    background = pygame.Rect((0, 0), (width, height))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position, block_size=BLOCK_SIZE):
    """Draw block with color at position"""
    block = pygame.Rect((position[1] * block_size, position[0] * block_size), (block_size, block_size))
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
