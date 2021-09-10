import pygame
from sys import exit
import os

import physics_engan

FPS = 100
WIDTH, HIEGHT = 900, 500
pygame.display.init()
Win = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("code for yet unnamed game")

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_screen():
    

    pygame.display.update()

def main():

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                exit()

        



if __name__ == "__main__":
    main()