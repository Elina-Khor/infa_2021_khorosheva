# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:28:52 2021

@author: elina
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen_size = [400, 400]

screen = pygame.display.set_mode((screen_size))

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 203, 200)
RED =   (255, 0, 0)
YELLOW = (255, 255, 0)

# Clear the screen and set the screen background
screen.fill(LIGHT_GRAY)

# Width of lines of figureson the screen
line_width = 1


def draw_face():
    """
    Draw face in center of screen.
    
    Returns
    -------
    None.
    
    """
    ellipse_size = [screen_size[0] / 4,
                    screen_size[1] / 4,
                    screen_size[0] / 2,
                    screen_size[1] / 2,
                    ]
    ellipse(screen, YELLOW, ellipse_size)
    ellipse(screen, BLACK, ellipse_size, line_width)


def draw_eye(x: int, y: int, height: int, width: int):
    """
    Draw an eye at the rectangle what begin in point with coordinates x, y
    and have height and width matching parameters height and width.
    
    Returns
    -------
    None.
    
    """
    
    pass


def draw_angry_face():
    """
    Draw angry face in center of screen, return None
    """
    draw_face()
    draw_eye()
    draw_eye()


draw_angry_face()

# Loop until the user clicks the close button.
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()