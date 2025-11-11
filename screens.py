"""This file makes all the game assets, including rectangles, the card class, and the screens"""

import pygame
import random

from drawing_tools import *
from Card import *
from constants import *

# Initialization stuff
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Draft")


# (x coordinate, y coordinate, width, height)
# Menu Rectangles
start_rect = pygame.Rect(button_centered_x, 100, button_width, button_height)
controls_rect = pygame.Rect(button_centered_x, 200, button_width, button_height)
options_rect = pygame.Rect(button_centered_x, 300, button_width, button_height)
quit_rect = pygame.Rect(button_centered_x, 400, button_width, button_height)

# Options Rectangles
color_cycle_rect = pygame.Rect(button_centered_x, 400, button_width, button_height)

# Start Up Rectangles
back_rect = pygame.Rect(40, SCREEN_HEIGHT - 100, button_width + 60, button_height)
begin_rect = pygame.Rect(500, SCREEN_HEIGHT - 100, button_width, button_height)

# Game Rectangles
turn_rect = pygame.Rect(SCREEN_WIDTH - 255, SCREEN_HEIGHT - 525, 110, button_height)
concede_rect = pygame.Rect(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 325, 100, button_height)

# Cards
deck = []
RANK_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
            # Spades, Diamonds, Clubs, Hearts
SUIT_LIST = ['S', 'D', 'C', 'H']
for suit in SUIT_LIST:
    for rank in RANK_LIST:        
        card = Card(rank, suit, draw_pile_x, draw_pile_y)
        deck.append(card)
random.shuffle(deck)
reversed_deck = list(reversed(deck))

# Lays out starting hands
starting_hand_count = 0
card_spread = SCREEN_WIDTH - sidebar_width + 25

for card in reversed_deck:
    # Player One's hand
    if starting_hand_count == 5:
        card_spread = SCREEN_WIDTH - sidebar_width + 25
    if starting_hand_count < 5:
        card.rect.y = 25
        card.rect.x = card_spread
        starting_hand_count += 1
    # Player Two's hand
    elif starting_hand_count < 10:
        card.rect.y = SCREEN_HEIGHT - card_height - 25
        card.rect.x = card_spread
        starting_hand_count += 1
    
    card_spread += 25

def draw_menu(surface, mouse_pos):
    """Makes the menu title screen."""

    surface.fill(DARKGRAY)

    draw_text("DUEL 52", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, 40)

    draw_button(screen, start_rect, "Start", BUTTON_FONT, RED, GREEN, mouse_pos)
    draw_button(screen, controls_rect, "Controls", BUTTON_FONT, RED, GREEN, mouse_pos)
    draw_button(screen, options_rect, "Options", BUTTON_FONT, RED, GREEN, mouse_pos)
    draw_button(screen, quit_rect, "Quit", BUTTON_FONT, RED, GREEN, mouse_pos)

def draw_game_startup(surface, mouse_pos):
    """Makes the start up screen before the game begins.
    This screen will have a couple of options for beginning the game.
    - Name each player.
    - Choose if one player will go first or if they want it randomly determined."""
    surface.fill(DARKGRAY)
    draw_text("Set Up", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, 40)
    draw_button(screen, back_rect, "Back to Menu", BUTTON_FONT, RED, GREEN, mouse_pos)
    draw_button(screen, begin_rect, "Begin", BUTTON_FONT, RED, GREEN, mouse_pos)

def draw_controls(surface, mouse_pos):
    """Makes the controls screen"""
    surface.fill(DARKGRAY)
    draw_text("Controls", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, 40)
    draw_button(screen, back_rect, "Back to Menu", BUTTON_FONT, RED, GREEN, mouse_pos)

def draw_options(surface, mouse_pos):
    """Makes the controls screen"""
    surface.fill(DARKGRAY)
    
    draw_button(screen, color_cycle_rect, "Color", BUTTON_FONT, RED, GREEN, mouse_pos)
    draw_button(screen, back_rect, "Back to Menu", BUTTON_FONT, RED, GREEN, mouse_pos)

def draw_game(surface, mouse_pos):
    '''The game'''
    surface.fill(DARKGRAY)
    
    # Buttons
    draw_button(screen, turn_rect, "Turn", BUTTON_FONT, RED, GREEN, mouse_pos)
    draw_button(screen, concede_rect, "Quit", BUTTON_FONT, RED, GREEN, mouse_pos)


    # Lane divisions
    draw_line(surface, WHITE, (vert_line_1, 0), (vert_line_1, SCREEN_HEIGHT))
    draw_line(surface, WHITE, (vert_line_2, 0), (vert_line_2, SCREEN_HEIGHT))
    draw_line(surface, WHITE, (vert_line_3, 0), (vert_line_3, SCREEN_HEIGHT))
    # Horizontal lines
    draw_line(surface, WHITE, (vert_line_3, SCREEN_HEIGHT // 4), (SCREEN_WIDTH, SCREEN_HEIGHT // 4))
    draw_line(surface, WHITE, (0, horz_midline), (SCREEN_WIDTH, horz_midline))
    draw_line(surface, WHITE, (vert_line_3, 3 * SCREEN_HEIGHT // 4), (SCREEN_WIDTH, 3 * SCREEN_HEIGHT // 4))

    # Draw Pile
    for card in deck:
        draw_card(screen, card.rect, card.text, BUTTON_FONT, card.color, card.color, mouse_pos, card.border_color)
  