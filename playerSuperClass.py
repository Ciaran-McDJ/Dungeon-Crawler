from enemySuperClass import EnemyClass
from entitySuperClass import Entity
import pygame
import config

class PlayerClass(Entity):
    def __init__(self, pos: pygame.Vector2, size: float, velocity: pygame.Vector2, image: str, health: float, weapon: object, speed:float, weaponCooldownMax:float):
        super().__init__(pos, size, velocity, image)
        self.health = health
        self.maxHealth = config.playerHealth
        self.speed = speed
        self.hurtCooldownTime = config.defaultPlayerHurtCoolDown
        self.weapon = weapon
        self.weaponCooldownMax = weaponCooldownMax
        # When cooldown is more than the time needed then it will happen again, resets to 0 when hit
        self.weaponCooldownTime = 0
    
    def doCollision(self, otherInstanceColliding):
        # If weapon and cooldown has expired, take damage and reset cooldown
        if isinstance(otherInstanceColliding, EnemyClass) and self.hurtCooldownTime >= config.defaultPlayerHurtCoolDown:
            self.health -= otherInstanceColliding.damage
            self.hurtCooldownTime = 0
        else: pass