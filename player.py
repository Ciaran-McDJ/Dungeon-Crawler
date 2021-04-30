from typing import TYPE_CHECKING
import pygame.transform

class Player():
    def __init__(self, xpos: int, ypos: int, image, speed: int, size: int):
        self.xpos = xpos
        self.ypos = ypos
        self.surface = pygame.transform.scale(pygame.image.load(image), (size,size))   
        self.speed = speed
        self.attacking = False
        self.weapon = Weapon("hammer")






class Weapon():
    def __init__(self, weaponType):
        # TO DO - make it so there's multiple weapons and specify what they are with types
        self.type = "hammer"
        if weaponType == "hammer":
            self.cooldown = 1
            self.damage = 1



