import collections
from pauseScreen import activatePauseScreen
from infoScreen import updateInfoScreen
from entitySuperClass import Entity
import typing
import math
from zombie import Zombie
from hammer import Hammer
import pygame # python works when only importing a submodule, but apparently pylance is dumb enough to require this import
import pygame.draw, pygame.display, pygame.image, pygame.surface
from player import Player
import config
import variables
import pygame.font

#THERE IS A DIVISION BY 0 ERROR HAPPENING SOMEWHERE - FIX IT!!! (I think when zombie is directly on top of character (check zombie movement))

# define a main function
def main():
   
    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo: pygame.Surface = pygame.image.load("/home/ciaran/Downloads/token_5.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("my test game")




    # TO DO add type to this list to specify it's a list of Entities
    thingsToUpdateEachFrame = set()
    myClocks = set()

    # making some variables
    player = Player()
    thingsToUpdateEachFrame.add(player)

    GameClock = pygame.time.Clock()
    myClocks.add(GameClock)

    roomCleared = False
    # TEMP I will remove this once I have rooms spawn enemies
    zombieSpawningTimer = 0
    zombieSpawningTimerClock = pygame.time.Clock()
    myClocks.add(zombieSpawningTimerClock)


    
    # main loop
    while variables.gameIsRunning:
        timeSinceLastRender = GameClock.tick()
        # do collision detection using boxes
        # start by getting size of largest thing and make that the size of the box
        boxSize = 0
        for instance in thingsToUpdateEachFrame:
            if instance.size > boxSize:
                boxSize = instance.size
        dictionary: typing.Dict[tuple, typing.List] = {}
        for instance in thingsToUpdateEachFrame.copy():
            if instance.isCollidingRelevant == True:
                # Assign them their keys based on their position
                key = (instance.pos.x//boxSize,instance.pos.y//boxSize)
                dictionary.setdefault(key, [])
                dictionary[key].append(instance)
        for key, instancesToCheck in dictionary.items():
            keyx,keyy = key

            keysOfNearGroups:typing.List[tuple] = []
            # instancesToCheck += dictionary[group+1]
            for xKeyComponent in [-1,0,1]:
                for yKeyComponent in [-1,0,1]:
                    newKey = (keyx+xKeyComponent,keyy+yKeyComponent)
                    if newKey in dictionary.keys():
                        keysOfNearGroups.append(newKey)


            for thisCellInstance in instancesToCheck:
                for group in keysOfNearGroups:
                    for otherCellInstance in dictionary[group]:
                        # TO DO make it so I don't need to check every time (only if same cell?)
                        if thisCellInstance != otherCellInstance:
                            if config.isColliding(thisCellInstance, otherCellInstance):
                                # TO DO make them do stuff
                                thisCellInstance.doCollision(otherCellInstance)
                                otherCellInstance.doCollision(thisCellInstance)


        # put images on screen
        if config.grossMode != True: variables.gameBoardScreen.fill("blue")
        updateInfoScreen()

        for instance in thingsToUpdateEachFrame.copy():
            entityState = instance.update(timeSinceLastRender)
            if entityState == config.EntityState.Dead:
                thingsToUpdateEachFrame.remove(instance)
        
        if roomCleared == True:
            pass
            # Make doors


        pygame.display.update()

        # print(pygame.font.get_fonts())


        # TEMP will get rid of once rooms implemented
        zombieSpawningTimer += zombieSpawningTimerClock.tick()
        if zombieSpawningTimer >= config.zombieSpawnTime:
            thingsToUpdateEachFrame.add(Zombie(1))
            zombieSpawningTimer = 0


        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            print(event)
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                variables.gameIsRunning = False
            # move player with wasd
            if event.type == pygame.KEYDOWN:
                # start moving
                if event.unicode == "a":
                    player.isMovingLeft = True
                if event.unicode == "d":
                    player.isMovingRight = True
                if event.unicode == "w":
                    player.isMovingUp = True
                if event.unicode == "s":
                    player.isMovingDown = True
                
                # attack
                if event.unicode == " ":
                    # if same or different then 0, if right then 1, if left then -1
                    movingx = player.isMovingRight-player.isMovingLeft
                    # if same or different then 0, if down then 1, if up then -1
                    movingy = player.isMovingDown-player.isMovingUp
                    
                    # code to start updating weapons 
                    instance = player.doAttack(movingx, movingy)
                    if instance.exists == True:
                        if player.weaponCooldownTime > player.weaponCooldownMax:
                            player.weaponCooldownTime = 0
                            thingsToUpdateEachFrame.add(instance)
                # add zombie on z press
                if event.unicode == "z":
                    instance = Zombie(1)
                    thingsToUpdateEachFrame.add(instance)

                if event.unicode == "\x1b":
                    activatePauseScreen()
                    # restart game after pause
                    for clock in myClocks:
                        clock.tick()
                    player.isMovingUp = False
                    player.isMovingDown = False
                    player.isMovingLeft = False
                    player.isMovingRight = False
            if event.type == pygame.KEYUP:
                # stop moving
                if event.unicode == "a":
                    player.isMovingLeft = False
                if event.unicode == "d":
                    player.isMovingRight = False
                if event.unicode == "w":
                    player.isMovingUp = False
                if event.unicode == "s":
                    player.isMovingDown = False
    


if __name__ == "__main__":
    main()

