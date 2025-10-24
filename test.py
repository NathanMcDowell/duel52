import pygame
import sys


class Card:
    suit: str
    rank: str
    flipped: bool
    health: int
    x_coord: int
    y_coord: int

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.flipped = False
        if rank == "J":
            self.health = 3
        else:
            self.health = 2
    def __repr__(self):
        return f"{self.rank} of {self.suit} with {self.health} health, flipped: {self.flipped}"
    
    # def move_with_mouse():


suits = ["S", "H", "D", "C"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Create a list of [suit, rank] pairs
deck = [[suit, rank] for suit in suits for rank in ranks]

print(deck)
print(len(deck))  # should be 52

for card in deck:
    play_card = Card(card[0], card[1])
    print(play_card)
