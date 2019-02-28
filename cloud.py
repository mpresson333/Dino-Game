import pygame, sys, time, random
from pygame.locals import *

#Image for cactus sprite
CLOUD = pygame.image.load('resources/cloud.png')

#Extends functionality from the Sprite class
class cloud(pygame.sprite.Sprite):

    #Initialize the attributes related to the cactus's position, image, hitbox, and jumping status
    def __init__(self):

        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        #Don't forget to add rect and image attributes!
        self.x = 400
        self.y = 50
        self.image = CLOUD
        self.rect = pygame.Rect(self.x, self.y, 0, 0)

    #Changes the cactus's horizontal location
    def move(self):
        self.rect.x -= 1

    #Updates the cactus's horizonal location.
    #If it's in the window, it will move.
    #If it's outside the window, the sprite will be killed.
    def update(self):
        if self.rect.x < -300:
            self.kill()
        else:
            self.move()
