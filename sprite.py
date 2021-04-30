import pygame

class Sprite():
    def __init__(self, size:int, imageLink:str):
        self.image = pygame.transform.scale(pygame.image.load("/home/ciaran/Pictures/broken_glass_PNG52_edited.png"), (size,size))
        self.size = size
    
    def getBlitArguments(self, xpos:float, ypos:float):
        return (self.image, (xpos+self.size, ypos+self.size))