import pygame
import time
from typing import Final
import game_manager
import render_manager

# INIT VARIABLES
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH: Final[int] = 1080
SCREEN_HEIGHT: Final[int] = 720
running: bool = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((10, 10, 50, 50))
BLACK: Final[tuple] = (0, 0, 0)

velocity: int = 300
last_time: float = time.time()
current_time: float = 0.0
dt: float = 0
FPS: int = 60

# MAIN GAME LOOP
while running:

    # CALCULATE DELTA TIME
    clock.tick(FPS)
    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time
    dt_velocity = velocity * dt

    # FILL SCREEN BLACK
    screen.fill(BLACK)
    canvas.fill(BLACK)

    # DRAW RECT TO REPRESENT PLAYER
    pygame.draw.rect(canvas, (255, 0, 0), player)
    player.move_ip(game_manager.get_movement(pygame, dt_velocity))

    # CHECK GAME EVENTS
    for event in pygame.event.get():

        # STOP GAME LOOP IF WINDOW IS CLOSED/ GAME IS QUIT
        if event.type == pygame.QUIT:
            running = False

    screen.blit(canvas, (0, 0))
    # UPDATE THE DISPLAY
    pygame.display.update()

# QUIT GAME
pygame.quit()
