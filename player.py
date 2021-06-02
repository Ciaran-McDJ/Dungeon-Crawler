from hammer import Hammer
from pygame import Vector2, time
from playerSuperClass import PlayerClass
from typing import TYPE_CHECKING
import pygame.transform
import config
import variables

class Player(PlayerClass):
    def __init__(self):
        super().__init__(
            pos=Vector2(0,0),
            size=config.playerSize,
            velocity=Vector2(0,0),
            image=config.playerImage,
            health=config.playerHealth,
            weapon=Hammer,
            speed = config.playerSpeed,
            weaponCooldownMax = config.weaponCooldown
        )
        self.attacking = False
        variables.registerPlayer(self)

        self.isMovingLeft = False
        self.isMovingRight = False
        self.isMovingUp = False
        self.isMovingDown = False


    def update(self, timeSinceLastRender:float):
        if self.health > 0:
            self.velocity = Vector2(0,0)
            if self.isMovingLeft == True:
                self.velocity.x -= 1*self.speed
            if self.isMovingRight == True:
                self.velocity.x += 1*self.speed
            if self.isMovingUp == True:
                self.velocity.y -= 1*self.speed
            if self.isMovingDown == True:
                self.velocity.y += 1*self.speed

            self.hurtCooldownTime += timeSinceLastRender
            self.weaponCooldownTime += timeSinceLastRender
            self.sprite.image.set_alpha((self.hurtCooldownTime/config.defaultPlayerHurtCoolDown)*255)

            super().update(timeSinceLastRender)
            return config.EntityState.Live

        else: return config.EntityState.Dead

    def doAttack(self, movingx, movingy):
        return self.weapon(level=1, movingx=movingx, movingy=movingy)


# I think I can  get rid of this
# class Weapon():
#     def __init__(self, weaponType):
#         # TO DO - make it so there's multiple weapons and specify what they are with types
#         self.type = "hammer"
#         if weaponType == "hammer":
#             self.cooldown = 1
#             self.damage = 1



