import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Dodger Game")

# Set the font for the score
font = pygame.font.SysFont('Comic Sans MS', 30)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define constants for the player and enemy sizes
PLAYER_SIZE = 50
ENEMY_SIZE = 30

# Load the player image
player_image = pygame.image.load("player.png")

# Scale the player image to the correct size
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))

# Create the player object
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
player_vel_y = 0
GRAVITY = 0.5
JUMP_VELOCITY = -10

# Define a list to hold the enemy objects
enemies = []

# Set the initial score
score = 0

# Create the main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= SCREEN_HEIGHT:
                player_vel_y = JUMP_VELOCITY
    
    # Apply gravity to the player's velocity
    player_vel_y += GRAVITY
    
    # Limit the player's vertical velocity
    if player_vel_y > 10:
        player_vel_y = 10
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
        player_x += 1
    player_rect.x = player_x

    # Create new enemies
    if len(enemies) < 5:
        enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
        enemy_y = -ENEMY_SIZE
        enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)
        enemies.append(enemy_rect)
    
    # Move the enemies and remove them if they go offscreen
    for enemy in enemies:
        enemy.y += 1
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)
    
    # Check for collisions between the player and enemies
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            running = False
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the player on the screen
    screen.blit(player_image, player_rect)
    
    # Draw the enemies on the screen
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    # Update the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Update the screen
    pygame.display.flip()
    
    # Increase the score by 1 every frame
    score += 1

    # Update the score 
    score += len(enemies) * 1
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate to 60 FPS
    clock.tick(300)

# Quit Pygame
pygame.quit()
