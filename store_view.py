import pygame
import numpy
import random
import logging

# colors that the background creator pulls from
BACK_COLORS = ((80, 198, 0), (0, 190, 9), (23, 198, 0))
TILE_SET_LOCATION = "tileBaseTileset.png"



class Level:
    def __init__(self, player, map="map.npy", collision_map="BigMapCollision"):
        self.logger = logging.getLogger(__name__)
        self.keyframe = 1
        self.map = map
        self.collision_map = collision_map
        self.player = player
        self.backdrop = pygame.surfarray.make_surface(self.initialize_background())
        self.characterN = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png")
        self.characterE = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png")
        self.characterS = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png")
        self.characterW = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png")
        self.objects = self.initilize_map_dict()
        self.collision = self.initialize_collision()
        tileset = pygame.image.load(TILE_SET_LOCATION)
        self.frogNPC = pygame.image.load("Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/NPCs/PNG/sprToadEatWithTongue.png")
        print(self.frogNPC.get_width())
        self.items = {
            "Wall": pygame.transform.scale(tileset.subsurface(pygame.Rect(465, 272, 15, 15)), (30, 30)),
            "Cabinet": tileset.subsurface(pygame.Rect(513, 257, 30, 30)),
            "Counter": tileset.subsurface(pygame.Rect(545, 257, 30, 30)),
            '': pygame.transform.scale(tileset.subsurface(pygame.Rect(659, 305, 29, 29)), (30, 30)),
            "Stash1": tileset.subsurface(pygame.Rect(370, 255, 30, 30)),
            "TorchN1": pygame.transform.scale(tileset.subsurface(pygame.Rect(737, 356, 15, 30)), (30, 30)),
            "TorchN2": pygame.transform.scale(tileset.subsurface(pygame.Rect(753, 356, 15, 30)), (30, 30)),
            "TorchN3": pygame.transform.scale(tileset.subsurface(pygame.Rect(769, 356, 15, 30)), (30, 30)),
            "TorchN4": pygame.transform.scale(tileset.subsurface(pygame.Rect(785, 356, 15, 30)), (30, 30)),
            "TorchS1": pygame.transform.scale(tileset.subsurface(pygame.Rect(737, 386, 15, 30)), (30, 30)),
            "TorchS2": pygame.transform.scale(tileset.subsurface(pygame.Rect(753, 386, 15, 30)), (30, 30)),
            "TorchS3": pygame.transform.scale(tileset.subsurface(pygame.Rect(769, 386, 15, 30)), (30, 30)),
            "TorchS4": pygame.transform.scale(tileset.subsurface(pygame.Rect(785, 386, 15, 30)), (30, 30)),
            "FloorTorch1": pygame.transform.scale(tileset.subsurface(pygame.Rect(736, 320, 15, 15)), (30, 30)),
            "FloorTorch4": pygame.transform.scale(tileset.subsurface(pygame.Rect(784, 320, 15, 15)), (30, 30)),
            "FloorTorch3": pygame.transform.scale(tileset.subsurface(pygame.Rect(768, 320, 15, 15)), (30, 30)),
            "FloorTorch2": pygame.transform.scale(tileset.subsurface(pygame.Rect(752, 320, 15, 15)), (30, 30)),
            "Frog1": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(0, 0, 24, 24)), (30, 30)),
            "Frog2": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(24, 0, 24, 24)), (30, 30)),
            "Frog3": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(48, 0, 24, 24)), (30, 30)),
            "Frog4": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(72, 0, 24, 24)), (30, 30))
            
        }
        self.resize()

    def resize(self):
        self.characterN = pygame.transform.scale_by(self.characterN, 3)
        self.characterE = pygame.transform.scale_by(self.characterE, 3)
        self.characterS = pygame.transform.scale_by(self.characterS, 3)
        self.characterW = pygame.transform.scale_by(self.characterW, 3)
        self.backdrop = pygame.transform.scale(self.backdrop, (816, 816))

    def initilize_map_dict(self):
        arr = numpy.load(self.map)
        dictionary = {}
        for row_num, row in enumerate(reversed(arr)):
            for column_num, column in enumerate(reversed(row)):
                dictionary[(row_num * 30, column_num * 30)] = column
        return dictionary
    
    def initialize_collision(self):
        carr = numpy.load(self.collision_map)
        dictionary = {}
        for row_num, row in enumerate(reversed(carr)):
            for column_num, column in enumerate(reversed(row)):
                dictionary[(row_num * 30, column_num * 30)] = column
        return dictionary

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
        screen.blit(self.frogNPC.subsurface(0, 0, 24, 24), (0,0))

    def draw_character(self, screen, keyframe):
        center = (screen.get_width() / 2 - self.characterN.get_width() / 4, screen.get_height() / 2 - self.characterN.get_height())
        screen.blit(self.player.get_player(), center)

    def check_for_items(self, screen):
        coords = self.player.get_coords()
        for key in reversed(self.objects):
            try:
                screen.blit(self.items[self.objects[key]], (key[0] + 208 - coords[0], key[1] + 208 + coords[1]))
            except KeyError:
                self.keyframe += 0.006
                object = self.objects[key]
                object += str(round(self.keyframe))
                try:
                    screen.blit(self.items[object], (key[0] + 208 - coords[0], key[1] + 208 + coords[1]))
                except KeyError:
                    self.keyframe = 0.9
                               
    def check_collision(self, coords, screen):
        tile = (coords[0]- coords[0] % 30 + 210, coords[1] - coords[1] % 30+(480*3)-90)
        print(f"Checking for items at {tile}, And your at {coords}.")
        try:
            collision = self.collision[tile]
            if collision == "TRUE":
                return True
            else:
                return False
        except KeyError:
            self.logger.warning(f"Out of Bounds collision checking at {tile}")


# This is so it always runs the game file even if I accidentaly try to run this onex                c
if __name__ == "__main__":
    import main
