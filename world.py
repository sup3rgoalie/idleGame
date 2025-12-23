import os
import pygame

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


class World:
    def __init__(self, name: str, world_folder_path: str) -> None:
        self.name: str = name
        self.world_files: list[str] = os.listdir(world_folder_path)
        self.layout: list[list[str]] = _read_layout_file(f"{world_folder_path}/{self.world_files[0]}")

    def __str__(self) -> str:
        return self.name



if __name__ == "__main__":
    print(_read_layout_file("test_files/_read_layout_file test"))

