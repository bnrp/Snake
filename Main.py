import os
import sys
import pygame
from pygame.locals import *
import Segment

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

segment_height = 30
segment_width = 30
segment_padding = 3

snake = pygame.sprite.Group()

screen_width = 492
screen_height = 492
screen = pygame.display.set_mode([screen_width, screen_height])

while True:
    spritelist.update()

    spritelist.draw(screen)

    pygame.display.flip()
