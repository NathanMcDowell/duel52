import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Game Draft")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (30, 30, 30)
LIGHTGRAY = (200, 200, 200)
BLUE = (0, 120, 215)
GREEN = (0, 180, 0)
RED = (200, 30, 30)


TITLE_FONT = pygame.font.SysFont("Arial", 70)
BUTTON_FONT = pygame.font.SysFont("Arial", 50)
# GAME_FONT = pygame.font.SysFont("Arial", 70)

MENU = "menu"
GAME = "game"
OPTIONS = "options"
current_state = MENU

def draw_text(text, font, color, surface, x, y, center = True):
    """When I need to draw text, this is the function that I will use to do so.
    -Text is what will be written.
    -Font is the font that it will be written in. I have made two font constants to be used up above.
    -Color is the color that the text will be. I also have constants for colors above.
    -Surface is the surface on which the text will be placed, which is the screen constant.
    -x and y are the coordinates for the text.
    -center = True means that the text will be centered on the x and y instead of that being the upper-left coordinate."""

def draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color = WHITE):
    """This makes buttons where I need them.
    -surface is the surface on which everything is placed, the screen.
    -rect is the predefined details for the button's shape and size.
    -text is the text on the button, which will be put into a draw text function within this one.
    -font is the font of above text, as determined by the above written font variables.
    -base_color"""

def draw_menu():
    ""

def draw_options():
    ""