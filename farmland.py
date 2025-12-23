import entity
import pygame
import game_manager
import plant


class Farmland(entity.Entity):
    def __init__(self, pos_x: int, pos_y: int, images: dict[str, pygame.Surface], game: game_manager.Game) -> None:
        super().__init__(pos_x, pos_y, images)
        self.set_hitbox((24, 24), (16, 16))
        self._image: pygame.Surface = self.images["player"]
        self.plant: plant.Plant = None

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self.get_position())
