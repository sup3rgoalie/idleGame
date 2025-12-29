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
        self._player_item: item.Item = None


        rarity_temp = "common"
        for i in range(self.inventory_size):
            temp_item_att: dict[str, str] = {}
            if i % 2 == 0:
                temp_item_att:dict[str, str] = {"type": "sword", "description": "test item sword"}
            else:
                temp_item_att:dict[str, str] = {"type": "bow", "description": "test item bow"}
            if rarity_temp == "common":
                rarity_temp = "uncommon"
            elif rarity_temp == "uncommon":
                rarity_temp = "rare"
            elif rarity_temp == "rare":
                rarity_temp = "epic"
            elif rarity_temp == "epic":
                rarity_temp = "legendary"
            elif rarity_temp == "legendary":
                rarity_temp = "common"
            temp_item_att["rarity"] = rarity_temp
            temp_item_images: dict[str, pygame.Surface] = {"inventory_icon": self._game.assets.ui_elements["basic_sword_icon"]}
            temp_item = item.Item(temp_item_att, temp_item_images)
            self.item_inventory.append(temp_item)
        self._player_item = self.item_inventory[0]

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

    def change_equipt_item(self, new_item: item.Item) -> None:
        if isinstance(new_item, item.Item):
            self._player_item = new_item
        else:
            print("TRIED TO EQUIPT NON ITEM OBJECT")
    def get_equipt_item(self) -> item.Item:
        return self._player_item

    def update_position(self, velo_change: tuple[float, float]) -> None:
        new_x: float = self._x + velo_change[0]
        new_y: float = self._y + velo_change[1]
        if 0 <= new_x <= self._game.SCREEN_WIDTH - self._game.TILE_SIZE:
            self._x += velo_change[0]
            self._hitbox.x += velo_change[0]
        if 0 <= new_y <= self._game.SCREEN_HEIGHT - self._game.TILE_SIZE:
            self._y += velo_change[1]
            self._hitbox.y += velo_change[1]
