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
avatDown = False
avatUp = False
avatRight = False
avatLeft = False
while end == False:
    clock.tick(60)
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, (255,255,255), (avatX, avatY, 20, 20))

    print(avatUp)    
    if avatUp == True:
        avatY = avatY - 1
    elif avatDown == True:
        avatY = avatY + 1
    elif avatRight == True:
        avatX = avatX + 1
    elif avatLeft == True:
        avatX = avatX - 1
    
    pygame.draw.rect(gameDisplay, (255,255,255), (avatX, avatY, 20, 20))
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
                avatDown = False
                avatRight = False
                avatLeft = False
                avatUp = True
            if event.key == pygame.K_DOWN:
                avatUp = False
                avatRight = False
                avatLeft = False
                avatDown = True
            if event.key == pygame.K_RIGHT:
                avatDown = False
                avatUp = False
                avatLeft = False
                avatRight = True
            if event.key == pygame.K_LEFT:
                avatDown = False
                avatUp = False
                avatRight = False
                avatLeft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                avatUp = False
            if event.key == pygame.K_DOWN:
                avatDown = False
            if event.key == pygame.K_RIGHT:
                avatRight = False
            if event.key == pygame.K_LEFT:
                avatLeft = False
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
