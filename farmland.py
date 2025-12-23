import entity
import pygame
import game_manager


class Farmland(entity.Entity):
    def __init__(self, pos_x: int, pos_y: int, image: pygame.Surface, game: game_manager.Game) -> None:
        super().__init__(pos_x, pos_y, image)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self.get_position())
