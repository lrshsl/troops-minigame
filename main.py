import enum, signal

import pygame
from pygame import Vector2
vec2 = Vector2

from src.levels import towers, get_tower_at
from src.tower import TroopTower
from src.screen import screen
from src.utils import draw_text_center
from src.server.client import start_client
from src.constants import *

class InputState(enum.Enum):
    Idle = enum.auto()
    DraggingTroops = enum.auto()
    SelectingTroops = enum.auto()

clock = pygame.time.Clock()
FPS = 60
dt = 0
running = True


drag_start: tuple[int, int] = 0, 0
drag_end  : tuple[int, int] = 0, 0
troops_to_be_sent: int = 0

input_state = InputState.Idle

def send_troops(s, t1, t2):
    if t1.color != p_color: return
    if troops_to_be_sent <= 0: return

    s.sendall(f"send {t1} {t2}\n".encode())

    t1.n_troops -= troops_to_be_sent
    if t1.color == t2.color:
        t2.n_troops += troops_to_be_sent
    else:
        t2.n_troops -= troops_to_be_sent
        if t2.n_troops <= 0:
            t2.n_troops *= -1
            t2.color = p_color

def show_drag(start_pos, end_pos) -> None:
    pygame.draw.line(screen, "white", start_pos, end_pos)

def show_num_troops() -> None:
    draw_text_center(screen, troops_to_be_sent,
        screen.get_width() - 50,
        screen.get_height() // 2,
        "white")

def main_loop(s):
    global dt, running, drag_start, drag_end, troops_to_be_sent, input_state

    while running:
        screen.fill(bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Left click (pressed)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # Drag (Source selected)
                if input_state == InputState.Idle:
                    t = get_tower_at(event.pos)
                    source_tower = t
                    if t is not None and t.color == p_color:
                        drag_start = event.pos
                        troops_to_be_sent = t.n_troops
                        source_tower = t
                        input_state = InputState.DraggingTroops

                # Send troops confirmation
                elif input_state == InputState.SelectingTroops:
                    input_state = InputState.Idle
                    if target_tower := get_tower_at(drag_end):
                        assert drag_start is not None
                        send_troops(s, source_tower, target_tower)

            # Left click (released)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                # Drag (Target selected)
                if input_state == InputState.DraggingTroops:
                    drag_end = event.pos
                    input_state = InputState.SelectingTroops

            # Mouse wheel
            if event.type == pygame.MOUSEWHEEL and input_state == InputState.SelectingTroops:
                n = troops_to_be_sent + event.y
                troops_to_be_sent = max(min(n, source_tower.n_troops), 0)


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
                show_num_troops()
            case _:
                assert input_state == InputState.Idle, "Unknown input_state"

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    start_client(main_loop)
    pygame.quit()

# vim: et ts=4 sts=4 sw=4

