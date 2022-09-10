#Snake Game
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

BLACK = (0,0,0)
WHITE = (255,255,255)

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
        
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass
    
    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

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
    global rows, width
    surface.fill(BLACK)
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
    s = snake((255,0,0), (10,10))

    clock = pygame.time.Clock()
    flag = True
    while flag:
        pygame.time.delay(50) #lower = faster
        clock.tick(FPS)  #for the program to run 10 FPS; lower = slower
        redrawWindow(win)      #refreshes the screen
    pass

main()


