import pygame, pygame.transform, pygame.image
import config

class Sprite():
    "ciarans sprite class"
    default_screen: pygame.Surface = None
    def __init__(self, size:int, imageLink:str):
        self.image = pygame.transform.scale(pygame.image.load(imageLink), (round(config.UnitLengthToPixels(size)), round(config.UnitLengthToPixels(size))))     
        self.size = size
    # def getBlitArguments(self, xpos:float, ypos:float):
    #     return (self.image, (xpos-self.size/2, ypos-self.size/2))

    def draw(self, pos:pygame.Vector2, screen:pygame.Surface = None):
        """draws the sprite on specified screen or the default screen if screen is not passed, takes in centers"""
        if screen is None:
            screen = Sprite.default_screen
        screen.blit(self.image, (config.UnitLengthToPixels(pos.x-self.size/2), config.UnitLengthToPixels(pos.y-self.size/2)))