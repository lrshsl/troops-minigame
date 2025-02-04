import pygame
from pygame import Rect, Color, draw
from src.constants import *
from src.utils import draw_text_center

class TroopTower:
    rect: Rect
    color: Color
    n_troops: int
    
    time_since_last_prod: float = 0.0
    prod_rate: float = 1.0
    
    def __init__(self, x, y, color):
        self.rect = Rect(x, y, tower_size, tower_size)
        self.color = color
        self.n_troops = 0
    
    def draw(self, surface):
        draw.rect(surface, self.color, self.rect, 10)
        x, y = self.rect.center
        draw_text_center(surface, str(self.n_troops),
                         x, y, self.color)

    def update(self, dt: float):
        self.time_since_last_prod += dt
        if self.time_since_last_prod >= self.prod_rate:
            self.time_since_last_prod = 0
            self.n_troops += 1

