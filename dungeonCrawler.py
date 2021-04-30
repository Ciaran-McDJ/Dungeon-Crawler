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
        # move player with wasd


        # put images on screen
        screen.fill("blue")

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

                    # code to start updating weapons
                    instance = Hammer(1, enemies, player.xpos, player.ypos, movingx, movingy, screen)
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
