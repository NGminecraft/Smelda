import pygame
import level as lvl
from PIL import Image
image = Image.open("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png")
print(image.size)


pygame.init()
screen = pygame.display.set_mode((816, 816))
clock = pygame.time.Clock()

walking = False
level = lvl.Level()

while True:
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
        level.walk()#me gustan coment-os
    level.draw_background(screen)
    level.draw_character(screen)
    level.check_for_items(screen)
    pygame.display.update()
    clock.tick(10)
