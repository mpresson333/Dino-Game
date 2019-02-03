import pygame, sys, time, random
from pygame.locals import *
#Importing modules from other files
from trex import trex
from cactus import cactus

#Always call before utilizing pygame functions
pygame.init()

#Sets FPS and starts game clock/
FPS = 10
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
#Sets title of GUI frame
pygame.display.set_caption("Dino Jump")

#Sets background color
WHITE = (250, 250, 250)

#Adds a new cactus sprite to the list of obstacles
def add_cacti():

#Updates each cactus sprite's location
#Removes the cactus from sprite group if it's off screen
#Scores removed cacti
#Redraws cactus image
def update_cacti():

#Updates trex sprite's location and redraws trex image
def update_rex():

#Starts game over actions
#Displays an end of game message in a text box
#Kills trex sprite
#Creates new game loop to display end game state
def game_over():

#Creates a text box with the text provided in location x, y on screen
def display_message(text, x, y):

#Displays current score in a text box
def display_score():

#Displays current time in a text box
def display_time():

#Determines whether the trex sprite collides with a cacti sprite
#If there is a collision, the game is over.
def is_collision():

#Increases the FPS by 5 every 100 seconds
#This is a placeholder for a challenge exercise.
def increase_FPS():

#Main game loop
while True:
    #Fill in background
    DISPLAYSURF.fill(WHITE)

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Update display
    pygame.display.update()
    fpsClock.tick(FPS)
