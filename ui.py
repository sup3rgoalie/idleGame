import pygame

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

    def add_farm_popup_to_ui(self, text: str, position: tuple[int, int], size: tuple[int, int]) -> None:
        text_box = pygame.Rect(0, 0, size[0], size[1])
        text_box_surface = pygame.Surface(text_box.size)
        text_box_surface.fill(pygame.Color("black"))
        pygame.draw.rect(text_box_surface, pygame.Color("green"), text_box, 5)
        self.outside_items_to_display.append((text_box_surface, position))

