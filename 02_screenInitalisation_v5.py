"""Screen Initialisation Component - Version 5
- Changed the background to be light grey
"""

import pygame

pygame.init()

# Set the screen size and caption
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Adventures of Lloyd")

# Define the gray color (optional)
GREY_TUPLE = (200, 200, 200)
LIGHT_GREY_TUPLE = (250, 250, 250)


# Load the floor image
floor_image = pygame.image.load("ground.png")

# Get the floor image width
floor_width = floor_image.get_width()

# Game loop
running = True
while running:
    # Handle events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with gray color (optional)
    screen.fill(LIGHT_GREY_TUPLE)

    # Calculate how many times to repeat the floor image
    num_tiles = int(screen_width / floor_width) + 1  # Add 1 to ensure complete coverage

    # Draw the floor by repeating the image
    for i in range(num_tiles):
        screen.blit(floor_image, (i * floor_width, screen_height - floor_image.get_height()))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
