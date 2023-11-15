import pygame
import numpy
import random

# colors that the background creator pulls from
BACK_COLORS = ((80, 198, 0), (0, 190, 9), (23, 198, 0))
TILE_SET_LOCATION = "tileBaseTileset.png"

class Level:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
        self.backdrop = pygame.surfarray.make_surface(self.initialize_background())
        self.backdrop = pygame.transform.scale(self.backdrop, (816, 816))
        self.characterN = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png")
        self.characterE = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png")
        self.characterS = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png")
        self.characterW = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png")
        # This is essentially a giant dictionary storing every object in the game.
        # Questionable efficiency but it works
        # Tag: ((locations), isPNG, either file or Rect representing object in tile png, collision)
        self.objects = {"Boulder": (((0, 0), (100, 0)), False, "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Props/PNG/sprBoulder.png", True)
                        }
        self.facing = 0
        self.walkKeyframe = 0
        self.coords = [0, 0]
        self.resize()

    def resize(self):
        self.characterN = pygame.transform.scale_by(self.characterN, 3)
        self.characterE = pygame.transform.scale_by(self.characterE, 3)
        self.characterS = pygame.transform.scale_by(self.characterS, 3)
        self.characterW = pygame.transform.scale_by(self.characterW, 3)

    def initialize_background(self):
        background = []
        for i in range(350):
            layer1 = []
            for j in range(350):
                layer1.append(random.choice(BACK_COLORS))
            background.append(layer1)
        return numpy.asarray(background)

    def draw_background(self, screen):
        screen.blit(self.backdrop, (0, 0))
        screen.blit(self.font.render(str(self.coords), (255, 0, 0), (0, 0, 0)), (0, 10))

    def draw_character(self, screen):
        # Image is (96, 48) pixels
        rect = pygame.Rect(0, 0, 46 * 3, 46 * 3)
        test = pygame.image.load("tileBaseTileset.png")
        screen.blit(pygame.transform.scale_by(test, 3), (100, 100), pygame.Rect(470*3, 272*3, 45, 45))
        if self.facing == 0:
            screen.blit(self.characterN, (screen.get_width() / 2 - self.characterN.get_width() / 4, screen.get_height() / 2 - self.characterN.get_height()), rect)
        elif self.facing == 3:
            screen.blit(self.characterW, (screen.get_width() / 2 - self.characterW.get_width() / 4, screen.get_height() / 2 - self.characterW.get_height()), rect)
        elif self.facing == 2:
            screen.blit(self.characterS, (screen.get_width() / 2 - self.characterS.get_width() / 4, screen.get_height() / 2 - self.characterS.get_height()), rect)
        elif self.facing == 1:
            screen.blit(self.characterE, (screen.get_width() / 2 - self.characterE.get_width() / 4, screen.get_height() / 2 - self.characterE.get_height()), rect)

    def walk(self):
        if self.facing == 0:
            self.coords[1] += 8
        if self.facing == 1:
            self.coords[0] += 8
        if self.facing == 2:
            self.coords[1] -= 8
        if self.facing == 3:
            self.coords[0] -= 8


    def check_for_items(self, screen):
        in_range = []
        for key in self.objects:
            for i in self.objects[key][0]:
                # test for objects in range
                if not self.objects[key][1]:
                    if self.coords[0] +408 >= i[0] and self.coords[0] - 408 <= i[0] and self.coords[1] + 408 >= i[1] and self.coords[1] - 408 <= i[1]:
                        screen.blit(pygame.transform.scale_by(pygame.image.load(self.objects[key][2]), 3), (i[0] + 408 - self.coords[0], i[1] + 408 + self.coords[1]))
                else:
                    if self.coords[0] +408 >= i[0] and self.coords[0] - 408 <= i[0] and self.coords[1] + 408 >= i[1] and self.coords[1] - 408 <= i[1]:
                        screen.blit(pygame.transform.scale_by(TILE_SET_LOCATION, 3), (i[0] + 408 - self.coords[0], i[1] + 408 + self.coords[1]))



# This is so it always runs the game file even if I accidentaly try to run this onex                c
if __name__ == "__main__":
    import game
