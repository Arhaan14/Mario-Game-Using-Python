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
pygame.display.set_caption("Mario Game")

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

# Load the player image
player_image = pygame.image.load("mario.png")

# Scale the player image to the correct size
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))

# Create the player object
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)

# Define a list to hold the enemy objects
enemies = []

# Set the initial score
score = 0

# Set initial values for jumping functionality
jumping = False
jump_count = 10

# Set the initial value for moving the player
player_move_x = 0

# Create the main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping = True
            if event.key == pygame.K_LEFT:
                player_move_x = -5
            if event.key == pygame.K_RIGHT:
                player_move_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_move_x < 0:
                player_move_x = 0
            if event.key == pygame.K_RIGHT and player_move_x > 0:
                player_move_x = 0
                
    # Move the player
    player_x += player_move_x
    
    # Jumping functionality
    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10
            
    if not jumping:
        if pygame.key.get_pressed()[pygame.K_UP] and player_y > 0:
            jumping = True
    
    player_rect.x = player_x
    player_rect.y = player_y
    
    # Create new enemies
    if len(enemies) < 5:
        enemy_x = random.randint(0, SCREEN_WIDTH - PLAYER_SIZE)
        enemy_y = -PLAYER_SIZE
        enemy_rect = pygame.Rect(enemy_x, enemy_y, PLAYER_SIZE, PLAYER_SIZE)
        enemies.append(enemy_rect)
    
    # Move the enemies and remove them if they go offscreen
    for enemy in enemies:
        enemy.y += 3
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)
    
    # Check for collisions between the player and enemies
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            running = False
    
    # Clear the screen
    screen.fill(WHITE)