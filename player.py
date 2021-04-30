from sprite import Sprite
from typing import TYPE_CHECKING
import pygame.transform
import config

class Player():
    def __init__(self):
        self.coro = self.update()
        self.health = 1
        self.xpos = 0
        self.ypos = 0
        self.sprite = Sprite(config.playerSize, config.playerImage)
        self.speed = config.playerSpeed
        self.attacking = False
        self.weapon = Weapon("hammer")

        self.isMovingLeft = False
        self.movingLeftClock = pygame.time.Clock()
        self.isMovingRight = False
        self.movingRightClock = pygame.time.Clock()
        self.isMovingUp = False
        self.movingUpClock = pygame.time.Clock()
        self.isMovingDown = False
        self.movingDownClock = pygame.time.Clock()


    def update(self) -> config.CoroutineToUpdateEachFrameType:

        while self.health > 0:
            if self.isMovingLeft == True:
                self.xpos -= self.speed*self.movingLeftClock.tick()
            if self.isMovingRight == True:
                self.xpos += self.speed*self.movingRightClock.tick()
            if self.isMovingUp == True:
                self.ypos -= self.speed*self.movingUpClock.tick()
            if self.isMovingDown == True:
                self.ypos += self.speed*self.movingDownClock.tick()

            inputs = yield
            self.sprite.draw(self.xpos, self.ypos)





class Weapon():
    def __init__(self, weaponType):
        # TO DO - make it so there's multiple weapons and specify what they are with types
        self.type = "hammer"
        if weaponType == "hammer":
            self.cooldown = 1
            self.damage = 1



