from plistlib import InvalidFileException
import pygame

class AssetHandler:
    def __init__(self) -> None:
        self.player_images: dict[str, pygame.Surface] = {}
        self.farmland_images: dict[str, pygame.Surface] = {}
        self.wheat_plant_images: dict[str, pygame.Surface] = {}
        self.ui_elements: dict[str, pygame.Surface] = {}
        self.tile_test: pygame.Surface = None

    def load_images(self) -> None:
        try:
            player_image = pygame.image.load("assets/player_placeholder.png")
            player_image = pygame.transform.scale(player_image, (64, 64))
            self.player_images["player"] = player_image

            farmland_healthy_image = pygame.image.load("assets/plant_images/farmland.png")
            farmland_healthy_image = pygame.transform.scale(farmland_healthy_image, (64, 64))
            self.farmland_images["farmland_healthy"] = farmland_healthy_image

            wheat_image_0 = pygame.image.load("assets/plant_images/wheat_0.png")
            wheat_image_0 = pygame.transform.scale(wheat_image_0, (64, 64))
            self.wheat_plant_images["wheat_0"] = wheat_image_0

            wheat_image_1 = pygame.image.load("assets/plant_images/wheat_1.png")
            wheat_image_1 = pygame.transform.scale(wheat_image_1, (64, 64))
            self.wheat_plant_images["wheat_1"] = wheat_image_1

            wheat_image_2 = pygame.image.load("assets/plant_images/wheat_2.png")
            wheat_image_2 = pygame.transform.scale(wheat_image_2, (64, 64))
            self.wheat_plant_images["wheat_2"] = wheat_image_2

            self.tile_test = pygame.image.load("assets/tile_png_folder/test_tile.png")
            self.tile_test = pygame.transform.scale(self.tile_test, (64, 64))

            ui_item_bar = pygame.image.load("assets/ui_elements/item_bar.png")
            ui_item_bar = pygame.transform.scale(ui_item_bar, (ui_item_bar.get_width() * 3, ui_item_bar.get_height() * 3))
            self.ui_elements["item_bar"] = ui_item_bar

            ui_wheat_icon = pygame.image.load("assets/ui_elements/wheat_icon.png")
            ui_wheat_icon = pygame.transform.scale(ui_wheat_icon, (24, 27))
            self.ui_elements["wheat_icon"] = ui_wheat_icon

        except FileNotFoundError:
            print("FILE NOT FOUND, FATAL ERROR")
            exit()
        except InvalidFileException:
            print("INVALID FILE, FATAL ERROR")
            exit()