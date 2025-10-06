"""
menu_tutorial.py

A small, commented Pygame program that:
- Shows a Main Menu with a title and three buttons (Start, Options, Quit).
- Demonstrates how text rendering, button drawing, event handling, and simple
  state switching works.
- Includes explanatory comments (teacher-style) to help you learn.

If you're following along: read comments, run the file, and tinker with values.
"""

import pygame
import sys
import math

# ----------------------------
# Basic initialization
# ----------------------------
pygame.init()  # Start all Pygame modules we plan to use (display, font, etc.)

# Window size constants (all caps => 'constant by convention')
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 850
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Tutorial - Learn by Reading the Comments")

# Clock to cap the framerate
clock = pygame.time.Clock()

# ----------------------------
# Colors (RGB tuples)
# ----------------------------
# Colors are tuples of three integers (R, G, B), each 0-255.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (30, 30, 30)
LIGHTGRAY = (200, 200, 200)
BLUE = (0, 120, 215)
GREEN = (0, 180, 0)
RED = (200, 30, 30)

# ----------------------------
# Fonts - how text will look
# ----------------------------
# pygame.font.SysFont(name, size) returns a Font object.
# We use fonts to *render* text into images (Surfaces).
TITLE_FONT = pygame.font.SysFont("Arial", 64)
BUTTON_FONT = pygame.font.SysFont("Arial", 36)
GAME_FONT = pygame.font.SysFont("Arial", 28)

# ----------------------------
# Game states
# ----------------------------
# We use simple string constants to represent which "screen" we're on.
MENU = "menu"
GAME = "game"
OPTIONS = "options"
current_state = MENU  # start at the menu

# ----------------------------
# Button helper function(s)
# ----------------------------
def draw_text(text, font, color, surface, x, y, center=True):
    """
    Render text and blit (draw) it to a surface.

    Steps:
    1. font.render(...) creates a new Surface with your text drawn onto it.
       - antialias=True smooths edges.
    2. .get_rect(...) returns a Rect describing size and position.
       - If you pass center=(x,y), the rect will be positioned so its center is (x,y).
    3. surface.blit(text_surface, text_rect) copies the text image onto the target surface.
    """
    text_surf = font.render(text, True, color)  # step 1
    if center:
        text_rect = text_surf.get_rect(center=(x, y))  # step 2 - center placement
    else:
        text_rect = text_surf.get_rect(topleft=(x, y))  # top-left placement
    surface.blit(text_surf, text_rect)  # step 3
    return text_rect  # return rect in case caller needs it (e.g. for mouse collision)


def draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color=WHITE):
    """
    Draw a rectangular button and give visual feedback when hovered.

    Arguments:
    - surface: where to draw
    - rect: a pygame.Rect specifying position/size
    - text: label
    - font: font for the label
    - base_color: normal fill color
    - hover_color: fill color when mouse is over the button
    - mouse_pos: current mouse coordinates (to test hover)
    - border_color: color of the button outline

    Returns:
    - True if the mouse is currently over the button (useful for handling clicks)
    """
    hovered = rect.collidepoint(mouse_pos)  # check if mouse is inside the button rect
    color = hover_color if hovered else base_color

    # Draw the filled rectangle (button body)
    pygame.draw.rect(surface, color, rect)

    # Draw a border to make it look like a button
    pygame.draw.rect(surface, border_color, rect, 2)  # '2' is the border thickness

    # Draw centered text on top of the rectangle
    draw_text(text, font, WHITE, surface, rect.centerx, rect.centery)

    return hovered


