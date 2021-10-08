import pygame
#from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

pygame.init()
FPS = 100
WIDTH, HIEGHT = 900, 500
pygame.display.init()
Win = pygame.display.set_mode((WIDTH, HIEGHT))


class Player(object):
    def __init__(self):
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        
        

    def update(self, keys):
       pass