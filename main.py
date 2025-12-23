import pygame
import time
from typing import Final
import game_manager
import player
import asset_handler
import world_manager

pygame.init()

# LOAD GAME ASSETS
assets = asset_handler.AssetHandler()
assets.load_images()

# INIT VARIABLES
clock = pygame.time.Clock()
SCREEN_WIDTH: Final[int] = 1024
SCREEN_HEIGHT: Final[int] = 768
TILE_SIZE: Final[int] = 64
running: bool = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Farm Wars")
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK: Final[tuple] = (0, 0, 0)

user: player.Player = player.Player(10, 10, assets.player_image, 300)
w_manager = world_manager.WorldManager("world_files")
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

    # FILL SCREEN BLACK
    screen.fill(BLACK)
    canvas.fill(BLACK)

    world_manager.draw_world(w_manager.worlds["world_0"], assets, canvas, TILE_SIZE)

    user.update(dt)
    user.draw(canvas)

    # CHECK GAME EVENTS
    for event in pygame.event.get():
        # STOP GAME LOOP IF WINDOW IS CLOSED/ GAME IS QUIT
        if event.type == pygame.QUIT:
            running = False
            break

    # UPDATE THE DISPLAY
    screen.blit(canvas, (0, 0))
    pygame.display.update()


# QUIT GAME
pygame.quit()
