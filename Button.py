'''This file has the Button class.'''

import pygame

from drawing_tools import *
from constants import *

class Button:
    
    text: str
    font: pygame.font

    x_coord: int
    y_coord: int
    width: int
    height: int

    color: tuple
    hover_color: tuple
    border_color: tuple
    
    def __init__(self, x, y, width, height, text, color=RED, hover_color=GREEN, border_color=WHITE):
        self.text = text
        self.font = TEXT_FONT

        self.x_coord = x
        self.y_coord = y
        self.width = width
        self.height = height

        self.color = color
        self.hover_color = hover_color
        self.border_color = border_color

        self.rect = pygame.Rect(self.x_coord, self.y_coord, self.width, self.height)
    
    # def draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color = WHITE):
    def draw_button(self, mouse_pos, surface=screen):
        hovered = self.rect.collidepoint(mouse_pos)  
        color = self.hover_color if hovered else self.color
    
        pygame.draw.rect(surface, color, self.rect) 
        pygame.draw.rect(surface, self.border_color, self.rect, 2)  # Determines border thickness
    
        draw_text(self.text, self.font, BLACK, surface, self.rect.centerx, self.rect.centery) # Adds text to the function
