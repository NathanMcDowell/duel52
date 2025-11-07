'''This file has the Card class.'''

import pygame

from drawing_tools import *
from screens import *
from constants import *


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
        # Moves it to the discard pile if in those boundaries
        if self.rect.x > SCREEN_WIDTH - 175 and self.rect.y > SCREEN_HEIGHT - 425 and self.rect.y < 500:
            self.put_in_discard()
        
        if self.rect.x < 0: # Shifts off the left wall
            self.rect.x = 5
        elif self.rect.x > SCREEN_WIDTH - card_width: # Shifts off the right wall
            self.rect.x = SCREEN_WIDTH - card_width - 5
        elif self.rect.x <= vert_line_1 - card_width // 2 and self.rect.x > vert_line_1 - card_width: # Shifts to the left of the vert_line_1
            self.rect.x = vert_line_1 - card_width - 5
        elif self.rect.x > vert_line_1 - card_width // 2 and self.rect.x < vert_line_1: # Shifts to the right of the vert_line_1
            self.rect.x = vert_line_1 + 5
        elif self.rect.x <= vert_line_2 - card_width // 2 and self.rect.x > vert_line_2 - card_width: # Shifts to the left of the vert_line_2
            self.rect.x = vert_line_2 - card_width - 5
        elif self.rect.x > vert_line_2 - card_width // 2 and self.rect.x < vert_line_2: # Shifts to the right of the vert_line_2
            self.rect.x = vert_line_2 + 5
        elif self.rect.x <= vert_line_3 - card_width // 2 and self.rect.x > vert_line_3 - card_width: # Shifts to the left of the vert_line_3
            self.rect.x = vert_line_3 - card_width - 5
        elif self.rect.x > vert_line_3 - card_width // 2 and self.rect.x < vert_line_3: # Shifts to the right of the vert_line_3
            self.rect.x = vert_line_3 + 5
        
        if self.rect.y < 0: # Shifts off the top wall
            self.rect.y = 5
        elif self.rect.y > SCREEN_HEIGHT - card_height: # Shifts off the bottom wall
            self.rect.y = SCREEN_HEIGHT - card_height - 5
        # This stuff will need to be changed once turns are an option. 
        # At that point you will not be able to move cards onto the opponent's side.
        elif self.rect.y > horz_midline - card_height // 2 and self.rect.y < horz_midline: # Shifts below the midline
            self.rect.y = horz_midline + 5
        elif self.rect.y <= horz_midline - card_height // 2 and self.rect.y > horz_midline - card_height: # Shifts above the midline
            self.rect.y = horz_midline - card_height - 5
        self.assign_lane()

    def assign_lane(self):
        "Takes the current area that the card is in and uses it to define which lane it is in."
        if self.rect.x < vert_line_1:
            self.lane = 1
        elif self.rect.x < vert_line_2:
            self.lane = 2
        elif self.rect.x < vert_line_3:
            self.lane = 3
        else:
            self.lane = 0
        if self.rect.y > horz_midline:
            self.lane = self.lane * 2
        # print(f"Lane {self.lane}") # DEBUG HELPER

    def update_drag(self, mouse_pos):
        """Call this every frame while dragging"""
        if self.dragging:
            self.rect.x = mouse_pos[0] - self.offset_x
            self.rect.y = mouse_pos[1] - self.offset_y

    def put_in_discard(self):
        # SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
        # card_width, card_height = 100, 150
        self.rect.x = SCREEN_WIDTH - card_width - 25
        self.rect.y = SCREEN_HEIGHT - card_height - 225
    
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