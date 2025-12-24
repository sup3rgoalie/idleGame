import pygame

import game_manager


class UI:
    def __init__(self, game: game_manager.Game) -> None:
        self.game: game_manager.Game = game
        self._ui_elements: dict[str, pygame.Surface] = self.game.assets.ui_elements
        self._sprite_counter: int = 0

    def update(self) -> None:

        if self.game.game_state == "PLAY":
            self.game.canvas.blit(self._ui_elements["item_bar"], (20, 20))