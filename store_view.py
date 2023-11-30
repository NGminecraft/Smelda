import pygame
import numpy
import random
import copy

# colors that the background creator pulls from
BACK_COLORS = ((80, 198, 0), (0, 190, 9), (23, 198, 0))
TILE_SET_LOCATION = "tileBaseTileset.png"



class Level:
    def __init__(self, player, map="map.npy", collision_map="BigMapCollision"):
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
        self.items = {
            "Wall": tileset.subsurface(pygame.Rect(25, 63, 30, 30)),
            "Cabinet": tileset.subsurface(pygame.Rect(513, 257, 30, 30)),
            "Counter": tileset.subsurface(pygame.Rect(545, 257, 30, 30)),
            '': tileset.subsurface(pygame.Rect(238, 100, 30, 30)),
            "Stash1": tileset.subsurface(pygame.Rect(370, 255, 30, 30))
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
        for row_num, row in enumerate(arr):
            for column_num, column in enumerate(row):
                dictionary[(row_num * 30, column_num * 30)] = column
        return dictionary
    
    def initialize_collision(self):
        carr = numpy.load(self.collision_map)
        dictionary = {}
        for row_num, row in enumerate(carr):
            for column_num, column in enumerate(row):
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

    def draw_character(self, screen, keyframe):
        center = (screen.get_width() / 2 - self.characterN.get_width() / 4, screen.get_height() / 2 - self.characterN.get_height())
        screen.blit(self.player.get_player(), center)

    def check_for_items(self, screen):
        coords = self.player.get_coords()
        for key in self.objects:
            screen.blit(self.items[self.objects[key]], (key[0] + 208 - coords[0], key[1] + 208 + coords[1]))
            
    def check_collision(self, coords):
        print(coords[0]-(coords[0]%30), coords[1]-(coords[1]%30))
        return self.collision[(coords[0] -(coords[0]%30), coords[1] -(coords[1]%30))]


# This is so it always runs the game file even if I accidentaly try to run this onex                c
if __name__ == "__main__":
    import main
