from random import randint

from snake.config import *
from snake.exceptions import SnakeExc
from snake.objects import Apple, Snake
from snake.rendering import draw_background, draw_text

class Board:
    def __init__(self, font, width=20, height=20, snake:Snake=None, apple:Apple=None):
        self.width = width
        self.height = height
        self.font = font
        
        self.snake = snake or Snake()
        self.apple = None
        self.eaten_apple_count = 0
        self.tick = self.snake.frequency
    
    def draw(self, screen):
        self.snake.draw(screen)
        self.apple.draw(screen)

    def put_new_apple(self):
        not_available_positions = [self.snake.head] + self.snake.tail

        def _find_new_apple_position():
            new_position = (randint(1, self.width) - 1, randint(1, self.height) - 1)
            if new_position in not_available_positions:
                new_position = _find_new_apple_position()

            return new_position
        
        self.apple = Apple(_find_new_apple_position())

    def processing(self):
        self.snake.processing(range(self.height), range(self.width))

        # put new random apple
        if self.apple is None:
            self.put_new_apple()

        # when snake eat apple
        if self.snake.head == self.apple.position:
            self.eaten_apple_count += 1
            self.snake.grow()
            self.put_new_apple()

        self.snake.crawl()
        self.tick = self.snake.frequency


def main():
    pygame.init()
    pygame.display.set_caption('SNAKE')
    screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT + Screen.BLOCK_SIZE))

    clock = pygame.time.Clock()
    general_font = pygame.font.SysFont('arial', 15)
    game_board = Board(general_font)

    def status_bar(text):
        draw_text(screen, general_font, text, Colors.WHITE, (1, game_board.height))

    game_on = True
    game_status = 'initial'

    while game_on:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game_on = False

            elif event.type == pygame.KEYDOWN:
                if event.key in Controller.DIRECTION_ON_KEY:
                    if game_status == 'playing':
                        game_board.snake.set_delta(Controller.DIRECTION_ON_KEY[event.key])

                if event.key == pygame.K_RETURN:
                    if game_status in ['initial', 'gameover']:
                        if game_status == 'gameover':
                            game_board = Board(general_font)
                        game_status = 'playing'

        try:
            screen.fill(Colors.BLACK)
            draw_background(screen)

            if game_status in ['initial', 'gameover']:
                text = f"{'GAME OVER! ' if game_status == 'gameover' else ''}PRESS ENTER TO START"

            elif game_status == 'playing':
                game_board.processing()
                game_board.draw(screen)
                text = f'SCORE: {100 * game_board.eaten_apple_count}'

            status_bar(text)
            pygame.display.flip()
            clock.tick(game_board.tick)

        except (SnakeExc.CollideItself, SnakeExc.OutOfBoundary):
            game_status = 'gameover'

        
