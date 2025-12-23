import pygame

class Plant:
    def __init__(self, position: tuple[int, int], images: dict[str, pygame.Surface]) -> None:
        self._position: tuple[int, int] = position
        self._images: dict[str, pygame.Surface] = images
        self._image: pygame.Surface = self.images["plant"]

    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, self._position)