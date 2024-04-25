"""Initialising Sprite Component - Version 4
- Change animation speed so that it doesn't depend on framerate
"""

import pygame
import sys

pygame.init()

# Set the screen size and caption
CLOCK = pygame.time.Clock()
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

LLAMA_JUMP = pygame.transform.scale(pygame.image.load("Llama.png"), (100, 100))
LLAMA_RUN1 = pygame.transform.scale(pygame.image.load("Llama2.png"), (100, 100))
LLAMA_RUN2 = pygame.transform.scale(pygame.image.load("Llama3.png"), (100, 100))

jumping = False

x_position = 100
y_position = 558
llama_count = 1
animation_tick_count = 0  # Keep track of animation ticks

Y_GRAVITY = 1
JUMP_HEIGHT = 20
y_velocity = JUMP_HEIGHT


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with gray color
    screen.fill(LIGHT_GREY_TUPLE)

    # Calculate how many times to repeat the floor image
    num_tiles = int(screen_width / floor_width) + 1  # Add 1 to ensure complete coverage

    # Draw the floor by repeating the image
    for i in range(num_tiles):
        screen.blit(floor_image, (i * floor_width, screen_height - floor_image.get_height()))

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    if not jumping:
        animation_tick_count += 1  # Increment counter
        if animation_tick_count >= 10:  # Check if 10 ticks have passed
            animation_tick_count = 0  # Reset counter
            if llama_count % 2 == 0:
                screen.blit(LLAMA_RUN1, (x_position, y_position))
            else:
                screen.blit(LLAMA_RUN2, (x_position, y_position))
            llama_count += 1  # Only update llama_count when animation occurs
    else:
        y_position -= y_velocity
        y_velocity -= Y_GRAVITY
        if y_velocity < -JUMP_HEIGHT:
            jumping = False
            y_velocity = JUMP_HEIGHT
        screen.blit(LLAMA_JUMP, (x_position, y_position))

    # Update the display
    pygame.display.flip()
    CLOCK.tick(60)


# Quit Pygame
pygame.quit()
