import pygame
from pygame import Color

def draw_text_center(surface, text, x: int, y: int, color: Color):
    font = pygame.font.Font(None, 42)
    text = font.render(str(text), True, color)
    textpos = text.get_rect(
        centerx=x,
        centery=y)
    surface.blit(text, textpos)