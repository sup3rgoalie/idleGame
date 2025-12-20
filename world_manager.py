import pygame
import world

class WorldManager:
    def __init__(self) -> None:
        self.worlds: list[world.World] = []