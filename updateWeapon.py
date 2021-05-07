import pygame
from sprite import Sprite
import config
import math

class Hammer():
    @property 
    def isCollidingRelevant(self):
        temp = self.__isCollidingRelevantVariable
        self.__isCollidingRelevantVariable = False
        return temp
    def __init__(self, level:float, listOfEnemies, weaponxpos:int, weaponypos:int, movingx:int, movingy:int, screen: pygame.Surface):

        self.timeSinceAttack = 0
        self.timeTillGone = 1000
        self.damage = 1
        self.size = config.hammerSmashSize
        self.screen = screen
        self.coro = self.update()
        self.psychYouDontExist = False
        self.sprite = Sprite(config.hammerSmashSize, config.hammerSmashImage)
        self.xpos = weaponxpos
        self.ypos = weaponypos
        self.__isCollidingRelevantVariable = True


        # figure out position of smash
        # if only one of them do first one, in other case it's moving diagonally so lengths are a bit different
        # player position - half images size to have center of image on center of player, then add or subtract distance between centers
        
        for enemy in listOfEnemies:
            if self.psychYouDontExist == False:
                deltax = abs(self.xpos - enemy.xpos)
                deltay = abs(self.ypos - enemy.ypos)
                distance = config.pytheorem(deltax, deltay)
                radiusesSize = (enemy.size + config.hammerSmashSize)/2
                if distance<radiusesSize:
                    enemy.health -= self.damage

    def update(self) -> config.CoroutineToUpdateEachFrameType:
            if self.psychYouDontExist == True:
                return
            while self.timeSinceAttack < config.timeTillHammerGone:
                inputs = yield
                self.timeSinceAttack += inputs.timeSinceLastRender
                self.sprite.image.set_alpha(255-(self.timeSinceAttack/config.timeTillHammerGone*255))
                self.sprite.draw(self.xpos, self.ypos)
