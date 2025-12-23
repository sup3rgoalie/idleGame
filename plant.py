import pygame

import game_manager


class Plant:
    def __init__(self, plant_type: str, position: tuple[int, int], game: game_manager.Game) -> None:
        self.game = game
        self._position: tuple[int, int] = position
        self._plant_type: str = plant_type
        self._growth_timer= 0
        self.can_be_harvested = False

        if self._plant_type == "wheat":
            self._images: dict[str, pygame.Surface] = game.assets.wheat_plant_images
            self._image: pygame.Surface = self._images["wheat_0"]
            self._grow_time: int = 1

    def get_plant_type(self) -> str:
        return self._plant_type


    def update(self) -> None:
        if not self.can_be_harvested:
            if self._growth_timer == self._grow_time * self.game.FPS:
                self._image: pygame.Surface = self._images["wheat_1"]
            elif self._growth_timer == 2 * self._grow_time * self.game.FPS:
                self._image: pygame.Surface = self._images["wheat_2"]
                self.can_be_harvested = True
            self._growth_timer += 1

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self._position)