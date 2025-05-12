import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Obtenir les dimensions de l'écran de l'utilisateur
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
background= pygame.transform.scale(pygame.image.load("643.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Définir la fenêtre en plein écran avec les dimensions de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de Plateforme")
clock = pygame.time.Clock()

# Couleurs
BACKGROUND_COLOR= (20,20,20)
PLAYER_COLOR = (255, 150, 100)
PLATFORM_COLOR = (180, 180, 180)
MOVING_PLATFORM_COLOR = (100, 180, 255)
TEXT_COLOR = (215, 215, 215)
FLOATING_TEXT_COLOR = (0, 255, 0)

# Joueur
player_radius = 20
player_pos = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
player_vel = pygame.Vector2(0, 0)
can_jump = False

# Gravité
gravity = 900

# Ensemble pour suivre les plateformes déjà visitées
visited_platforms = set()

# Compteur de victoires
wins = 0

# Liste pour les textes flottants
floating_texts = []

# Niveaux
class Level:
    def __init__(self, platform_count, vertical_spacing, mobile_indices):
        self.platform_count = platform_count
        self.vertical_spacing = vertical_spacing
        self.mobile_indices = mobile_indices
        self.generate_platforms()

    def generate_platforms(self):
        self.platforms = []
        self.moving_platforms = {}
        y = SCREEN_HEIGHT - 100
        last_x = SCREEN_WIDTH // 2
        for i in range(self.platform_count):
            width = random.randint(100, 200)
            while True:
                x_offset = random.randint(-300, 300)
                new_x = max(0, min(SCREEN_WIDTH - width, last_x + x_offset))
                overlap = any(abs(new_x - plat.x) < 80 and abs(y - plat.y) < 40 for plat in self.platforms)
                if not overlap:
                    break
            plat = pygame.Rect(new_x, y, width, 20)
            self.platforms.append(plat)
            if i in self.mobile_indices:
                self.moving_platforms[i] = [100, 1]  # Vitesse et direction
            last_x = new_x
            y -= self.vertical_spacing
        # Ajouter une plateforme de départ
        self.platforms.insert(0, pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 20))

    def update_moving_platforms(self, dt):
        for idx, (speed, direction) in self.moving_platforms.items():
            plat = self.platforms[idx]
            plat.x += speed * direction * dt
            if plat.left < 0 or plat.right > SCREEN_WIDTH:
                self.moving_platforms[idx][1] *= -1

# Définir les niveaux
levels = [
    Level(10, 120, []),  # Niveau 1 : 10 plateformes fixes
    Level(15, 120, [2, 5, 8]),  # Niveau 2 : 15 plateformes, certaines mobiles
    Level(20, 120, list(range(20)))  # Niveau 3 : 20 plateformes, toutes mobiles
]
current_level_index = 0
current_level = levels[current_level_index]
platforms_reached = 0
required_platforms = [8, 8, 8]
game_over = False

# Police pour le texte
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y, color=TEXT_COLOR):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_controls():
    controls_text = [
        "Commandes:",
        "<- : Aller à gauche",
        "-> : Aller à droite",
        "Espace : Sauter",
        "Échap or ALT + F4 : Quitter le jeu"
    ]
    for i, line in enumerate(controls_text):
        draw_text(line, 10, SCREEN_HEIGHT - 150 + i * 30)

class FloatingText:
    def __init__(self, text, position, color, duration=1.0):
        self.text = text
        self.position = position
        self.color = color
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def draw(self, surface):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        if elapsed_time < self.duration:
            font = pygame.font.SysFont(None, 36)
            text_surface = font.render(self.text, True, self.color)
            surface.blit(text_surface, (self.position.x + 30, self.position.y - 30))
            return True
        return False

def plateforme_collision(position, velocity, radius):
    global can_jump, platforms_reached, visited_platforms, floating_texts
    rect = pygame.Rect(position.x - radius, position.y - radius, radius * 2, radius * 2)
    for idx, plat in enumerate(current_level.platforms):
        if rect.colliderect(plat):
            if velocity.y >= 0 and position.y < plat.top and plat.left + 5 < position.x < plat.right - 5:
                position.y = plat.top - radius
                velocity.y = -velocity.y * 0.5  # Rebond
                can_jump = True
                if idx not in visited_platforms:
                    visited_platforms.add(idx)
                    platforms_reached += 1
                    floating_texts.append(FloatingText("+1", position.copy(), FLOATING_TEXT_COLOR))
                if idx in current_level.moving_platforms:
                    current_level.moving_platforms[idx][0] = 0
            else:
                if position.x < plat.left:
                    position.x = plat.left - radius
                    velocity.x = 0
                elif position.x > plat.right:
                    position.x = plat.right + radius
                    velocity.x = 0
                elif position.y > plat.bottom:
                    position.y = plat.bottom + radius
                    velocity.y = 0
    return position, velocity

def check_level_completion():
    global current_level_index, current_level, platforms_reached, player_pos, player_vel, can_jump, game_over, visited_platforms, wins
    if platforms_reached >= required_platforms[current_level_index]:
        if current_level_index + 1 < len(levels):
            current_level_index += 1
            current_level = levels[current_level_index]
            platforms_reached = 0
            visited_platforms = set()
            player_pos.update(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
            player_vel.update(0, 0)
            can_jump = False
        else:
            wins += 1
            show_end_screen("Vous avez gagné !")

def show_end_screen(message):
    global current_level_index, current_level, platforms_reached, player_pos, player_vel, can_jump, visited_platforms, game_over, floating_texts
    screen.fill(BACKGROUND_COLOR)
    draw_text(message, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60)
    draw_text("Appuyez sur R pour rejouer ou Échap pour quitter", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    # Réinitialiser le jeu
                    current_level_index = 0
                    current_level = Level(
                        current_level.platform_count,
                        current_level.vertical_spacing,
                        current_level.mobile_indices
                    )
                    platforms_reached = 0
                    visited_platforms = set()
                    player_pos.update(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
                    player_vel.update(0, 0)
                    can_jump = False
                    game_over = False
                    floating_texts.clear()
                    waiting = False

# Boucle principale
running = True
while running:
    dt = clock.tick(60) / 1000  # Durée d'une frame en secondes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and can_jump:
                player_vel.y = -500  # Hauteur de saut ajustée
                can_jump = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel.x = -300
    elif keys[pygame.K_RIGHT]:
        player_vel.x = 300
    else:
        player_vel.x = 0

    player_vel.y += gravity * dt
    player_pos += player_vel * dt
    player_pos, player_vel = plateforme_collision(player_pos, player_vel, player_radius)

    current_level.update_moving_platforms(dt)
    check_level_completion()
    if player_pos.y - player_radius > SCREEN_HEIGHT:
        show_end_screen("Game Over ! Voulez-vous rejouer ?")

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, PLAYER_COLOR, (int(player_pos.x), int(player_pos.y)), player_radius)
    for idx, plat in enumerate(current_level.platforms):
        color = MOVING_PLATFORM_COLOR if idx in current_level.moving_platforms else PLATFORM_COLOR
        pygame.draw.rect(screen, color, plat)

    # Afficher les textes flottants
    for text in floating_texts[:]:
        if not text.draw(screen):
            floating_texts.remove(text)

    # Afficher les informations du jeu
    draw_text(f"Niveau: {current_level_index + 1}", 10, 10)
    draw_text(f"Plateformes atteintes: {platforms_reached}/{required_platforms[current_level_index]}", 10, 40)
    draw_text(f"Wins: {wins}", 10, 70)

    # Afficher les commandes
    draw_controls()

    pygame.display.flip()


pygame.quit()