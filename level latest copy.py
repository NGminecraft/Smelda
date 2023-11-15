import pygame
import numpy
import random

# colors that the background creator pulls from
BACK_COLORS = ((80, 198, 0), (0, 190, 9), (23, 198, 0))
TILE_SET_LOCATION = "tileBaseTileset.png"

class Level:
    def __init__(self):
        self.map = numpy.load("map.npy")
        print(self.map)
        self.font = pygame.font.SysFont(None, 48)
        self.backdrop = pygame.surfarray.make_surface(self.initialize_background())
        self.backdrop = pygame.transform.scale(self.backdrop, (816, 816))
        self.characterN = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png")
        self.characterE = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png")
        self.characterS = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png")
        self.characterW = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png")
        self.objects = {"Wall": (True, pygame.Rect(384, 131, 16, 16), (20, 20)),
                        '': (False, False),
                        "Cabinet": (True, pygame.Rect(513, 257, 30, 30))
                        }
        self.facing = 0
        self.walkKeyframe = 0
        self.coords = [25, 50]
        self.resize()

    def initialize_map():
        pass

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
#        screen.blit(test, (100, 100), pygame.Rect(384, 131, 16, 16))
        if self.facing == 0:
            screen.blit(self.characterN, (screen.get_width() / 2 - self.characterN.get_width() / 4, screen.get_height() / 2 - self.characterN.get_height()), rect)
        elif self.facing == 3:
            screen.blit(self.characterW, (screen.get_width() / 2 - self.characterW.get_width() / 4, screen.get_height() / 2 - self.characterW.get_height()), rect)
        elif self.facing == 2:
            screen.blit(self.characterS, (screen.get_width() / 2 - self.characterS.get_width() / 4, screen.get_height() / 2 - self.characterS.get_height()), rect)
        elif self.facing == 1:
            screen.blit(self.characterE, (screen.get_width() / 2 - self.characterE.get_width() / 4, screen.get_height() / 2 - self.characterE.get_height()), rect)

    def walk(self, screen):
        print(self.coords)
        if self.facing == 0:
            self.coords[1] += 8
        if self.facing == 1:
            self.coords[0] += 8
        if self.facing == 2:
            self.coords[1] -= 8
        if self.facing == 3:
            self.coords[0] -= 8
        self.check_for_items(screen)


    def check_for_items(self, screen):
        for i in range(34):
#            print(i, "IIII")
            for j in range(34):
                obj_name = self.map[min(max(self.coords[1] + i - 17, 0), 49), min(max(self.coords[0] + (j - 17), 0), 49)]
                if self.objects[obj_name][0]:
#                    print(j, "JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
                    self.sixteenSegment((min(max(self.coords[1] + i - 17, 0), 49) + 408 - self.coords[0], min(max(self.coords[0] + (j - 17), 0), 49) + 408 + self.coords[1]), self.objects[obj_name][1], screen)
        self.sixteenSegment((25 + 408 - self.coords[0], 50 + 408 + self.coords[1]), pygame.Rect(384, 131, 16, 16), screen)
        
    def sixteenSegment(self, location, object, screen):
#        print(object)
        screen.blit(pygame.image.load("tileBaseTileset.png"), location, object)
        screen.blit(pygame.image.load("tileBaseTileset.png"), (location[0], location[1] + 16), object)
        screen.blit(pygame.image.load("tileBaseTileset.png"), (location[0] + 16, location[1]), object)
        screen.blit(pygame.image.load("tileBaseTileset.png"), (location[0] + 16, location[1] + 16), object)
        



# This is so it always runs the game file even if I accidentaly try to run this onex                c
if __name__ == "__main__":
    import game
