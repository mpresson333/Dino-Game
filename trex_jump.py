import pygame, sys, time, random
from pygame.locals import *
#Importing modules from other files
from trex import trex
from cactus import cactus

#Always call before utilizing pygame functions
pygame.init()
#Sets FPS and starts game clock/
FPS = 40
fpsClock = pygame.time.Clock()
frame_counter = 0

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
#Sets title of GUI frame
pygame.display.set_caption("Dino Jump")
BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

#Sets background color
WHITE = (250, 250, 250)
rex = trex(150)
cacti = pygame.sprite.Group()

#Adds a new cactus sprite to the list of obstacles
def add_cacti():
    plant = cactus(120)
    cacti.add(plant)

#Updates each cactus sprite's location
#Removes the cactus from sprite group if it's off screen
#Scores removed cacti
#Redraws cactus image
def update_cacti():
    for plant in cacti:
        plant.update()

#Updates trex sprite's location and redraws trex image
def update_rex(jumping):
    if jumping:
        rex.move(150)

#Starts game over actions
#Displays an end of game message in a text box
#Kills trex sprite
#Creates new game loop to display end game state
def game_over2(game_over):
    if game_over:
        DISPLAYSURF.fill((255, 255, 255))
        rex.kill()
        for c in cacti:
            c.kill()
        Surf = BASICFONT.render("GAME OVER", 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (10, 10)
        DISPLAYSURF.blit(Surf, Rect)

#Creates a text box with the text provided in location x, y on screen
def display_message(text, x, y):
    print

#Displays current score in a text box
def display_score():
    Surf = BASICFONT.render(str(frame_counter), 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (10, 10)
    DISPLAYSURF.blit(Surf, Rect)

#Displays current time in a text box
def display_time():
    print

#Determines whether the trex sprite collides with a cacti sprite
#If there is a collision, the game is over.
def is_collision():
    if pygame.sprite.spritecollideany(rex, cacti):
        return True
    else:
        return False

#Increases the FPS by 5 every 100 seconds
#This is a placeholder for a challenge exercise.
def increase_FPS():
    if frame_counter % 1000 == 0:
        FPS += 5

#Main game loop
jumping = False
game_over = False
while True:

    #Fill in background
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 190), (400, 190), 2)
    frame_counter += 1

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                jumping = True

    #Update display
    game_over2(game_over)
    if not game_over:
        update_cacti()
        update_rex(jumping)
        if rex.rect.y == 150:
            jumping = False
        display_score()
        increase_FPS()
        game_over = is_collision()
        for plant in cacti:
            DISPLAYSURF.blit(plant.image, plant.rect)
        DISPLAYSURF.blit(rex.image, rex.rect)
        if frame_counter % 75 == 0:
            add_cacti()
    pygame.display.update()
    fpsClock.tick(FPS)
