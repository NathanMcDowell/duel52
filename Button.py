'''This file has the Button class.'''

import pygame

from drawing_tools import *
from constants import *

card_abilities = {
    "2": "Add a card to your hand from the draw pile, then discard any card from your hand into the discard pile. The drawn card may be played if an action is available. If draw pile is empty, does nothing.",
    "3": "When your opponent kills a face-down 3, instead of being discarded, it flips and is now a normal live card with 2 hit points.",
    "4": "Look at any face-down card on the board. If you look at a Base card, do not show it to your opponent.",
    "5": "Flip all face-down cards in its lane. Flipped card powers activate in the order that you choose, and they can attack if actions are available. If draw pile is empty, will also flip base card.",
    "6": "All enemy cards in lane are frozen for one turn, they may not attack or flip themselves. They may still be flipped by a 5, healed by a 7, moved by a Queen or activated by a King. Cannot freeze a 9. New cards may be played into the lane.",
    "7": "Heals all your damaged cards, in all lanes, face-down and face-up. Heals a Jack to full. Does nothing if there are no damaged cards.",
    "8": "Any card that attacks an 8 will take one damage (except a 9).",
    "9": "Cannot be frozen by a 6. Doesn't take damage when attacking an 8. Cannot be damaged by a 10's twinstrike (can still be attacked, but only alone). Deals two damage to a Jack.",
    "10": "When attacking, deals one damage each to two cards in the opposing lane. The cards do not have to be next to each other. Cannot damage past a Jack, cannot damage a 9 and another card (can still choose to damage one of them).",
    "J": "A Jack must be killed before other cards can be attacked. Place him at the front of the lane to remind your opponent. He has three hit points; turn 45 degrees for first damage, 90 degrees for second damage.",
    "Q": "May move an ally card from another lane to her lane, face-down or face-up. The moved card does not reactivate flip powers but retains constant powers. It may attack if an action is available. If the draw pile is empty, she may move a Base card.",
    "K": "All your face-up cards in lane reactivate their powers. Does not affect other Kings. Does not affect cards with constant powers. You may choose the order of activations.",
    "A": "When flipped, gain one action. You may use this action however you like. On its first turn, an Ace may attack twice. When Kinged, gain one action, and may attack twice."
}

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
    

    def draw_button(self, mouse_pos, surface=screen):
        hovered = self.rect.collidepoint(mouse_pos)  
        color = self.hover_color if hovered else self.color
    
        pygame.draw.rect(surface, color, self.rect) 
        pygame.draw.rect(surface, self.border_color, self.rect, 2)  # Determines border thickness
    
        draw_text(self.text, self.font, BLACK, surface, self.rect.centerx, self.rect.centery) # Adds text to the function

    def display_card_information(self):
        for rank in card_abilities:
            if self.text == rank:
                print(card_abilities[rank])
