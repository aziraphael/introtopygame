#! python3
#main file for basic pygame intro game
import pygame
from pygame import *
import sys

#globals
pygame.init()
screeninfo = pygame.display.Info()
screenSize = (screeninfo.current_w,screeninfo.current_h)
clock = pygame.time.Clock()
color = (0,127,255)
screen = pygame.display.set_mode(screenSize)
#robot sprite and rect

robot = pygame.image.load('sprite.png')
robo_rect = robot.get_rect()

#actual code stufffffffff



def main():
    global screeninfo
    global screenSize
    global clock
    global color


    
    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)
        screen.blit(robot,robo_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()

