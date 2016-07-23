import os
import sys
import pygame
from pygame.locals import *
import Segment
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

segment_height = 33
segment_width = 33
segment_pad = 3

changey = 0
changex = 0

spritelist = pygame.sprite.Group()

# Use this as reference

"""
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_pad) * i
    y = 30
    segment = Segment.Segment(WHITE, segment_width, segment_height, x, y)
    snake_segments.append(segment)
    spritelist.add(segment)

use .pop to get rid of final array entry, then use .pop to remove from spritelist

once back is removed, simultaneously add a new segment in the direction of motion <- or add a a new segment to the end of the array

"""

def getx(Segment):
    return Segment.rect.x

def gety(Segment):
    return Segment.rect.y

# Initial segment

snake_segment = []
snake_segment.append(Segment.Segment(WHITE, segment_width, segment_height, 36 * 7, 36 * 3))
spritelist.add(snake_segment[0])

screen_width = 537
screen_height = 537
screen = pygame.display.set_mode([screen_width, screen_height])

clock = pygame.time.Clock()
done = False

while not done:

    time.sleep(.2)

    # Event handler

    for event in pygame.event.get():

        # Movement events

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left`')
                changex = -1 * (segment_height + segment_pad)
                changey = 0
            elif event.key == pygame.K_RIGHT:
                print('right')
                changex = segment_height + segment_pad
                changey = 0
            elif event.key == pygame.K_UP:
                print('up')
                changex = 0
                changey = -1 * (segment_height + segment_pad)
            elif event.key == pygame.K_DOWN:
                print('down')
                changex =0
                changey = 1 * (segment_height + segment_pad)

    # Movement

    sslength = len(snake_segment) - 1 # Gets length of list
    tempx = getx(snake_segment[sslength]) # Gets x location of forward most segment
    tempy = gety(snake_segment[sslength]) # Gets y location of forward most segment
    spritelist.remove(snake_segment.pop(0)) # Removes backward most sprite and list index
    snake_segment.append(Segment.Segment(WHITE, segment_width, segment_height, tempx + changex, tempy + changey)) # Creates new forward most index
    spritelist.add(snake_segment[-1]) # Creates new forward most sprite

    # Update the window

    screen.fill(BLACK)

    spritelist.draw(screen)

    pygame.display.flip()
