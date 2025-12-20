from plistlib import InvalidFileException
import pygame

class AssetHandler:
    def __init__(self) -> None:
        self.player_image: pygame.Surface = None

    def load_images(self) -> None:
        try:
            self.player_image = pygame.image.load("assets/player_placeholder.png")
            exit()
        except FileNotFoundError:
            print("FILE NOT FOUND, FATAL ERROR")
            exit()
        except InvalidFileException:
            print("INVALID FILE, FATAL ERROR")
            exit()