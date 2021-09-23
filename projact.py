#import os
from sys import exit

import pygame
import player as p

import physics_engan

FPS = 100
WIDTH, HIEGHT = 900, 500
pygame.init()
pygame.display.init()
Win = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("code for yet unnamed game")


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_screen():
    player = p.Player()

    Win.fill(BLACK)

    Win.blit(player.surf, (WIDTH/2, HIEGHT/2))
    

    pygame.display.update()

def main():
    
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                exit()

        

        draw_screen()


if __name__ == "__main__":
    main()
