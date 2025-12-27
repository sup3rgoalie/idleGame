import copy
import os
import pygame

import change_world_event
import entity
import world
import game_manager


# LOAD WORLDS AND SAVE THEM IN A DICT[world name, world]
def _load_worlds(world_files_path: str, game: game_manager.Game) -> dict[str, world.World]:
    world_paths: list[str] = os.listdir(world_files_path)

    worlds: dict[str, world.World] = {}

    for world_file in world_paths:
        if world_file.find("txt") == -1:
            temp_world: world.World = world.World(world_file, f"{world_files_path}/{world_file}", game)
            worlds[temp_world.name] = temp_world
    return worlds

def _load_tile_config(file_path: str) -> dict[str, tuple[str, int]]:
    tile_config: dict[str, tuple[str, int]] = {}
    with (open(file_path, "r") as file):
        file_lines: list[str] = file.readlines()
        for line in file_lines:
            line.strip()
            print(line)
            line_elements:list[str] = line.split(" ")
            print(line_elements)
            if len(line_elements) == 3:
                tile_config[line_elements[0]] = (line_elements[1], int(line_elements[2]))
    print(tile_config)
    return tile_config

class WorldManager:
    def __init__(self, game: game_manager.Game) -> None:
        self._game: game_manager.Game = game
        self._tile_config: dict[str, tuple[str, int]] = {}
        self._worlds: dict[str, world.World] = {}
        self.current_world: world.World = None
        self.current_entity_list: list[entity.Entity] = []

    def load_tile_config(self):
        self._tile_config = _load_tile_config("world_files/tile_types_and_rotations.txt")

    def load_worlds(self, world_files_path: str):
        self._worlds = _load_worlds(world_files_path, self._game)


    # GET A COPY OF THE WORLDS ENTITIES
    def load_world_entities(self, world_name: str) -> list[entity.Entity]:
        return self._worlds[world_name].entities.copy()

    def change_world(self, world_name: str):
        self.current_world = self._worlds[world_name]
        if len(self.current_world.entities) > 0:
            for e in self.current_entity_list:
                if isinstance(e, change_world_event.ChangeWorldEvent):
                    e.loaded = False
        self.current_entity_list = self.current_world.entities
        for e in self.current_entity_list:
            if isinstance(e, change_world_event.ChangeWorldEvent):
                e.loaded = True

    # DRAW WORLD ONTO THE SCREEN
    def draw_world(self, world_name: str, screen: pygame.Surface) -> None:

        screen.blit(self._worlds.get(world_name).world_surface, (0, 0))

    def get_worlds(self) -> dict[str, world.World]:
        return self._worlds

    def get_tile_config(self) -> dict[str, tuple[str, int]]:
        return self._tile_config


# UNIT TEST
if __name__ == "__main__":
    test_game: game_manager.Game = game_manager.Game()
    world_manager_test = WorldManager("test_files/test_world_file_dirct", test_game)
    print(world_manager_test._worlds['test_world_1'])
    print(world_manager_test._worlds['test_world_1'].layout)
    print(world_manager_test._worlds['test_world_2'])
    print(world_manager_test._worlds['test_world_2'].layout)
