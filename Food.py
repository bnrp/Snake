import pygame
from pygame.locals import *
import random

x = None
y = None

class Food(pygame.sprite.Sprite):

    def __init__(self, color, snake_segment):
        super().__init__()

        def ranCoords():
            global x
            global y

            x = 36 * random.randint(0, 14)
            y = 36 * random.randint(0, 14)

        def getx(snake_segment):
            return snake_segment.rect.x

        def gety(snake_segment):
            return snake_segment.rect.y

        height = 33
        width = 33

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        ranCoords()

        for i in range(0, len(snake_segment)):
            if x == getx(snake_segment[i]) or y == gety(snake_segment[i]):
                ranCoords()
                i = 0

        self.rect.x = x
        self.rect.y = y
