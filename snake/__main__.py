from datetime import datetime, timedelta

from snake.exceptions import *
from snake.models import *
from snake.settings import *
from snake.UI import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE!")
    
    LAST_MOVED_TIME = datetime.now()
    game_board = Board()

    playing = True
    while playing:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                playing = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False

                if event.key in DIRECTION_ON_KEY:
                    game_board.snake.set_delta(DIRECTION_ON_KEY[event.key])

        if datetime.now() - LAST_MOVED_TIME > game_board.time_interval:
            try:
                game_board.processing()
            except (SnakeCollideItselfException, SnakeOutOfBoundaryException):
                playing = False

            LAST_MOVED_TIME = datetime.now()

        draw_background(screen)
        game_board.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
