#import modules
import pygame
import sys
from pygame.locals import *
from pet import Pet

#initialize pygame
pygame.init()

#loads music to python readable form
def loadMusic(music):
    pygame.mixer.music.load(music)

#loads images to python readable form
def loadImage(image, alpha=False):
    image = pygame.image.load(image)
    return image.convert_alpha() if alpha else image.convert()

#assign Clock object that will set the frame rate
fpsClock = pygame.time.Clock()

#set window size (270, 270)
screen = pygame.display.set_mode((350, 270), 0, 32)

#sets title of window
pygame.display.set_caption('Tamagotchi')

#retrieve miscellaneous images
screenIcon = loadImage('images/pet/idleL1.png', True)

#sets icon on window
pygame.display.set_icon(screenIcon)

#retrieve theme music
pygame.mixer.init()
pygame.mixer.music.load('./music/theme.ogg')

#plays background music indefinitely starting at 0 sec
pygame.mixer.music.play(-1, 0)

#set the delay and interval for a pygame.KEYDOWN event to repeat
pygame.key.set_repeat(1, 10)

#retrieve player images
petIdleL1 = loadImage('images/pet/idleL1.png', True)
petIdleL2 = loadImage('images/pet/idleL2.png', True)
petIdleR1 = loadImage('images/pet/idleR1.png', True)
petIdleR2 = loadImage('images/pet/idleR2.png', True)

#create a Pet object named pet
pet = Pet(petIdleL2)
pet.setWidth(108)
pet.setHeight(108)
pet.setPosition(screen.get_width() / 2 - pet.getWidth() / 2, screen.get_height() / 2 - pet.getHeight() / 2)
pet.setIdleLAnim(2, petIdleL1, petIdleL2)
pet.setIdleRAnim(2, petIdleR1, petIdleR2)
#pet.setStep(21)

movingLeft = True

#main loop for running the game
while True:

    #allows user to exit game when necessary
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == K_m:
            pass

    #draws background image
    screen.blit(loadImage('images/bg/pattern.jpg'), (0, 0))

    if pet.getX() < 80:
        movingLeft = False
    elif pet.getX() > screen.get_width() - pet.getWidth() - 80:
        movingLeft = True

    if movingLeft:
        pet.moveIdleL()
    else:
        pet.moveIdleR()

    #sets hero in center of upper-left grass tile
    screen.blit(pet.getImage(), pet.getPosition())

    #updates what happens onto the screen
    pygame.display.update()

    #sets frame rate
    fpsClock.tick(20)

pygame.quit()
sys.exit()
