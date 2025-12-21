import os
import pygame

# FUNCTION THAT READS A MAP LAYOUT FILE, A 2D LIST OF INTS
# input: file path for layout file
# output: 2d list of int for tile mapping
def _read_layout_file(file_path: str) -> list[list[int]]:

    map_layout: list[list[int]] = []

    with open(file_path, "r") as file:
        file_contents: list[str] = file.readlines()

        for line in file_contents:
            line = line.strip()
            temp_list: list[int] = []
            for char in line:
                if char != " ":
                    temp_list.append(int(char))
            map_layout.append(temp_list)

    return map_layout

def _read_config_file(file_path: str) -> None:


    with open(file_path, "r") as file:
        file_contents: list[str] = file.readlines()


class World:
    def __init__(self, name: str, world_folder_path: str) -> None:
        self.name = name
        self.world_files: list[str] = os.listdir(world_folder_path)
        self.layout = _read_layout_file(self.world_files[0])



if __name__ == "__main__":
    _read_layout_file("world_files/_read_layout_file test")

