"""This file makes all the game assets, including rectangles, the card class, and the screens"""

import pygame
import random

from drawing_tools import *
from Card import *
from Button import *
from constants import *

# Initialization stuff
pygame.init()
pygame.display.set_caption("Game Draft")


# pygame.Rect(x coordinate, y coordinate, width, height)
# Menu Rectangles
start_button = Button(button_centered_x, 100, button_width, button_height, "Start")
controls_button = Button(button_centered_x, 200, button_width, button_height, "Controls")
options_button = Button(button_centered_x, 300, button_width, button_height, "Options")
quit_button = Button(button_centered_x, 400, button_width, button_height, "Quit")

# Controls Rectangles
to_card_abilities_button = Button(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT - 100, 50, button_height, ">")
to_controls_button = Button(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 100, 50, button_height, "<")

# Options Rectangles
color_red_button = Button(25, 150, button_width - 50, button_height, "Red")
color_blue_button = Button(275, 150, button_width - 50, button_height, "Blue")
color_green_button = Button(525, 150, button_width - 50, button_height, "Green")

# Start Up Rectangles
back_button = Button(40, SCREEN_HEIGHT - 100, button_width + 60, button_height, "Back to Menu")
begin_button = Button(500, SCREEN_HEIGHT - 100, button_width, button_height, "Start Game")

# Game Rectangles
turn_button = Button(SCREEN_WIDTH - 255, SCREEN_HEIGHT - 525, 110, button_height, "Turn")
concede_button = Button(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 325, 100, button_height, "Quit")
p1_indicator_button = Button(SCREEN_WIDTH - 255, SCREEN_HEIGHT - 580, 30, 30, "")
p2_indicator_button = Button(SCREEN_WIDTH - 255, SCREEN_HEIGHT - 445, 30, 30, "")

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

    start_button.draw_button(mouse_pos)
    controls_button.draw_button(mouse_pos)
    options_button.draw_button(mouse_pos)
    quit_button.draw_button(mouse_pos)
    

def draw_game_startup(surface, mouse_pos):
    """Makes the start up screen before the game begins.
    This screen will have a couple of options for beginning the game.
    - Name each player.
    - Choose if one player will go first or if they want it randomly determined."""
    surface.fill(DARKGRAY)
    draw_text("Set Up", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, 40)
    back_button.draw_button(mouse_pos)
    begin_button.draw_button(mouse_pos)

def draw_controls(surface, mouse_pos):
    """Makes the controls screen"""
    surface.fill(DARKGRAY)
    draw_text("Controls", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, 40)
    draw_text("Left click and drag to move cards", TEXT_FONT, WHITE, screen, 50, 150, center= False)
    draw_text("Right click to flip a card over", TEXT_FONT, WHITE, screen, 50, 250, center= False)
    draw_text("Middle click to damage a card", TEXT_FONT, WHITE, screen, 50, 350, center= False)

    to_card_abilities_button.draw_button(mouse_pos)
    back_button.draw_button(mouse_pos)

ca_button_x = 100
ca_button_y = 200
control_buttons = []
for rank in RANK_LIST:
    if rank == "6" or rank == "J":
        ca_button_y += 125
        ca_button_x = 100
    rank = Button(ca_button_x, ca_button_y, 100, 100, rank)
    control_buttons.append(rank)
    ca_button_x += 125

def draw_card_abilities(surface, mouse_pos):
    surface.fill(DARKGRAY)
    draw_text("Card Abilities", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, 40)
    
    for button in control_buttons:
        button.draw_button(mouse_pos)

    """
    show buttons
    if button pushed
        display information
        and button for back
    if back button pushed
        display all buttons
    """

    to_controls_button.draw_button(mouse_pos)
    

    back_button.draw_button(mouse_pos)

def draw_options(surface, mouse_pos):
    """Makes the controls screen"""
    surface.fill(DARKGRAY)
    
    draw_text("Card Colors:", TITLE_FONT, WHITE, screen, 400, 75)

    color_red_button.draw_button(mouse_pos)
    color_blue_button.draw_button(mouse_pos)
    color_green_button.draw_button(mouse_pos)

    back_button.draw_button(mouse_pos)

def draw_game(surface, mouse_pos, player_turn):
    '''The game'''
    surface.fill(DARKGRAY)
    
    # Buttons
    turn_button.draw_button(mouse_pos)
    concede_button.draw_button(mouse_pos)

    # Current turn indicatior
    if player_turn == 1:
        p1_indicator_button.draw_button(mouse_pos)
    elif player_turn == 2:
        p2_indicator_button.draw_button(mouse_pos)

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
        draw_card(screen, card.rect, card.text, TEXT_FONT, card.color, card.color, mouse_pos, card.border_color)
  