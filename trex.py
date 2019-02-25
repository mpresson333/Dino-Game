import pygame, sys, time, random
from pygame.locals import *

#Images for trex sprite
DINO = [pygame.image.load('resources/dino1.png'), pygame.image.load('resources/dino2.png'), pygame.image.load('resources/dino3.png')]

#Extends functionality from the Sprite class
class trex(pygame.sprite.Sprite):

    #Initialize the attributes related to the trex's position (x and y coords), image, and rectangle hitbox
    def __init__(self, ground):

        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        self.x = 25
        self.y = ground
        self.image = DINO[0]
        self.rect = pygame.Rect(self.x, self.y, 15, 15)
        self.counter = 1

    #Change the trex's vertical position to above the ground
    def up(self):
        self.rect.y -= 5

    #Change the trex's vertical position gradually to fall down to the ground
    def fall(self):
        self.rect.y += 5

    #Change the trex's position based on updates from the game.
    #How do you know if the trex should be falling, going up, or stationary?
    def move(self, ground):

        if self.rect.y > 80 and self.counter % 10 != 0:
            self.up()
        elif self.rect.y == 80:
            self.counter += 1
        if self.counter % 10 == 0:
            self.fall()
        if self.rect.y == ground:
            self.counter = 1

    #Update the trex's game status with regards to movement
    # and later animation (challenge)
    def update(self):
        print

    #Select which frame to display for your sprite
    #This is a placeholder for a challenge exercise.
    def animate(self):
        print
