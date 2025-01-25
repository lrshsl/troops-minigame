from random import randint
import enum
import pygame
from pygame import Vector2
vec2 = Vector2

from src.tower import TroopTower
from src.constants import *

class InputState(enum.Enum):
    Idle = enum.auto()
    DraggingTroops = enum.auto()
    SelectingTroops = enum.auto()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60
running = True
dt = 0

drag_start: tuple[int, int] = 0, 0
drag_end  : tuple[int, int] = 0, 0

input_state = InputState.Idle

w = screen.get_width()
h = screen.get_height()
towers = [
        TroopTower(
            randint(w // 2, w - tower_size),
            randint(h // 2, h - tower_size),
            p_color)
        for _ in range(5)
    ] + [
        TroopTower(
            randint(0, w // 2 - tower_size),
            randint(0, h // 2 - tower_size),
            enemy_color)
        for _ in range(3)
    ]

def get_tower_at(pos) -> TroopTower | None:
    for t in towers:
        if t.rect.collidepoint(pos):
            return t

def send_troops(t1, t2):
    if t1.color != p_color: return
    if t1.n_troops <= 0: return

    troops = t1.n_troops // 2
    t1.n_troops -= troops
    if t1.color == t2.color:
        t2.n_troops += troops
    else:
        t2.n_troops -= troops
        if t2.n_troops <= 0:
            t2.n_troops *= -1
            t2.color = p_color

def show_drag(start_pos, end_pos):
    pygame.draw.line(screen, "white", start_pos, end_pos)

while running:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        
        # Left click (pressed)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if input_state == InputState.Idle and get_tower_at(event.pos):
                drag_start = event.pos
            elif input_state == InputState.SelectingTroops:
                input_state = InputState.Idle
                if t2 := get_tower_at(drag_end):
                    assert drag_start is not None
                    t1 = get_tower_at(drag_start)
                    send_troops(t1, t2)
        
        # Left click (released)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if input_state == InputState.DraggingTroops:
                drag_end = event.pos
                input_state = InputState.SelectingTroops

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    for tower in towers:
        tower.update(dt)

    for tower in towers:
        tower.draw(screen)

    match input_state:
        case InputState.DraggingTroops:
            show_drag(drag_start, pygame.mouse.get_pos())
        case InputState.SelectingTroops:
            show_drag(drag_start, drag_end)
        case _:
            assert input_state == InputState.Idle, "Unknown input_state"

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()