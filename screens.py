"""This file makes all the game assets, including rectangles, the card class, and the screens"""

import pygame
import random
from drawing_tools import *

#Initialization stuff
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Draft")

# Lines
sidebar_width = 300
vert_line_1, vert_line_2, vert_line_3 = (SCREEN_WIDTH - sidebar_width) // 3, 2 * (SCREEN_WIDTH - sidebar_width) // 3, SCREEN_WIDTH - sidebar_width

# Coordinate References
button_width, button_height = 260, 64
card_width, card_height = 100, 150

centered_width = (SCREEN_WIDTH // 2) - (button_width // 2)
card_centered_height = (SCREEN_HEIGHT // 2) - (card_height // 2)
draw_pile_x, draw_pile_y = SCREEN_WIDTH - 175, (SCREEN_HEIGHT // 4) - 50
card_two_thirds_height = (2 * SCREEN_HEIGHT // 3) - (card_height // 2)

# (x coordinate, y coordinate, width, height)
# Menu Rectangles
start_rect = pygame.Rect(centered_width, 100, button_width, button_height)
controls_rect = pygame.Rect(centered_width, 200, button_width, button_height)
options_rect = pygame.Rect(centered_width, 300, button_width, button_height)
quit_rect = pygame.Rect(centered_width, 400, button_width, button_height)
# Start Up Rectangles
back_rect = pygame.Rect(40, SCREEN_HEIGHT - 100, button_width + 60, button_height)
begin_rect = pygame.Rect(500, SCREEN_HEIGHT - 100, button_width, button_height)

class Card:
    suit: str
    rank: str
    flipped: bool
    health: int
    player: int
    lane: int
    x_coord: int
    y_coord: int
    text: str

    def __init__(self, rank, suit, x, y):
        self.suit = suit
        self.rank = rank
        self.flipped = False
        if rank == "J":
            self.health = 3
            self.text = "J*"
        else:
            self.health = 2
            self.text = self.rank
        self.player = 0
        self.lane = 0
        self.x_coord = x + (card_width // 2)
        self.y_coord = y + (card_height // 2)

        self.rect = pygame.Rect(self.x_coord, self.y_coord, card_width, card_height)

        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

        self.color = RED
        self.border_color = BLACK

    def __repr__(self):
        return f"{self.rank} of {self.suit} with {self.health} health, flipped: {self.flipped}"
    
    def start_drag(self, mouse_pos):
        """Call this when mouse clicks the card"""
        self.dragging = True
        self.offset_x = mouse_pos[0] - self.rect.x
        self.offset_y = mouse_pos[1] - self.rect.y
    
    def stop_drag(self):
        """Call this when mouse button is released"""
        self.dragging = False

    def update_drag(self, mouse_pos):
        """Call this every frame while dragging"""
        if self.dragging:
            self.rect.x = mouse_pos[0] - self.offset_x
            self.rect.y = mouse_pos[1] - self.offset_y

    def put_in_discard(self):
        self.rect.x = 1275
        self.rect.y = 425
    
    def flip(self):
        if self.flipped == False:
            self.flipped = True
            self.color = WHITE
            self.border_color = RED
        elif self.flipped == True:
            self.flipped = False
            self.color = RED
            self.border_color = BLACK

    def damage(self):
        if self.health == 3:
            if self.flipped == False:
                self.health = 1
                self.rect.width = card_height
                self.rect.height = card_width
            elif self.flipped == True:
                self.health = 2
            self.text = self.rank
        elif self.health == 2:
            self.health = 1
            self.rect.width = card_height
            self.rect.height = card_width

        elif self.health == 1:
            self.health = 0
            self.rect.width = card_width
            self.rect.height = card_height
            if self.rank == "3" and self.flipped == False:
                self.health = 2
                self.flip()
                self.rect.width = card_width
                self.rect.height = card_height
                return
            else:
                self.text = self.rank + "X"
        elif self.health == 0:
            if self.rank == "J":
                self.health = 3
                self.text = "J*"
            else:
                self.health = 2
                self.text = self.rank

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

def draw_menu(surface, mouse_pos):
    """Makes the menu title screen.
    -TO DO-
    - Set the background
    - Print the header text 'DUEL 52' 
    - Make the buttons"""
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

    draw_button(screen, back_rect, "Back to Menu", BUTTON_FONT, RED, GREEN, mouse_pos)

def draw_game(surface, mouse_pos):
    '''The game'''
    surface.fill(DARKGRAY)
    
    # Menu button
    draw_button(screen, back_rect, "Back to Menu", BUTTON_FONT, RED, GREEN, mouse_pos)
   
    # Lane divisions
    draw_line(surface, WHITE, (vert_line_1, 0), (vert_line_1, SCREEN_HEIGHT))
    draw_line(surface, WHITE, (vert_line_2, 0), (vert_line_2, SCREEN_HEIGHT))
    draw_line(surface, WHITE, (vert_line_3, 0), (vert_line_3, SCREEN_HEIGHT))
    # Horizontal lines
    draw_line(surface, WHITE, (vert_line_3, 200), (SCREEN_WIDTH, 200))
    draw_line(surface, WHITE, (0, SCREEN_HEIGHT - 400), (SCREEN_WIDTH, SCREEN_HEIGHT - 400))
    draw_line(surface, WHITE, (vert_line_3, SCREEN_HEIGHT - 200), (SCREEN_WIDTH, SCREEN_HEIGHT - 200))

    # Draw Pile
    for card in deck:
        draw_card(screen, card.rect, card.text, BUTTON_FONT, card.color, card.color, mouse_pos, card.border_color)
  