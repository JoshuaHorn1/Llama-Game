"""Screen Initialisation Component - Version 1
Initialise a terrain box
"""

# Imports & Initialisations...
import pygame
pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1080, 720))
GAME_ICON = pygame.image.load('llama_icon.png')

pygame.display.set_icon(GAME_ICON)
pygame.display.set_caption("The Adventures of Lloyd")

clock.tick(60)