import pygame, sys, time, random
from pygame.locals import *
#Importing modules from other files
from trex import trex
from cactus import cactus
from cloud import cloud

#Always call before utilizing pygame functions
pygame.init()
#Sets FPS and starts game clock/
FPS = 40
fpsClock = pygame.time.Clock()
frame_counter = 0
pygame.mixer.music.load('resources/gerudo.mp3')
pygame.mixer.music.play(-1, 0.0)

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
#Sets title of GUI frame
pygame.display.set_caption("Dino Jump")
BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

#Sets background color
WHITE = (250, 250, 250)
rex = trex(150)
cacti = pygame.sprite.Group()
clouds = pygame.sprite.Group()

#Adds a new cactus sprite to the list of obstacles
def add_cacti():
    plant = cactus(120)
    cacti.add(plant)

def add_cloud():
    x = cloud()
    clouds.add(x)

#Updates each cactus sprite's location
#Removes the cactus from sprite group if it's off screen
#Scores removed cacti
#Redraws cactus image
def update_cacti():
    for plant in cacti:
        plant.update()

def update_clouds():
    for y in clouds:
        y.update()

#Updates trex sprite's location and redraws trex image
def update_rex(jumping):
    if jumping:
        rex.move(150)
    if frame_counter % 3 == 0:
        rex.image = DINO[0]
    elif frame_counter % 3 == 1:
        rex.image = DINO[1]
    elif frame_counter % 3 == 2:
        rex.image = DINO[2]

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
        for c in clouds:
            c.kill()
        Surf = BASICFONT.render("GAME OVER", 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (10, 10)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render("PRESS ENTER TO RESTART", 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (150, 150)
        DISPLAYSURF.blit(Surf, Rect)
        Surf = BASICFONT.render("SCORE: " + str(frame_counter), 1, (0,0,0))
        Rect = Surf.get_rect()
        Rect.topleft = (10, 250)
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
    if frame_counter % 500 == 0:
        return FPS + 5
    else:
        return FPS

#Main game loop
jumping = False
game_over = False
DINO = [pygame.image.load('resources/dino1.png'), pygame.image.load('resources/dino2.png'), pygame.image.load('resources/dino3.png')]
while True:

    #Fill in background
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 190), (400, 190), 2)
    if not game_over:
        frame_counter += 1
    restart = False

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                jumping = True
            if event.key == K_RETURN:
                restart = True

    #some functionality
    game_over2(game_over)
    if not game_over:
        update_cacti()
        update_clouds()
        update_rex(jumping)
        if rex.rect.y == 150:
            jumping = False
        FPS = increase_FPS()
        game_over = is_collision()
        if frame_counter % 75 == 0:
            add_cacti()
        if frame_counter % 500 == 5:
            add_cloud()

    #Update display
        for plant in cacti:
            DISPLAYSURF.blit(plant.image, plant.rect)
        for x in clouds:
            DISPLAYSURF.blit(x.image, x.rect)
        display_score()
        DISPLAYSURF.blit(rex.image, rex.rect)

    if game_over and restart:
        rex = trex(150)
        FPS = 40
        frame_counter = 0
        game_over = False

    pygame.display.update()
    fpsClock.tick(FPS)
