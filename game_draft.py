import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Draft")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (30, 30, 30)
LIGHTGRAY = (200, 200, 200)
BLUE = (0, 120, 215)
GREEN = (0, 180, 0)
RED = (200, 30, 30)


TITLE_FONT = pygame.font.SysFont("Arial", 70)
BUTTON_FONT = pygame.font.SysFont("Arial", 50)
GAME_FONT = pygame.font.SysFont("Arial", 70)

MENU = "menu"
GAME_START = "game_start"
GAME = "game"
OPTIONS = "options"
CONTROLS = "controls"
current_state = MENU

# Lines
vert_line_1, vert_line_2, vert_line_3 = (SCREEN_WIDTH - 150) // 3, 2 * (SCREEN_WIDTH - 150) // 3, SCREEN_WIDTH - 150

# Rectangles
# (x coordinate, y coordinate, width, height)
button_width, button_height = 260, 64
card_width, card_height = 100, 150
centered_width = (SCREEN_WIDTH // 2) - (button_width // 2)
card_centered_height = (SCREEN_HEIGHT // 2) - (card_height // 2)
card_one_third_height = (SCREEN_HEIGHT // 3) - (card_height // 2)
card_two_thirds_height = (2 * SCREEN_HEIGHT // 3) - (card_height // 2)

# Menu Rectangles
start_rect = pygame.Rect(centered_width, 100, button_width, button_height)
controls_rect = pygame.Rect(centered_width, 200, button_width, button_height)
options_rect = pygame.Rect(centered_width, 300, button_width, button_height)
quit_rect = pygame.Rect(centered_width, 400, button_width, button_height)
# Start Up Rectangles
back_rect = pygame.Rect(40, SCREEN_HEIGHT - 100, button_width + 60, button_height)
begin_rect = pygame.Rect(500, SCREEN_HEIGHT - 100, button_width, button_height)

# Card class test
class Card:
    suit: str
    rank: str
    flipped: bool
    health: int
    player: int
    x_coord: int
    y_coord: int

    def __init__(self, rank, suit, x, y):
        self.suit = suit
        self.rank = rank
        self.flipped = False
        if rank == "J":
            self.health = 3
        else:
            self.health = 2
        player = 0
        self.x_coord = x
        self.y_coord = y
        
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
        self.rect.y = 625
    
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
        if self.health == 2:
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
            else:
                self.rank = self.rank = self.rank + "X"
        

deck = []
RANK_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
            # Spades, Diamonds, Clubs, Hearts
SUIT_LIST = ['S', 'D', 'C', 'H']
for suit in SUIT_LIST:
    for rank in RANK_LIST:
        card = Card(rank, suit, (SCREEN_WIDTH - (card_width + 25)), card_centered_height)
        deck.append(card)
random.shuffle(deck)
reversed_deck = list(reversed(deck))



def draw_text(text, font, color, surface, x, y, center = True):
    """When I need to draw text, this is the function that I will use to do so.
    -Text is what will be written.
    -Font is the font that it will be written in. I have made two font constants to be used up above.
    -Color is the color that the text will be. I also have constants for colors above.
    -Surface is the surface on which the text will be placed, which is the screen constant.
    -x and y are the coordinates for the text.
    -center = True means that the text will be centered on the x and y instead of that being the upper-left coordinate."""
    text_surf = font.render(text, True, color)
    if center:
        text_rect = text_surf.get_rect(center=(x, y))
    else:
        text_rect = text_surf.get_rect(topleft=(x, y))
    surface.blit(text_surf, text_rect)
    return text_rect

def draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color = WHITE):
    """This makes buttons where I need them.
    -surface is the surface on which everything is placed, the screen.
    -rect is the predefined details for the button's shape and size.
    -text is the text on the button, which will be put into a draw text function within this one.
    -font is the font of above text, as determined by the above written font variables.
    -base_color is the color that the rectangle will be unless it is hovered over. Use constant colors.
    -hover_color is the color that the rectangle will be when hovered over. Use constant colors.
    -mouse_pos in this case is used to determine if the mouse is over the button. It will take from a function that determines mouse position.
    -border_color is the color of the border that the button has. It will be white unless otherwise specified."""
    
    hovered = rect.collidepoint(mouse_pos)  
    color = hover_color if hovered else base_color
    
    pygame.draw.rect(surface, color, rect) 
    pygame.draw.rect(surface, border_color, rect, 2)  # Determines border thickness
    
    draw_text(text, font, BLACK, surface, rect.centerx, rect.centery) # Adds text to the function

    return hovered

def draw_card(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color):
    """This makes buttons where I need them.
    -surface is the surface on which everything is placed, the screen.
    -rect is the predefined details for the button's shape and size.
    -text is the text on the button, which will be put into a draw text function within this one.
    -font is the font of above text, as determined by the above written font variables.
    -base_color is the color that the rectangle will be unless it is hovered over. Use constant colors.
    -hover_color is the color that the rectangle will be when hovered over. Use constant colors.
    -mouse_pos in this case is used to determine if the mouse is over the button. It will take from a function that determines mouse position.
    -border_color is the color of the border that the button has. It will be white unless otherwise specified."""
    
    hovered = rect.collidepoint(mouse_pos)  
    color = hover_color if hovered else base_color
    
    pygame.draw.rect(surface, color, rect) 
    pygame.draw.rect(surface, border_color, rect, 2)  # Determines border thickness
    
    draw_text(text, font, RED, surface, rect.centerx, rect.centery) # Adds text to the function

    return hovered

def draw_line(surface, color, start_pos, end_pos, width=5):
    pygame.draw.line(surface, color, start_pos, end_pos, width)

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
    # Discard pile division
    draw_line(surface, WHITE, (vert_line_3 , SCREEN_HEIGHT - 200), (SCREEN_WIDTH, SCREEN_HEIGHT - 200))

    # Draw Pile
    for card in deck:
        draw_card(screen, card.rect, card.rank, BUTTON_FONT, card.color, card.color, mouse_pos, card.border_color)
    
def main():
    """The main game loop."""
    global current_state
    global x, y
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
                    if current_state == MENU:
                        if quit_rect.collidepoint(mouse_pos):
                            running = False
                        if start_rect.collidepoint(mouse_pos):
                            current_state = GAME_START
                        if controls_rect.collidepoint(mouse_pos):
                            current_state = CONTROLS
                        if options_rect.collidepoint(mouse_pos):
                            current_state = OPTIONS
                    
                    if current_state == OPTIONS:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                    
                    if current_state == CONTROLS:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                    
                    if current_state == GAME_START:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                        if begin_rect.collidepoint(mouse_pos):
                            current_state = GAME
                    
                    if current_state == GAME:
                        if back_rect.collidepoint(mouse_pos):
                            current_state = MENU
                        for card in reversed_deck:
                            if card.rect.collidepoint(mouse_pos):
                                card.start_drag(mouse_pos)
                                break

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # If the left mouse button is lifted
                if current_state == GAME:
                    for card in deck:
                        card.stop_drag()
                        if card.rect.x > SCREEN_WIDTH - 175 and card.rect.y > SCREEN_HEIGHT - 225:
                            card.put_in_discard()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2: # If the scroll button mouse button is clicked
                for card in reversed_deck:
                    if card.rect.collidepoint(mouse_pos):
                        card.damage()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # If the right mouse button is clicked
                for card in reversed_deck:
                    if card.rect.collidepoint(mouse_pos):
                        card.flip()
        
        if current_state == GAME:
            for card in deck:
                card.update_drag(mouse_pos)
                        
            
            


        pygame.display.flip()

        clock.tick(60)

main()

pygame.quit()
sys.exit()