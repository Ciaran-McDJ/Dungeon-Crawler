from sprite import Sprite
import typing
import pygame.transform
import config
import math
import random

class Zombie():
    def __init__(self, level:float):
        # TO DO give them random positions
        self.coro = self.update()
        self.xpos = random.random()*config.swidth
        self.ypos = random.random()*config.sheight
        self.size = config.zombieSize
        self.health = config.zombieHealth
        self.damage = config.zombieDamage
        self.sprite = Sprite(config.zombieSize, config.zombieImage)
        self.isCollidingRelevant = True

    def update(self) -> config.CoroutineToUpdateEachFrameType:

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

            self.sprite.draw(self.xpos, self.ypos)
        def die():
            inputs.enemies.remove(self)
            return
        die()
