import os
import pygame
import world

def _load_worlds() -> list[world.World]:
    world_paths: list[str] = os.listdir("world_files")
    worlds: list[world.World] = []

    return worlds

class WorldManager:
    def __init__(self) -> None:
        self.worlds: list[world.World] = _load_worlds()

