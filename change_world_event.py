import pygame

import entity
import game_manager
import player
from entity import Entity


class ChangeWorldEvent(entity.Entity):
    def __init__(self, pos_x: int, pos_y: int, size_x: int, size_y: int, world_name: str, game: game_manager.Game) -> None:
        super().__init__(pos_x, pos_y, game)
        self.set_hitbox((0, 0), (size_x, size_y))
        self._world_name = world_name
        self._cooldown_counter = 0
        self.loaded = False

    def update(self):
        if self.loaded:
            self._cooldown_counter += 1

    def collide_logic(self, e: Entity) -> None:
        if isinstance(e, player.Player):
            if self._game.key_h.enter_pressed and self._cooldown_counter > 60:
                self._cooldown_counter = 0
                self._game.w_manager.change_world(self._world_name)
                if self._x < 100:
                    self._game.user.set_positon(self._game.SCREEN_WIDTH - self._game.TILE_SIZE - 2, int(5.5 * self._game.TILE_SIZE))
                else:
                    self._game.user.set_positon(2, int(5.5 * self._game.TILE_SIZE))


