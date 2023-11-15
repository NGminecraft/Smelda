import pygame
import numpy
import random

BACK_COLORS = ((30, 126, 47), (33, 140, 52), (77, 163, 93))


class Level:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
        self.backdrop = pygame.surfarray.make_surface(self.initialize_background())
        self.backdrop = pygame.transform.scale(self.backdrop, (816, 816))
        self.characterN = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png")
        self.characterE = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png")
        self.characterS = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png")
        self.characterW = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png")
        self.objects = {"Boulder": (((0, 0), (100, 0)), "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Props/PNG/sprBoulder.png"),
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
                if self.coords[0] +408 >= i[0] and self.coords[0] - 408 <= i[0] and self.coords[1] + 408 >= i[1] and self.coords[1] - 408 <= i[1]:
                    screen.blit(pygame.transform.scale_by(pygame.image.load(self.objects[key][1]), 3), (i[0] + 408 - self.coords[0], i[1] + 408 + self.coords[1]))



# This is so it always runs the game file even if I accidentaly try to run this onex                c
if __name__ == "__main__":
    import game
