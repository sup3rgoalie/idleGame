import pygame

# BASE CLASS FOR ALL ENTITY OBJECTS IN GAME
class Entity:
    def __init__(self, x: float, y: float, images: dict[str, pygame.Surface]) -> None:
        self._x: float = x
        self._y: float = y
        self.images: dict[str, pygame.Surface] = images
        self._hitbox: pygame.Rect = pygame.Rect(self._x + 16, self._y + 16, 96, 96)

    # UPDATE ENTITY OBJECT
    def update(self, dt: float) -> None:
        pass

    # DRAW ENTITY OBJECT
    def draw(self, screen: pygame.Surface) -> None:
        pass

    # GET ENTITY POSITION
    def get_position(self) -> tuple[float, float]:
        return self._x, self._y

    # GET ENTITY HITBOX
    def get_hitbox(self) -> pygame.Rect:
        return self._hitbox

    # GET ENTITY IMAGE
    def get_image(self) -> pygame.Surface:
        return self._image

    # SET ENTITY POSITION, AS WELL AS UPDATE HITBOX TO NEW POSITION
    def set_position(self, velo_change: tuple[float, float]) -> None:
        self._x += velo_change[0]
        self._y += velo_change[1]
        self._hitbox.x += velo_change[0]
        self._hitbox.y += velo_change[1]

    def set_hitbox(self, offset: tuple[int, int], size: tuple[int, int]) -> None:
        self._hitbox = pygame.Rect(self._x + offset[0], self._y + offset[1], size[0], size[1])
