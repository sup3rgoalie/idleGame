import os

import pygame

import game_manager
import world


class Dungeon:
    def __init__(self, file_path: str, game: game_manager.Game):
        self._dungeon_files = os.listdir(file_path)
        self._dungeon_rooms: dict[str, pygame.Surface] = {}
        self._dungeon_name = file_path.split("/")[-1].split(".")[0]
        print(self._dungeon_files)
        print(self._dungeon_name)
        dungeon_background: list[list[str]] = []
        background_index = -1

        for i, file in enumerate(self._dungeon_files):
            if file.find("background") != -1:
                dungeon_background = world.read_layout_file(os.path.join(file_path, file))
                background_index = i
                break

        if background_index != -1:
            self._dungeon_files.pop(background_index)
            for file in self._dungeon_files:
                dungeon_room_name = file
                dungeon_layout_file = os.listdir(os.path.join(file_path, dungeon_room_name))[0]
                dungeon_layout = world.read_layout_file(os.path.join(file_path, file, dungeon_layout_file))
                dungeon_image = world.create_world_surface(dungeon_layout, dungeon_background, game)
                self._dungeon_rooms[dungeon_room_name] = dungeon_image
            print("dungeon_success")

    def get_name(self) -> str:
        return self._dungeon_name

    def get_rooms(self) -> dict[str, pygame.Surface]:
        return self._dungeon_rooms



class DungeonManager:
    def __init__(self, game: game_manager.Game) -> None:
        self._game = game
        self._dungeons: dict[str, Dungeon] = {}
        self.load_dungeon_worlds()

    def load_dungeon_worlds(self):
        dungeon_file_path: str = "dungeon_files"
        dungeons: list[str] = os.listdir(dungeon_file_path)
        for dungeon in dungeons:
            new_dungeon = Dungeon(os.path.join(dungeon_file_path, dungeon), self._game)
            name = new_dungeon.get_name()
            self._dungeons[name] = new_dungeon

