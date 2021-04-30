import pygame

class Sprite():
    default_screen: pygame.Surface = None
    def __init__(self, size:int, imageLink:str):
        self.image = pygame.transform.scale(pygame.image.load("/home/ciaran/Pictures/broken_glass_PNG52_edited.png"), (size,size))
        self.size = size
    
    def getBlitArguments(self, xpos:float, ypos:float):
        return (self.image, (xpos-self.size/2, ypos-self.size/2))

    def draw(self, xpos: float, ypos: float, screen:pygame.Surface = None):
        """draws the sprite on specified screen or the default screen if screen is not passed, takes in centers"""
        if screen is None:
            screen = Sprite.default_screen
        screen.blit(self.image, (xpos-self.size/2, ypos-self.size/2))