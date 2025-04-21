import pygame
from math import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True
dt = 0

# game setup
lives = 3
jump_strength = 0
fond = pygame.image.load("643.jpg")
player = pygame.image.load("standinggirlcropped.png.png")
keys = pygame.key.get_pressed()
posx = 0
posy = 0

#jump setup
vert_jump = 0
vertstr = 0
horstr = 0
velx = 0
vely = 0

# coordinates
player_pos = [screen.get_width() // 2 + posx, screen.get_height() // 2 + posy]
center_player_coord = [screen.get_width() // 2 + player.get_width() // 2 + posx,
                       screen.get_height() // 2 + player.get_height() // 2 + posy]

while running:
    keys = pygame.key.get_pressed()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(fond, (0, 0))
    player_pos = [screen.get_width() // 2 + posx, screen.get_height() // 2 + posy]
    center_player_coord = [screen.get_width() // 2 + player.get_width() // 2 + posx,
                           screen.get_height() // 2 + player.get_height() // 2 + posy]

    screen.blit(player, dest = player_pos)
    pygame.draw.circle(screen, "green", center_player_coord, 5)

    if player_pos[1] <= screen.get_height() // 2:
        posy += 100 * dt

    if player_pos[1] == 300:
        running = False
        screen.blit(player, dest=player_pos)



    if vertstr > 0:
        pygame.draw.rect(screen, "red", (player_pos[0], player_pos[1] - jump_strength, 20, jump_strength))

    if keys[pygame.K_g]:
        vertstr += 100 * dt

    if not keys[pygame.K_g]:
        posy -= vertstr
        vertstr = 0

    if keys[pygame.K_g]:
        pygame.draw.circle(screen, "blue", (player_pos[0], player_pos[1]-vertstr),5)



    if jump_strength > 0:
        pygame.draw.rect(screen, "blue", (player_pos[0], player_pos[1] - jump_strength, 20, jump_strength))

    if keys[pygame.K_SPACE]:
        jump_strength += 100 * dt

    if not keys[pygame.K_SPACE]:
        posy -= jump_strength
        jump_strength = 0


    if keys[pygame.K_UP]:
        posy -= 300 * dt
    if keys[pygame.K_DOWN] and player_pos[1] <= screen.get_height() // 2:
        posy += 300 * dt
    if keys[pygame.K_LEFT]:
        posx -= 300 * dt
    if keys[pygame.K_RIGHT]:
        posx += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    dt = clock.tick(60) / 1000

    pygame.draw
pygame.quit()