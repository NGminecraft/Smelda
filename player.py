import pygame

class Player():
    def __init__(self):
        self.coords = [100, 80]
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
        self.walking_animation = 1
        
    def walk(self, map):
        if self.facing == 0:
            if map.check_collision((self.coords[0], self.coords[1] + 4)):
                print("up")
                self.coords[1] += 4
        if self.facing == 1:
            if map.check_collision((self.coords[0] + 4, self.coords[1])):
                self.coords[0] += 4
        if self.facing == 2:
            if map.check_collision((self.coords[0], self.coords[1] - 4)):
                self.coords[1] -= 4
        if self.facing == 3:
            if map.check_collision((self.coords[0] - 4, self.coords[1])):
                self.coords[0] -= 4
        self.walking_animation += 0.05
            
    def get_player(self, keyframe = False):
        if self.walking_animation >= 1 and not keyframe:
            self.walking_animation = 0
        elif keyframe:
            self.walking_animation = keyframe
        if self.walking_animation >= 0.5:
            keyframe = 1
        else:
            keyframe = 0
        rect = pygame.Rect(pygame.Rect(keyframe*(self.characterN.get_width() / 2), 0, self.characterN.get_width() / 2, self.characterN.get_height()))
        if self.facing == 0:
            return self.characterN.subsurface(rect)
        elif self.facing == 3:
            return self.characterW.subsurface(rect)
        elif self.facing == 2:
            return self.characterS.subsurface(rect)
        elif self.facing == 1:
            return self.characterE.subsurface(rect)
    
    def get_coords(self):
        return self.coords
            
if __name__ == "__main__":
    import main