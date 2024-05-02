"""Sprite Collision Component - Version 3
"""

import pygame
import random

# INITIALISATIONS...
pygame.init()


# CLASSES...
class Cactus(pygame.sprite.Sprite):
    def __init__(self, scale, cactus_x, cactus_y, speed):
        super().__init__()
        self.scale = scale
        self.image = pygame.image.load("cactus.png")
        # Adjust image size based on scale
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect(topleft=(cactus_x, cactus_y))
        self.speed = speed

    def __getitem__(self, index):
        if index == 0:
            return self.scale
        else:
            raise IndexError("Invalid index for Cactus")

    def move(self):
        self.rect.x -= self.speed


class Llama(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = LLAMA_JUMP  # Initial image
        self.mask = pygame.mask.from_surface(self.image)  # Create mask for collision detection
        self.rect = self.image.get_rect(center=(100, 558))  # Initial position

        self.count = 1
        self.animation_tick_count = 0
        self.current_frame = LLAMA_RUN1
        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 18
        self.y_velocity = self.JUMP_HEIGHT
        self.jumping = False

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            self.jumping = True

        if not self.jumping:
            self.animation_tick_count += 1
            # Always blit the current frame, even on non-update ticks:
            screen.blit(self.current_frame, self.rect)
            if self.animation_tick_count >= 10:  # Check if it's time to update the frame
                self.animation_tick_count = 0
                # Switch to the other animation frame:
                self.current_frame = LLAMA_RUN2 if self.current_frame == LLAMA_RUN1 else LLAMA_RUN1
        else:
            self.y_velocity -= self.Y_GRAVITY
            self.rect.y -= self.y_velocity
            if self.y_velocity < -self.JUMP_HEIGHT:
                self.jumping = False
                self.y_velocity = self.JUMP_HEIGHT
            screen.blit(LLAMA_JUMP, self.rect)


# FUNCTIONS...
def check_collision(llama_sprite, cacti_group):
    return pygame.sprite.spritecollide(llama_sprite, cacti_group, False)  # Check for collision, don't delete on collision

# MAIN PROGRAM...
# Set the screen size and caption
CLOCK = pygame.time.Clock()
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Adventures of Lloyd")

# Colour Tuples
GREY_TUPLE = (200, 200, 200)
LIGHT_GREY_TUPLE = (250, 250, 250)
SCORE_TEXT_COLOUR = (50, 50, 50)
GAME_OVER_TEXT_COLOUR = (150, 150, 150)

# Fonts
SCORE_FONT = pygame.font.SysFont('couriernew', 30)
GAME_OVER_FONT = pygame.font.SysFont('chiller', 150)
GAME_RESTART_FONT = pygame.font.SysFont('copperplategothic', 80)

# Floor image variables
floor_image = pygame.image.load("ground.png")  # load floor image
floor_width = floor_image.get_width()  # get floor width

# Llama animation frames
LLAMA_JUMP = pygame.transform.scale(pygame.image.load("Llama.png"), (100, 100))
LLAMA_RUN1 = pygame.transform.scale(pygame.image.load("Llama2.png"), (100, 100))
LLAMA_RUN2 = pygame.transform.scale(pygame.image.load("Llama3.png"), (100, 100))

# Create llama sprite group
llama_sprite = Llama()
llama_group = pygame.sprite.GroupSingle(llama_sprite)

# Create cacti sprite group
cacti_group = pygame.sprite.Group()

# User scoring variable
score = 0

# Game loop:
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

        # Update score and speed counter
        score += 1
        speed_counter += 1

        # Format the score to 6 digits
        display_score = "{:06d}".format(score)

        # Display score on the screen
        score_text = SCORE_FONT.render(f"Score: {display_score}", True, SCORE_TEXT_COLOUR)
        score_rect = score_text.get_rect(center=(125, 20))
        screen.blit(score_text, score_rect)

        # Incrementally increases cactus speed relative to the score
        if speed_counter == 500:
            speed_counter = 0
            speed += 0.5
            cacti_delay_reset -= 1

        # Format the speed to 3 digits
        display_speed = "{:0.1f}".format(speed).zfill(4)

        # Display the speed on the screen
        speed_text = SCORE_FONT.render(f"Effective Speed: {display_speed}", True, SCORE_TEXT_COLOUR)
        speed_rect = speed_text.get_rect(center=(885, 20))
        screen.blit(speed_text, speed_rect)

        # Calculate how many times to repeat the floor image
        num_tiles = int(screen_width / floor_width) + 1  # Add 1 to ensure complete coverage

        # Draw the floor by repeating the image
        for i in range(num_tiles):
            screen.blit(floor_image, (i * floor_width, screen_height - floor_image.get_height()))

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            jumping = True

        # Update llama sprite
        llama_group.update()

        # Move and draw cacti
        for cactus in cacti:
            cactus.move()
            cacti_group.add(cactus)  # Add cactus to the group
            screen.blit(cactus.image, cactus.rect)

        # Check collision between llama and cacti
        collisions = check_collision(llama_sprite, cacti_group)
        if collisions:
            game_over = True

        # Draw ground after updating everything else
        screen.blit(floor_image, (0, screen_height - floor_image.get_height()))

        # Update the display
        pygame.display.flip()

        # Set the FPS
        CLOCK.tick(60)

        # Handle game over and reset screen
        if game_over:
            screen.fill(GREY_TUPLE)
            game_over_text = GAME_OVER_FONT.render("Game Over", True, GAME_OVER_TEXT_COLOUR)
            game_over_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(game_over_text, game_over_rect)

            restart_text = GAME_RESTART_FONT.render("Press 'R' to Restart", True, SCORE_TEXT_COLOUR)
            restart_rect = restart_text.get_rect(center=(screen_width / 2, screen_height * 3 / 4))
            screen.blit(restart_text, restart_rect)

            exit_text = SCORE_FONT.render("Press 'X' to Exit", True, SCORE_TEXT_COLOUR)
            exit_rect = exit_text.get_rect(center=(screen_width / 2, 5 * screen_height / 6))
            screen.blit(exit_text, exit_rect)

            pygame.display.flip()
            CLOCK.tick(60)

        pygame.display.flip()

    # Reset the game when requested
    if resetting_game:
        # Reset score and game variables
        score = 0
        speed = 6
        speed_counter = 0
        cacti_delay_reset = 100  # Adjust delay between cactus spawns

        # Clear cacti group
        cacti_group.empty()

        # Reset llama position
        llama_sprite.rect.x = 100
        llama_sprite.rect.y = 558
        llama_sprite.jumping = False

    CLOCK.tick(60)

pygame.quit()