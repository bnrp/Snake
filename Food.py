import pygame
from pygame.locals import *
import random

class Food(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()

        height = 33
        width = 33

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        x = 36 * random.randint(0, 14)
        y = 36 * random.randint(0, 14)

        self.rect.x = x
        self.rect.y = y
