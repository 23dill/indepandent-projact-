import pygame
import random
WIDTH, HIEGHT = 852, 480

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH + 20, WIDTH + 100),
                random.randint(0, HIEGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()