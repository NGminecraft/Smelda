import pygame
import store_view as lvl


pygame.init()
screen = pygame.display.set_mode((816, 816))
clock = pygame.time.Clock()

walking = False
level = lvl.Level()
level.check_for_items(screen)
while True:
    pressed = pygame.key.get_pressed()
    try:
        for i, v in enumerate(pressed):
            if v:
                if i == 22:
                    level.facing = 2
                    level.walk()
                if i == 7:
                    level.facing = 1
                    level.walk()
                if i == 4:
                    level.facing = 3
                    level.walk()
                if i == 26:
                    level.facing = 0
                    level.walk()
    except:
        pass
    level.draw_background(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
            
    level.check_for_items(screen)
    level.draw_character(screen)
    pygame.display.update()
    clock.tick(100)
