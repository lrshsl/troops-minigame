from random import randint

from src.screen import screen
from src.tower import TroopTower
from src.constants import *

_w = screen.get_width()
_h = screen.get_height()
hmargin = _w // 10
towers = [
        TroopTower(
            randint(tower_size, _w // 3 - hmargin),
            randint(tower_size, _h - tower_size),
            p_color)
        for _ in range(5)
    ] + [
        TroopTower(
            randint(_w // 3 + hmargin, _w * 2 // 3 - hmargin),
            randint(tower_size, _h - tower_size),
            neutral_color)
        for _ in range(5)
    ] + [
        TroopTower(
            randint(_w * 2 // 3 + hmargin, _w - tower_size),
            randint(tower_size, _h - tower_size),
            enemy_color)
        for _ in range(5)
    ]

def get_tower_index_at(pos) -> int | None:
    for i, t in enumerate(towers):
        if t.rect.collidepoint(pos):
            return i

def get_tower_at(pos) -> TroopTower | None:
    for t in towers:
        if t.rect.collidepoint(pos):
            return t
