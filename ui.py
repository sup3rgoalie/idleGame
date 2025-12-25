import pygame

import farmland
import game_manager

# RENDER TEXT TO THE GAME SCREEN
def render_text(text: str, color: tuple, pos: tuple[int, int], font: pygame.Font, screen: pygame.Surface) -> None:
    text_to_draw: pygame.Surface = font.render(text, True, pygame.Color(color))
    screen.blit(text_to_draw, (pos[0], pos[1]))


class UI:
    def __init__(self, game: game_manager.Game) -> None:
        self.game: game_manager.Game = game
        self._ui_elements: dict[str, pygame.Surface] = self.game.assets.ui_elements
        self._sprite_counter: int = 0
        self.ui_font = pygame.font.SysFont("Arial", 24, True)
        self.outside_items_to_display: list[tuple[pygame.Surface, tuple[int, int]]] = []

    def update(self) -> None:

        if self.game.game_state == "PLAY":
            self.game.canvas.blit(self._ui_elements["item_bar"], (20, 20))
            render_text(f"{self.game.user.inventory["wheat"]}", pygame.Color("white"), (56, 32), self.ui_font, self.game.canvas)
            self.game.canvas.blit(self._ui_elements["wheat_icon"], (36, 32))

            if len(self.outside_items_to_display) > 0:
                for item in self.outside_items_to_display:
                    self.game.canvas.blit(item[0], item[1])
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
                    current_growth_count: str = f"Seconds\nleft: {round((farm_land_plant.grow_time * 60 - farm_land_plant.growth_timer) / 60)}"
                    render_text(current_growth_count, pygame.Color("white"), (18, 48), growth_count_font, farm_popup_surface)
        else:
            render_text("Empty", pygame.Color("white"), (26, 18), farm_popup_font, farm_popup_surface)
        self.outside_items_to_display.append((farm_popup_surface, position))

