import pygame
import entity
import game_manager
import item


# CLASS FOR PLAYER
class Player(entity.Entity):
    def __init__(self, x: float, y: float, images: dict[str, pygame.Surface], velocity: int, game: game_manager.Game) -> None:
        super().__init__(x, y, game, images)
        self._velocity = velocity
        self.set_hitbox((16, 8), (32, 48))
        self._image = self._images["player"]
        self._can_move = True
        self.interacting = False
        self.crop_inventory: dict[str, int] = {"wheat": 10000, "carrot": 1000, "corn": 1000, "tomato": 1000}
        self.inventory_size: int = 16
        self.item_inventory: list[item.Item] = []
        self.seed_inventory: dict[str, int] = {"wheat_seed": 0, "carrot_seed": 0, "corn_seed": 0, "tomato_seed": 0}

        for i in range(self.inventory_size):
            temp_item_att:dict[str, str] = {"type": "sword", "description": "test item"}
            temp_item_images: dict[str, pygame.Surface] = {"inventory_icon": self._game.assets.tile_images["grass_whole"]}
            temp_item = item.Item(temp_item_att, temp_item_images)
            self.item_inventory.append(temp_item)

    # UPDATE PLAYER
    def update(self, dt: float) -> None:
        self.interacting = False
        game_manager.check_collision(self, self._game.w_manager.current_entity_list)
        dt_velocity = self._velocity * dt
        velo_x, velo_y = game_manager.get_movement_from_keyboard(dt_velocity, self._game)

        self.update_position((velo_x, velo_y))

    # DRAW PLAYER
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._image, (self._x, self._y))
        # DEBUG pygame.draw.rect(screen, pygame.Color("black"), self._hitbox)


    def update_position(self, velo_change: tuple[float, float]) -> None:
        new_x: float = self._x + velo_change[0]
        new_y: float = self._y + velo_change[1]
        if 0 <= new_x <= self._game.SCREEN_WIDTH - self._game.TILE_SIZE:
            self._x += velo_change[0]
            self._hitbox.x += velo_change[0]
        if 0 <= new_y <= self._game.SCREEN_HEIGHT - self._game.TILE_SIZE:
            self._y += velo_change[1]
            self._hitbox.y += velo_change[1]
