'''This file has the Button class.'''

import pygame

from drawing_tools import *
from constants import *

class Button:
    
    text: str
    x_coord: int
    y_coord: int
    width: int
    height: int
    color: tuple
    border_color: tuple
    
    def __init__(self, x, y, width, height, text):
        self.x_coord = x
        self.y_coord = y
        self.width = width
        self.height = height

        self.text = text

        self.rect = pygame.Rect(self.x_coord, self.y_coord, self.width, self.height)
    
    def draw_button(self, mouse_pos):
        draw_button(screen, self.rect, self.text, TEXT_FONT, RED, GREEN, mouse_pos)
