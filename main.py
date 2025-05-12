import pygame
from math import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
dt = 0
fond = pygame.transform.scale(pygame.image.load("643.jpg"),(screen.get_width(),screen.get_height()))

def how_to_play():
    running = True
    screen.blit(fond, (0, 0))
    black = (0, 0, 0)
    keys = pygame.key.get_pressed()
    pygame.display.set_caption("Bouncy Kingdom")
    myfont = pygame.font.SysFont("Arial", 50,True)

    while running:
        labelC = myfont.render("Press C to increase horizontal strength", 1, black)
        labelV = myfont.render("Press V to increase vertical strength", 1, black)
        labelR = myfont.render("Press R to reset both strengths", 1, black)
        labelSpace = myfont.render("Press Spacebar to jump", 1, black)

        if keys[pygame.K_ESCAPE]:
            running = False

        screen.blit(labelC, (450, 200))
        screen.blit(labelV, (470, 300))
        screen.blit(labelR, (520, 400))
        screen.blit(labelSpace, (550, 500))

        # show the whole thing
        pygame.display.flip()

        # event loop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit




def game(queen):
    running = True
    clock = pygame.time.Clock()
    dt = 0
    pygame.display.set_caption("Bouncy Kingdom")


    # gameplay practicality 
    delay = 0
    #    if delay > 0:
    #        delay-=1

    ### game setup
    lives = 3
    g = 2     # Gravity
    jumping = False

    # Character selection
    screen.blit(fond,(0,0))
    if queen: 
        player = pygame.transform.scale(pygame.image.load("princesseeeeeeee.png"),(60,100))
        playerweight = 80
    else :
        player = pygame.transform.scale(pygame.image.load("Prince_png.png"),(50,100))
        playerweight = 100


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


    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_ESCAPE]:
            running = False


        screen.blit(fond, (0, 0))

        player_pos = [screen.get_width() // 2 + posx, screen.get_height() // 2 + posy]
        center_player_coord = [screen.get_width() // 2 + player.get_width() // 2 + posx,
                            screen.get_height() // 2 + player.get_height() // 2 + posy]
    ###update speeds
        velx = velx*0.8
        if vely != 0:
            vely += g


    ###update position
        posx += velx
        posy += vely


    ###show character
        screen.blit(player, dest = player_pos)


        if player_pos[1] < screen.get_height() // 2:
            print(player_pos)
            print(screen.get_height() // 2 )
            vely = 0

        if player_pos[1] == 300:
            running = False
            screen.blit(player, dest=player_pos)

    ###Floor
        pygame.draw.rect(screen, "red", (0, player_pos[1]+player.get_height(), 2500, 4))

        if horstr != 0 or verstr != 0:
            pygame.draw.line(screen,"brown",(center_player_coord),(center_player_coord[0]-horstr/1000,center_player_coord[1]-verstr/1000),4)

    ###Horizontal jump

        if keys[pygame.K_c]:
            horstr += 100000 * dt * rightfacing



    ###Vertical jump
        if keys[pygame.K_v]:
            verstr += 100000 * dt

        if keys[pygame.K_r]:
            verstr = 0
            horstr = 0

        if keys[pygame.K_SPACE]:
            vely -= sqrt(2*verstr/playerweight)
            if horstr < 0:
                velx -= -sqrt(2*abs(horstr)/playerweight) 
            else:
                velx -= sqrt(2*horstr/playerweight) 
            horstr = 0
            verstr = 0


        if keys[pygame.K_LEFT] and delay == 0:
            horstr = abs(horstr)
            rightfacing = 1

        if keys[pygame.K_RIGHT] and delay == 0:
            horstr = -abs(horstr)
            rightfacing = -1
            


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






def main_menu():
    pygame.display.set_caption("Bouncy Kingdom")
    running = True
    Queen = 1
    pointer = 0
    playbutton = pygame.image.load("Play_pas_appuye_DECOUPE.png")
    girldisplay = pygame.image.load("princesseeeeeeee.png")
    girlsize = 1
    boydisplay =pygame.image.load("Prince_png.png")
    boysize = 1
    options = pygame.image.load("rouage_a_decouper.png")

    while running:
        global game
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


        playbutton = pygame.image.load("Play_pas_appuye_DECOUPE.png")
        girldisplay = pygame.image.load("princesseeeeeeee.png")
        boydisplay =pygame.image.load("Prince_png.png")
        options = pygame.image.load("rouage_a_decouper.png")
        options_size = (240,240)


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
            playbutton = pygame.image.load("play_appuye_DECOUPE.png")
            if keys[pygame.K_SPACE]:
                game(Queen)

        elif pointer == 2:
            colorright = (50,150,60)
            girldisplay = pygame.transform.grayscale(girldisplay)
            if keys[pygame.K_SPACE]:
                Queen = 0
                girlsize = 1
                boysize = 1.2

        elif pointer == 3:
            colorbelow = (50,150,60)
            options_size = (280,280)
            if keys[pygame.K_SPACE]:
                how_to_play( )


        elif pointer == 4:
            colorleft = (50,150,60)
            boydisplay = pygame.transform.grayscale(boydisplay)
            if keys[pygame.K_SPACE]:
                Queen = 1
                boysize = 1
                girlsize = 1.2
        


        
        screen.blit(pygame.transform.scale(playbutton,(600,240)),dest=(screen.get_width()//2-1.2*playbutton.get_width()//2,30))
        screen.blit(pygame.transform.scale(options,(options_size)),dest=(screen.get_width()//2-options_size[0]//2,screen.get_height()-options.get_height()))
        screen.blit(pygame.transform.scale_by(girldisplay,girlsize),dest=(30,screen.get_height()//3))
        screen.blit(pygame.transform.scale_by(boydisplay,boysize),dest=(screen.get_width()-boydisplay.get_width()-30,screen.get_height()//3))


        pygame.draw.rect(screen,"blue",(screen.get_width() // 2,screen.get_height() // 2,50,50))
        pygame.draw.rect(screen,colorabove,(screen.get_width() // 2,screen.get_height() // 2 - 50,50,50))
        pygame.draw.rect(screen,colorright,(screen.get_width() // 2 +50,screen.get_height() // 2,50,50))
        pygame.draw.rect(screen,colorbelow,(screen.get_width() // 2,screen.get_height() // 2 + 50,50,50))
        pygame.draw.rect(screen,colorleft,(screen.get_width() // 2 - 50,screen.get_height() // 2,50,50))



        pygame.display.flip()


main_menu()
game()


pygame.quit()