'''This file has all the constant variables for the game.'''

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800

# Fonts
TITLE_FONT = pygame.font.SysFont("Arial", 70)
BUTTON_FONT = pygame.font.SysFont("Arial", 50)
GAME_FONT = pygame.font.SysFont("Arial", 70)

# Lines
sidebar_width = 300
vert_line_1, vert_line_2, vert_line_3 = (SCREEN_WIDTH - sidebar_width) // 3, 2 * (SCREEN_WIDTH - sidebar_width) // 3, SCREEN_WIDTH - sidebar_width
horz_midline = SCREEN_HEIGHT // 2

# Coordinate and Size References
button_width, button_height = 260, 64
card_width, card_height = 100, 150
button_centered_x = (SCREEN_WIDTH // 2) - (button_width // 2)
draw_pile_x, draw_pile_y = SCREEN_WIDTH - 175, (SCREEN_HEIGHT // 4) - 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (30, 30, 30)
LIGHTGRAY = (200, 200, 200)
BLUE = (0, 120, 215)
GREEN = (0, 180, 0)
RED = (200, 30, 30)

# Turn Tracker
player_turn = 1