import pygame
import pygame.font
import pygame.draw
import config
from variables import infoScreen
import variables

def updateInfoScreen():
    # OPTIMIZE - lots here probably only needs to be run when first opened or when new weapon is gotten (figuring out sizes and whatnot)
    infoScreen.fill("yellow")

    makeInfoBar(5,pygame.Vector2(2,5),f"Health: {variables.playerRef.health}","blue","red",variables.playerRef.maxHealth,variables.playerRef.health)
    makeInfoBar(5,pygame.Vector2(2,15),"Weapon Cooldown", "red", "blue", variables.playerRef.weaponCooldownMax, variables.playerRef.weaponCooldownTime, "green")
    drawText(5, pygame.Vector2(2,25), "press 'esc' to pause", "black")




def drawText(height:float, pos:pygame.Vector2, text:str, colour:str, backgroundColour:str=None, font:str=None):
    # draws text onto info screen, takes in percent of height as arguments (100 is bottom, 50 is right edge)
    fontObject = pygame.font.Font(font, round(config.UnitLengthToPixels(height)))
    surface = fontObject.render(text,False,colour,backgroundColour)
    infoScreen.blit(surface,(config.UnitLengthToPixels(pos.x),config.UnitLengthToPixels(pos.y)))
    return surface

def makeInfoBar(
    height:float,
    pos:pygame.Vector2,
    text:str,
    textColour:str,
    backgroundColour:str,
    maxNumber:float,
    currentNumber:float,
    maxColour:str=None,
    font:str=None
    ):
    # If not specified, then make it always just the colour
    if maxColour == None:
        maxColour = backgroundColour
    # If maxed out, make it the special colour (if not specified it will be the original colour)
    if currentNumber >= maxNumber:
        backgroundColour = maxColour
    # OPTIMIZE I'm drawing twice, the first time just to get the width, there's probably a better way
    textSurface = drawText(height, pos, text, textColour, font=font)

    widthOfBox = textSurface.get_width()*(currentNumber/maxNumber)
    if widthOfBox >= textSurface.get_width():
        widthOfBox = textSurface.get_width()

    pygame.draw.rect(infoScreen, backgroundColour, ((config.UnitLengthToPixels(pos.x),config.UnitLengthToPixels(pos.y)),((widthOfBox),textSurface.get_height())))
    drawText(height, pos, text, textColour, font=font)
    


