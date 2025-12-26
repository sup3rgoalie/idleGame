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


    def collide_logic(self, e: Entity) -> None:
        if isinstance(e, player.Player):
            if self._game.key_h.enter_pressed:
                self._game.current_world = self._game.w_manager.get_worlds()[self._world_name]

