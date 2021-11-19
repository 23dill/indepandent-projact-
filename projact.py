import os
from sys import exit
import pygame

from charecter import Players
from enamey import Enemy


FPS = 27
WIDTH, HIEGHT = 852, 480
pygame.init()
pygame.display.init()
Win = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("It just works")


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


bg = pygame.image.load(os.path.join('images','bg.jpg'))
char = pygame.image.load(os.path.join('images','standing.png'))

Enames = pygame.sprite.Group()
All_Sprites = pygame.sprite.Group()






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
    elif keys[pygame.K_RIGHT] and man.x < WIDTH - man.width - man.vel:
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
