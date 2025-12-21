import pygame

def _read_layout_file(file_path: str):
    with open(file_path, "r") as file:
        file_contents: str = file.read()


class World:
    def __init__(self, name: str, layout_path: str, config_path: str) -> None:
        self.name = name





