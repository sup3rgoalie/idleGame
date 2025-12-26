import copy
import os
import pygame
import entity
import world
import game_manager


# LOAD WORLDS AND SAVE THEM IN A DICT[world name, world]
def _load_worlds(world_files_path: str, game: game_manager.Game) -> dict[str, world.World]:
    world_paths: list[str] = os.listdir(world_files_path)

    worlds: dict[str, world.World] = {}

    for world_file in world_paths:
        temp_world: world.World = world.World(world_file, f"{world_files_path}/{world_file}", game)
        worlds[temp_world.name] = temp_world
    return worlds


class WorldManager:
    def __init__(self, world_files_path: str, game: game_manager.Game) -> None:
        self._game: game_manager.Game = game
        self._worlds: dict[str, world.World] = _load_worlds(world_files_path, game)

    # GET A COPY OF THE WORLDS ENTITIES
    def load_world_entities(self, world_name: str) -> list[entity.Entity]:
        return self._worlds[world_name].entities.copy()

    # DRAW WORLD ONTO THE SCREEN
    def draw_world(self, world_name: str, screen: pygame.Surface) -> None:

        screen.blit(self._worlds.get(world_name).world_surface, (0, 0))

    def get_worlds(self) -> dict[str, world.World]:
        return self._worlds


# UNIT TEST
if __name__ == "__main__":
    test_game: game_manager.Game = game_manager.Game()
    world_manager_test = WorldManager("test_files/test_world_file_dirct", test_game)
    print(world_manager_test._worlds['test_world_1'])
    print(world_manager_test._worlds['test_world_1'].layout)
    print(world_manager_test._worlds['test_world_2'])
    print(world_manager_test._worlds['test_world_2'].layout)
