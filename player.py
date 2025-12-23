import pygame
import entity
import game_manager

# CLASS FOR PLAYER
class Player(entity.Entity):
    def __init__(self, x: float, y: float, images: dict[str, pygame.Surface], velocity: int, game: game_manager.Game) -> None:
        super().__init__(x, y, images, game)
        self._velocity = velocity
        self.set_hitbox((16, 8), (32, 48))
        self._image = self._images["player"]
        self._can_move = True
        self.inventory: dict[str, int] = {"wheat": 0}

    # UPDATE PLAYER
    def update(self, dt: float) -> None:
        dt_velocity = self._velocity * dt
        velo_x, velo_y = game_manager.get_movement_from_keyboard(dt_velocity, self._game)

        self.set_position((velo_x, velo_y))

    # DRAW PLAYER
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, (self._x, self._y))

    def set_position(self, velo_change: tuple[float, float]) -> None:
        new_x: float = self._x + velo_change[0]
        new_y: float = self._y + velo_change[1]
        if 0 <= new_x <= self._game.SCREEN_WIDTH - self._game.TILE_SIZE:
            self._x += velo_change[0]
            self._hitbox.x += velo_change[0]
        if 0 <= new_y <= self._game.SCREEN_HEIGHT - self._game.TILE_SIZE:
            self._y += velo_change[1]
            self._hitbox.y += velo_change[1]
