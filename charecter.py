import pygame
import os

pygame.init()
WIDTH, HIEGHT = 900, 500
pygame.display.init()
win = pygame.display.set_mode((WIDTH, HIEGHT))

walkRight = [pygame.image.load(os.path.join('images', 'R1.png')), pygame.image.load(os.path.join('images','R2.png')), pygame.image.load(os.path.join('images','R3.png')), pygame.image.load(os.path.join('images','R4.png')), pygame.image.load(os.path.join('images','R5.png')), pygame.image.load(os.path.join('images','R6.png')), pygame.image.load(os.path.join('images','R7.png')), pygame.image.load(os.path.join('images','R8.png')), pygame.image.load(os.path.join('images','R9.png'))]
walkLeft = [pygame.image.load(os.path.join('images','L1.png')), pygame.image.load(os.path.join('images','L2.png')), pygame.image.load(os.path.join('images','L3.png')), pygame.image.load(os.path.join('images','L4.png')), pygame.image.load(os.path.join('images','L5.png')), pygame.image.load(os.path.join('images','L6.png')), pygame.image.load(os.path.join('images','L7.png')), pygame.image.load(os.path.join('images','L8.png')), pygame.image.load(os.path.join('images','L9.png'))]
bg = pygame.image.load(os.path.join('images','bg.jpg'))
char = pygame.image.load(os.path.join('images','standing.png'))


class Players(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)