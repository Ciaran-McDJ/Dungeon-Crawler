from entitySuperClass import Entity
import pygame

class weaponInstanceClass(Entity):
    def __init__(self, pos: pygame.Vector2, size: float, velocity: pygame.Vector2, image: str, level: float, damage: float):
        super().__init__(pos, size, velocity, image)
        self.level = level
        self.damage = damage
        self.exists = True