import pygame

import farmland
import game_manager
import item


# RENDER TEXT TO THE GAME SCREEN
def render_text(text: str, color: pygame.Color, pos: tuple[int, int], font: pygame.Font, screen: pygame.Surface) -> None:
    text_to_draw: pygame.Surface = font.render(text, True, color)
    screen.blit(text_to_draw, (pos[0], pos[1]))


class UI:
    def __init__(self, game: game_manager.Game) -> None:
        self.game: game_manager.Game = game
        self._ui_elements: dict[str, pygame.Surface] = self.game.assets.ui_elements
        self._sprite_counter: int = 0
        self.ui_font = pygame.font.SysFont("Arial", 24)
        self.outside_items_to_display: list[tuple[pygame.Surface, tuple[int, int]]] = []
        self._click_cooldown_counter: int = 0
        self._selected_item: item.Item = None
        self._selected_item_rarity_border: pygame.Surface = None
        self._selected_item_icon: pygame.Surface = None


    def update(self) -> None:
        canvas = self.game.canvas
        self._click_cooldown_counter += 1
        if self.game.game_state == "PLAY":
            # DRAW ITEM BAR
            canvas.blit(self._ui_elements["item_bar"], (20, 20))
            icon_x, text_x = 36, 58
            icon_y, text_y = 36, 32
            x_offset_per_item: int = 70
            for crop_type in self.game.user.crop_inventory:
                if self.game.user.crop_inventory[crop_type] > 9999:
                    adjusted_count_str: str = f"{round(self.game.user.crop_inventory[crop_type] / 1000)}K"
                    render_text(adjusted_count_str, pygame.Color("white"), (text_x, text_y), self.ui_font,
                                canvas)
                else:
                    render_text(f"{self.game.user.crop_inventory[crop_type]}", pygame.Color("white"), (text_x, text_y), self.ui_font,
                                canvas)
                if crop_type == "wheat":
                    icon_y -= 2
                    canvas.blit(self._ui_elements[f"{crop_type}_icon"], (icon_x, icon_y))
                    icon_y += 2
                else:
                    canvas.blit(self._ui_elements[f"{crop_type}_icon"], (icon_x, icon_y))
                text_x += x_offset_per_item
                icon_x += x_offset_per_item

            if len(self.outside_items_to_display) > 0:
                for item in self.outside_items_to_display:
                    canvas.blit(item[0], item[1])

            if self.game.key_h.tab_pressed:
                canvas.blit(self._ui_elements["inventory_image"], (64,48))
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
                item_x, item_y = 130, 112
                image_size = 96
                selected_image_size: tuple[int, int] = (128, 128)
                item_offset_x, item_offset_y = 144, 144
                inventory_button_dict: dict[int, pygame.Rect] = {}

                for i, user_item in enumerate(self.game.user.item_inventory):
                    temp_rect: pygame.Rect = pygame.Rect(item_x, item_y, image_size, image_size)
                    inventory_button_dict[i] = temp_rect

                    item_icon_image: pygame.Surface = user_item.get_images()["inventory_icon"]
                    item_rarity_border: pygame.Surface = self._ui_elements[f"{user_item.get_rarity()}_border"]
                    if temp_rect.collidepoint(mouse_pos):
                        item_icon_image = pygame.transform.scale(item_icon_image, selected_image_size)
                        item_rarity_border = pygame.transform.scale(item_rarity_border, selected_image_size)
                        selected_item_x: int = item_x - 16
                        selected_item_y: int = item_y - 16
                        if user_item == self.game.user.get_equipt_item():
                            border_size = selected_image_size[0] + 4
                            border_rect: pygame.Rect = pygame.Rect(selected_item_x - 2, selected_item_y - 2, border_size, border_size)
                            pygame.draw.rect(canvas, pygame.Color("green"), border_rect)
                        canvas.blit(item_rarity_border, (selected_item_x, selected_item_y))
                        canvas.blit(item_icon_image, (selected_item_x, selected_item_y))
                        if self.game.left_click and self._click_cooldown_counter > 10:
                            self._selected_item = user_item
                            self._selected_item_icon = pygame.transform.scale(item_icon_image, (160, 160))
                            self._selected_item_rarity_border = pygame.transform.scale(item_rarity_border, (160, 160))
                            self._click_cooldown_counter = 0
                    else:
                        if user_item == self.game.user.get_equipt_item():
                            border_rect: pygame.Rect = pygame.Rect(item_x - 2, item_y - 2, image_size + 4, image_size + 4)
                            pygame.draw.rect(canvas, pygame.Color("green"), border_rect)
                        canvas.blit(item_rarity_border, (item_x, item_y))
                        canvas.blit(item_icon_image, (item_x, item_y))
                    item_x += item_offset_x
                    if (i + 1) % 4 == 0:
                        item_x = 130
                        item_y += item_offset_y

                if self._selected_item is not None:
                    bottom_button_x, top_button_x = 760, 760
                    top_button_y, bottom_button_y, button_width, button_height = 560, 620, 128, 48
                    canvas.blit(self._selected_item_rarity_border, (740, 96))
                    canvas.blit(self._selected_item_icon, (740, 96))
                    render_text(self._selected_item.get_description(), pygame.Color("white"), (740, 300), self.ui_font, canvas)
                    top_button: pygame.Rect = pygame.Rect(top_button_x, top_button_y, button_width, button_height)
                    bottom_button: pygame.Rect = pygame.Rect(bottom_button_x, bottom_button_y, button_width, button_height)
                    selected_item_is_equipt = self.game.user._player_item is not None and self.game.user._player_item == self._selected_item

                    if top_button.collidepoint(mouse_pos):
                        top_button_x -= 16
                        top_button_y -= 6
                        if selected_item_is_equipt:
                            button_image = pygame.transform.scale(self._ui_elements["yellow_button"],
                                                                  (button_width + 32, button_height + 12))
                        else:
                            button_image = pygame.transform.scale(self._ui_elements["green_button"], (button_width + 32, button_height + 12))
                        if self.game.left_click and self._click_cooldown_counter > 10:
                            self._click_cooldown_counter = 0
                            self.game.user.change_equipt_item(self._selected_item)
                    else:
                        if selected_item_is_equipt:
                            button_image = self._ui_elements["yellow_button"]
                        else:
                            button_image = self._ui_elements["green_button"]
                    canvas.blit(button_image, (top_button_x, top_button_y))


                    if bottom_button.collidepoint(mouse_pos):
                        bottom_button_x -= 16
                        bottom_button_y -= 6
                        button_image = pygame.transform.scale(self._ui_elements["red_button"], (button_width + 32, button_height + 12))
                        canvas.blit(button_image, (bottom_button_x, bottom_button_y))
                    else:
                        canvas.blit(self._ui_elements["red_button"], (bottom_button_x, bottom_button_y))

            else:
                self._selected_item = None
                self._selected_item_icon = None
                self._selected_item_rarity_border = None


        self.outside_items_to_display.clear()

    def add_farm_popup_to_ui(self, position: tuple[int, int], calling_farmland: farmland.Farmland) -> None:
        farm_popup_font: pygame.font.Font = pygame.font.SysFont("Arial", 18, True)
        farm_popup_surface: pygame.Surface = pygame.Surface((96, 96))
        farm_popup_surface.blit(self._ui_elements["farm_popup"], (0,0))
        farm_popup_surface.set_colorkey((0,0,0))
        farm_land_plant = calling_farmland.get_plant()
        if farm_land_plant is not None:
            if farm_land_plant.get_plant_type() == "wheat":
                farm_popup_surface.blit(self._ui_elements["wheat_icon"], (12,12))
                render_text("Wheat", pygame.Color("white"), (32, 16), farm_popup_font, farm_popup_surface)
                if farm_land_plant.can_be_harvested:
                    render_text("Ready!", pygame.Color("white"), (24, 54), farm_popup_font, farm_popup_surface)
                else:
                    growth_count_font: pygame.Font = pygame.font.SysFont("Arial", 14, True)
                    current_growth_count: str = f"Seconds\nleft: {round((farm_land_plant.grow_time * 60 - farm_land_plant.growth_timer) / 60 + 0.5)}"
                    render_text(current_growth_count, pygame.Color("white"), (18, 48), growth_count_font, farm_popup_surface)
        else:
            render_text("Empty", pygame.Color("white"), (26, 18), farm_popup_font, farm_popup_surface)
        self.outside_items_to_display.append((farm_popup_surface, position))

