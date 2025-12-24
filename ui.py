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

    def update(self) -> None:

        if self.game.game_state == "PLAY":
            self.game.canvas.blit(self._ui_elements["item_bar"], (20, 20))
            render_text(f"{self.game.user.inventory["wheat"]}", pygame.Color("white"), (56, 32), self.ui_font, self.game.canvas)
            self.game.canvas.blit(self._ui_elements["wheat_icon"], (36, 32))
