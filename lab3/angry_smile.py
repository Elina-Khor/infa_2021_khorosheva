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


def draw_face(*face_size):
    """
    Draw face in center of screen.
    
    Returns
    -------
    None.
    
    """
    ellipse(screen, YELLOW, face_size)
    ellipse(screen, BLACK, face_size, line_width)


def draw_eye(*eye_size):
    """
    Draw an eye at the rectangle what begin in point with coordinates x, y
    and have height and width matching parameters height and width.
    
    Returns
    -------
    None.
    
    """
    ellipse(screen, RED, eye_size)
    ellipse(screen, BLACK, eye_size, line_width)


def draw_angry_face():
    """
    Draw angry face in center of screen, return None
    """
    min_size = min(screen_size)
    right_eye_diam = min_size * 5 // 64
    left_eye_diam = min_size * 3 // 32 + 2
    max_diam = max(right_eye_diam, left_eye_diam)
    eye_center = min_size // 16
    
    face = [min_size // 4,
            min_size // 4,
            min_size // 2,
            min_size // 2,
            ]
    left = [face[0] + eye_center,
            2 * face[1] - max_diam,
            left_eye_diam,
            left_eye_diam,
            ]
    right = [3 * face[0] - max_diam - eye_center,
             2 * face[1] - max_diam,
             right_eye_diam,
             right_eye_diam,
             ]
    
    draw_face(face)
    draw_eye(left)
    draw_eye(right)


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