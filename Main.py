
# To do:

'''
    - Fix wall collision
    - Add scoreboard
    - Add game over screen
    - Add restart button (make entire thing loop)
    - Add highscore scoreboard
'''

import os
import sys
import time
import pygame
from pygame.locals import *
import Segment
import Food
import Wall

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
wallsprite = pygame.sprite.Group()

snake_segment = []

isfood = True
food = None

walllist = [None] * 4

walltop = None
wallleft = None
wallright = None
wallbot = None

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
    spritelist.add(snake_segment[-1]) # Creates new forward most sprite

def update():
    screen.fill(BLACK)
    wallsprite.draw(screen)
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

def segmentInit():
    global snake_segment
    snake_segment.append(Segment.Segment(WHITE, segment_width, segment_height, 36 * 7, 36 * 3))
    spritelist.add(snake_segment[0])

def wallsCreate():
    global wallsprite
    global walltop
    global wallleft
    global wallright
    global wallbot

    walltop = Wall.Wall(screen_width, 4, 0, -4)
    wallleft = Wall.Wall(4, screen_height, -4, 0)
    wallright = Wall.Wall(4, screen_height, screen_width, 0)
    wallbot = Wall.Wall(screen_width, 4, 0, screen_height)

    wallsprite.add(walltop)
    wallsprite.add(wallleft)
    wallsprite.add(wallright)
    wallsprite.add(wallbot)

    walllist[0] = walltop
    walllist[1] = wallleft
    walllist[2] = wallright
    walllist[3] = wallbot

# Create screen

screen_width = segment_width * 15 + segment_pad * 14
screen_height = segment_height * 15 + segment_pad * 14
screen = pygame.display.set_mode([screen_width, screen_height])

# Create walls

wallsCreate()

# Initial segment creation

segmentInit()

done = False

while not done:

    time.sleep(.2) # Refresh speed

    # Event handler

    for event in pygame.event.get():

        # Movement events

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if changex != segment_width + segment_pad or len(snake_segment) == 1:
                    changex = -1 * (segment_width + segment_pad)
                    changey = 0
            elif event.key == pygame.K_RIGHT:
                if changex != -1 * (segment_width + segment_pad) or len(snake_segment) == 1:
                    changex = segment_width + segment_pad
                    changey = 0
            elif event.key == pygame.K_UP:
                if changey != segment_height + segment_pad or len(snake_segment) == 1:
                    changex = 0
                    changey = -1 * (segment_height + segment_pad)
            elif event.key == pygame.K_DOWN:
                if changey != -1 * (segment_height + segment_pad) or len(snake_segment) == 1:
                    changex =0
                    changey = segment_height + segment_pad

    # Self collision

    if len(snake_segment) > 1:
        for i in range(0, len(snake_segment) - 1):
            if pygame.sprite.collide_rect(snake_segment[-1], snake_segment[i]):
                done = True

    '''

    # Wall collision

    for i in range(0, 4):
        print(i)
        if pygame.sprite.collide_rect(snake_segment[-1], walllist[i]):
                 done = True

    '''

    # Things that happen when you don't lose

    if done == False:

        # Food

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

    else:
        print('GAME OVER')
        print('Score: ', len(snake_segment) - 1)

# Game Over Screen


