from os import times
from pprint import pprint
from sprite import Sprite
from zombie import Zombie
from updateWeapon import Hammer
import pygame.draw
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

    # create a surface on screen
    screen: pygame.Surface = pygame.display.set_mode((config.swidth,config.sheight))
    Sprite.default_screen = screen 

    #making some variables
    player = Player(0, 0, "/home/ciaran/Downloads/token_5.png", config.playerSpeed, config.playerSize)
    isMovingLeft = False
    movingLeftClock = pygame.time.Clock()
    isMovingRight = False
    movingRightClock = pygame.time.Clock()
    isMovingUp = False
    movingUpClock = pygame.time.Clock()
    isMovingDown = False
    movingDownClock = pygame.time.Clock()
    GameClock = pygame.time.Clock()

    thingsToUpdateEachFrame = set()
    enemies = []

    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        timeSinceLastRender = GameClock.tick()
        # move player with wasd
        if isMovingLeft == True:
            player.xpos -= player.speed*movingLeftClock.tick()
        if isMovingRight == True:
            player.xpos += player.speed*movingRightClock.tick()
        if isMovingUp == True:
            player.ypos -= player.speed*movingUpClock.tick()
        if isMovingDown == True:
            player.ypos += player.speed*movingDownClock.tick()

        # put images on screen
        screen.fill("blue")

        screen.blit(player.surface, [player.xpos,player.ypos])
        for instance in thingsToUpdateEachFrame.copy():
            try:
                instance.coro.send(config.Inputs(timeSinceLastRender, player.xpos, player.ypos))
            except StopIteration:
                thingsToUpdateEachFrame.remove(instance)

        # quick fix TO DO come back to this and make sure its good
        for data in enemies:
            print(data)




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
                    isMovingLeft = True
                    movingLeftClock.tick()
                if event.unicode == "d":
                    isMovingRight = True
                    movingRightClock.tick()
                if event.unicode == "w":
                    isMovingUp = True
                    movingUpClock.tick()
                if event.unicode == "s":
                    isMovingDown = True
                    movingDownClock.tick()
                # attack
                if event.unicode == " ":
                    # if same or different then 0, if right then 1, if left then -1
                    movingx = isMovingRight-isMovingLeft
                    # if same or different then 0, if down then 1, if down then -1
                    movingy = isMovingDown-isMovingUp

                    # code to start updating weapons
                    instance = Hammer(1, [], player.xpos, player.ypos, movingx, movingy, screen)
                    thingsToUpdateEachFrame.add(instance)
                    next(instance.coro, None)
                # add zombie on z press
                if event.unicode == "z":
                    # new_data = [0, len(enemies)]
                    instance = Zombie(1)
                    instance.update(screen, 1)
                    # enemies.append(new_data)
                    thingsToUpdateEachFrame.add(instance)
                    next(instance.update, None)
            if event.type == pygame.KEYUP:
                # stop moving
                if event.unicode == "a":
                    isMovingLeft = False
                if event.unicode == "d":
                    isMovingRight = False
                if event.unicode == "w":
                    isMovingUp = False
                if event.unicode == "s":
                    isMovingDown = False

if __name__ == "__main__":
    main()
