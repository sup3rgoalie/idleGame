import pygame


class Item:
    def __init__(self, item_attributes: dict[str, str], item_images: dict[str, pygame.Surface]) -> None:
        self._item_type: str = item_attributes["type"]
        self._item_description: str = item_attributes["description"]
        self._item_images: dict[str, pygame.Surface] = item_images

    def get_images(self) -> dict[str, pygame.Surface]:
        return self._item_images
