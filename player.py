import math

import pygame
import entity
import game_manager
import item


# CLASS FOR PLAYER
class Player(entity.Entity):
    def __init__(self, x: float, y: float, images: dict[str, pygame.Surface], velocity: int, game: game_manager.Game) -> None:
        super().__init__(x, y, game, images)
        self._velocity: int = velocity
        self.set_hitbox((16, 8), (32, 48))
        self._image: pygame.Surface  = self._images["farmer_standing_1"]
        self._can_move: bool = True
        self.interacting: bool = False
        self.crop_inventory: dict[str, int] = {"wheat": 10000, "carrot": 1000, "corn": 1000, "tomato": 1000}
        self.inventory_size: int = 16
        self.item_inventory: list[item.Item] = []
        self.seed_inventory: dict[str, int] = {"wheat_seed": 0, "carrot_seed": 0, "corn_seed": 0, "tomato_seed": 0}
        self._player_item: item.Item = None
        self._sprite_counter: int = 0
        self._moving: bool = False
        self._attacking: bool = False
        self._attack_counter: int = 0
        self._attacking_dir: int = 0
        self._attack_rotation: float = 0
        self._attack_x, self._attack_y = 0, 0
        self._attacking_rect = pygame.Rect(0,0, 48, 48)


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
            temp_item_att["cooldown"] = "30"
            temp_item_images: dict[str, pygame.Surface] = {"inventory_icon": self._game.assets.ui_elements["basic_sword_icon"]}
            temp_item = item.Item(temp_item_att, temp_item_images)
            self.item_inventory.append(temp_item)
        self._player_item = self.item_inventory[0]

    # UPDATE PLAYER
    def update(self, dt: float) -> None:
        self.interacting = False
        game_manager.check_collision(self, self._game.w_manager.current_entity_list)
        dt_velocity = self._velocity * dt
        velo_x, velo_y, self._moving = self.get_movement_from_keyboard(dt_velocity)
        if self._game.left_click:
            if not self._attacking and self._game.game_state == "PLAY" and self._player_item is not None:
                self._attacking = True
                self._attack_counter = self._player_item.get_cooldown()
                mouse_x: int = pygame.mouse.get_pos()[0]
                self._attack_rotation = 180 / self._attack_counter
                if self._x - mouse_x > 0:
                    self._attacking_dir = -1
                else:
                    self._attacking_dir = 1

        if self._attacking:
            self._attack_counter -= 1
            if self._attack_counter == 0:
                self._attacking = False


        self.update_position((velo_x, velo_y))

    # DRAW PLAYER
    def draw(self, screen: pygame.Surface) -> None:
        self._sprite_counter += 1
        if self._moving:
            if self._sprite_counter > 20:
                self._image = self._images["farmer_standing_2"]
                self._sprite_counter = 0
            elif self._sprite_counter > 15:
                self._image = self._images["farmer_moving_1"]
            elif self._sprite_counter > 10:
                self._image = self._images["farmer_standing_1"]
            elif self._sprite_counter > 5:
                self._image = self._images["farmer_moving_2"]
        else:
            if self._sprite_counter > 60:
                self._image = self._images["farmer_standing_1"]
                self._sprite_counter = 0
            elif self._sprite_counter > 30:
                self._image = self._images["farmer_standing_2"]

        screen.blit(self._image, (self._x, self._y))

        if self._attacking:
            image_rotation_angle: int = int(180 + (self._attack_rotation * self._attack_counter * self._attacking_dir))
            attack_image = self._player_item.get_images()["inventory_icon"]

            game_manager.blit_rotate(screen,attack_image, (self._x + 32, self._y + 32), (attack_image.get_width() / 2, attack_image.get_height()), image_rotation_angle)

            self._attacking_rect.y = self._y + 64 - self._attack_counter * 4
            self._attacking_rect.x = self._x + 8 + (4 * abs(self._player_item.get_cooldown() / 2 - self._attack_counter) * -self._attacking_dir) + (64 * self._attacking_dir)


            pygame.draw.rect(screen, (255, 0, 0), self._attacking_rect, 2)# DEBUG pygame.draw.rect(screen, pygame.Color("black"), self._hitbox)

    def change_equipt_item(self, new_item: item.Item) -> None:
        if isinstance(new_item, item.Item):
            self._player_item = new_item
        elif new_item is None:
            self._player_item = None
        else:
            print("TRIED TO EQUIPT NON ITEM OBJECT")
    def get_equipt_item(self) -> item.Item:
        return self._player_item

    # GETS MOVEMENT FROM KEYBOARD FOR THE PLAYER
    def get_movement_from_keyboard(self, dt_velocity: float) -> tuple[float, float, bool]:

        # DIAGONAL MOVEMENT FACTOR FOR 8 DIRECTION MOVEMENT
        diagonal_movement_factor: float = (math.sqrt(2) / 2)
        moving: bool = True
        # CHANGE VELOCITY BASED ON KEY PRESSED
        velo_x: float = 0
        velo_y: float = 0
        if self._game.key_h.a_pressed:
            velo_x = -dt_velocity
        if self._game.key_h.d__pressed:
            velo_x = dt_velocity
        if self._game.key_h.w_pressed:
            velo_y = -dt_velocity
        if self._game.key_h.s_pressed:
            velo_y = dt_velocity

        # MULTIPLY VELOCITY BY DIAGONAL FACTOR IF MOVING IN BOTH X AND Y AXIS
        if velo_x != 0 and velo_y != 0:
            velo_x *= diagonal_movement_factor
            velo_y *= diagonal_movement_factor
        elif velo_x == 0 and velo_y == 0:
            moving = False
        return round(velo_x), round(velo_y), moving

    def update_position(self, velo_change: tuple[float, float]) -> None:
        new_x: float = self._x + velo_change[0]
        new_y: float = self._y + velo_change[1]
        if 0 <= new_x <= self._game.SCREEN_WIDTH - self._game.TILE_SIZE:
            self._x += velo_change[0]
            self._hitbox.x += velo_change[0]
        if 0 <= new_y <= self._game.SCREEN_HEIGHT - self._game.TILE_SIZE:
            self._y += velo_change[1]
            self._hitbox.y += velo_change[1]
