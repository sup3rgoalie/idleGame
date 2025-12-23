import pygame

import game_manager


# BASE CLASS FOR ALL ENTITY OBJECTS IN GAME
class Entity:
    def __init__(self, x: float, y: float, images: dict[str, pygame.Surface], game: game_manager.Game) -> None:
        self._x: float = x
        self._y: float = y
        self._game = game
        self._can_move = False
        self._images: dict[str, pygame.Surface] = images
        self._hitbox: pygame.Rect = pygame.Rect(self._x + 16, self._y + 16, 96, 96)

    def update(self, *args) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass
    # GET ENTITY POSITION
    def get_position(self) -> tuple[int, int]:
        return int(self._x), int(self._y)

    # GET ENTITY HITBOX
    def get_hitbox(self) -> pygame.Rect:
        return self._hitbox

    # GET ENTITY IMAGE
    def get_image(self) -> pygame.Surface:
        return self._image

    def collide_logic(self, entity: Entity) -> bool:
        pass

    # SET ENTITY POSITION, AS WELL AS UPDATE HITBOX TO NEW POSITION
    def set_position(self, velo_change: tuple[float, float]) -> None:

        self._x += velo_change[0]
        self._hitbox.x += velo_change[0]

        self._y += velo_change[1]
        self._hitbox.y += velo_change[1]

    def set_hitbox(self, offset: tuple[int, int], size: tuple[int, int]) -> None:
        self._hitbox = pygame.Rect(self._x + offset[0], self._y + offset[1], size[0], size[1])
