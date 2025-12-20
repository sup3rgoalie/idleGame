import pygame
import entity
import game_manager

# CLASS FOR PLAYER
class Player(entity.Entity):
    def __init__(self, x: float, y: float, image: pygame.Surface, velocity: int) -> None:
        super().__init__(x, y, image)
        self._velocity = velocity

    # UPDATE PLAYER
    def update(self, dt: float) -> None:
        dt_velocity = self._velocity * dt
        new_x, new_y = game_manager.get_movement_from_keyboard(dt_velocity)
        self._x += new_x
        self._y += new_y
        self.set_position((self._x, self._y))

    # DRAW PLAYER
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, (self._x, self._y))
