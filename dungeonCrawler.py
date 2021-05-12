import collections
import typing
import math
from sprite import Sprite
from zombie import Zombie
from updateWeapon import Hammer
import pygame # python works when only importing a submodule, but apparently pylance is dumb enough to require this import
import pygame.draw, pygame.display, pygame.image, pygame.surface
from player import Player
import config

# define a main function
def main():
   
    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo: pygame.Surface = pygame.image.load("/home/ciaran/Downloads/token_5.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("my test game")

    #making some variables
    player = Player()
    GameClock = pygame.time.Clock()

    thingsToUpdateEachFrame = set()
    thingsToUpdateEachFrame.add(player)
    next(player.coro, None)

    enemies = []

    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
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
                key = (instance.xpos//boxSize,instance.ypos//boxSize)
                dictionary.setdefault(key, [])
                dictionary[key].append(instance)
        for key, instancesToCheck in dictionary.items():
            keyx,keyy = key

            keysOfGroups:typing.List[tuple] = []
            # instancesToCheck += dictionary[group+1]
            for xKeyComponent in [-1,0,1]:
                for yKeyComponent in [-1,0,1]:
                    newKey = (keyx+xKeyComponent,keyy+yKeyComponent)
                    if newKey in dictionary.keys():
                        keysOfGroups.append(newKey)


            for thisCellInstance in instancesToCheck:
                for group in keysOfGroups:
                    for otherCellInstance in dictionary[group]:
                        # TO DO make it so I don't need to check every time (only if same cell?)
                        if thisCellInstance != otherCellInstance:
                            if config.isColliding(thisCellInstance, otherCellInstance) == True:
                                # TO DO make them do stuff
                                print("OMG THERE'S A COLLISION")


        # put images on screen
        config.screen.fill("blue")

        for instance in thingsToUpdateEachFrame.copy():
            try:
                instance.coro.send(config.Inputs(timeSinceLastRender, player.xpos, player.ypos, enemies))
            except StopIteration:
                thingsToUpdateEachFrame.remove(instance)


        pygame.display.update()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            print(event)
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # move player with wasd
            if event.type == pygame.KEYDOWN:
                # start moving
                if event.unicode == "a":
                    player.isMovingLeft = True
                    player.movingLeftClock.tick()
                if event.unicode == "d":
                    player.isMovingRight = True
                    player.movingRightClock.tick()
                if event.unicode == "w":
                    player.isMovingUp = True
                    player.movingUpClock.tick()
                if event.unicode == "s":
                    player.isMovingDown = True
                    player.movingDownClock.tick()
                # attack
                if event.unicode == " ":
                    # if same or different then 0, if right then 1, if left then -1
                    movingx = player.isMovingRight-player.isMovingLeft
                    # if same or different then 0, if down then 1, if down then -1
                    movingy = player.isMovingDown-player.isMovingUp
                    
                    isRendering = True

                    if abs(movingy - movingx) == 1:
                        weaponxpos = player.xpos + (movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
                        weaponypos = player.ypos + (movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))
                    elif movingy==0 & movingx==0:
                        isRendering = False
                    else:
                        weaponxpos = player.xpos + (1/math.sqrt(2))*(movingx*((config.hammerSmashSize/2)+(config.playerSize/2)))
                        weaponypos = player.ypos + (1/math.sqrt(2))*(movingy*((config.hammerSmashSize/2)+(config.playerSize/2)))

                    # code to start updating weapons
                    if isRendering == True:    
                        instance = Hammer(1, enemies, weaponxpos, weaponypos, movingx, movingy, config.screen)
                        thingsToUpdateEachFrame.add(instance)
                        next(instance.coro, None)
                # add zombie on z press
                if event.unicode == "z":
                    # new_data = [0, len(enemies)]
                    instance = Zombie(1)
                    # enemies.append(new_data)
                    thingsToUpdateEachFrame.add(instance)
                    next(instance.coro, None)
                    enemies.append(instance)
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
