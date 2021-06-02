from weaponInstanceSuperClass import weaponInstanceClass
import pygame
from sprite import Sprite
import config
import math
import variables

class Hammer(weaponInstanceClass):   
    def __init__(self, level:float, movingx:int, movingy:int):
        super().__init__(
            pos=pygame.Vector2(0,),
            size=config.hammerSmashSize,
            velocity=pygame.Vector2(0,0),
            image=config.hammerSmashImage,
            level=level,
            damage=level*1
        )
        self.timeSinceAttack = 0
        self.timeTillGone = 1000

        # figure out position of smash
        # if only one of them do first one, in other case it's moving diagonally so lengths are a bit different
        # player position, add or subtract distance between centers
        if abs(movingy - movingx) == 1:
            self.pos.x = variables.playerRef.pos.x + (movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
            self.pos.y = variables.playerRef.pos.y + (movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))
        elif movingy==0 & movingx==0:
            self.exists = False
        else:
            self.pos.x = variables.playerRef.pos.x + (1/math.sqrt(2))*(movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
            self.pos.y = variables.playerRef.pos.y + (1/math.sqrt(2))*(movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))


        self.__isCollidingRelevantVariable = True

    # let's me return true for first render, and false for all renders afterwards
    @property 
    def isCollidingRelevant(self):
        temp = self.__isCollidingRelevantVariable
        self.__isCollidingRelevantVariable = False
        return temp

    def update(self, timeSinceLastRender:float):
            if self.timeSinceAttack < config.timeTillHammerGone:
                self.timeSinceAttack += timeSinceLastRender
                self.sprite.image.set_alpha(255-(self.timeSinceAttack/config.timeTillHammerGone*255))
                super().update(timeSinceLastRender)
                return config.EntityState.Live
            else: return config.EntityState.Dead
