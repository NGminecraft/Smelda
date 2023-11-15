import pygame
import store_view as lvl


pygame.init()
screen = pygame.display.set_mode((816, 816))
clock = pygame.time.Clock()

walking = False
level = lvl.Level()
level.check_for_items(screen)
while True:
    level.draw_background(screen)
    level.check_for_items(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                level.facing = 0
                walking = True
            elif event.key == pygame.K_a:
                level.facing = 3
                walking = True
            elif event.key == pygame.K_s:
                level.facing = 2
                walking = True
            elif event.key == pygame.K_d:
                level.facing = 1
                walking = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                level.facing = 0
                walking = False
            elif event.key == pygame.K_a:
                level.facing = 3
                walking = False
            elif event.key == pygame.K_s:
                level.facing = 2
                walking = False
            elif event.key == pygame.K_d:
                level.facing = 1
                walking = False
    if walking:
        level.walk()
    level.draw_character(screen)
    pygame.display.update()
    clock.tick(10)
