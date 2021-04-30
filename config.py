from math import sqrt
from typing import NamedTuple
import typing
import pygame
import collections

def unitLength(percent):
    return swidth*percent
def pytheorem(x:int, y:int):
    return sqrt(x**2 + y**2)

Inputs = collections.namedtuple("Inputs", ["timeSinceLastRender", "playerx", "playery"])

CoroutineToUpdateEachFrameType = typing.Generator[None, Inputs, None]

NamedTuple
# inputs
swidth = 500
sheight = 500
playerSpeed = unitLength(0.0003)
playerSize = round(unitLength(0.1))
hammerSmashSize = round(unitLength(0.2))
timeTillHammerGone = 1000

zombieHealth = 1
zombieSize = round(unitLength(0.1))
zombieSpeed = unitLength(0.0001)

