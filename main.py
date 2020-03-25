#! python3
#main file for basic pygame intro game
import pygame
from pygame import *
import sys
import random
from robot import *

#globals
pygame.init()
screeninfo = pygame.display.Info()
screenSize = (screeninfo.current_w,screeninfo.current_h)
width, height = (screeninfo.current_w, screeninfo.current_h)
clock = pygame.time.Clock()
color = (0,127,255)
screen = pygame.display.set_mode(screenSize)
#robot sprite and rect
robots = []



#actual code stufffffffff
def main():
    
    for i in range(10):
        robots.append(Robot((width//2,height//2)))

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.fill(color)
        for robot in robots:
            robot.move_robot()
        for robot in robots:
            robot.draw_robot(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()

