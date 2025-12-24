import math
import pygame
import time
from typing import Final, no_type_check

import entity
import key_handler
import player
import asset_handler
import world_manager
from ui import UI


def check_collision(user: player.Player, entity_list: list[entity.Entity]) -> None:
    for e in entity_list:
        if user.get_hitbox().colliderect(e.get_hitbox()):
            e.collide_logic(user)

# GETS MOVEMENT FROM KEYBOARD FOR THE PLAYER
def get_movement_from_keyboard(dt_velocity: float, game: Game) -> tuple[float, float]:

    # DIAGONAL MOVEMENT FACTOR FOR 8 DIRECTION MOVEMENT
    diagonal_movement_factor: float = (math.sqrt(2) / 2)

    # CHANGE VELOCITY BASED ON KEY PRESSED
    velo_x: float = 0
    velo_y: float = 0
    if game.key_h.a_pressed:
        velo_x = -dt_velocity
    if game.key_h.d__pressed:
        velo_x = dt_velocity
    if game.key_h.w_pressed:
        velo_y = -dt_velocity
    if game.key_h.s_pressed:
        velo_y = dt_velocity

    # MULTIPLY VELOCITY BY DIAGONAL FACTOR IF MOVING IN BOTH X AND Y AXIS
    if velo_x != 0 and velo_y != 0:
        velo_x *= diagonal_movement_factor
        velo_y *= diagonal_movement_factor

    return round(velo_x), round(velo_y)

class Game:
    def __init__(self):
        pygame.init()

        # LOAD GAME ASSETS
        self.assets = asset_handler.AssetHandler()
        self.assets.load_images()

        # INIT VARIABLES
        self.clock = pygame.time.Clock()
        self.SCREEN_WIDTH: Final[int] = 1024
        self.SCREEN_HEIGHT: Final[int] = 768
        self.TILE_SIZE: Final[int] = 64
        self.running: bool = True
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Farm Wars")
        self.canvas = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.BLACK: Final[tuple] = (0, 0, 0)
        self.text_font = pygame.font.SysFont("Arial", 48, True)

        self.user: player.Player = player.Player(10, 10, self.assets.player_images, 300, self)
        self.w_manager = world_manager.WorldManager("world_files", self)
        self.key_h: key_handler.KeyHandler = key_handler.KeyHandler(self)
        self.last_time: float = time.time()
        self.current_time: float = 0.0
        self.dt: float = 0
        self.FPS: int = 60
        self.game_states: list[str] = ["PLAY", "MAIN_MENU", "INVENTORY"]
        self.game_state: str = self.game_states[0]
        self.entity_list: list[entity.Entity] = []
        self.ui: UI = UI(self)

        temp_list = self.w_manager.load_world_entities("world_0")
        for e in temp_list:
            self.entity_list.append(e)


    # MAIN GAME LOOP FUNCTION
    def run(self) -> None:
        # MAIN GAME LOOP
        while self.running:

            # CALCULATE DELTA TIME
            self.clock.tick(60)
            self.current_time = time.time()
            self.dt = self.current_time - self.last_time
            self.last_time = self.current_time

            # FILL SCREEN BLACK
            self.screen.fill(self.BLACK)
            self.canvas.fill(self.BLACK)

            self.key_h.get_key_pressed()
            # DRAW CURRENT WORLD
            self.w_manager.draw_world("world_0", self.canvas)
            check_collision(self.user, self.entity_list)
            for e in self.entity_list:
                e.update()
                e.draw(self.canvas)
                # DEBUG pygame.draw.rect(self.canvas, pygame.Color("white"), e.get_hitbox())

            self.user.update(self.dt)
            self.user.draw(self.canvas)

            # CHECK GAME EVENTS
            for event in pygame.event.get():
                # STOP GAME LOOP IF WINDOW IS CLOSED/ GAME IS QUIT
                if event.type == pygame.QUIT or self.key_h.exit_pressed:
                    self.running = False
                    break

            self.ui.update()

            # UPDATE THE DISPLAY
            self.screen.blit(self.canvas, (0, 0))

            pygame.display.update()

        # QUIT GAME
        pygame.quit()
