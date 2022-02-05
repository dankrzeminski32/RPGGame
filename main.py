import pygame
import random
from data.sprites.player import Player

def main():
    # initialize pygame

    pygame.init()

    #define screen width and screen height

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600


    #create a player object
    player = Player()

    # variable to keep game running
    running = True

    # Import pygame.locals for easier access to key coordinates
    # Key handler constants
    from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
    )

    # create a screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
    # Main Loop
    while running:
        #look at event queue
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)

        screen.fill((200,0,0))

        screen.blit(player.surf, player.rect)

        pygame.display.flip()
        
    
if __name__ == '__main__': main()