import os
from sys import exit
import pygame

from charecter import Players


FPS = 27
WIDTH, HIEGHT = 800, 800
pygame.init()
pygame.display.init()
Win = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("It just works")


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


walkRight = [pygame.image.load(os.path.join('images', 'R1.png')), pygame.image.load(os.path.join('images','R2.png')), pygame.image.load(os.path.join('images','R3.png')), pygame.image.load(os.path.join('images','R4.png')), pygame.image.load(os.path.join('images','R5.png')), pygame.image.load(os.path.join('images','R6.png')), pygame.image.load(os.path.join('images','R7.png')), pygame.image.load(os.path.join('images','R8.png')), pygame.image.load(os.path.join('images','R9.png'))]
walkLeft = [pygame.image.load(os.path.join('images','L1.png')), pygame.image.load(os.path.join('images','L2.png')), pygame.image.load(os.path.join('images','L3.png')), pygame.image.load(os.path.join('images','L4.png')), pygame.image.load(os.path.join('images','L5.png')), pygame.image.load(os.path.join('images','L6.png')), pygame.image.load(os.path.join('images','L7.png')), pygame.image.load(os.path.join('images','L8.png')), pygame.image.load(os.path.join('images','L9.png'))]
bg = pygame.image.load(os.path.join('images','bg.jpg'))
char = pygame.image.load(os.path.join('images','standing.png'))





def redrawGameWindow():
    Win.blit(bg, (0,0))
    man.draw(Win)
    
    pygame.display.update()


#mainloop
clock = pygame.time.Clock()
man = Players(200, 410, 64,64)
run = True
while run:
    clock.tick(FPS)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
