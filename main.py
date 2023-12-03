import pygame
import store_view as lvl
import player as player


pygame.init()
screen = pygame.display.set_mode((816, 816))
clock = pygame.time.Clock()
main_actor = player.Player()
walking = False
level = lvl.Level(main_actor, map="map.npy", collision_map="BigMapCollision.npy")
level.check_for_items(screen)
while True:
    pressed = pygame.key.get_pressed()
    level.draw_background(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
            
    level.check_for_items(screen)
    level.draw_character(screen, 0)
    for i, v in enumerate(pressed):
        if v:
            if i == 22:
                main_actor.facing = 2
                main_actor.walk(level, screen)
            if i == 7:
                main_actor.facing = 1
                main_actor.walk(level, screen)
            if i == 4:
                main_actor.facing = 3
                main_actor.walk(level, screen)
            if i == 26:
                main_actor.facing = 0
                main_actor.walk(level, screen)
    pygame.display.update()
    clock.tick(100)

print("bananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaananananananananananananaananananananananananaanananananananananananana")