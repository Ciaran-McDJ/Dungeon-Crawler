import math
import enum
from typing import NamedTuple
import typing
import pygame
import pygame.draw
import collections

def pixelsToUnitLength(pixels:int):
    return pixels/swidth*100
def UnitLengthToPixels(UnitLength):
    return swidth*UnitLength/100

def pytheorem(x:int, y:int):
    return math.sqrt(x**2 + y**2)

class EntityState(enum.Enum):
    Live = "Live"
    Dead = "Dead"
    

# inputs
swidth = 500
sheight = 500
playerHealth = 20
grossMode = False
# How many percent do they move per milisecond
playerSpeed = 0.03
playerSize = 10
playerImage = "/home/ciaran/Downloads/token_5.png"
defaultPlayerHurtCoolDown = 1000

hammerSmashSize = 20
timeTillHammerGone = 1000
hammerSmashImage = "/home/ciaran/Pictures/broken_glass_PNG52_edited.png"
weaponCooldown = 1000

enemyHurtCooldownTime = 1000

zombieHealth = 3
zombieSize = 10
# percent of screen per milisecond
zombieSpeed = 0.01
zombieDamage = 1
zombieImage = "/home/ciaran/Pictures/zombie.png"
# Distances between player center and enemy center
minimumSpawnDistanceFromPlayer = 5

# PauseScreen
# 0 is invisible, 255 is completely grey
pauseScreenGreyAlpha = 150
# In percent of screen (width is 150 percent)
pauseScreenBoxWidth = 90
pauseScreenBoxHeight = 60

# TEMP how long between automatic zombie spawn
zombieSpawnTime = 1000


def isColliding(firstInstance, secondInstance):
    if math.sqrt((firstInstance.pos.x-secondInstance.pos.x)**2 + (firstInstance.pos.y-secondInstance.pos.y)**2) < (firstInstance.size+secondInstance.size)/2:
        return True
    else:
        return False

