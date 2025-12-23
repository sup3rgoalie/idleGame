import entity
import pygame
import game_manager
import plant


class Farmland(entity.Entity):
    def __init__(self, pos_x: int, pos_y: int, images: dict[str, pygame.Surface], game: game_manager.Game) -> None:
        super().__init__(pos_x, pos_y, images)
        self.game: game_manager.Game = game
        self.set_hitbox((24, 24), (16, 16))
        self._image: pygame.Surface = self._images["farmland_healthy"]
        self._plant: plant.Plant = plant.Plant("wheat", self.get_position(), self.game)

    def update(self) -> None:
        self._plant.update()
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self.get_position())
        self._plant.draw(screen)
