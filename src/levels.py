from random import randint

from src.tower import TroopTower
from src.constants import *

towers = [
        TroopTower(
            randint(tower_size, W // 3 - hmargin),
            randint(tower_size, H - tower_size),
            p1_color)
        for _ in range(5)
    ] + [
        TroopTower(
            randint(W // 3 + hmargin, W * 2 // 3 - hmargin),
            randint(tower_size, H - tower_size),
            n_color)
        for _ in range(5)
    ] + [
        TroopTower(
            randint(W * 2 // 3 + hmargin, W - tower_size),
            randint(tower_size, H - tower_size),
            p2_color)
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
