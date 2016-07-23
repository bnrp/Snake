import os
import sys
import pygame
from pygame.locals import *

class Segment(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
