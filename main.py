#Snake Game
import math
from os import supports_fd
import random
import pygame
import tkinter as tk
from tkinter import messagebox

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(RED)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        
    def move(self, dirnx, dirny):
        self.dirnx  = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)    #updates the position of the snake ex. (10,4)
    
    def draw(self, surface, eyes=False):
        dis = self.w//self.rows
        i = self.pos[0] #row
        j = self.pos[1] #column

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2)) #rect x, rect y, x, y

        if eyes: # Draws the eyes
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if user hit the X button
                pygame.quit()

            keys = pygame.key.get_pressed()  # See which keys are being pressed

            for key in keys:  # Loop through all the keys
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):  # Loop through every cube in body
            p = c.pos[:]  # cubes position in the grid
            if p in self.turns:  # If the cube's current position is one where we turned
                turn = self.turns[p]  # Get the direction we should turn
                c.move(turn[0],turn[1])  # Move our cube in that direction
                if i == len(self.body)-1:  # if the cube is the last cube
                    self.turns.pop(p)
            else:  # If we are not turning the cube
                # If the cube reaches the edge of the screen
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)  # if the edge is not reached

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i==0:    #draw an eye if it is the head
                c.draw(surface, True)
            else:
                c.draw(surface)

def drawGrid(w, rows, surface):
    sizeBtwn = w//rows  #for equally sized cells

    x = 0
    y = 0
    for l in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, WHITE, (x,0), (x,w))  #horizontal line (x stays the same) 0 to w
        pygame.draw.line(surface, WHITE, (0,y), (w,y))  #vertical line (y stays the same) 0 to w

def redrawWindow(surface):
    global rows, width, s
    surface.fill(BLACK)
    s.draw(surface)     #draws the snake in the surface
    drawGrid(width, rows, surface)
    pygame.display.update() #updates the display

def randomSnack(rows, items):
    pass

def main():
    global rows, width, s
    width = 500
    height = 500
    rows = 20
    FPS = 10
    win = pygame.display.set_mode((width, height))
    s = snake(RED, (10,10))

    clock = pygame.time.Clock()
    flag = True
    while flag:
        pygame.time.delay(50) #lower = faster
        clock.tick(FPS)  #for the program to run 10 FPS; lower = slower
        s.move()
        redrawWindow(win)      #refreshes the screen
    pass

main()


