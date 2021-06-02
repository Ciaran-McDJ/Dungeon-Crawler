from sprite import Sprite
import pygame
import config

class Entity():
    isCollidingRelevant = True

    def __init__(self, pos: pygame.Vector2, size: float, velocity: pygame.Vector2, image: str):
        self.pos = pos
        self.size = size
        self.velocity = velocity
        self.sprite = Sprite(size, image)

    def update(self, timeSinceLastRender: float):
        self.pos += timeSinceLastRender*self.velocity
        # OPTIMIZE - can probably find a better way to do this
        # Stop from going past the edge
        if self.pos.x >= 100-(self.size/2):
            self.pos.x = 100-(self.size/2)
        if self.pos.x <= 0+(self.size/2):
            self.pos.x = 0+(self.size/2)
        if self.pos.y >= 100-(self.size/2):
            self.pos.y = 100-(self.size/2)
        if self.pos.y <=0+(self.size/2):
            self.pos.y = 0+(self.size/2)
        self.sprite.draw(self.pos)
    def draw(self):
        # All units are from 0-100 of percent of the screen
        self.sprite.draw(self.pos)
    def doCollision(self, otherInstanceColliding):
        pass

    # @property
    # def xpos(self):
    #     "LEGACY WILL REMOVE"
    #     return self.pos.x
        
