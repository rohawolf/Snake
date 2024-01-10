from snake.config import Colors
from snake.exceptions import SnakeExc
from snake.rendering import draw_block


class Apple:
    """Apple Object"""
    color=Colors.RED

    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self, screen):
        draw_block(screen, self.color, self.position)


class Snake:
    """Snake Object"""
    head_color=Colors.BLUE
    color=Colors.GREEN

    def __init__(self, length=4, head=(6, 6), delta=(1, 0)):
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
        draw_block(screen, self.head_color, self.head)

        # draw trailing tails
        for tail_pos in self.tail:
            draw_block(screen, self.color, tail_pos)

    def set_delta(self, delta):
        checker = tuple(sum(p) for p in zip(self.delta, delta))
        if 0 not in checker:
            self.delta = delta

    def crawl(self):
        # add current head as tail
        self.tail = [self.head] + self.tail[:-1]

        # set next head
        self.head = tuple(sum(pos) for pos in zip(self.head, self.delta))

    def grow(self):
        last_two_tail_pos = self.tail[-2:]
        self.tail.append(tuple(2 * d - p for p, d in zip(*last_two_tail_pos)))

    def processing(self, board_height_range:range, board_width_range:range):
        # when snake collide itself
        if self.head in self.tail:
            raise SnakeExc.CollideItself()
    
        # when snake out of boundary
        if (
            self.head[0] not in board_height_range
            or self.head[1] not in board_width_range
        ):
            raise SnakeExc.OutOfBoundary()
    
    @property
    def frequency(self):
        return 5 - 0.1 * int(self.length / 5)