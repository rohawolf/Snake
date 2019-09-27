from random import randint
from snake.UI import *


class Apple:
    """Apple Object"""
    color = RED

    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self, screen):
        draw_block(screen, self.color, self.position)


class Snake:
    """Snake Object"""
    color = GREEN

    def __init__(self, length=4, head=(6, 6), delta=(0, 1)):
        self.length = length
        self.delta = delta
        self.head = head
        self.tail = []

        for i in range(1, self.length):
            tail = (self.head[0] - i * self.delta[0],
                    self.head[1] - i * self.delta[1])
            self.tail.append(tail)

    def draw(self, screen):
        # draw head
        draw_block(screen, self.color, self.head)

        # draw trailing tails
        for tail_pos in self.tail:
            draw_block(screen, self.color, tail_pos)

    def set_delta(self, delta):
        self.delta = delta

    def crawl(self):
        # add current head as tail
        self.tail = [self.head] + self.tail[:-1]

        # set next head
        self.head = tuple(sum(pos) for pos in zip(self.head, self.delta))

    def grow(self):
        last_two_tail_pos = self.tail[-2:]
        self.tail.append(tuple(2 * d - p for p, d in zip(*last_two_tail_pos)))


class Board:
    """Game Board Object"""

    def __init__(self, width=20, height=20, snake=Snake(), apple=Apple()):
        self.width = width
        self.height = height
        self.snake = snake
        self.apple = apple

    def draw(self, screen):
        self.snake.draw(screen)
        self.apple.draw(screen)

    def processing(self):
        self.snake.crawl()

        # case.1 snake eat apple
        if self.snake.head == self.apple.position:
            self.snake.grow()
            self.put_new_apple()

    def put_new_apple(self):
        not_available_positions = [self.snake.head] + self.snake.tail
        self.apple = Apple((randint(0, 19), randint(0, 19)))
        for pos in not_available_positions:
            if self.apple.position == pos:
                self.put_new_apple()
                break
