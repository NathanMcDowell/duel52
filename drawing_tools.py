import pygame
import sys
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (30, 30, 30)
LIGHTGRAY = (200, 200, 200)
BLUE = (0, 120, 215)
GREEN = (0, 180, 0)
RED = (200, 30, 30)


def draw_text(text, font, color, surface, x, y, center = True):
    """When I need to draw text, this is the function that I will use to do so.
    -Text is what will be written.
    -Font is the font that it will be written in. I have made two font constants to be used up above.
    -Color is the color that the text will be. I also have constants for colors above.
    -Surface is the surface on which the text will be placed, which is the screen constant.
    -x and y are the coordinates for the text.
    -center = True means that the text will be centered on the x and y instead of that being the upper-left coordinate."""
    text_surf = font.render(text, True, color)
    if center:
        text_rect = text_surf.get_rect(center=(x, y))
    else:
        text_rect = text_surf.get_rect(topleft=(x, y))
    surface.blit(text_surf, text_rect)
    return text_rect

def draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color = WHITE):
    """This makes buttons where I need them.
    -surface is the surface on which everything is placed, the screen.
    -rect is the predefined details for the button's shape and size.
    -text is the text on the button, which will be put into a draw text function within this one.
    -font is the font of above text, as determined by the above written font variables.
    -base_color is the color that the rectangle will be unless it is hovered over. Use constant colors.
    -hover_color is the color that the rectangle will be when hovered over. Use constant colors.
    -mouse_pos in this case is used to determine if the mouse is over the button. It will take from a function that determines mouse position.
    -border_color is the color of the border that the button has. It will be white unless otherwise specified."""
    
    hovered = rect.collidepoint(mouse_pos)  
    color = hover_color if hovered else base_color
    
    pygame.draw.rect(surface, color, rect) 
    pygame.draw.rect(surface, border_color, rect, 2)  # Determines border thickness
    
    draw_text(text, font, BLACK, surface, rect.centerx, rect.centery) # Adds text to the function

    return hovered

def draw_card(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color):
    """This makes buttons where I need them.
    -surface is the surface on which everything is placed, the screen.
    -rect is the predefined details for the button's shape and size.
    -text is the text on the button, which will be put into a draw text function within this one.
    -font is the font of above text, as determined by the above written font variables.
    -base_color is the color that the rectangle will be unless it is hovered over. Use constant colors.
    -hover_color is the color that the rectangle will be when hovered over. Use constant colors.
    -mouse_pos in this case is used to determine if the mouse is over the button. It will take from a function that determines mouse position.
    -border_color is the color of the border that the button has. It will be white unless otherwise specified."""
    
    hovered = rect.collidepoint(mouse_pos)  
    color = hover_color if hovered else base_color
    
    pygame.draw.rect(surface, color, rect) 
    pygame.draw.rect(surface, border_color, rect, 2)  # Determines border thickness
    
    draw_text(text, font, RED, surface, rect.centerx, rect.centery) # Adds text to the function

    return hovered

def draw_line(surface, color, start_pos, end_pos, width=5):
    pygame.draw.line(surface, color, start_pos, end_pos, width)
