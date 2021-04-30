import typing
import pygame.transform
import config
import math

image = pygame.transform.scale(pygame.image.load("/home/ciaran/Pictures/zombie.png"), (config.zombieSize,config.zombieSize))

class Zombie():
    def __init__(self, level:float):
        # TO DO give them random positions
        self.xpos = 0
        self.ypos = 0
        self.health = config.zombieHealth

    def update(self, screen: pygame.Surface) -> config.CoroutineToUpdateEachFrameType:

        while self.health > 0:
            inputs = yield
            # mutable_shared_data_structure_that_changes_can_be_visible_outside[0] += 1
            deltax = inputs.playerx - self.xpos
            deltay = inputs.playery - self.ypos
            deltaTotal = config.pytheorem(deltax, deltay)
            
            xUnitStep = deltax/deltaTotal
            yUnitStep = deltay/deltaTotal

            self.xpos += xUnitStep*config.zombieSpeed*inputs.timeSinceLastRender
            self.ypos += yUnitStep*config.zombieSpeed*inputs.timeSinceLastRender

            screen.blit(image, (self.xpos,self.ypos))
