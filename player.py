import pygame

pygame.init()
FPS = 100
WIDTH, HIEGHT = 900, 500
pygame.init()
pygame.display.init()
#Win = pygame.display.set_mode((WIDTH, HIEGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

