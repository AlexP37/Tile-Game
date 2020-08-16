#Initialization
import os
import pygame
import math
import random
from PIL import Image, ImageDraw
pygame.init()
pygame.font.init()
display_width = 750
display_height = 750
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tile Based RPG')
clock = pygame.time.Clock()
gameDisplay.fill((255,255,255))


#Functions
def textBoxBlack(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

def textBoxWhite(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (255,255,255)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

def makeGame():
    print("Game Initialised")
    gameDisplay.fill((0,0,0))
    pygame.display.update()

#Opening Menu
cont = False
pygame.draw.rect(gameDisplay, (0,0,0), (250, 250, 100, 100))
textBoxBlack("START", 20, (300,300), (255,255,255))
while cont == False:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.font.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
                pygame.quit()
                pygame.font.quit()
                quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 250 < mx < 350:
                if 250 < my < 350:
                    cont = True
    pygame.display.update()

#Begins Game
makeGame()
end = False
avatX = 25
avatY = 313

enemyX = 720
enemyY = 720

avatDown = False
avatUp = False
avatRight = False
avatLeft = False
avatLeftIn = False
avatRightIn = False
avatDownIn = False
avatUpIn = False

speed = 1

csizeX = 26
csizeY = 30

bullets = []

# PILimg = Image.new('RGB', (750, 750), color = (0,0,0))

# movabil = []

# f = open("tiles/map1.txt")
# for l in f:
#     lin = l.split("|")
#     movabil.append(lin[1])
# f.close()

# print(movabil)

# def makeMap():
#     global PILimg
#     global MAPimg

#     imgCount = -1

#     for y in range(10):
#         for x in range(10):
#             imgCount = imgCount + 1
#             imgNumber = movabil[imgCount]
#             PILimg.paste(Image.open('tiles/' + imgNumber + '.png'), (75*x, 75*y))
#     MAPimg = pygame.image.fromstring(PILimg.tobytes(), PILimg.size, PILimg.mode)

# makeMap()

movementCount = 0

arrowX = avatX
arrowY = avatY

arrow = False
arrowFire = False
    
shooting = False

rotateArrowDEG = 0

while end == False:
    # gameDisplay.blit(MAPimg, (0,0))

    img = pygame.image.load('map1.png')

    gameDisplay.blit(img, (0,0))

    clock.tick(60)
    

    # s = pygame.Surface((csize, csize)) # Size of Shadow
    # s.set_alpha(180) # Alpha of Shadow
    # s.fill((0, 255, 255)) # Color of Shadow
    # gameDisplay.blit(s, ((avatX - 2), (avatY - 2))) # Position of Shadow
    # pygame.draw.rect(gameDisplay, (0, 255, 255), (avatX, avatY, csize, csize)) # Location, location, size, size

    # pygame.draw.rect(gameDisplay, (0,0,155), (enemyX, enemyY, csize, csize))
    if arrowFire == False:
        arrowX = avatX
        arrowY = avatY

    if arrow == True:
        arrowDifL = avatX - mx
        arrowDifH = avatY - my
        rotateArrow = math.atan2(arrowDifL, arrowDifH)
        rotateArrowDEG = 90+(rotateArrow * (180/math.pi))
        
        print(rotateArrowDEG)
        
        arrowSin = -1 * math.sin(rotateArrowDEG / (180/math.pi))
        arrowCos = math.cos(rotateArrowDEG / (180/math.pi))

        avatShootX = avatX
        avatShootY = avatY
        arrow = False

    if arrowFire == True:
        arrowX = arrowX + (8.00 * (arrowCos))
        arrowY = arrowY + (8.00 * (arrowSin))
        if arrowY <= 0 or arrowY >= 750 or arrowX <= 0 or arrowX >= 750:
            arrow = False
            arrowFire = False

        arrowPic = pygame.image.load('arrowPic.png')
        arrowPic = pygame.transform.rotate(arrowPic, rotateArrowDEG)

        gameDisplay.blit(arrowPic, (arrowX, arrowY))

    CHARACTERimg = pygame.image.load('arrowRunning.png')
    if shooting == True:
        CHARACTERimg = pygame.image.load('arrowShooting.png')

    if avatUp == True:
        avatY = avatY - speed
    if avatDown == True:
        avatY = avatY + speed
    if avatRight == True:
        avatX = avatX + speed
    if avatLeft == True:
        avatX = avatX - speed
        if avatRight == False:
            CHARACTERimg = pygame.image.load('arrowRunningL.png')
        if shooting == True:
            CHARACTERimg = pygame.image.load('arrowShootingL.png')

    if avatX > 750 - csizeX:
        avatX = 750 - csizeX
    if avatX < 0:
        avatX = 0

    if avatY > 750 - csizeY:
        avatY = 750 - csizeY
    if avatY < 0:
        avatY = 0

    gameDisplay.blit(CHARACTERimg, (avatX, avatY))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            pygame.quit()
            pygame.font.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                speed = speed * 4
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                avatUp = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                avatDown = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                avatRight = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                avatLeft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                speed = speed / 4
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                avatUp = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                avatDown = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                avatRight = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                avatLeft = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            shooting = True
            arrow = True
            arrowFire = True
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            shooting = False

            
    pygame.display.update()

#Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()