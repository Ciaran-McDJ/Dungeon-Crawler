from sprite import Sprite
from player import Player
import pygame
import pygame.draw
import pygame.font
import config

# reference to player object, set by the player's init function
playerRef: Player = None
# define a variable to control the main loop
gameIsRunning = True
# updated in Player
def registerPlayer(reference:Player):
    global playerRef
    playerRef = reference

# Create the main screen
mainScreen: pygame.Surface = pygame.display.set_mode((round(config.swidth*1.5),config.sheight))

gameBoardScreen = mainScreen.subsurface((0,0,config.swidth,config.sheight))
infoScreen = mainScreen.subsurface((config.swidth,0,config.swidth*0.5,config.sheight))

Sprite.default_screen = gameBoardScreen




# My Functions


def pixelsToUnitLengthWidth(pixels:int, surface:pygame.Surface=mainScreen):
    return pixels/surface.get_width()*100
def pixelsToUnitLengthHeight(pixels:int, surface:pygame.Surface=mainScreen):
    return pixels/surface.get_height()*100
def UnitLengthToPixelsWidth(UnitLength, surface:pygame.Surface=mainScreen):
    return surface.get_width()*UnitLength/100
def UnitLengthToPixelsHeight(UnitLength, surface:pygame.Surface=mainScreen):
    return surface.get_height()*UnitLength/100


# all values should be in percent of the screen
def drawBox(colour:str, center:pygame.Vector2, width:int, height:int, alpha:int=255):
    
    mySurface = pygame.Surface((config.UnitLengthToPixels(width),config.UnitLengthToPixels(height)))
    mySurface.fill(colour)
    mySurface.set_alpha(alpha)
    
    mainScreen.blit(mySurface, (config.UnitLengthToPixels(center.x-width*0.5),config.UnitLengthToPixels(center.y-height*0.5)),)
    return mySurface

def drawTextOnSurface(surfaceToBlitOn:pygame.Surface, height:float, pos:pygame.Vector2, text:str, colour:str, backgroundColour:str=None, font:str=None):
    # draws text onto a surface, takes in percent of surfaceToBlitOn as arguments (100 is bottom, 100 is right edge)
    fontObject = pygame.font.Font(font, round(UnitLengthToPixelsHeight(height, surfaceToBlitOn)))
    textSurface = fontObject.render(text,False,colour,backgroundColour)
    surfaceToBlitOn.blit(textSurface,(UnitLengthToPixelsWidth(pos.x, surfaceToBlitOn)-(textSurface.get_width()*0.5),UnitLengthToPixelsHeight(pos.y, surfaceToBlitOn)-(textSurface.get_height()*0.5)))
    return textSurface
    