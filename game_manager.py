import math
from typing import Final

import pygame
import time
import entity
import key_handler
import player
import asset_handler
import world
import world_manager
from ui import UI


def blit_rotate(surf, image, pos, origin_pos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - origin_pos[0], pos[1] - origin_pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


def check_collision(user: player.Player, entity_list: list[entity.Entity]) -> None:
    for e in entity_list:
        if user.get_hitbox().colliderect(e.get_hitbox()):
            e.collide_logic(user)


class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH: Final[int] = 1024
        self.SCREEN_HEIGHT: Final[int] = 768
        self.TILE_SIZE: Final[int] = 64
        self.BLACK: Final[tuple] = (0, 0, 0)
        self.running: bool = True
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Farm Wars")
        self.canvas = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # LOAD GAME ASSETS
        self.assets = asset_handler.AssetHandler()
        self.assets.load_images()

        self.w_manager = world_manager.WorldManager(self)
        self.w_manager.load_tile_config()
        self.w_manager.load_worlds("world_files")
        self.w_manager.change_world("world_0")

        # INIT VARIABLES
        self.clock = pygame.time.Clock()
        self.text_font = pygame.font.SysFont("Arial", 48, True)

        self.user: player.Player = player.Player(10, 10, self.assets.player_images, 300, self)
        self.key_h: key_handler.KeyHandler = key_handler.KeyHandler(self)
        self.last_time: float = time.time()
        self.current_time: float = 0.0
        self.dt: float = 0
        self.FPS: int = 60
        self.game_states: list[str] = ["PLAY", "MAIN_MENU", "INVENTORY"]
        self.game_state: str = self.game_states[0]
        self.entity_list: list[entity.Entity] = []
        self.ui: UI = UI(self)
        self.left_click: bool = False
        self.right_click: bool = False
        self.middle_click: bool = False



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

            # CHECK GAME EVENTS
            for event in pygame.event.get():
                # STOP GAME LOOP IF WINDOW IS CLOSED/ GAME IS QUIT
                if event.type == pygame.QUIT or self.key_h.exit_pressed:
                    self.running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.left_click = True
                    if event.button == 2:
                        self.middle_click = True
                    if event.button == 3:
                        self.right_click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.left_click = False
                    if event.button == 2:
                        self.middle_click = False
                    if event.button == 3:
                        self.right_click = False

            self.key_h.get_key_pressed()
            # DRAW CURRENT WORLD
            self.w_manager.draw_world(self.w_manager.current_world.name, self.canvas)

            for world_name in self.w_manager.get_worlds():
                for e in self.w_manager.get_worlds()[world_name].entities:
                    e.update()

            for e in self.w_manager.current_world.entities:
                e.draw(self.canvas)

            self.user.update(self.dt)
            self.user.draw(self.canvas)
            if self.key_h.tab_pressed:
                self.game_state = self.game_states[2]
            else:
                self.game_state = self.game_states[0]
            self.ui.update()

            # UPDATE THE DISPLAY
            self.screen.blit(self.canvas, (0, 0))

            pygame.display.update()

        # QUIT GAME
        pygame.quit()
