import pygame

import farmland
import game_manager
import item


# RENDER TEXT TO THE GAME SCREEN
def render_text(text: str, color: tuple, pos: tuple[int, int], font: pygame.Font, screen: pygame.Surface) -> None:
    text_to_draw: pygame.Surface = font.render(text, True, pygame.Color(color))
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
                item_offset_x, item_offset_y = 144, 144
                inventory_button_dict: dict[int, pygame.Rect] = {}

                for i, user_item in enumerate(self.game.user.item_inventory):
                    temp_rect = pygame.Rect(item_x, item_y, image_size, image_size)
                    inventory_button_dict[i] = temp_rect
                    if temp_rect.collidepoint(mouse_pos):
                        pygame.draw.rect(canvas, pygame.Color("black"), temp_rect)
                        if self.game.left_click and self._click_cooldown_counter > 10:
                            self._selected_item = user_item
                    else:
                        pygame.draw.rect(canvas, pygame.Color("white"), temp_rect)
                    canvas.blit(user_item.get_images()["inventory_icon"], (item_x, item_y))
                    item_x += item_offset_x
                    if (i + 1) % 4 == 0:
                        item_x = 130
                        item_y += item_offset_y
                test = pygame.mouse.get_just_pressed()
                if self._selected_item is not None:
                    canvas.blit(self._selected_item.get_images()["inventory_icon"], (760, 112))
                if self.game.left_click and self._click_cooldown_counter > 10:
                    print(f'Clicked: {mouse_pos}')
                    self._click_cooldown_counter = 0
            else:
                self._selected_item = None


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

