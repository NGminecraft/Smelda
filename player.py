import pygame

class Player():
    def __init__(self):
        self.coords = [0, 0]
        self.facing = 0
        self.walk_speed = 4
        self.characterN = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png"), 3)
        self.characterE = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png"), 3)
        self.characterS = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png"), 3)
        self.characterW = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png"), 3)
        
    def walk(self):
        if self.facing == 0:
            self.coords[1] += 4
        if self.facing == 1:
            self.coords[0] += 4
        if self.facing == 2:
            self.coords[1] -= 4
        if self.facing == 3:
            self.coords[0] -= 4
            
    def get_player(self, screen, keyframe = 0):
        rect = pygame.Rect(0 + 46*keyframe, 0+46*keyframe, 46 * 3, 46 * 3)
        center = (screen.get_width() / 2 - self.characterN.get_width() / 4, screen.get_height() / 2 - self.characterN.get_height())
        print(self.characterN.get_height(), self.characterN.get_width())
        print(rect)
        if keyframe == 1:
            rect = pygame.Rect(self.characterN.get_height() / 2, self.characterN.get_height(), 288, 288)
        if self.facing == 0:
            return self.characterN.subsurface(rect)
        elif self.facing == 3:
            return self.characterW.subsurface(rect)
        elif self.facing == 2:
            return self.characterS.subsurface(rect)
        elif self.facing == 1:
            return self.characterE.subsurface(rect)
            
if __name__ == "__main__":
    import main