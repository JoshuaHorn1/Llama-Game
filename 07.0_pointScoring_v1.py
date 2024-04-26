"""Point Scoring Component - Version 1
- User scores based on time stayed alive, and is displayed to the screen
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
CACTI_SIZE_1 = 620  # lists holding the different y positions for generating the cacti
CACTI_SIZE_2 = 608
CACTI_SIZE_3 = 594

speed = 5  # movement speed of cacti objects
speed_counter = 0

cacti_delay_reset = 30  # a value that the counter must reach for a new cacti to spawn
cacti_delay_counter = 0  # cacti counter

cacti_force_spawn = 0

score = 0  # a variable to store the user's score

# Game loop
running = True
game_over = False
resetting_game = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Reset game
                game_over = False
                resetting_game = True
            if event.key == pygame.K_x and game_over:
                running = False

    if not game_over and not resetting_game:
        # Fill the screen with gray color
        screen.fill(LIGHT_GREY_TUPLE)

        # Update score
        score += 1

        # Format the score to 6 digits
        display_score = "{:06d}".format(score)

        # Display score on the screen
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score:", True, (50, 180, 50))
        score_value_text = font.render(f"{display_score}", True, (50, 180, 50))
        score_rect = score_text.get_rect(center=(50, 20))
        score_value_rect = score_value_text.get_rect(center=(50, 50))
        screen.blit(score_text, score_rect)
        screen.blit(score_value_text, score_value_rect)

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

        # Incrementally increases cactus speed
        speed_counter += 1
        if speed_counter == 600:
            speed += 0.2
            cacti_delay_reset -= 1

        # Generate a new cactus after a random time interval
        cacti_delay_counter += 1
        if cacti_delay_counter >= cacti_delay_reset:  # check if a cacti has been placed recently
            # Generates random chance for cacti to spawn, or forces one to spawn if it has been 300 ticks without one
            if random.randint(0, 600) < 2 or cacti_force_spawn == 180:
                cacti_force_spawn = 0
                cacti_delay_counter = 0
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
                cacti.append(Cactus(cactus_scale, screen_width, cactus_y, speed))
            else:
                cacti_force_spawn += 1  # adds 1 to counter

        # Move and draw cacti
        for cactus in cacti:
            cactus.move()
            screen.blit(cactus.image, (cactus.cactus_x, cactus.cactus_y))

            # Custom bounding box for cactus
            cactus_rect = pygame.Rect(cactus.cactus_x + 10, cactus.cactus_y + 10,
                                      cactus.image.get_width(), cactus.image.get_height())

            # Custom bounding box for llama
            llama_rect = pygame.Rect(x_position, y_position, 80, 80)

            if llama_rect.colliderect(cactus_rect):
                game_over = True
                game_over_font = pygame.font.Font(None, 150)
                game_over_text = game_over_font.render("~~ GAME OVER! ~~", True, (180, 50, 50))
                game_restart_font = pygame.font.Font(None, 80)
                game_restart_text = game_over_font.render("Press 'r' to restart,", True, (180, 50, 50))
                game_quit_text = game_over_font.render("or press 'x' to quit.", True, (180, 50, 50))
                game_over_rect = game_over_text.get_rect(center=(screen_width // 2, 150))
                game_restart_rect = game_restart_text.get_rect(center=(screen_width // 2, 350))
                game_quit_rect = game_quit_text.get_rect(center=(screen_width // 2, 450))
                screen.blit(game_over_text, game_over_rect)
                screen.blit(game_restart_text, game_restart_rect)
                screen.blit(game_quit_text, game_quit_rect)

        pygame.display.flip()

    if resetting_game:  # checks if the game is being reset, then resets variables if yes
        cacti = []
        x_position = 100
        y_position = 558  # Reset y-position to the ground level
        jumping = False  # Reset jumping status
        speed = 5
        speed_counter = 0
        cacti_delay_reset = 30
        cacti_delay_counter = 0
        cacti_force_spawn = 0
        score = 0
        resetting_game = False

    CLOCK.tick(60)

# Quit Pygame
pygame.quit()
