from sprite import Sprite
import pygame

class EntitySubClass():
    def __init__(self, xpos: float, ypos: float, size: float, velocity: tuple, image: str):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.velocity = velocity
        self.sprite = Sprite(size, image)
    
    def update(self, timeSinceLastRender):
        self.xpos += timeSinceLastRender*self.velocity[0]
        self.ypos += timeSinceLastRender*self.velocity[1]
        self.sprite.draw(self.xpos, self.ypos)
        
