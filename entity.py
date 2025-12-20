import pygame

# BASE CLASS FOR ALL ENTITY OBJECTS IN GAME
class Entity:
    def __init__(self, x: float, y: float, image: pygame.Surface) -> None:
        self._x: float = x
        self._y: float = y
        self._image: pygame.Surface = image
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
    def set_position(self, position: tuple[float, float]) -> None:
        self._x = position[0]
        self._y = position[1]
        self.set_hitbox_position((self._x, self._y))

    # SET ENTITY HITBOX SIZE
    def set_hitbox_size(self, size: tuple[float, float]) -> None:
        self._hitbox.update(self._x, self._y, size[0], size[1])

    # CHANGE ENTITY HITBOX POSITION
    def set_hitbox_position(self, location: tuple[float, float]) -> None:
        self._hitbox.x = location[0]
        self._hitbox.y = location[1]
