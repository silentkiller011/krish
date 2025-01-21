import pygame
import sys
import random

pygame.init()

# -------------------------------------------------------
# 1. GLOBAL SETTINGS & WINDOW CONFIG
# -------------------------------------------------------
WIDTH, HEIGHT = 600, 400  # Window dimensions in pixels
FPS = 60  # Frames per second (game speed)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My PyGame C.A Project")

# Defines color in form of (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# A "clock" to manage frame rate
clock = pygame.time.Clock()

# -------------------------------------------------------
# 2. LOAD ASSETS (Images, Sounds, Fonts, etc.)
# -------------------------------------------------------

# Placeholder image for player(40x40 green square)
player_img = pygame.Surface((40, 40))
player_img.fill((0, 255, 0))  # Fill with green

# Placeholder image for enemies (30x30 red square)
enemy_img = pygame.Surface((30, 30))
enemy_img.fill((255, 0, 0))  # Fill with red

# Placeholder background (entire screen size, filled with bluish color)
background_img = pygame.Surface((WIDTH, HEIGHT))
background_img.fill((100, 100, 255))

font = pygame.font.SysFont("Arial", 24)

# Heart Images
heart_full = pygame.image.load("heart_full.jpg").convert_alpha()
heart_broken = pygame.image.load("heart_broken.jpg").convert_alpha()

# Animation 
heart_state = "full"
heart_break_timer = 0
HEART_BREAK_DURATION = 30

# Sound Effects
pygame.mixer.init()
life_lost_sound = pygame.mixer.Sound("life_lost.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
life_pickup_sound = pygame.mixer.Sound("life_pickup.wav")

# Background Music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.5)

# High Score File
HIGH_SCORE_FILE = "high_score.txt"

# High Score
def load_high_score():
    """Loads the high score from the file, or returns 0 if not found."""
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

# Saves The High Score 
def save_high_score(score):
    """Saves the high score to the file."""
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

high_score = load_high_score()

# -------------------------------------------------------
# 3. GAME STATES
# -------------------------------------------------------
# using inytergers to label different screens/states:
START = 0  # Start screen before the game begins
PLAYING = 1  # Main gameplay
GAME_OVER = 2  # Game over screen after losing

game_state = START

# -------------------------------------------------------
# 4. GAME VARIABLES
# -------------------------------------------------------
# Player position in the middle of the screen
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 4  # Movement speed of the player
player_health = 3  # How many hits the player can take
MAX_HEALTH = 5  # Max number of lives
score = 0  # The player's score

# Store enemies in a list of [x_position, y_position]
enemies = []

# Define a custom event for periodically spawning enemies
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
# Trigger this event every 2000ms (2 second)
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 2000)
# Player Sprite Class 
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > 0:
            self.rect.y -= self.speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed
        
        ''' the above code is about the movement of the player/box in the game it using the arror keys 
            or WASD keys to move the player/box in the game'''

# Life Sprite Class
class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = heart_full
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 5000  # Life will stay for 5 seconds

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > self.duration:
            self.kill()  # Remove the life from all groups

# Create player instance
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create a sprite group for lives
lives = pygame.sprite.Group()

# spawns lives
LIFE_SPAWN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(LIFE_SPAWN_EVENT, 10000)  # Trigger every 10 seconds

# -------------------------------------------------------
# 5. HELPER FUNCTIONS
# -------------------------------------------------------
def reset_game():
    """
    Resets the game's variables to their initial state.
    Useful for restarting the game.
    """
    global player_x, player_y, player_health, score, enemies, heart_state, all_sprites, player
    player_x = WIDTH // 2
    player_y = HEIGHT // 2
    player_health = 3
    score = 0
    enemies = []
    heart_state = "full"
    lives.empty()

    # Reset and add player to sprite groups
    all_sprites.empty()
    player = Player(player_x, player_y)
    all_sprites.add(player)

def draw_text(text, x, y, color=WHITE):
    """
    Renders the specified text at (x, y) on the screen in the given color.
    """
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (x, y))

# -------------------------------------------------------
# 6. MAIN GAME LOOP
# -------------------------------------------------------
running = True

while running:
    clock.tick(FPS)

    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == ENEMY_SPAWN_EVENT and game_state == PLAYING:
            ex = random.randint(0, WIDTH - 30)
            ey = -20
            enemies.append([ex, ey])

        if event.type == pygame.KEYDOWN:
            if game_state == START:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    game_state = PLAYING
                    reset_game()
            elif game_state == GAME_OVER:
                if event.key == pygame.K_r:
                    game_state = START

        if event.type == LIFE_SPAWN_EVENT and game_state == PLAYING:
            x = random.randint(0, WIDTH - heart_full.get_width())
            y = random.randint(0, HEIGHT - heart_full.get_height())
            life = Life(x, y)
            lives.add(life)

    if game_state == START:
        draw_text("WELCOME TO THE GAME!", 150, 100)
        draw_text("Press [SPACE/ENTER] to Start", 130, 150)
        draw_text("Use arrow keys to move. Avoid enemies!", 80, 200)
        draw_text("Collect points - Survive!", 190, 230)

    elif game_state == PLAYING:
        pygame.mixer.music.play(1)

        # Update enemy positions
        for e in enemies:
            e[1] += 2
            if e[1] > HEIGHT:
                e[1] = -30
                e[0] = random.randint(0, WIDTH - 30)
                score += 1

        # Check for collisions between player and enemies
        for e in enemies:
            if player.rect.colliderect(pygame.Rect(e[0], e[1], enemy_img.get_width(), enemy_img.get_height())):
                player_health -= 1
                e[1] = -30
                e[0] = random.randint(0, WIDTH - 30)
                life_lost_sound.play()
                heart_state = "broken"
                heart_break_timer = HEART_BREAK_DURATION
                if player_health <= 0:
                    game_state = GAME_OVER
                    game_over_sound.play()

        # Check for collisions between player and lives
        collisions = pygame.sprite.spritecollide(player, lives, True)
        for life in collisions:
            if player_health < MAX_HEALTH:
                player_health += 1
                life_pickup_sound.play()

        # Update and draw game elements
        all_sprites.update()
        lives.update()
        all_sprites.draw(screen)
        for e in enemies:
            screen.blit(enemy_img, (e[0], e[1]))
        lives.draw(screen)

        # Draw hearts for health
        heart_x = 10
        heart_y = 10
        for i in range(player_health):
            if heart_state == "full":
                screen.blit(heart_full, (heart_x, heart_y))
            elif heart_state == "broken":
                screen.blit(heart_broken, (heart_x, heart_y))
            heart_x += heart_full.get_width() + 5

        if heart_state == "broken":
            heart_break_timer -= 1
            if heart_break_timer <= 0:
                heart_state = "full"

        # Draw score and high score
        draw_text(f"Score: {score}", 10, 40)
        draw_text(f"High Score: {high_score}", 10, 70)

    elif game_state == GAME_OVER:
        pygame.mixer.music.stop()
        draw_text("GAME OVER!", 230, 120)
        draw_text(f"Score: {score}", 250, 160)
        if score > high_score:
            high_score = score
            save_high_score(high_score)
        draw_text(f"High Score: {high_score}", 230, 190)
        draw_text("Press [R] to Restart", 210, 250)

    pygame.display.flip()

pygame.quit()
sys.exit()