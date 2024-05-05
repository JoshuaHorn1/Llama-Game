# IMPORTS AND INITIALISATIONS...
import pygame
pygame.init()


# FUNCTIONS...
def welcome_screen():
    welcome = True
    while welcome:
        # Handle events (e.g., closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # Check if it's a key press event
                if event.key == pygame.K_RETURN:  # Check if Enter key is pressed
                    welcome = False

        # Fill the screen with gray color
        screen.fill(LIGHT_GREY_TUPLE)

        # Calculate how many times to repeat the floor image
        num_tiles = int(screen_width / floor_width) + 1  # Add 1 to ensure complete coverage

        # Draw the floor by repeating the image
        for i in range(num_tiles):
            screen.blit(floor_image, (i * floor_width, screen_height - floor_image.get_height()))

        # Set the welcome text using the welcome font
        welcome_text_1 = WELCOME_FONT.render("Press >SPACEBAR< to Jump!", True, SCORE_TEXT_COLOUR)
        welcome_text_2 = WELCOME_FONT.render("Presss >ENTER< to start!", True, SCORE_TEXT_COLOUR)
        welcome_rect_1 = welcome_text_1.get_rect(center=(screen_width // 2, screen_height // 2 - 120))
        welcome_rect_2 = welcome_text_2.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(welcome_text_1, welcome_rect_1)
        screen.blit(welcome_text_2, welcome_rect_2)

        screen.blit(LLAMA_JUMP, (x_position, y_position))

        pygame.display.flip()
        CLOCK.tick(60)

    return


# MAIN PROGRAM...
CLOCK = pygame.time.Clock()
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Adventures of Lloyd")
GREY_TUPLE = (200, 200, 200)
LIGHT_GREY_TUPLE = (250, 250, 250)
SCORE_TEXT_COLOUR = (50, 50, 50)
WELCOME_FONT = pygame.font.SysFont('consolas', 75)
floor_image = pygame.image.load("ground.png")
floor_width = floor_image.get_width()
x_position = 100
y_position = 558
LLAMA_JUMP = pygame.transform.scale(pygame.image.load("Llama.png"), (100, 100))
LLAMA_RUN1 = pygame.transform.scale(pygame.image.load("Llama2.png"), (100, 100))
LLAMA_RUN2 = pygame.transform.scale(pygame.image.load("Llama3.png"), (100, 100))

welcome_screen()