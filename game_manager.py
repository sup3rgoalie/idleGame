import pygame
def get_movement_from_keyboard(dt_velocity: float) -> tuple[float, float]:
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        return -1 * dt_velocity, 0
    elif key[pygame.K_d]:
        return dt_velocity, 0
    elif key[pygame.K_w]:
        return 0, -1 * dt_velocity
    elif key[pygame.K_s]:
        return 0, dt_velocity
    else:
        return 0, 0
