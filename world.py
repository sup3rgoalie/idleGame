import os
import pygame

import game_manager


# FUNCTION THAT READS A MAP LAYOUT FILE, A 2D LIST OF INTS
# input: file path for layout file
# output: 2d list of int for tile mapping
def _read_layout_file(file_path: str) -> list[list[str]]:
    map_layout: list[list[str]] = []
    # OPEN WORLD LAYOUT FILE
    with open(file_path, "r") as file:
        file_contents: list[str] = file.readlines()
        # PARSE FILE CONTENTS
        for line in file_contents:
            line = line.strip()
            line_elements: list[str] = line.split(" ")
            map_layout.append(line_elements)
    # RETURN MAP LAYOUT AS 2D ARRAY
    return map_layout

def _read_config_file(file_path: str) -> None:
    # OPEN WORLD CONFIG FILE
    with open(file_path, "r") as file:
        file_contents: list[str] = file.readlines()

# CREATES A SURFACE WITH WORLDS TILES
def _create_world_surface(layout: list[list[str]], game: game_manager.Game) -> pygame.Surface:
    world_surface: pygame.Surface = pygame.Surface((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            screen_x = game.TILE_SIZE * x
            screen_y = game.TILE_SIZE * y
            if tile == "0":
                world_surface.blit(game.assets.tile_test,(screen_x, screen_y))
    return world_surface

class World:
    def __init__(self, name: str, world_folder_path: str, game: game_manager.Game) -> None:
        self.name: str = name
        self.game: game_manager.Game = game
        self.world_files: list[str] = os.listdir(world_folder_path)
        self.layout: list[list[str]] = _read_layout_file(f"{world_folder_path}/{self.world_files[0]}")
        self.world_surface: pygame.Surface = _create_world_surface(self.layout, self.game)
        print(game.TILE_SIZE)

    def __str__(self) -> str:
        return self.name



if __name__ == "__main__":
    print(_read_layout_file("test_files/_read_layout_file test"))

