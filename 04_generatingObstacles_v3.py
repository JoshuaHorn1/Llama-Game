"""Generating Obstacles Component - Version 3
- Correctly places moving cacti on the ground
"""

import pygame
import random
pygame.init()


# CLASSES...
class Cactus:
    def __init__(self, scale, cactus_x, cactus_y, speed):
        self.scale = scale
        self.cactus_x = cactus_x
        self.cactus_y = cactus_y
        self.speed = speed
        self.image = pygame.image.load("cactus.png")
        # Adjust image size based on scale
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()

    def move(self):
        self.cactus_x -= self.speed


# MAIN LOOP...
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
current_frame = LLAMA_RUN1  # Start with the first animation frame

Y_GRAVITY = 1
JUMP_HEIGHT = 18
y_velocity = JUMP_HEIGHT

cacti = []  # a list to hold the different cactus variables
CACTI_SIZE_1 = 620  # lists holding the different y positions for generating the cactus's
CACTI_SIZE_2 = 608
CACTI_SIZE_3 = 594

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
        animation_tick_count += 1  # Increment tick counter
        # Always blit the current frame, even on non-update ticks:
        screen.blit(current_frame, (x_position, y_position))
        if animation_tick_count >= 10:  # Check if it's time to update the frame
            animation_tick_count = 0  # Reset counter
            # Switch to the other animation frame:
            current_frame = LLAMA_RUN2 if current_frame == LLAMA_RUN1 else LLAMA_RUN1
    else:
        y_position -= y_velocity
        y_velocity -= Y_GRAVITY
        if y_velocity < -JUMP_HEIGHT:
            jumping = False
            y_velocity = JUMP_HEIGHT
        screen.blit(LLAMA_JUMP, (x_position, y_position))

    # Generate a new cactus after a random time interval
    if random.randint(0, 100) < 2:
        cactus_scale = random.randint(1, 3)  # Random scale
        if cactus_scale == 1:
            cactus_y = CACTI_SIZE_1
            cactus_scale = 1.2
        elif cactus_scale == 2:
            cactus_y = CACTI_SIZE_2
            cactus_scale = 1.6
        else:
            cactus_y = CACTI_SIZE_3
            cactus_scale = 2
        cacti.append(Cactus(cactus_scale, screen_width, cactus_y, 10))

    # Move and draw cacti
    for cactus in cacti:
        cactus.move()
        screen.blit(cactus.image, (cactus.cactus_x, cactus.cactus_y))

    # Update the display
    pygame.display.flip()
    CLOCK.tick(60)

# Quit Pygame
pygame.quit()
