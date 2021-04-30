import pygame
from sprite import Sprite
import config
import math

image = pygame.transform.scale(pygame.image.load("/home/ciaran/Pictures/broken_glass_PNG52_edited.png"), (config.hammerSmashSize,config.hammerSmashSize))

class Hammer():
    def __init__(self, level:float, listOfEnemies, playerxpos:int, playerypos:int, movingx:int, movingy:int, screen: pygame.Surface):

        self.timeSinceAttack = 0
        self.timeTillGone = 1000
        self.screen = screen
        self.coro = self.update()
        self.psychYouDontExist = False
        
        # figure out position of smash
        # if only one of them do first one, in other case it's moving diagonally so lengths are a bit different
        # player position - half images size to have center of image on center of player, then add or subtract distance between centers
        if abs(movingy - movingx) == 1:
            self.xpos = playerxpos - (config.hammerSmashSize/2) + (movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
            self.ypos = playerypos - (config.hammerSmashSize/2) + (movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))
        elif movingy==0 & movingx==0:
            self.psychYouDontExist = True
        else:
            self.xpos = round(playerxpos - (config.hammerSmashSize/2) + (1/math.sqrt(2))*(movingx*((config.hammerSmashSize/2)+(config.playerSize/2))))
            self.ypos = round(playerypos - (config.hammerSmashSize/2) + (1/math.sqrt(2))*(movingy*((config.hammerSmashSize/2)+(config.playerSize/2))))
        self.image = Sprite(config.hammerSmashSize, "/home/ciaran/Pictures/broken_glass_PNG52_edited.png")


    def update(self) -> config.CoroutineToUpdateEachFrameType:
            if self.psychYouDontExist == True:
                return
            while self.timeSinceAttack < config.timeTillHammerGone:
                inputs = yield
                self.timeSinceAttack += inputs.timeSinceLastRender
                image.set_alpha(255-(self.timeSinceAttack/config.timeTillHammerGone*255))
                self.screen.blit(*self.image.getBlitArguments(self.xpos, self.ypos))
