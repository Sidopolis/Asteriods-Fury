import pygame
import math
import random
 
# Initialize pygame
pygame.init()
 
# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
 
# Set up the game clock
clock = pygame.time.Clock()
 
# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Set up the player
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_speed = 5
player_rotation_speed = 5
player_rotation = 0
 
# Set up the asteroids
asteroid_image = pygame.image.load("asteroid.png")
asteroid_list = []
for i in range(10):
    asteroid_rect = asteroid_image.get_rect()
    asteroid_rect.x = random.randint(0, screen_width)
    asteroid_rect.y = random.randint(0, screen_height)
    asteroid_speed = random.randint(1, 5)
    asteroid_rotation_speed = random.randint(-5, 5)
    asteroid_rotation = 0
    asteroid_list.append((asteroid_rect, asteroid_speed, asteroid_rotation_speed, asteroid_rotation))
 
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rotation -= player_rotation_speed
    if keys[pygame.K_RIGHT]:
        player_rotation += player_rotation_speed
    if keys[pygame.K_UP]:
        player_rect.x += player_speed * math.cos(math.radians(player_rotation))
        player_rect.y -= player_speed * math.sin(math.radians(player_rotation))
 
    # Draw the screen
    screen.fill(BLACK)
    screen.blit(player_image, player_rect)
    for asteroid in asteroid_list:
        screen.blit(asteroid_image, asteroid[0])
 
    # Update the screen
    pygame.display.flip()
 
    # Limit the frame rate
    clock.tick(60)
 
# Quit the game
pygame.quit()
