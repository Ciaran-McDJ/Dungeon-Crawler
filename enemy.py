import pygame

class Enemies():
    def __init__(self, xpos: int, ypos: int, size: int):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
    
    def updatePos(self, x, y):
        self.xpos = x
        self.ypos = y