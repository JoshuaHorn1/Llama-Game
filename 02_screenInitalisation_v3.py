"""Screen Initialisation Component - Version 3
- Set background to be grey
- Initialised a floor sprite
"""

import pygame

pygame.init()

# Set the screen size and caption
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Adventures of Lloyd")

# Define the gray color
GREY_TUPLE = (200, 200, 200)

# Load the floor image
floor_image = pygame.image.load("ground.png")

# Game loop
running = True
while running:
    # Handle events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with gray color
    screen.fill(GREY_TUPLE)

    # Draw the floor sprite (add this section)
    screen.blit(floor_image, (0, screen_height - floor_image.get_height()))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()