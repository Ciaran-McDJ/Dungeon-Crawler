import pygame
from sprite import Sprite
import config
import math

class Hammer():
    def __init__(self, level:float, listOfEnemies, playerxpos:int, playerypos:int, movingx:int, movingy:int, screen: pygame.Surface):

        self.timeSinceAttack = 0
        self.timeTillGone = 1000
        self.screen = screen
        self.coro = self.update()
        self.psychYouDontExist = False
        self.sprite = Sprite(config.hammerSmashSize, config.hammerSmashImage)
        
        # figure out position of smash
        # if only one of them do first one, in other case it's moving diagonally so lengths are a bit different
        # player position - half images size to have center of image on center of player, then add or subtract distance between centers
        if abs(movingy - movingx) == 1:
            self.xpos = playerxpos + (movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
            self.ypos = playerypos + (movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))
        elif movingy==0 & movingx==0:
            self.psychYouDontExist = True
        else:
            self.xpos = playerxpos + (1/math.sqrt(2))*(movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
            self.ypos = playerypos + (1/math.sqrt(2))*(movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))


    def update(self) -> config.CoroutineToUpdateEachFrameType:
            if self.psychYouDontExist == True:
                return
            while self.timeSinceAttack < config.timeTillHammerGone:
                inputs = yield
                self.timeSinceAttack += inputs.timeSinceLastRender
                self.sprite.image.set_alpha(255-(self.timeSinceAttack/config.timeTillHammerGone*255))
                self.sprite.draw(self.xpos, self.ypos)
