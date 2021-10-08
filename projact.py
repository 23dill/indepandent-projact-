import os
from sys import exit, path

import pygame
from pygame.constants import K_ESCAPE, KEYDOWN

#import player as p

#import physics_engan

FPS = 27
WIDTH, HIEGHT = 500, 500
pygame.init()
pygame.display.init()
Win = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("code for yet unnamed game")


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



width = 64
height = 63

walkRight = [pygame.image.load(os.path.join('images', 'R1.png')), pygame.image.load(os.path.join('images','R2.png')), pygame.image.load(os.path.join('images','R3.png')), pygame.image.load(os.path.join('images','R4.png')), pygame.image.load(os.path.join('images','R5.png')), pygame.image.load(os.path.join('images','R6.png')), pygame.image.load(os.path.join('images','R7.png')), pygame.image.load(os.path.join('images','R8.png')), pygame.image.load(os.path.join('images','R9.png'))]
walkLeft = [pygame.image.load(os.path.join('images','L1.png')), pygame.image.load(os.path.join('images','L2.png')), pygame.image.load(os.path.join('images','L3.png')), pygame.image.load(os.path.join('images','L4.png')), pygame.image.load(os.path.join('images','L5.png')), pygame.image.load(os.path.join('images','L6.png')), pygame.image.load(os.path.join('images','L7.png')), pygame.image.load(os.path.join('images','L8.png')), pygame.image.load(os.path.join('images','L9.png'))]
bg = pygame.image.load(os.path.join('images','bg.jpg'))
char = pygame.image.load(os.path.join('images','standing.png'))

walkCount = 0

x = 50
y = 425
vel = 5




def redrawGameWindow():
    global walkCount
    left = False
    right = False

    Win.blit(bg, (0,0))  # This will draw our background image at (0,0)

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  # If we are facing left
        Win.blit(walkLeft[walkCount//3], (x,y))  # We integer divide walkCounr by 3 to ensure each
        walkCount += 1                           # image is shown 3 times every animation
    elif right:
        Win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        Win.blit(char, (x, y))  # If the character is standing still
        walkCount = 0

    pygame.display.update() 


    
run = True
clock = pygame.time.Clock()
vel = 5
jumpCount = 10
isJump = False
left = False
right = False
while run:
        clock.tick(FPS)
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                run = False
                exit()
                    

        

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
        

        if keys[pygame.K_LEFT] and x > vel: 
            x -= vel
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
            x += vel
            left = False
            right = True
        
        else: # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
            left = False
            right = False
            walkCount = 0


        if not(isJump): # Checks is user is not jumping

            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: # This will execute if our jump is finished
                jumpCount = 10
                isJump = False
                # Resetting our Variables

        redrawGameWindow() 
