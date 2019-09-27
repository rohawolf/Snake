from datetime import datetime, timedelta

from snake.models import *
from snake.settings import *
from snake.UI import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    LAST_MOVED_TIME = datetime.now()
    TIME_INTERVAL = timedelta(seconds=0.3)

    game_board = Board()

    playing = True
    while playing:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                playing = False

            elif event.type == pygame.KEYDOWN:
                if event.key in DIRECTION_ON_KEY:
                    game_board.snake.set_delta(DIRECTION_ON_KEY[event.key])

        if datetime.now() - LAST_MOVED_TIME > TIME_INTERVAL:
            game_board.processing()
            LAST_MOVED_TIME = datetime.now()

        draw_background(screen)
        game_board.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
