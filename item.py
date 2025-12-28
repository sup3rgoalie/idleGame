import pygame

class Item:
    def __init__(self, item_attributes: dict[str, str], item_images: dict[str, pygame.Surface]) -> None:
        self._item_type: str = item_attributes["type"]
        self._item_name: str = item_attributes["name"]
        self._item_damage: str = item_attributes["damage"]
        self._item_images: dict[str, pygame.Surface] = item_images
