import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen (width, height)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Duel 52 Menu")

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 60)
button_font = pygame.font.SysFont("Arial", 40)

# Colors
WHITE = (255, 255, 255)
RED = (200, 12, 12)

# Game States
MENU = "menu"
GAME = "game"

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    running = True
    while running == True:
        print("Hi")
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state here

    # Draw background (fill screen with color)
    screen.fill((30, 30, 30))  # dark gray background

    # Flip display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame cleanly
pygame.quit()
sys.exit()
