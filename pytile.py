#Initialization
import os
import pygame
import math
import random
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
avatX = 10
avatY = 10

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

speed = 4
while end == False:
    clock.tick(60)
    gameDisplay.fill((0,0,0))

    if avatX > 749:
        avatX = -19
    if avatX < -19:
        avatX = 749

    if avatY < -19:
        avatY = 749
    if avatY > 749:
        avatY = -19

    pygame.draw.rect(gameDisplay, (0,255,255), (avatX, avatY, 20, 20))
    pygame.draw.rect(gameDisplay, (0,0,155), (enemyX, enemyY, 20, 20))

    if avatUp == True:
        avatY = avatY - speed
    elif avatDown == True:
        avatY = avatY + speed
    elif avatRight == True:
        avatX = avatX + speed
    elif avatLeft == True:
        avatX = avatX - speed
    
    
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
            if event.key == pygame.K_UP:
                avatUpIn = True
                avatDown = False
                avatRight = False
                avatLeft = False
                avatUp = True
            if event.key == pygame.K_DOWN:
                avatDownIn = True
                avatUp = False
                avatRight = False
                avatLeft = False
                avatDown = True
            if event.key == pygame.K_RIGHT:
                avatRightIn = True
                avatDown = False
                avatUp = False
                avatLeft = False
                avatRight = True
            if event.key == pygame.K_LEFT:
                avatLeftIn = True
                avatDown = False
                avatUp = False
                avatRight = False
                avatLeft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                avatUpIn = False
                avatUp = False
                if avatLeftIn == True:
                    avatLeft = True
                if avatRightIn == True:
                    avatRight = True
                if avatDownIn == True:
                    avatDown = True
                if avatUpIn == True:
                    avatUp = True
            if event.key == pygame.K_DOWN:
                avatDownIn = False
                avatDown = False
                if avatLeftIn == True:
                    avatLeft = True
                if avatRightIn == True:
                    avatRight = True
                if avatDownIn == True:
                    avatDown = True
                if avatUpIn == True:
                    avatUp = True
            if event.key == pygame.K_RIGHT:
                avatRightIn = False
                avatRight = False
                if avatLeftIn == True:
                    avatLeft = True
                if avatRightIn == True:
                    avatRight = True
                if avatDownIn == True:
                    avatDown = True
                if avatUpIn == True:
                    avatUp = True
            if event.key == pygame.K_LEFT:
                avatLeftIn = False
                avatLeft = False
                if avatLeftIn == True:
                    avatLeft = True
                if avatRightIn == True:
                    avatRight = True
                if avatDownIn == True:
                    avatDown = True
                if avatUpIn == True:
                    avatUp = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 250 < mx < 350:
                if 250 < my < 350:
                    end = True
                    print(end)
    pygame.display.update()

#Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()