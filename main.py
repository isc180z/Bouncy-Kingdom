import pygame
from math import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True
dt = 0

### main menu characteristic
Queen = 1
pointer = 0


### game setup
lives = 3
g = 2     # Gravity
jumping = False
fond = pygame.transform.scale(pygame.image.load("643.jpg"),(1000,667))
screen.blit(fond,(0,0))
player = pygame.image.load("standinggirlcropped.png")
playerboi = pygame.image.load("Standing.png")
playerweight = 50
playerboiweight = 100


keys = pygame.key.get_pressed()
posx = 0
posy = 0
rightfacing = 1

#jump setup
verstr = 0
horstr = 0
velx = 0
vely = 0

# coordinates
player_pos = [screen.get_width() // 2 + posx, screen.get_height() // 2 + posy]
center_player_coord = [screen.get_width() // 2 + player.get_width() // 2 + posx,
                       screen.get_height() // 2 + player.get_height() // 2 + posy]

# gameplay practicality 
delay = 0
#    if delay > 0:
#        delay-=1

def main_menu():
    pygame.display.set_caption("Menu") 


    running = True
    pointer = 0


    while running:
        keys = pygame.key.get_pressed()
        menu_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(fond, (0, 0))

        colorabove = (50,230,60)
        colorright = (50,230,60)
        colorbelow = (50,230,60)
        colorleft = (50,230,60)

        playbutton = 
        girlchoice = 
        boychoice =
        options = 

        if keys[pygame.K_UP]:
            pointer = 1
        if keys[pygame.K_RIGHT]:
            pointer = 2
        if keys[pygame.K_DOWN]:
            pointer = 3
        if keys[pygame.K_LEFT]:
            pointer = 4


        if pointer == 1:
            colorabove = (50,150,60)
            playbutton = 
        elif pointer == 2:
            colorright = (50,150,60)
            girlchoice = 
        elif pointer == 3:
            colorbelow = (50,150,60)
            boychoice = 
        elif pointer == 4:
            colorleft = (50,150,60)
            options =

        pygame.draw.rect(screen,"blue",(screen.get_width() // 2,screen.get_height() // 2,50,50))
        pygame.draw.rect(screen,colorabove,(screen.get_width() // 2,screen.get_height() // 2 - 50,50,50))
        pygame.draw.rect(screen,colorright,(screen.get_width() // 2 +50,screen.get_height() // 2,50,50))
        pygame.draw.rect(screen,colorbelow,(screen.get_width() // 2,screen.get_height() // 2 + 50,50,50))
        pygame.draw.rect(screen,colorleft,(screen.get_width() // 2 - 50,screen.get_height() // 2,50,50))



        pygame.display.flip()


main_menu()

running = True

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
    playerboi_pos = [0,0]
    player_pos = [screen.get_width() // 2 + posx, screen.get_height() // 2 + posy]
    center_player_coord = [screen.get_width() // 2 + player.get_width() // 2 + posx,
                           screen.get_height() // 2 + player.get_height() // 2 + posy]
###update speeds
    velx = velx*0.9
    if vely != 0:
        vely += g


###update position
    posx += velx
    posy += vely


###show character
    screen.blit(player, dest = player_pos)
    screen.blit(playerboi, dest = playerboi_pos)

    pygame.draw.circle(screen, "green", center_player_coord, 5)

    if player_pos[1] < screen.get_height() // 2:
        print(player_pos)
        print(screen.get_height() // 2 )
        vely = 0

    if player_pos[1] == 300:
        running = False
        screen.blit(player, dest=player_pos)

###Floor
    pygame.draw.rect(screen, "red", (0, player_pos[1]+player.get_height(), 2500, 4))

    if horstr > 0 or verstr > 0:
        pygame.draw.line(screen,"brown",(center_player_coord),(center_player_coord[0]-horstr,center_player_coord[1]-verstr),4)

###Horizontal jump

    if keys[pygame.K_c]:
        horstr += 50 * dt * rightfacing



###Vertical jump
    if keys[pygame.K_v]:
        verstr += 50 * dt

    if keys[pygame.K_r]:
        verstr = 0
        horstr = 0

    if keys[pygame.K_SPACE]:
        vely -= verstr
        velx -= horstr
        horstr = 0
        verstr = 0


    if keys[pygame.K_LEFT] and delay == 0:
        horstr = abs(horstr)
        rightfacing = 1

    if keys[pygame.K_RIGHT] and delay == 0:
        horstr = -abs(horstr)
        rightfacing = -1
        


    #if keys[pygame.K_UP]:
    #    posy -= 300 * dt
    #if keys[pygame.K_DOWN] and player_pos[1] <= screen.get_height() // 2:
    #    posy += 300 * dt
    #if keys[pygame.K_LEFT]:
    #    posx -= 300 * dt
    #if keys[pygame.K_RIGHT]:
    #    posx += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    dt = clock.tick(60) / 1000

    pygame.draw
pygame.quit()