import pygame

class Entity:
    def __init__(self, x: float, y: float, image: pygame.Surface) -> None:
        self.__x: float = x
        self.__y: float = y
        self.__velocity: tuple[float, float] = (0, 0)
        self.__image: pygame.Surface = image
        self.__hitbox: pygame.Rect = pygame.Rect(self.x, self.y, 10, 10)

    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def get_position(self) -> tuple[float, float]:
        return self.__x, self.__y

    def get_hitbox(self) -> pygame.Rect:
        return self.__hitbox