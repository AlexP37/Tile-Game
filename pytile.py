#Initialization
import os
import pygame
import math
import random

os.system("clear")

pygame.init()
pygame.font.init()
display_width = 750
display_height = 750
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Arrowverse: Enter The League')
clock = pygame.time.Clock()
gameDisplay.fill((255,255,255))

line =[]

f = open("map1.txt", "r")
# read in each line of the file
for l in f:
    # split the file on the pipes "|"
    singleLine = l.split("|")
    singleLine.remove(singleLine[-1])
    line.append(singleLine)
f.close()

# print(line)

# for i in line:
#     print(i)

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

def textBoxClear(text, size, position, color):
    font = pygame.font.Font('Serpentine-BoldOblique.otf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect)

def textBoxClearR(text, size, position, color):
    font = pygame.font.Font('Courier.dfont', size)
    font.set_bold(True)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.midright = position
    gameDisplay.blit(text, textRect)

def textBoxClearLemonMilk(text, size, position, color):
    font = pygame.font.Font('LemonMilklightFt.otf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect)

def makeGame():
    print("Game Initialised")
    gameDisplay.fill((0,0,0))
    pygame.display.update()

def col():
    global avatX
    global avatY
    global avatX_OG
    global avatY_OG

    m = 0
    X = avatX
    Y = avatY
    while m < 4:
        m = m + 1

        for co in line:
            if (int(co[0]) < X < int(co[1])) and (int(co[2]) < Y < int(co[3])):

        # if (X < 44 and Y < 280) or (X < 510 and Y < 18) or ((108 < X < 272) and (80 < Y < 280)) or ((338 < X < 436) and (82 < Y < 280)) or ((496 < X < 566) and (82 < Y < 280)) or ((566 < X < 750) and (0 < Y < 280)) or ((X < 130) and (376 < Y)) or ((702 < Y)) or ((314 < X) and (612 < Y)) or ((176 < X < 260) and (376 < Y < 658)) or ((622 < X) and (376 < Y)) or ((314 < X < 576) and (376 < Y < 498)) or ((486 < X < 576) and (498 < Y < 538)) or ((314 < X < 576) and (538 < Y < 569)):
                avatX = avatX_OG
                avatY = avatY_OG
                m = 4

        if m == 1:
            X = avatX + csizeX
        elif m == 2:
            Y = avatY + csizeY
        elif m == 3:
            X = avatX
            
    avatX_OG = avatX
    avatY_OG = avatY

def ENEMYcolY():
    global enemies
    global enemyOG_X
    global enemyOG_Y

    m = 0
    X = i[0]
    Y = i[1]
    while m < 4:
        m = m + 1

        for co in line:
            if (int(co[0]) < X < int(co[1])) and (int(co[2]) < Y < int(co[3])):

        # if (X < 44 and Y < 280) or (X < 510 and Y < 18) or ((108 < X < 272) and (80 < Y < 280)) or ((338 < X < 436) and (82 < Y < 280)) or ((496 < X < 566) and (82 < Y < 280)) or ((566 < X < 750) and (0 < Y < 280)) or ((X < 130) and (376 < Y)) or ((702 < Y)) or ((314 < X) and (612 < Y)) or ((176 < X < 260) and (376 < Y < 658)) or ((622 < X) and (376 < Y)) or ((314 < X < 576) and (376 < Y < 498)) or ((486 < X < 576) and (498 < Y < 538)) or ((314 < X < 576) and (538 < Y < 569)):
                i[1] = enemyOG_Y
                m = 4

        if m == 1:
            X = i[0] + csizeX
        elif m == 2:
            Y = i[1] + csizeY
        elif m == 3:
            X = i[0]
            
    enemyOG_Y = avatY

def ENEMYcolX():
    global enemies
    global enemyOG_X
    global enemyOG_Y

    m = 0
    X = i[0]
    Y = i[1]
    while m < 4:
        m = m + 1

        for co in line:
            if (int(co[0]) < X < int(co[1])) and (int(co[2]) < Y < int(co[3])):

        # if (X < 44 and Y < 280) or (X < 510 and Y < 18) or ((108 < X < 272) and (80 < Y < 280)) or ((338 < X < 436) and (82 < Y < 280)) or ((496 < X < 566) and (82 < Y < 280)) or ((566 < X < 750) and (0 < Y < 280)) or ((X < 130) and (376 < Y)) or ((702 < Y)) or ((314 < X) and (612 < Y)) or ((176 < X < 260) and (376 < Y < 658)) or ((622 < X) and (376 < Y)) or ((314 < X < 576) and (376 < Y < 498)) or ((486 < X < 576) and (498 < Y < 538)) or ((314 < X < 576) and (538 < Y < 569)):
                i[0] = enemyOG_X
                m = 4

        if m == 1:
            X = i[0] + csizeX
        elif m == 2:
            Y = i[1] + csizeY
        elif m == 3:
            X = i[0]
            
    enemyOG_X = avatX

score = 0

arrowColidedWithBuilding = False

def colArrow():
    global singleArrow
    global multipleArrows
    global arrowX_OG
    global arrowY_OG
    global arrowColidedWithBuilding

    m = 0
    X = i[0]
    Y = i[1]
    for co in line:
        if (int(co[0]) < X < int(co[1])) and (int(co[2]) < Y < int(co[3])):
            arrowColidedWithBuilding = True
            
    arrowX_OG = i[0]
    arrowY_OG = i[1]

def colArrowHit():
    global singleArrow
    global multipleArrows
    global arrowX_OG
    global arrowY_OG
    global arrowColidedWithBuilding
    global enemies

    m = 0
    X = i[0]
    Y = i[1]
    gotcha = False
    for e in enemies:
        if gotcha == False:
            eX = e[0]
            eY = e[1]
            eL = e[3]
            eH = e[4]
            if (eX < X < (eX + eL)) and (eY < Y < (eY + eH)):
                multipleArrows.remove(i)
                e[5] = e[5] - projectilePower
                gotcha = True
        if e[5] <= 0:
            if e[6] == "Shadow Demon":
                score = score + 100
            else:
                score = score + 50
            enemies.remove(e)
            
    arrowX_OG = i[0]
    arrowY_OG = i[1]

def eColArrowHit():
    global eMultipleArrows
    global enemies
    global playerHealth

    m = 0
    X = i[0]
    Y = i[1]

    eX = avatX
    eY = avatY
    eL = csizeX
    eH = csizeY
    
    if (eX < X < (eX + eL)) and (eY < Y < (eY + eH)):
        eMultipleArrows.remove(i)
        if forceField != True or avatar != "The Flash":
            playerHealth = playerHealth - 4
            # print("PLY HEALTH::::::::::: " + str(playerHealth))
    
    if playerHealth <= 0:
        death = True

loadGame = False

#Opening Menu
cont = False
pygame.draw.rect(gameDisplay, (0,0,0), (250, 250, 100, 100))
textBoxBlack("START", 20, (300,300), (255,255,255))
while cont == False:
    clock.tick(60)
    img = pygame.image.load('title.png')
    gameDisplay.blit(img, (0, 0))
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
            if 22 < mx < 727:
                if 627 < my < 717:
                    cont = True
            if 160 < mx < 591:
                if 553 < my < 607:
                    f = open("enemySaves.txt", "r")
                    for l in f:
                        if l != "BLANK":
                            loadGame = True
                            cont = True
                    f.close()
    pygame.display.update()

#Begins Game
makeGame()
end = False
avatX = 25
avatX = 362
avatY = 313

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

playerHealth = 40
playerHealthMax = 40

asizeX = 20
asizeY = 5

movementCount = 0

arrowX = avatX
arrowY = avatY

arrow = False
arrowFire = False
    
shooting = False

speeded = False
doubleSpeeded = False

rotateArrowDEG = 0

singleArrow = []
multipleArrows = []

avatX_OG = avatX
avatY_OG = avatY
arrowX_OG = arrowX
arrowY_OG = arrowY

enemyArrow = False
eRotateArrowDEG = 0
eSingleArrow = []
eMultipleArrows = []

projectilePic = 'arrowPic.png'
standingR = 'arrowRunning.png'
standingL = 'arrowRunningL.png'
movingR = 'flashMoving.png'
movingL = 'flashMovingL.png'
shootingR = 'arrowShooting.png'
shootingL = 'arrowShootingL.png'
forceImg = pygame.image.load('force1.png')
projectilePower = 1

startup = True

enemies = []
enemySINGLE = []
spawnEnemy = 400
enemyX = 760
enemyY = 313
enemyImage = pygame.image.load('archerRunningL.png')
enemyL = 26
enemyH = 30
enemyHealth = 10
arrowSpeed = 8
punch = False
facingLeft = False
pause = False
pause2 = False
charChange = False
charChange2 = False
eArrowTicker = 0

shooterTimer = 0
bulletsLeft = 10
reloadGun = 0

theMouseButtonIsDown = False

charSelector = False

hitbox = False

healthPackCount = 0

healthPacks = []

healthPackRespawnTicker = 20

forceFieldCount = 0
forceField = False
forceFieldUnlock = False
forceFeildUnlockCount = 0
goUp = True

charHitboxIMG = pygame.image.load("charHitbox.png")

characters = [[0, "The Flash"], [1, "Green Arrow"], [2, "Black Lightning"], [3, "Deathstroke"]]
charNum = 0
avatar = "The Flash"

data = []

spawnEmenyCOUNTER = 300

if loadGame == True:
    f = open("saveData.txt", "r")
    # read in each line of the file
    for l in f:
        # split the file on the pipes "|"
        data = l.split("|")
    f.close()

    avatar = data[0]
    charNum = int(data[1])
    healthPackCount = int(data[2])
    playerHealth = int(data[3])
    avatX = int(float(data[4]))
    avatY = int(float(data[5]))
    score = int(float(data[6]))

    f = open("enemySaves.txt", "r")
    # read in each line of the file
    for l in f:
        # split the file on the pipes "|"
        data2 = []
        data = []
        data = l.split("|")
        data2.append(int(data[0]))
        data2.append(int(data[1]))
        data2.append(data[2])
        data2.append(int(data[3]))
        data2.append(int(data[4]))
        data2.append(int(data[5]))
        data2.append(data[6])
        print(data2)
        enemies.append(data2)
    f.close()

else:
    f = open("saveData.txt", "w")
    f.write(str(avatar) + "|" + str(charNum) + "|" + str(healthPackCount) + "|" + str(playerHealth)  + "|" + str(avatX) + "|" + str(avatY) + "|" + str(score))
    f.close()
    f = open("enemySaves.txt", "w")
    f.write("BLANK")
    f.close()

maxHealth = False

while end == False:

    if playerHealth <= 0:
        f = open("saveData.txt", "w")
        f.write(str(avatar) + "|" + str(charNum) + "|" + str(healthPackCount) + "|" + str(playerHealth)  + "|" + str(avatX) + "|" + str(avatY) + "|" + str(score))
        f.close()
        f = open("enemySaves.txt", "w")
        f.write("BLANK")
        f.close()
        s = pygame.Surface((750, 750)) # Size of Shadow
        s.set_alpha(160) # Alpha of Shadow
        s.fill((0, 0, 0)) # Color of Shadow
        gameDisplay.blit(s, (0, 0)) # Position of Shadow
        textBoxClear("You Died...", 100, (375, 555), (255,255,255))
        textBoxClear("PRESS ESC TO EXIT", 50, (375, 640), (255,255,255))
        textBoxClear("PRESS SPACE TO CONTINUE IN ENDLESS MODE", 10, (375, 675), (255,255,255))
        imgE = pygame.image.load('enterTheLeague.png')
        gameDisplay.blit(imgE, (51,20))
        textBoxClear("Score: " + str(int(score)), 40, (375, 710), (255,255,255))
        while end == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        end = True
                        pygame.quit()
                        pygame.font.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        end = True
                if event.type == pygame.QUIT:
                    end = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
            
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                end = False
                maxHealth = True

    if maxHealth == True:
        playerHealthMax = 5000
        playerHealth = playerHealthMax

    if pause == True:
        s = pygame.Surface((750, 750)) # Size of Shadow
        s.set_alpha(160) # Alpha of Shadow
        s.fill((0, 0, 0)) # Color of Shadow
        gameDisplay.blit(s, (0, 0)) # Position of Shadow
        imgP = pygame.image.load('pauseMenu.png')
        gameDisplay.blit(imgP, (0,0))

    while pause == True:
        clock.tick(60)
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
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if (20 < mx < 727) and (605 < my < 727) and (pause2 == True):
                    pause = False
                    pause2 = False
                elif (167 < mx < 582) and (532 < my < 579) and (pause2 == True):
                    pause = False
                    pause2 = False

                    if maxHealth == False:
                        f = open("saveData.txt", "w")
                        f.write(str(avatar) + "|" + str(charNum) + "|" + str(healthPackCount) + "|" + str(playerHealth)  + "|" + str(avatX) + "|" + str(avatY) + "|" + str(score))
                        f.close()

                    enemySaves = ""

                    for i in enemies:
                        for e in i:
                            enemySaves = enemySaves + str(e) + "|"
                        enemySaves = enemySaves + "\n"

                    if maxHealth == False:
                        f = open("enemySaves.txt", "w")
                        f.write(enemySaves)
                        f.close()


                    end = True
                else:
                    pause2 = True

        pygame.display.update()

    if charChange == True:
        s = pygame.Surface((750, 750)) # Size of Shadow
        s.set_alpha(160) # Alpha of Shadow
        s.fill((0, 0, 0)) # Color of Shadow
        gameDisplay.blit(s, (0, 0)) # Position of Shadow
        # imgP = pygame.image.load('pauseMenu.png')
        # gameDisplay.blit(imgP, (0,0))
        ogCharNum = charNum
        ogAvatar = avatar
    
    while charChange == True:
        clock.tick(60)

        pygame.draw.rect(gameDisplay, (200,200,200), (50, 50, 650, 650))

        img = pygame.image.load('rightArrow.png').convert_alpha()
        gameDisplay.blit(img, (590,600))
        img = pygame.image.load('leftArrow.png').convert_alpha()
        gameDisplay.blit(img, (90,600))

        img = pygame.image.load('tickCross.png').convert_alpha()
        gameDisplay.blit(img, (591,65))
        
        img = pygame.image.load('char' + str(charNum) +'.png').convert_alpha()
        imgRect = img.get_rect()
        imgRect.centerx = 375
        imgRect.centery = 325
        gameDisplay.blit(img, imgRect)

        textBoxClear(characters[charNum][1], 47, (375, 622), (0,0,0))
        avatar = characters[charNum][1]

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
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if (595 < mx < 635) and (70 < my < 90) and (charChange2 == True):
                    charChange = False
                    charChange2 = False
                if (642 < mx < 681) and (70 < my < 90) and (charChange2 == True):
                    charChange = False
                    charChange2 = False
                    avatar = ogAvatar
                    charNum = ogCharNum
                else:
                    charChange2 = True
                if (590 < mx < 660) and (600 < my < 655):
                    charNum = charNum + 1
                elif (90 < mx < 160) and (600 < my < 655):
                    charNum = charNum - 1
                if charNum == -1:
                    charNum = characters[-1][0]
                if charNum > characters[-1][0]:
                    charNum = 0

        pygame.display.update()
    # gameDisplay.blit(MAPimg, (0,0))

    img = pygame.image.load('map1.png')
    gameDisplay.blit(img, (0,0))

    clock.tick(60)

    eProjectilePic = 'arrowPic2.png'

    if avatar == 'The Flash':
        projectilePic = ''
        standingR = 'flashStanding.png'
        standingL = 'flashStandingL.png'
        shootingR = 'flashAttack.png'
        shootingL = 'flashAttackL.png'
        movingR = 'flashMoving.png'
        movingL = 'flashMovingL.png'
        projectileIconIMG = 'forceFeildIcon.png'
        projectileIcon = projectileIconIMG
        projectileIconIMG2 = ''
        projectileIconIMG3 = ''
        projectileIconIMG4 = ''
        csizeX = 26
        csizeY = 30
        asizeX = 0
        asizeY = 0
        arrowSpeed = 0

    if avatar == 'Green Arrow':
        projectilePic = 'arrowPic.png'
        standingR = 'arrowRunning.png'
        standingL = 'arrowRunningL.png'
        shootingR = 'arrowShooting.png'
        shootingL = 'arrowShootingL.png'
        projectileIconIMG = 'bow.png'
        projectileIconIMG2 = 'bowAndArrow1.png'
        projectileIconIMG3 = 'bowAndArrow2.png'
        projectileIconIMG4 = 'bowAndArrow3.png'
        movingR = ''
        movingL = ''
        arrowSpeed = 8
        csizeX = 26
        csizeY = 30
        asizeX = 20
        asizeY = 5
        projectilePower = 4

    if avatar == 'Deathstroke':
        projectilePic = 'bulletPic.png'
        standingR = 'deathstrokeRunning.png'
        standingL = 'deathstrokeRunningL.png'
        shootingR = 'deathstrokeShooting.png'
        shootingL = 'deathstrokeShootingL.png'
        projectileIconIMG = 'gun' + str(bulletsLeft) + '.png'
        projectileIconIMG2 = ''
        projectileIconIMG3 = ''
        projectileIconIMG4 = ''
        movingR = ''
        movingL = ''
        arrowSpeed = 10
        csizeX = 26
        csizeY = 30
        asizeX = 5
        asizeY = 3
        projectilePower = 2

    if avatar == 'Black Lightning':
        projectilePic = 'electricityPic.png'
        standingR = 'blightningRunning.png'
        standingL = 'blightningRunningL.png'
        shootingR = 'blightningShooting.png'
        shootingL = 'blightningShootingL.png'
        projectileIconIMG = 'electricityBall.png'
        projectileIconIMG2 = 'electricityCharging1.png'
        projectileIconIMG3 = 'electricityCharging2.png'
        projectileIconIMG4 = 'electricityCharging3.png'
        movingR = ''
        movingL = ''
        arrowSpeed = 15
        csizeX = 26
        csizeY = 30
        asizeX = 10
        asizeY = 6
        projectilePower = 3


    # s = pygame.Surface((csize, csize)) # Size of Shadow
    # s.set_alpha(180) # Alpha of Shadow
    # s.fill((0, 255, 255)) # Color of Shadow
    # gameDisplay.blit(s, ((avatX - 2), (avatY - 2))) # Position of Shadow
    # pygame.draw.rect(gameDisplay, (0, 255, 255), (avatX, avatY, csize, csize)) # Location, location, size, size

    # pygame.draw.rect(gameDisplay, (0,0,155), (enemyX, enemyY, csize, csize))

    if projectilePic != '':

        # print(str(shooterTimer) + "THIS IS THE SHOOTER TIMER")

        if avatar != "Deathstroke":
            if shooterTimer == 0:
                projectileIcon = projectileIconIMG
            elif shooterTimer == 1:
                projectileIcon = projectileIconIMG2
            elif shooterTimer == 2:
                projectileIcon = projectileIconIMG3
            elif shooterTimer >= 3:
                projectileIcon = projectileIconIMG4
        else:
            projectileIcon = projectileIconIMG
        
        if bulletsLeft <= 0:
            reloadGun = reloadGun + 1
            s = pygame.Surface((50, (50 - (5 * reloadGun)/6))) # Size of Shadow
            s.set_alpha(80) # Alpha of Shadow
            s.fill((255, 130, 0)) # Color of Shadow
            gameDisplay.blit(s, (198, 4)) # Position of Shadow

            # pygame.draw.rect(gameDisplay, (0,0,155), (enemyX, enemyY, csize, csize))
            if reloadGun >= 60:
                bulletsLeft = 10
                reloadGun = 0

        if arrow == True:
            arrow = False

            if avatar == "Deathstroke":
                shooterTimer = 4

            if shooterTimer > 3 and bulletsLeft > 0:
                if avatar == "Deathstroke":
                    bulletsLeft = bulletsLeft - 1

                arrowX = avatX + (csizeX / 2)
                arrowY = avatY + (csizeY / 2)

                arrowDifL = arrowX - mx
                arrowDifH = arrowY - my
                rotateArrow = math.atan2(arrowDifL, arrowDifH)
                rotateArrowDEG = 90+(rotateArrow * (180/math.pi))
                
                # print(rotateArrowDEG)
                
                arrowSin = -1 * math.sin(rotateArrowDEG / (180/math.pi))
                arrowCos = math.cos(rotateArrowDEG / (180/math.pi))

                singleArrow.append(arrowX)
                singleArrow.append(arrowY)
                singleArrow.append(arrowCos)
                singleArrow.append(arrowSin)
                singleArrow.append(rotateArrowDEG)
                multipleArrows.append(singleArrow)
                singleArrow = []
                # print(multipleArrows)
            
            shooterTimer = 0

        for i in multipleArrows:
            arrowX_OG = i[0]
            arrowY_OG = i[1]

            i[0] = i[0] + (arrowSpeed * (i[2]))
            i[1] = i[1] + (arrowSpeed * (i[3]))

            colArrow()
            colArrowHit()

            if i[1] <= 0 or i[1] >= 750 or i[0] <= 0 or i[0] >= 750 or arrowColidedWithBuilding == True:
                multipleArrows.remove(i)
                arrowColidedWithBuilding = False
            else:
                arrowPic = pygame.image.load(projectilePic)
                arrowPic = pygame.transform.rotate(arrowPic, i[4])

                gameDisplay.blit(arrowPic, (i[0], i[1]))

    eArrowTicker = eArrowTicker + 1
    eArrow = True
    eArrowSpeed = 8

    if eArrowTicker > 20:
        eArrowTicker = 0
    
        for e in enemies:
            if eArrow == True:

                eArrowX = e[0] + (asizeX / 2)
                eArrowY = e[1] + (asizeY / 2)
                eArrowDifL = eArrowX - avatX - (csizeX/2)
                eArrowDifH = eArrowY - avatY - (csizeY/2)
                eRotateArrow = math.atan2(eArrowDifL, eArrowDifH)
                eRotateArrowDEG = 90+(eRotateArrow * (180/math.pi))
                
                # print(eRotateArrowDEG)
                
                eArrowSin = -1 * math.sin(eRotateArrowDEG / (180/math.pi))
                eArrowCos = math.cos(eRotateArrowDEG / (180/math.pi))

                enemyForm = "Dark Arrow"

                if e[6] == "Shadow Demon":
                    enemyForm = "Shadow Demon"

                eSingleArrow.append(eArrowX)
                eSingleArrow.append(eArrowY)
                eSingleArrow.append(eArrowCos)
                eSingleArrow.append(eArrowSin)
                eSingleArrow.append(eRotateArrowDEG)
                eSingleArrow.append(enemyForm)
                eMultipleArrows.append(eSingleArrow)
                eSingleArrow = []
                # print(eMultipleArrows)
        if eArrow == True:
            eArrow = False

    for i in eMultipleArrows:
        eArrowX_OG = i[0]
        eArrowY_OG = i[1]

        i[0] = i[0] + (eArrowSpeed * (i[2]))
        i[1] = i[1] + (eArrowSpeed * (i[3]))

        colArrow()
        eColArrowHit()

        if i[1] <= 0 or i[1] >= 750 or i[0] <= 0 or i[0] >= 750 or arrowColidedWithBuilding == True:
            eMultipleArrows.remove(i)
            arrowColidedWithBuilding = False
        else:
            if i[5] == "Shadow Demon":
                eProjectilePic = "shadowFire.png"
            else:
                eProjectilePic = "arrowPic2.png"
            arrowPic = pygame.image.load(eProjectilePic)
            arrowPic = pygame.transform.rotate(arrowPic, i[4])

            gameDisplay.blit(arrowPic, (i[0], i[1]))

    spawnEnemy = spawnEnemy + 1
    if spawnEnemy >= spawnEmenyCOUNTER:
        print(spawnEmenyCOUNTER)
        if spawnEmenyCOUNTER > 120:
            spawnEmenyCOUNTER = spawnEmenyCOUNTER - 15
        enemyType = "Dark Arrow"
        enemyImage = pygame.image.load('archerRunningL.png')
        shadowDemon = random.randrange(0,4)
        if shadowDemon == 3:
            enemyType = "Shadow Demon"
            enemyImage = pygame.image.load("shadowDemon.png")

        enemyPosChecker = random.randint(0,2)
        if enemyPosChecker == 1:
            enemyX = 760
            enemyY = 313
        if enemyPosChecker == 2:
            enemyX = 528
            enemyY = -32
        else:
            enemyX = -30
            enemyY = 313

        enemySINGLE.append(enemyX)
        enemySINGLE.append(enemyY)
        enemySINGLE.append(enemyImage)
        enemySINGLE.append(enemyL)
        enemySINGLE.append(enemyH)
        enemySINGLE.append(enemyHealth)
        enemySINGLE.append(enemyType)
        enemies.append(enemySINGLE)
        enemySINGLE = []
        spawnEnemy = 0

    avatX_OG = avatX
    avatY_OG = avatY

    CHARACTERimg = pygame.image.load(standingR)
    if shooting == True:
        CHARACTERimg = pygame.image.load(shootingR)

    if avatUp == True:
        avatY = avatY - speed
        col()
    if avatDown == True:
        avatY = avatY + speed
        col()
    if avatRight == True:
        avatX = avatX + speed
        col()
        facingLeft = False
    if avatLeft == True:
        avatX = avatX - speed
        col()
        facingLeft = True
        if avatRight == False:
            CHARACTERimg = pygame.image.load(standingL)
        if shooting == True:
            CHARACTERimg = pygame.image.load(shootingL)

    if facingLeft == True:
        if shooting == True:
            CHARACTERimg = pygame.image.load(shootingL)
        else:
            CHARACTERimg = pygame.image.load(standingL)

    if (avatUp == True or avatLeft == True or avatRight == True or avatDown == True) and (speeded == True):
        if movingR != '':
            CHARACTERimg = pygame.image.load(movingR)
            if avatRight == False and avatLeft == True:
                CHARACTERimg = pygame.image.load(movingL)

    if avatX > 750 - csizeX:
        avatX = 750 - csizeX
    if avatX < 0:
        avatX = 0

    if avatY > 750 - csizeY:
        avatY = 750 - csizeY
    if avatY < 0:
        avatY = 0
       
    gameDisplay.blit(CHARACTERimg, (avatX, avatY))
    
    forceFieldCount = forceFieldCount + 1

    if forceFieldCount >= 5:
        forceFieldCount = 1

    forceImg = pygame.image.load('force' + str(forceFieldCount) + 'Clear.png')
    if (forceField == True) and (avatar == 'The Flash'):
        gameDisplay.blit(forceImg, (avatX - 2, avatY - 3))

    if forceFeildUnlockCount < 250 and forceFieldUnlock == False and goUp == True:
        forceFeildUnlockCount += 0.5
        if forceFeildUnlockCount >= 250:
            forceFieldUnlock = True
            goUp = False
    
    if forceFeildUnlockCount <= 0:
        goUp = True
    
    if forceField == True:
        forceFeildUnlockCount -= 1
    
    if forceFeildUnlockCount < 0:
        forceField = False
        forceFieldUnlock = False
        forceFeildUnlockCount = 1


    if avatar == 'The Flash':
        p = pygame.Surface((50, ((forceFeildUnlockCount)/5))) # Size of Shadow
        p.set_alpha(180) # Alpha of Shadow
        p.fill((255, 130, 0)) # Color of Shadow
        gameDisplay.blit(p, (199, 3)) # Position of Shadow

    if hitbox == True:
        gameDisplay.blit(charHitboxIMG, (avatX, avatY))

    pygame.draw.rect(gameDisplay, (230,0,0), (40, 12, 140 * (playerHealth / playerHealthMax), 32))

    HealthBarImg = pygame.image.load('HB.png')
    gameDisplay.blit(HealthBarImg, (4, 4))



    newHealthPackX = 470
    newHealthPackY = 513
    
    characterHitbox = pygame.Rect(avatX, avatY, csizeX, csizeY)

    if healthPackCount < 9:
        healthPackRespawnTicker = healthPackRespawnTicker + 1

    # print(str(healthPackCount) + "EHURIAFEIYFKHGA")
    if healthPackRespawnTicker > 250:
        healthPack = [newHealthPackX,newHealthPackY]
        healthPackRespawnTicker = 0

        healthPackSpawn = True
        for i in healthPacks:
            if -15 < (i[0] - newHealthPackX) < 15:
                healthPackSpawn = False
            if -15 < (i[1] - newHealthPackY) < 15:
                healthPackSpawn = False
        
        if healthPackSpawn == True:
            healthPacks.append(healthPack)
            print("SPAWNIGN!!!!!!!!!!!!!!!!!!")

    for i in healthPacks:
        healthPackImg = pygame.image.load('healthGrab.png')
        gameDisplay.blit(healthPackImg, (i[0], i[1]))

        healthPackImgRect = pygame.Rect(i[0], i[1], 12, 12)

        if healthPackImgRect.colliderect(characterHitbox):
            healthPackRespawnTicker = 0
            healthPackCount = healthPackCount + 1
            healthPacks.remove(i)

    punchY = 31
    punchX = 27
    punchXb = -2

    for i in enemies:

        if hitbox == True:
            gameDisplay.blit(charHitboxIMG, (i[0], i[1]))

        pygame.draw.rect(gameDisplay, (230,0,0), (i[0] + 1, i[1] - 10, 2.4 * (i[5]), 8))

        HealthBarImg = pygame.image.load('eHealthBar.png')
        gameDisplay.blit(HealthBarImg, (i[0], i[1] - 12))
        if speeded == True:
            if doubleSpeeded == True:
                punchX = 40
                punchXb = -5
            else:
                punchX = 33
                punchXb = -10
        if punch == True:
            print("punching")
            if -punchY < (i[1] - avatY) < punchY:
                print("y is fine for the punch..")
                if facingLeft == False:
                    if punchXb < (i[0] - avatX) < punchX:
                        print("xxxxxxxx is fine for the punch..")
                        i[5] = i[5] - 6
                        punch = False
                if facingLeft == True:
                    if -punchXb > (i[0] - avatX) > -punchX:
                        print("xxxxx is fine for the punch..")
                        i[5] = i[5] - 6
                        punch = False
            if i[5] <= 0:
                if e[6] == "Shadow Demon":
                    score = score + 100
                else:
                    score = score + 50
                enemies.remove(i)

        enemyOG_X = i[0]

        if avatX - 1 > i[0]:
            i[0] = i[0] + 1
            if i[6] != "Shadow Demon":
                i[2] = pygame.image.load('archerRunning.png')
        elif avatX + 1 < i[0]:
            i[0] = i[0] - 1
            if i[6] != "Shadow Demon":
                i[2] = pygame.image.load('archerRunningL.png')

        if i[6] != "Shadow Demon":
            ENEMYcolX()

        enemyOG_Y = i[1]

        if avatY - 1 > i[1]:
            i[1] = i[1] + 1
        elif avatY + 1 < i[1]:
            i[1] = i[1] - 1

        if i[6] != "Shadow Demon":
            ENEMYcolY()
        
        if i[6] == "Shadow Demon":
            i[2] = pygame.image.load('shadowDemon.png')

        gameDisplay.blit(i[2], (i[0], i[1]))
    
    punch = False

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
                if speeded == False:
                    speed = speed * 4
                else:
                    doubleSpeeded = True
                    if movingR != '':
                        speed = speed * 4
                speeded = True
            if event.key == pygame.K_w:
                avatUp = True
            if event.key == pygame.K_s:
                avatDown = True
            if event.key == pygame.K_d:
                avatRight = True
            if event.key == pygame.K_a:
                avatLeft = True
            if event.key == pygame.K_h:
                if hitbox == True:
                    hitbox = False
                else:
                    hitbox = True
            if event.key == pygame.K_q:
                if healthPackCount > 0:
                    if playerHealth != playerHealthMax:
                        playerHealth = playerHealthMax
                        healthPackCount = healthPackCount - 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                if (speeded == True) and (doubleSpeeded == False):
                    speed = speed / 4
                    speeded = False
                if doubleSpeeded == True:
                    doubleSpeeded = False
                    if movingR != '':
                        speed = speed / 4
            if event.key == pygame.K_w:
                avatUp = False
            if event.key == pygame.K_s:
                avatDown = False
            if event.key == pygame.K_d:
                avatRight = False
            if event.key == pygame.K_a:
                avatLeft = False
            if event.key == pygame.K_f:
                if forceFieldUnlock == True:
                    forceField = True
                    forceFieldUnlock = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 706 < mx < 746 and 4 < my < 44:
                pause = True
            elif 654 < mx < 700 and 4 < my < 44:
                charChange = True
            else:
                shooting = True
                theMouseButtonIsDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            if pause == False:
                theMouseButtonIsDown = False
                mx, my = pygame.mouse.get_pos()
                if startup == False:
                    shooting = False
                    arrow = True
                    arrowFire = True
                    punch = True
                startup = False
    
    if theMouseButtonIsDown == True:
        shooterTimer = shooterTimer + 1

    if pause == False:
        img = pygame.image.load('pause.png')
        gameDisplay.blit(img, (706, 4))

    if projectileIconIMG != '':
        if avatar != "The Flash":
            img = pygame.image.load(projectileIcon)
            gameDisplay.blit(img, (200,4))
        else:
            projectileIcon = "forceFeildIcon2.png"
            if forceFieldUnlock == True:
                projectileIcon = "forceFeildIcon.png"
            img = pygame.image.load(projectileIcon)
            gameDisplay.blit(img, (200,4))
    
    if charSelector == False:
        img = pygame.image.load('characterSelector.png')
        gameDisplay.blit(img, (654, 4))
    
    if healthPackCount > 0:
        img = pygame.image.load('healthGrabIcon.png')
        gameDisplay.blit(img, (266, 4))
        if healthPackCount > 1:
            img = pygame.image.load('itemCount.png')
            gameDisplay.blit(img, (306, 4))
            textBoxClearLemonMilk(str(healthPackCount), 10, (312, 10), (0,0,0))


    score = score + 0.1
    if maxHealth == False:
        textBoxClearR("Score: " + str(int(score)), 30, (730, 727), (0,0,0))
    else:
        textBoxClearR("ENDLESS MODE", 30, (730, 727), (0,255,0))
    

    pygame.display.update()

#Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()