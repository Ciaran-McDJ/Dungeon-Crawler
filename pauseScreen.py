from optionsPauseScreen import activateOptionsPauseScreen
import pygame
import pygame.draw
import config
import variables

def activatePauseScreen():
    pauseScreenActive = True
    # TO DO, break the link between these variables
    gameScreen = variables.mainScreen.copy()
    # This is to make a light grey layer over the screen
    myGreySurface = pygame.Surface((variables.mainScreen.get_width(),variables.mainScreen.get_height()))
    myGreySurface.fill("grey")
    myGreySurface.set_alpha(config.pauseScreenGreyAlpha)
    variables.mainScreen.blit(myGreySurface,(0,0))


    while pauseScreenActive == True & variables.gameIsRunning == True:

        # render screen
        brownBox = variables.drawBox("brown", pygame.Vector2(75,50), config.pauseScreenBoxWidth, config.pauseScreenBoxHeight)

        variables.drawTextOnSurface(
            surfaceToBlitOn= brownBox,
            height=10,
            pos=pygame.Vector2(50,10),
            text="press 'o' for options",
            colour="black",
            backgroundColour="white"
            )

        variables.mainScreen.blit(brownBox, (config.swidth*0.75-(brownBox.get_width()*0.5),config.sheight*0.5-(brownBox.get_height()*0.5)))

        pygame.display.update()


        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                variables.gameIsRunning = False
            if event.type == pygame.KEYDOWN:
                if event.unicode == "\x1b":
                    pauseScreenActive = False
                if event.unicode == "o":
                    activateOptionsPauseScreen(gameScreen)