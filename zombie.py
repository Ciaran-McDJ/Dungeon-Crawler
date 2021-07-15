from pygame import Vector2
from enemySuperClass import EnemyClass
from sprite import Sprite
import typing
import pygame.transform
import pygame.draw
import config
import variables
import math
import random

class Zombie(EnemyClass):
    def __init__(self, level:float):
        pos = Vector2(random.random()*100, random.random()*100)
        while abs(pos.x-variables.playerRef.pos.x) < config.minimumSpawnDistanceFromPlayer and abs(pos.y-variables.playerRef.pos.y) < config.minimumSpawnDistanceFromPlayer:
            pos = Vector2(random.random()*100, random.random()*100)
            print("wow a zombie was about to spawn on you")
        super().__init__(
            # TO DO make it so they don't spawn on the player
            pos=Vector2(random.random()*100, random.random()*100), 
            size=config.zombieSize, 
            velocity=Vector2(), 
            image=config.zombieImage,
            health=config.zombieHealth, 
            damage=config.zombieDamage
        )

    def update(self, timeSinceLastRender:float):

        if self.health > 0:

            deltapos:Vector2 = variables.playerRef.pos - self.pos
            
            # divide x and y each by the total distance, so that the velocity vector has a magnitude of 1. Then multiply by speed
            if deltapos.magnitude != 0:
                self.velocity = (deltapos/deltapos.magnitude())*config.zombieSpeed
            else: self.velocity = (0,0)

            # Make alpha 0 when hit and renew to represent cooldown
            self.hurtCooldownTime += timeSinceLastRender
            self.sprite.image.set_alpha((self.hurtCooldownTime/config.enemyHurtCooldownTime)*255)

            super().update(timeSinceLastRender)

            return config.EntityState.Live

        else: return config.EntityState.Dead
        # TO DO make dead zombie animation
