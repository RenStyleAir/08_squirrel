# Squirrel Eat Squirrel, by Al Sweigart al@inventwithpython.com
# (Pygame) A game where squirrels eat each other and grow monstrously large.



import random, sys, time, math, pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HALF_WINWIDTH = int(WINWIDTH /2 )
HALF_WINHEIGHT = int(WINHEIGHT /2 )

GRASSCOLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

CAMERASLACK = 90
MOVERATE = 9
BOUNCERATE = 6
BOUNCEHEIGHT = 30
STARTSIZE = 25
WINSIZE = 300
INVULNTIME = 2
GAMEOVERTIME = 4
MAXHEALTH = 3

NUMGRASS = 80
NUMSQUIRRELS = 30
SQUIRRELNIMSPEED = 3
SQUIRRELMAXSPEED = 7
DIRCHANGEFREQ = 2
LEFT = 'left'
RIGHT = 'right'

"""
This program has three data structures to represent the player, enemy squirrels, and grass background objects. The data structures are dictionaries with the following keys:

Keys used by all three data structures:
    'x' - the left edge coordinate of the object in the game world (not a pixel coordinate on the screen)
    'y' - the top edge coordinate of the object in the game world (not a pixel coordinate on the screen)
    'rect' - the pygame.Rect object representing where on the screen the object is located.
Player data structure keys:
    'surface' - the pygame.Surface object that stores the image of the squirrel which will be drawn to the screen.
    'facing' - either set to LEFT or RIGHT, stores which direction the player is facing.
    'size' - the width and height of the player in pixels. (The width & height are always the same.)
    'bounce' - represents at what point in a bounce the player is in. 0 means standing (no bounce), up to BOUNCERATE (the completion of the bounce)
    'health' - an integer showing how many more times the player can be hit by a larger squirrel before dying.
Enemy Squirrel data structure keys:
    'surface' - the pygame.Surface object that stores the image of the squirrel which will be drawn to the screen.
    'movex' - how many pixels per frame the squirrel moves horizontally. A negative integer is moving to the left, a positive to the right.
    'movey' - how many pixels per frame the squirrel moves vertically. A negative integer is moving up, a positive moving down.
    'width' - the width of the squirrel's image, in pixels
    'height' - the height of the squirrel's image, in pixels
    'bounce' - represents at what point in a bounce the player is in. 0 means standing (no bounce), up to BOUNCERATE (the completion of the bounce)
    'bouncerate' - how quickly the squirrel bounces. A lower number means a quicker bounce.
    'bounceheight' - how high (in pixels) the squirrel bounces
Grass data structure keys:
    'grassImage' - an integer that refers to the index of the pygame.Surface object in GRASSIMAGES used for this grass object
"""

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Squirrel eat Squirrel')
    BASICFONT = pygame.font.Font('freesansbold', 32)

    # 
    L_SQUIR_IMG = pygame.image.load('squirrel.png')
    R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)
    GRASSIMAGES = []
    for i in range(1,5):
        GRASSIMAGES.append(pygame.image.load('grass%s.png'% i ))

    while True:
        runGame()


def runGame():
    # 
    invulnerableMode = False
    invulnerableStartTime = 0   
    gameOverMode = False
    gameOverStartTime = 0
    winMode = False

    # 
    gameOverSurf = BASICFONT.render('Game Over', True, WHITE)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    winSurf = BASICFONT.render('You have achieved OMEGA SQUIRREL!', True, WHITE )
    winRect = winSurf.get_rect()
    winRect.center = (HALF_WINWIDTH, HALF_WINWIDTH)

    winSurf2 = BASICFONT.render('(Press "r" to restart)', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT + 30)

    # 
    camerax = 0
    cameray = 0 

    grassObjs = []
    squirrelObjs = []
    # 
    playerObj = {'surface': pygame.transform.scale(L_SQUIR_IMG, (STARTSIZE, STARTSIZE)),
        'facing': LEFT,
        'size': STARTSIZE,
        'x': HALF_WINWIDTH,
        'y': HALF_WINHEIGHT,
        'bounce': 0,
        'health': MAXHEALTH}

    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    # 
    for i in range(10):
        grassObjs.append(makeNewGrass(camerax, cameray))
        grassObjs[i]['x'] = random.randint(0,WINWIDTH)
        grassObjs[i]['y'] = random.randint(0,WINHEIGHT)

    while True:
        # 
        if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
            invulnerableMode = False

        # 
        for sObj in squirrelObjs:
            # 
            sObj['x'] += sObj['movex']
            sObj['y'] += sObj['movey']
            sObj['bounce'] += 1
            if sObj['bounce'] > sObj['bouncerate']:
                sObj['bounce'] = 0 