# ----------------------------
# Layout / Button rectangles
# ----------------------------
# A Rect is defined by (x, y, width, height) where (x,y) is top-left.
# We'll position buttons relative to screen center for simplicity.
button_width, button_height = 260, 64
start_button_rect = pygame.Rect(
    (SCREEN_WIDTH // 2) - (button_width // 2), 250, button_width, button_height
)
options_button_rect = pygame.Rect(
    (SCREEN_WIDTH // 2) - (button_width // 2), 330, button_width, button_height
)
quit_button_rect = pygame.Rect(
    (SCREEN_WIDTH // 2) - (button_width // 2), 410, button_width, button_height
)
close_rect = pygame.Rect(10, 10, 50, 50)
# Options screen state (example)
options_back_rect = pygame.Rect(20, SCREEN_HEIGHT - 80, 140, 50)  # back button in options
enable_sound = True  # example toggle that might be changed in options


# ----------------------------
# Small helper to draw the menu
# ----------------------------
def draw_menu(surface, mouse_pos):
    """
    Draw the entire menu screen:
    - Title
    - Buttons (Start, Options, Quit)
    The function returns which button (if any) is hovered - but does not handle clicks.
    """
    # Background for menu
    surface.fill(DARKGRAY)

    # Title text: large and centered near the top
    draw_text("My Learning Game", TITLE_FONT, WHITE, surface, SCREEN_WIDTH // 2, 120)

    # Subtitle / hint
    draw_text("Use the mouse to select a menu item", GAME_FONT, LIGHTGRAY, surface, SCREEN_WIDTH // 2, 180)

    # Draw buttons and find which is hovered
    start_hover = draw_button(surface, start_button_rect, "Start Game", BUTTON_FONT, BLUE, GREEN, mouse_pos)
    options_hover = draw_button(surface, options_button_rect, "Options", BUTTON_FONT, BLUE, LIGHTGRAY, mouse_pos)
    quit_hover = draw_button(surface, quit_button_rect, "Quit", BUTTON_FONT, RED, LIGHTGRAY, mouse_pos)

    return start_hover, options_hover, quit_hover


def draw_options(surface, mouse_pos):
    """
    A simple Options screen that shows a toggle for sound and a Back button.
    This demonstrates how you might have multiple menu pages.
    """
    surface.fill(DARKGRAY)
    draw_text("Options", TITLE_FONT, WHITE, surface, SCREEN_WIDTH // 2, 100)
    draw_text(f"Sound: {'On' if enable_sound else 'Off'} (click toggle)", GAME_FONT, LIGHTGRAY, surface, SCREEN_WIDTH // 2, 220)

    # Draw a simple toggle button (we'll just reuse Rect/draw_button for simplicity)
    toggle_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 260, 200, 56)
    toggle_hover = draw_button(surface, toggle_rect, "Toggle Sound", BUTTON_FONT, BLUE, LIGHTGRAY, mouse_pos)

    # Back button (top-left-ish)
    back_hover = draw_button(surface, options_back_rect, "Back", BUTTON_FONT, BLUE, LIGHTGRAY, mouse_pos)
    return toggle_hover, back_hover

def draw_lines(surface):
    # lines that divide the screen into sixths
    v_line1_start_pos = SCREEN_WIDTH // 3, 0
    v_line1_end_pos = SCREEN_WIDTH // 3, SCREEN_HEIGHT
    pygame.draw.line(surface, WHITE, v_line1_start_pos, v_line1_end_pos, 5)
    v_line2_start_pos = (SCREEN_WIDTH // 3) * 2, 0
    v_line2_end_pos = (SCREEN_WIDTH // 3) * 2, SCREEN_HEIGHT
    pygame.draw.line(surface, WHITE, v_line2_start_pos, v_line2_end_pos, 5)
    h_line1_start_pos = 0, SCREEN_HEIGHT // 2
    h_line1_end_pos = SCREEN_WIDTH, SCREEN_HEIGHT // 2
    pygame.draw.line(surface, WHITE, h_line1_start_pos, h_line1_end_pos, 5)

def draw_game(surface):
    """
    Placeholder for the main game screen. Replace with your actual game drawing.
    This example draws a simple moving rectangle to show the game is active.
    """
    surface.fill((18, 24, 40))  # a different background so you know you're in the game
    draw_text("Game Running - Press ESC to return to Menu", GAME_FONT, LIGHTGRAY, surface, SCREEN_WIDTH // 2, 30)
    
    draw_lines(surface)

    # Simple demo: a rectangle that moves back and forth based on time
    t = pygame.time.get_ticks() / 1000.0  # time in seconds since Pygame started
    x = SCREEN_WIDTH // 2 + int(200 * math.sin(t * 2.0))
    demo_rect = pygame.Rect(x - 25, SCREEN_HEIGHT // 2 - 25, 50, 50)
    pygame.draw.rect(surface, BLUE, demo_rect)
    # My attempt at creating a button
    # draw_button(surface, rect, text, font, base_color, hover_color, mouse_pos, border_color=WHITE)
    
    draw_button(surface, close_rect, "X", BUTTON_FONT, RED, WHITE, mouse_pos)
    


# ----------------------------
# Main loop
# ----------------------------
running = True
while running:
    # Get mouse position at the start of the frame (used to compute hover states)
    mouse_pos = pygame.mouse.get_pos()

    # Event handling loop (this is how Pygame gives us input events)
    # This loop *must* be run regularly, otherwise the OS may think the program is frozen.
    for event in pygame.event.get():
        # QUIT event is fired when the user clicks the window 'X' button.
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN handles keyboard presses (for example, ESC to return to menu)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # pressing ESC returns you to the main menu from anywhere
                current_state = MENU

        # MOUSEBUTTONDOWN handles mouse clicks.
        # We check which state we're in so clicks do different things in menu/options/game.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 = left mouse button
            if current_state == MENU:
                # If click happened while we're in MENU, see which button was clicked.
                if start_button_rect.collidepoint(mouse_pos):
                    # Start the game: switch state
                    current_state = GAME
                elif options_button_rect.collidepoint(mouse_pos):
                    current_state = OPTIONS
                elif quit_button_rect.collidepoint(mouse_pos):
                    running = False  # quit the entire program
            elif current_state == OPTIONS:
                # Options screen clicks:
                toggle_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 260, 200, 56)
                if toggle_rect.collidepoint(mouse_pos):
                    # Toggle a setting - here we flip a boolean
                    enable_sound = not enable_sound
                if options_back_rect.collidepoint(mouse_pos):
                    current_state = MENU
            elif current_state == GAME:
                # Example: clicking in game could do something; for now do nothing special
                if close_rect.collidepoint(mouse_pos):
                    current_state = MENU
                pass

    # Drawing happens after input handling. This keeps input & drawing in sync.
    if current_state == MENU:
        # draw_menu returns (start_hover, options_hover, quit_hover) but we don't need them here
        draw_menu(screen, mouse_pos)

    elif current_state == OPTIONS:
        draw_options(screen, mouse_pos)

    elif current_state == GAME:
        draw_game(screen)

    # After all drawing calls, swap the display buffer to show the new frame.
    pygame.display.flip()

    # Cap the framerate to 60 FPS. This keeps timing predictable and reduces CPU usage.
    clock.tick(60)

# Clean up Pygame and exit the program.
# Always call pygame.quit() before exiting so Pygame can restore system resources.
pygame.quit()
sys.exit()
