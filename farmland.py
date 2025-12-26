import entity
import pygame
import game_manager
import plant
import player
from entity import Entity


class Farmland(entity.Entity):
    def __init__(self, pos_x: int, pos_y: int, images: dict[str, pygame.Surface], game: game_manager.Game) -> None:
        super().__init__(pos_x, pos_y, game, images)
        self.set_hitbox((30, 30), (4, 4))
        self._image: pygame.Surface = self._images["farmland_healthy"]
        self._plant: plant.Plant = plant.Plant("wheat", self.get_position(), self._game)

    def get_plant(self) -> plant.Plant:
        return self._plant

    def update(self) -> None:
        if self._plant is not None:
            self._plant.update()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self.get_position())
        if self._plant is not None:
            self._plant.draw(screen)

    def collide_logic(self, e: Entity) -> None:
        if isinstance(e, player.Player):
            if self._plant is not None:
                if self._plant.can_be_harvested and self._game.key_h.enter_pressed:
                    e.inventory[self._plant.get_plant_type()] += 1
                    self._plant = None
            elif self._game.key_h.space_pressed:
                self._plant = plant.Plant("wheat", self.get_position(), self._game)
            self._game.ui.add_farm_popup_to_ui((self._x - 16, self._y - 110), self)
