import pygame
import pygame.draw
import config
import variables

def activateThisPauseScreen(gameScreenState:pygame.Surface):
    thisPauseScreenActive = True
    variables.mainScreen.blit(gameScreenState, (0,0))
    # This is to make a light grey layer over the screen
    myGreySurface = pygame.Surface((variables.mainScreen.get_width(),variables.mainScreen.get_height()))
    myGreySurface.fill("grey")
    myGreySurface.set_alpha(config.pauseScreenGreyAlpha)
    variables.mainScreen.blit(myGreySurface,(0,0))
    while thisPauseScreenActive == True & variables.gameIsRunning == True:

        # render screen
        variables.drawBox("brown", pygame.Vector2(75,50), config.pauseScreenBoxWidth, config.pauseScreenBoxHeight)

        # Put stuff here you want to show

        
        pygame.display.update()


        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                variables.gameIsRunning = False
            if event.type == pygame.KEYDOWN:
                if event.unicode == "\x1b":
                    thisPauseScreenActive = False