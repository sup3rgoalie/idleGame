import os
import pygame
import asset_handler
import world
import game_manager

# DRAW WORLD ONTO THE SCREEN
def draw_world(wrld: world.World, a_handler: asset_handler.AssetHandler, screen: pygame.Surface, tile_size: int) -> None:

    # ITERATE THROUGH THE WORLD LAYOUT FILE, DRAW TILES TO SCREEN
    screen.blit(wrld.world_surface, (0,0))

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
        self.game: game_manager.Game = game
        self.worlds: dict[str, world.World] = _load_worlds(world_files_path, game)


# UNIT TEST
if __name__ == "__main__":
    world_manager_test = WorldManager("test_files/test_world_file_dirct")
    print(world_manager_test.worlds['test_world_1'])
    print(world_manager_test.worlds['test_world_1'].layout)
    print(world_manager_test.worlds['test_world_2'])
    print(world_manager_test.worlds['test_world_2'].layout)
