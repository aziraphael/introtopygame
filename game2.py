#!python3

#main file for basic pygame intro game
import pygame
from pygame import *
import sys
import random

#globals
pygame.init()
screeninfo = pygame.display.Info()
screenSize = (screeninfo.current_w,screeninfo.current_h)
width, height = (screeninfo.current_w, screeninfo.current_h)
clock = pygame.time.Clock()
color = (0,0,0)
screen = pygame.display.set_mode(screenSize)
#robot sprite and rect




#actual code stufffffffff
def main():
    

    

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.fill(color)
        pygame.display.flip()


if __name__ == '__main__':
    main()

