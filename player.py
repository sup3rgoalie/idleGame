import pygame
import entity
import game_manager

# CLASS FOR PLAYER
class Player(entity.Entity):
    def __init__(self, x: float, y: float, images: dict[str, pygame.Surface], velocity: int) -> None:
        super().__init__(x, y, images)
        self._velocity = velocity
        self.set_hitbox((16, 8), (32, 48))
        self._image = self._images["player"]

    # UPDATE PLAYER
    def update(self, dt: float) -> None:
        dt_velocity = self._velocity * dt
        new_x, new_y = game_manager.get_movement_from_keyboard(dt_velocity)
        self.set_position((new_x, new_y))

    # DRAW PLAYER
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, (self._x, self._y))
