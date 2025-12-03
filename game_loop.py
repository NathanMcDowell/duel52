import pygame
import sys

pygame.init()

from screens import *
from drawing_tools import *
from constants import *


pygame.display.set_caption("Game Draft")

clock = pygame.time.Clock()

MENU = "menu"
GAME = "game"
OPTIONS = "options"
CONTROLS = "controls"
CARD_ABILITIES = "card_abilities"
current_state = MENU


def main():
    """The main game loop."""
    global current_state
    global player_turn
    current_card = "1"
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        if current_state == MENU:
            draw_menu(screen, mouse_pos)

        elif current_state == OPTIONS:
            draw_options(screen, mouse_pos)

        elif current_state == CONTROLS:
            draw_controls(screen, mouse_pos)

        elif current_state == CARD_ABILITIES:
            draw_card_abilities(screen, mouse_pos, current_card)

        elif current_state == GAME:
            draw_game(screen, mouse_pos, player_turn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # If the left mouse button is clicked
                    
                    # Menu Buttons
                    if current_state == MENU:
                        if quit_button.rect.collidepoint(mouse_pos):
                            running = False
                        if start_button.rect.collidepoint(mouse_pos):
                            current_state = GAME
                        if controls_button.rect.collidepoint(mouse_pos):
                            current_state = CONTROLS
                        if options_button.rect.collidepoint(mouse_pos):
                            current_state = OPTIONS
                    
                    # Options Buttons
                    if current_state == OPTIONS:
                        if back_button.rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if color_red_button.rect.collidepoint(mouse_pos):
                            for card in reversed_deck:
                                card.change_color(RED)
                        if color_blue_button.rect.collidepoint(mouse_pos):
                            for card in reversed_deck:
                                card.change_color(BLUE)
                        if color_green_button.rect.collidepoint(mouse_pos):
                            for card in reversed_deck:
                                card.change_color(GREEN)
                                
                    # Controls Buttons
                    if current_state == CONTROLS:
                        if back_button.rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if to_card_abilities_button.rect.collidepoint(mouse_pos):
                            current_state = CARD_ABILITIES

                    if current_state == CARD_ABILITIES:
                        if back_button.rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if to_controls_button.rect.collidepoint(mouse_pos):
                            current_state = CONTROLS
                        for button in ability_buttons:
                            if button.rect.collidepoint(mouse_pos):
                                current_card = button.text
                    
                    # Game Buttons and Card Dragging
                    if current_state == GAME:
                        if concede_button.rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if turn_button.rect.collidepoint(mouse_pos):
                            if player_turn == 1:
                                player_turn = 2
                            elif player_turn == 2:
                                player_turn = 1
                            print(f"Player {player_turn}'s turn")
                        for card in reversed_deck:
                            if card.rect.collidepoint(mouse_pos):
                                card.start_drag(mouse_pos, player_turn)
                                break
                        
            
            # Card stops moving when click is lifted
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # If the left mouse button is lifted
                if current_state == GAME:
                    for card in deck:
                        card.stop_drag(player_turn)
            
            # Damage for cards
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2: # If the scroll button mouse button is clicked
                for card in reversed_deck:
                    if card.rect.collidepoint(mouse_pos):
                        card.damage()
            # Flips cards
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # If the right mouse button is clicked
                for card in reversed_deck:
                    if card.rect.collidepoint(mouse_pos):
                        card.flip()
                # print(mouse_pos) # DEBUG HELPER
        #Constantly updating the drag of the mouse if it is being held
        if current_state == GAME:
            for card in deck:
                card.update_drag(mouse_pos)
                        
            
            


        pygame.display.flip()

        clock.tick(60)

main()

pygame.quit()
sys.exit()