import pygame
from pygame.locals import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])

        BLACK = (0, 0, 0)
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
