from plistlib import InvalidFileException
import pygame

class AssetHandler:
    def __init__(self) -> None:
        self.player_images: dict[str, pygame.Surface] = {}
        self.tile_test: pygame.Surface = None

    def load_images(self) -> None:
        try:
            player_image = pygame.image.load("assets/player_placeholder.png")
            player_image = pygame.transform.scale(player_image, (64, 64))
            self.player_images["player"] = player_image

            self.tile_test = pygame.image.load("assets/tile_png_folder/test_tile.png")
            self.tile_test = pygame.transform.scale(self.tile_test, (64, 64))

        except FileNotFoundError:
            print("FILE NOT FOUND, FATAL ERROR")
            exit()
        except InvalidFileException:
            print("INVALID FILE, FATAL ERROR")
            exit()