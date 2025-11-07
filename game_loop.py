import pygame
import sys

pygame.init()

from screens import *
from drawing_tools import *
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Draft")

clock = pygame.time.Clock()

MENU = "menu"
GAME_START = "game_start"
GAME = "game"
OPTIONS = "options"
CONTROLS = "controls"
current_state = MENU


def main():
    """The main game loop."""
    global current_state
    global player_turn
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        if current_state == MENU:
            draw_menu(screen, mouse_pos)
        
        if current_state == GAME_START:
            ''''''
            draw_game_startup(screen, mouse_pos)

        if current_state == OPTIONS:
            draw_options(screen, mouse_pos)

        if current_state == CONTROLS:
            draw_controls(screen, mouse_pos)

        if current_state == GAME:
            draw_game(screen, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # If the left mouse button is clicked
                    
                    # Menu Buttons
                    if current_state == MENU:
                        if quit_rect.collidepoint(mouse_pos):
                            running = False
                        if start_rect.collidepoint(mouse_pos):
                            current_state = GAME_START
                        if controls_rect.collidepoint(mouse_pos):
                            current_state = CONTROLS
                        if options_rect.collidepoint(mouse_pos):
                            current_state = OPTIONS
                    
                    # Options Buttons
                    if current_state == OPTIONS:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                    
                    # Controls Buttons
                    if current_state == CONTROLS:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                    
                    # Game Start Up Buttons
                    if current_state == GAME_START:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if begin_rect.collidepoint(mouse_pos):
                            current_state = GAME
                    
                    # Game Buttons and Card Dragging
                    if current_state == GAME:
                        if concede_rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if turn_rect.collidepoint(mouse_pos):
                            if player_turn == 1:
                                player_turn = 2
                            elif player_turn == 2:
                                player_turn = 1
                            print(player_turn)
                        for card in reversed_deck:
                            if card.rect.collidepoint(mouse_pos):
                                card.start_drag(mouse_pos)
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