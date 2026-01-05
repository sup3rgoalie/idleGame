import os
from plistlib import InvalidFileException
import pygame
def load_images_from_folder(folder_path: str, scale_x: int, scale_y: int) -> dict[str, pygame.Surface]:
    return_dict: dict[str, pygame.Surface] = {}
    image_names = os.listdir(folder_path)
    for image_name in image_names:
        name = image_name.split(".")[0]
        image = pygame.image.load(os.path.join(folder_path, image_name))
        image = pygame.transform.scale(image, (scale_x, scale_y))
        image.convert_alpha()
        return_dict[name] = image
    return return_dict

class AssetHandler:
    def __init__(self) -> None:
        self.player_images: dict[str, pygame.Surface] = {}
        self.farmland_images: dict[str, pygame.Surface] = {}
        self.wheat_plant_images: dict[str, pygame.Surface] = {}
        self.ui_elements: dict[str, pygame.Surface] = {}
        self.tile_test: pygame.Surface = None
        self.tile_images: dict[str, pygame.Surface] = {}

    def load_images(self) -> None:
        try:
            player_images_path = "assets/farmer_images"
            self.player_images = load_images_from_folder(player_images_path, 64, 64)

            tile_images_path = "assets/tile_png_folder"
            self.tile_images = load_images_from_folder(tile_images_path, 64, 64)

            item_icons_path = "assets/ui_elements/item_icons"
            temp_image_dict = load_images_from_folder(item_icons_path, 96, 96)
            for image_name in temp_image_dict.keys():
                self.ui_elements[image_name] = temp_image_dict[image_name]


            farmland_healthy_image = pygame.image.load("assets/plant_images/farmland.png")
            farmland_healthy_image.convert_alpha()
            farmland_healthy_image = pygame.transform.scale(farmland_healthy_image, (64, 64))
            self.farmland_images["farmland_healthy"] = farmland_healthy_image

            wheat_image_0 = pygame.image.load("assets/plant_images/wheat_0.png")
            wheat_image_0.convert_alpha()
            wheat_image_0 = pygame.transform.scale(wheat_image_0, (64, 64))
            self.wheat_plant_images["wheat_0"] = wheat_image_0

            wheat_image_1 = pygame.image.load("assets/plant_images/wheat_1.png")
            wheat_image_1.convert_alpha()
            wheat_image_1 = pygame.transform.scale(wheat_image_1, (64, 64))
            self.wheat_plant_images["wheat_1"] = wheat_image_1

            wheat_image_2 = pygame.image.load("assets/plant_images/wheat_2.png")
            wheat_image_2.convert_alpha()
            wheat_image_2 = pygame.transform.scale(wheat_image_2, (64, 64))
            self.wheat_plant_images["wheat_2"] = wheat_image_2

            self.tile_test = pygame.image.load("assets/tile_png_folder/test_tile.png")
            self.tile_test.convert_alpha()
            self.tile_test = pygame.transform.scale(self.tile_test, (64, 64))

            ui_item_bar = pygame.image.load("assets/ui_elements/item_bar.png")
            ui_item_bar.convert_alpha()
            ui_item_bar = pygame.transform.scale(ui_item_bar, (ui_item_bar.get_width() * 3, ui_item_bar.get_height() * 3))
            self.ui_elements["item_bar"] = ui_item_bar

            ui_wheat_icon = pygame.image.load("assets/ui_elements/wheat_icon.png")
            ui_wheat_icon.convert_alpha()
            ui_wheat_icon = pygame.transform.scale(ui_wheat_icon, (24, 27))
            self.ui_elements["wheat_icon"] = ui_wheat_icon

            ui_carrot_icon = pygame.image.load("assets/ui_elements/carrot_icon.png")
            ui_carrot_icon.convert_alpha()
            ui_carrot_icon = pygame.transform.scale(ui_carrot_icon, (24, 24))
            self.ui_elements["carrot_icon"] = ui_carrot_icon

            ui_corn_icon = pygame.image.load("assets/ui_elements/corn_icon.png")
            ui_corn_icon.convert_alpha()
            ui_corn_icon = pygame.transform.scale(ui_corn_icon, (24, 24))
            self.ui_elements["corn_icon"] = ui_corn_icon

            ui_tomato_icon = pygame.image.load("assets/ui_elements/tomato_icon.png")
            ui_tomato_icon.convert_alpha()
            ui_tomato_icon = pygame.transform.scale(ui_tomato_icon, (24, 24))
            self.ui_elements["tomato_icon"] = ui_tomato_icon

            ui_farm_popup_image = pygame.image.load("assets/ui_elements/farm_popup.png")
            ui_farm_popup_image.convert_alpha()
            ui_farm_popup_image = pygame.transform.scale(ui_farm_popup_image, (96, 96))
            self.ui_elements["farm_popup"] = ui_farm_popup_image

            ui_inventory_image = pygame.image.load("assets/ui_elements/inventory_image.png")
            ui_inventory_image.convert_alpha()
            ui_inventory_image = pygame.transform.scale(ui_inventory_image, (ui_inventory_image.get_width() * 7, ui_inventory_image.get_height() * 7))
            self.ui_elements["inventory_image"] = ui_inventory_image

            star_image = pygame.image.load("assets/ui_elements/star.png")
            star_image.convert_alpha()
            self.ui_elements["star"] = star_image

            button_icons_path = "assets/ui_elements/buttons"
            button_icon_images = os.listdir(button_icons_path)
            for button_file_name in button_icon_images:
                name = button_file_name.split(".")[0]
                button_image = pygame.image.load(os.path.join(button_icons_path, button_file_name))
                button_image = pygame.transform.scale(button_image, (128, 48))
                button_image.convert_alpha()
                self.ui_elements[name] = button_image

        except FileNotFoundError:
            print("FILE NOT FOUND, FATAL ERROR")
            exit()
        except InvalidFileException:
            print("INVALID FILE, FATAL ERROR")
            exit()