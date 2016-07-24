import os
import sys
import pygame
from pygame.locals import *
import Segment
import Food
import time

pygame.init()

# Variables

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

segment_height = 33
segment_width = 33
segment_pad = 3

changey = 0
changex = 0

spritelist = pygame.sprite.Group()
foodsprite = pygame.sprite.Group()

isfood = True
food = None

addTurn = False

# Functions

def getx(Segment):
    return Segment.rect.x

def gety(Segment):
    return Segment.rect.y

def move():
    sslength = len(snake_segment) - 1 # Gets length of list
    tempx = getx(snake_segment[sslength]) # Gets x location of forward most segment
    tempy = gety(snake_segment[sslength]) # Gets Y location of forward most segment
    spritelist.remove(snake_segment.pop(0)) # Removes backward most sprite and list index
    snake_segment.append(Segment.Segment(WHITE, segment_width, segment_height, tempx + changex, tempy + changey)) # Creates new forward most index
    spritelist.add(snake_segment[-1]) # Creates new forward mos sprite

def update():
    screen.fill(BLACK)
    foodsprite.draw(screen)
    spritelist.draw(screen)
    pygame.display.flip()

def createFood():
    global food
    food = Food.Food(RED)
    foodsprite.add(food)
    global isfood
    isfood = False

def removeFood():
    global food
    foodsprite.remove(food)
    food = None
    global isfood
    isfood = True

def addSegment():
    global spritelist
    global snake_segment
    global addTurn
    addTurn = True
    newsegment = Segment.Segment(WHITE, segment_width, segment_height, getx(snake_segment[-1]) + changex, gety(snake_segment[-1]) + changey)
    snake_segment.append(newsegment)
    spritelist.add(newsegment)

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

    time.sleep(.2) # Refresh speed

    # Event handler

    for event in pygame.event.get():

        # Movement events

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex = -1 * (segment_height + segment_pad)
                changey = 0
            elif event.key == pygame.K_RIGHT:
                changex = segment_height + segment_pad
                changey = 0
            elif event.key == pygame.K_UP:
                changex = 0
                changey = -1 * (segment_height + segment_pad)
            elif event.key == pygame.K_DOWN:
                changex =0
                changey = 1 * (segment_height + segment_pad)

    if isfood == True:
        createFood()

    if pygame.sprite.collide_rect(snake_segment[-1], food):
        removeFood()
        addSegment()

    # Movement
    if addTurn == False:
        move()
    elif addTurn == True:
        addTurn = False

    # Update the window

    update()

# Game Over Screen
