import config
import typing
from weaponInstanceSuperClass import weaponInstanceClass
from entitySuperClass import Entity
import pygame.time


class EnemyClass(Entity):
    def __init__(self, pos: pygame.Vector2, size: float, velocity: pygame.Vector2, image: str, health: float, damage: float):
        super().__init__(pos, size, velocity, image)
        self.health = health
        self.damage = damage
        # When cooldown is more than the time needed then it will happen again, resets to 0 when hit
        self.hurtCooldownTime = config.enemyHurtCooldownTime
    def doCollision(self, otherInstanceColliding):
        # If weapon and cooldown has expired, take damage and reset cooldown
        if isinstance(otherInstanceColliding, weaponInstanceClass) and self.hurtCooldownTime >= config.enemyHurtCooldownTime:
            self.health -= otherInstanceColliding.damage
            self.hurtCooldownTime = 0
        else: pass


