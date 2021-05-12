import math
from sprite import Sprite
from typing import NamedTuple
import typing
import pygame
import collections

def unitLength(percent):
    return swidth*percent
def pytheorem(x:int, y:int):
    return math.sqrt(x**2 + y**2)

Inputs = collections.namedtuple("Inputs", ["timeSinceLastRender", "playerx", "playery", "enemies"])

CoroutineToUpdateEachFrameType = typing.Generator[None, Inputs, None]

# inputs
swidth = 500
sheight = 500
playerHealth = 20
playerSpeed = unitLength(0.0003)
playerSize = round(unitLength(0.1))
playerImage = "/home/ciaran/Downloads/token_5.png"

hammerSmashSize = round(unitLength(0.2))
timeTillHammerGone = 1000
hammerSmashImage = "/home/ciaran/Pictures/broken_glass_PNG52_edited.png"

zombieHealth = 1
zombieSize = round(unitLength(0.1))
zombieSpeed = unitLength(0.0001)
zombieDamage = 1
zombieImage = "/home/ciaran/Pictures/zombie.png"

# Create the main screen
screen: pygame.Surface = pygame.display.set_mode((swidth,sheight))
Sprite.default_screen = screen 


def isColliding(firstInstance, secondInstance):
    if math.sqrt((firstInstance.xpos-secondInstance.xpos)**2 + (firstInstance.ypos-secondInstance.ypos)**2) < (firstInstance.size+secondInstance.size)/2:
        return True
    else:
        return False