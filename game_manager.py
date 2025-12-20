
def get_movement(pygame, dt_velocity) -> tuple:
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
