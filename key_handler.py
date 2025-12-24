import pygame
import game_manager


class KeyHandler:
    def __init__(self, game: game_manager.Game) -> None:
        self._game: game_manager.Game = game

        self.w_pressed: bool = False
        self.s_pressed: bool = False
        self.d__pressed: bool = False
        self.a_pressed: bool = False
        self.enter_pressed: bool = False
        self.space_pressed: bool = False
        self.exit_pressed: bool = False

    def get_key_pressed(self) -> None:

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.a_pressed = True
        else:
            self.a_pressed = False

        if key[pygame.K_d]:
            self.d__pressed = True
        else:
            self.d__pressed = False

        if key[pygame.K_w]:
            self.w_pressed = True
        else:
            self.w_pressed = False

        if key[pygame.K_s]:
            self.s_pressed = True
        else:
            self.s_pressed = False

        if key[pygame.K_RETURN]:
            self.enter_pressed = True
        else:
            self.enter_pressed = False

        if key[pygame.K_SPACE]:
            self.space_pressed = True
        else:
            self.space_pressed = False

        if key[pygame.K_ESCAPE]:
            self.exit_pressed = True
        else:
            self.exit_pressed = False