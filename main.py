import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platform Example")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Platform settings
platforms = [
    pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 20),
    pygame.Rect(300, 400, 150, 20),
    pygame.Rect(500, 250, 180, 20)
]

# Player settings
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5
player_vel_y = 0
gravity = 0.5
on_ground = False
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    player_movement = player_rect.copy()
    
    if keys[pygame.K_LEFT]:
        player_movement.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_movement.x += player_speed
    
    # Apply gravity
    player_vel_y += gravity
    player_movement.y += player_vel_y
    
    # Horizontal collision detection
    for platform in platforms:
        if player_movement.colliderect(platform):
            if player_rect.bottom > platform.top and player_rect.top < platform.bottom:  # Side collision check
                if player_movement.right > platform.left and player_rect.left < platform.left:
                    player_movement.right = platform.left
                elif player_movement.left < platform.right and player_rect.right > platform.right:
                    player_movement.left = platform.right
    
    player_rect.x = player_movement.x  # Apply horizontal movement
    
    # Vertical collision detection
    on_ground = False
    for platform in platforms:
        if player_movement.colliderect(platform):
            # Landing on top of a platform
            if player_vel_y > 0 and player_rect.bottom <= platform.top + player_vel_y:
                player_rect.bottom = platform.top
                player_vel_y = 0
                on_ground = True
            # Hitting the underside of a platform
            elif player_vel_y < 0 and player_rect.top >= platform.bottom + player_vel_y:
                player_rect.top = platform.bottom
                player_vel_y = 0
            break
    else:
        player_rect.y = player_movement.y  # Apply vertical movement
    
    # Reset position if player falls off the screen
    if player_rect.top > HEIGHT:
        player_rect.x = WIDTH // 2
        player_rect.y = HEIGHT // 2
        player_vel_y = 0
    
    # Jumping
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = -10
         
    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)
    
    # Draw player
    pygame.draw.rect(screen, BLUE, player_rect)
    
    pygame.display.flip()
    pygame.time.delay(30)
    
pygame.quit()
