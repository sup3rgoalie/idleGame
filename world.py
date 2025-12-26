import os
import pygame

import change_world_event
import entity
import farmland
import game_manager

# FUNCTION THAT READS A MAP LAYOUT FILE, A 2D LIST OF INTS
# input: file path for layout file
# output: 2d list of int for tile mapping
def _read_layout_file(file_path: str) -> list[list[str]]:
    map_layout: list[list[str]] = []
    # OPEN WORLD LAYOUT FILE
    print(f"Reading layout file {file_path}")

    with open(file_path, "r") as file:
        file_contents: list[str] = file.readlines()
        # PARSE FILE CONTENTS
        for line in file_contents:
            line = line.strip()
            line_elements: list[str] = line.split(" ")
            map_layout.append(line_elements)
    # RETURN MAP LAYOUT AS 2D ARRAY
    return map_layout

# READ CONFIG FILE FOR WORLD
def _read_config_file(file_path: str, game: game_manager.Game) -> list[entity.Entity]:
    # OPEN WORLD CONFIG FILE
    file_entity_list: list[entity.Entity] = []
    with (open(file_path, "r") as file):
        file_contents: list[str] = file.readlines()

        for line in file_contents:
            line = line.strip()
            line_elements: list[str] = line.split(" ")

            # CREATE FARMLAND OBJECT
            if line_elements[0] == "farm":
                pos_x: int = int(line_elements[1]) * game.TILE_SIZE
                pos_y: int = int(line_elements[2]) * game.TILE_SIZE
                new_farmland: farmland.Farmland = farmland.Farmland(pos_x, pos_y, game.assets.farmland_images, game)
                file_entity_list.append(new_farmland)
                print(f"farm created at {pos_x}, {pos_y}")

            # CREATE WORLD TELEPORT OBJECT
            elif line_elements[0] == "world":
                pos_x: int = int(line_elements[1]) * game.TILE_SIZE
                pos_y: int = int(line_elements[2]) * game.TILE_SIZE
                size_x: int = int(line_elements[3]) * game.TILE_SIZE
                size_y: int = int(line_elements[4]) * game.TILE_SIZE
                world_name: str = str(line_elements[5])
                new_change_world_event: change_world_event.ChangeWorldEvent = change_world_event.ChangeWorldEvent(pos_x, pos_y, size_x, size_y, world_name, game)
                file_entity_list.append(new_change_world_event)
                print(f"world teleport created at {pos_x}, {pos_y}")
    return file_entity_list


# CREATES A SURFACE WITH WORLDS TILES
def _create_world_surface(layout: list[list[str]], background: list[list[str]], game: game_manager.Game) -> pygame.Surface:
    world_surface: pygame.Surface = pygame.Surface((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))

    for y, row in enumerate(background):
        for x, tile in enumerate(row):
            screen_x = game.TILE_SIZE * x
            screen_y = game.TILE_SIZE * y
            if tile == "l":
                world_surface.blit(game.assets.tile_images["lava_background"],(screen_x, screen_y))
            if tile == "d":
                world_surface.blit(game.assets.tile_images["dirt_background"],(screen_x, screen_y))
            if tile == "w":
                world_surface.blit(game.assets.tile_images["water_background"],(screen_x, screen_y))

    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            screen_x = game.TILE_SIZE * x
            screen_y = game.TILE_SIZE * y
            if tile == "ggg":
                world_surface.blit(game.assets.tile_images["grass_whole"],(screen_x, screen_y))

            elif tile == "gi1":
                world_surface.blit(game.assets.tile_images["grass_inside_corner"],(screen_x, screen_y))
            elif tile == "gi2":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_inside_corner"], 90)
                world_surface.blit(rotated_tile_image,(screen_x, screen_y))
            elif tile == "gi3":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_inside_corner"], 180)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))
            elif tile == "gi4":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_inside_corner"], 270)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))


            elif tile == "go1":
                world_surface.blit(game.assets.tile_images["grass_outer_corner"],(screen_x, screen_y))
            elif tile == "go2":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_outer_corner"], 90)
                world_surface.blit(rotated_tile_image,(screen_x, screen_y))
            elif tile == "go3":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_outer_corner"], 180)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))
            elif tile == "go4":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_outer_corner"], 270)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))

            elif tile == "g11":
                world_surface.blit(game.assets.tile_images["grass_one_side"],(screen_x, screen_y))
            elif tile == "g12":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_one_side"], 90)
                world_surface.blit(rotated_tile_image,(screen_x, screen_y))
            elif tile == "g13":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_one_side"], 180)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))
            elif tile == "g14":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_one_side"], 270)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))

            elif tile == "g2v":
                world_surface.blit(game.assets.tile_images["grass_two_side"],(screen_x, screen_y))
            elif tile == "g2h":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_two_side"], 90)
                world_surface.blit(rotated_tile_image,(screen_x, screen_y))

            elif tile == "g31":
                world_surface.blit(game.assets.tile_images["grass_three_side"],(screen_x, screen_y))
            elif tile == "g32":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_three_side"], 90)
                world_surface.blit(rotated_tile_image,(screen_x, screen_y))
            elif tile == "g33":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_three_side"], 180)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))
            elif tile == "g34":
                rotated_tile_image = pygame.transform.rotate(game.assets.tile_images["grass_three_side"], 270)
                world_surface.blit(rotated_tile_image, (screen_x, screen_y))
    world_surface.convert_alpha()
    return world_surface

class World:
    def __init__(self, name: str, world_folder_path: str, game: game_manager.Game) -> None:
        self.name: str = name
        self.game: game_manager.Game = game
        self.world_files: list[str] = os.listdir(world_folder_path)

        for file in self.world_files:
            if file.find("bottom") != -1:
                self.background: list[list[str]] = _read_layout_file(os.path.join(world_folder_path, file))
            if file.find("layout") != -1:
                self.layout: list[list[str]] = _read_layout_file(os.path.join(world_folder_path, file))
            if file.find("config") != -1:
                self.entities: list[entity.Entity] = _read_config_file(os.path.join(world_folder_path, file), game)
        self.world_surface: pygame.Surface = _create_world_surface(self.layout, self.background, self.game)


    def __str__(self) -> str:
        return self.name



if __name__ == "__main__":
    print(_read_layout_file("test_files/_read_layout_file test"))

