import random

# Two lists are created in this code. The original list is used as the template for everything. 
# The second list is a copy. If there were only one list, removing cards from the list would
# be permanent, meaning the users would not be able to reshuffle the deck as easily.
cards_original = ["Ace of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"]
cards = cards_original.copy() # Copy the original list
jokers = ["Red Joker", "Black Joker"] # Jokers for later use
discard_pile = []
next_step = None # This variable determines which action the player will use. If it ever equals "stop", the program will stop.
print("Welcome to Playing Cards!")

while next_step != "stop":
    print("Type the number of your desired action:") # Displays the actions the user can take.
    print("1. Draw a card")
    print("2. Reshuffle Deck")
    print("3. Add Jokers")
    print("4. View Discard Pile")
    # The player's next action, entered as a number, is saved in this variable.
    next_step = input("Choose your action: ")
    if next_step == "1": # Action 1: Draw a card
        if len(cards) > 0: # Make sure the deck isn't empty.
            card_num = random.randint(0, len(cards))
            selected_card = cards.pop(card_num - 1)
            discard_pile.append(selected_card)
            print(f"Your card is: {selected_card}")
            move_on = input("Type ENTER to continue. ") # move_on is added so the user has time to read the displayed message, then choose to continue before they're sent right to the options screen again.
            # The above code selects a random card, pops it off and adds it to the discard pile,
            # then displays the card's value. In the future--link each value to an image file using dictionaries?
        else:
            print("Please reshuffle the deck.") # If the deck is empty, prompt the user to reshuffle.
    elif next_step == "2": # Action 2: Reshuffle deck
        cards = cards_original.copy()
        print("Deck Reshuffled.")
        move_on = input("Type ENTER to continue. ")
        # This code completely resets the edited card list by matching it to the original list.
    elif next_step == "3": # Action 3: Add Jokers
        cards_original = cards_original + jokers
        cards = cards + jokers
        print("Jokers added.")
        move_on = input("Type ENTER to continue. ")
        # This code adds the Jokers to both the original card pile and the edited one. This allows
        # the Jokers to be included when the player reshuffles. Currently, the player can't remove Jokers.
    elif next_step == "4": # Action 4: Display Discard Pile
        print(f"The discard pile contains: {discard_pile}")
        move_on = input("Type ENTER to continue.")
        # Very simple. This prints the discard pile.
print("Goodbye!")
print(cards)
# STRETCH GOALS:
# Deal Hand action: enter the number of players and the number of cards in the hand. The program will do so automatically, capping off at the maximum number of cards each player can have (i.e. if there are 5 cards split btwn 5 people, you can't ask for everyone to have hands of two cards.)
# Import Deck action: Allow the user to make custom decks and substitute them in for the deck reference list.
# Change the randomization for step 1 to use random.choice() rather than random.randint()
# Adapt this into main() function format