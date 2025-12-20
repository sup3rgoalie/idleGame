from asyncio.windows_events import NULL
from traceback import print_exception

import pygame

class AssetHandler:
    def __init__(self):
        self.player_image: pygame.Surface = None

    def load_images(self) -> bool:
        try:
            self.player_image = pygame.image.load("assets/player_placeholder.png")

            return True
        except FileNotFoundError:
            print("FILE NOT FOUND, FATAL ERROR")
            return False