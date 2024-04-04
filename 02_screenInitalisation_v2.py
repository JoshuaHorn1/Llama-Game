"""Screen Initialisation Component - Version 2
- Created a game loop allowing the box to stay up
"""

# Imports & Initialisations...
import pygame
pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1080, 720))
GAME_ICON = pygame.image.load('llama_icon.png')

pygame.display.set_icon(GAME_ICON)
pygame.display.set_caption("The Adventures of Lloyd")

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

