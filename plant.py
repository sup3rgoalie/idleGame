import pygame

class Plant:
    def __init__(self, position: tuple[int, int], images: list[pygame.Surface]) -> None:
        self.position = position
        self.images = images