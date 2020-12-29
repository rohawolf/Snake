import pygame

from snake.config import *

def draw_block(screen, color, position):
    """Draw block with color at position"""
    block = pygame.Rect((position[0] * Screen.BLOCK_SIZE, position[1] * Screen.BLOCK_SIZE), (Screen.BLOCK_SIZE, Screen.BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

def draw_background(screen):
    """ Draw background of pygame screen"""
    background = pygame.Rect((0, 0), (Screen.WIDTH, Screen.HEIGHT))
    pygame.draw.rect(screen, Colors.GRAY, background)

def draw_text(screen, font_style, text, color, position):
    text_img = font_style.render(text, True, color)
    screen.blit(text_img, (position[0] * Screen.BLOCK_SIZE, position[1] * Screen.BLOCK_SIZE))
