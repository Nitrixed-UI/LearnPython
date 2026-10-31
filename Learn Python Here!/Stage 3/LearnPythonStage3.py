# -------- STAGE 3: Pygame Pong Example --------
# This project introduces basic Pygame concepts such as rendering, collision detection,
# and handling user input to create an interactive Pong game with a CPU opponent.

import pygame
import sys
from pygame.locals import QUIT
import random

# --- WINDOW SETTINGS ---
WIDTH, HEIGHT = 800, 500        # Window resolution
FPS = 120                        # Frames per second (controls speed consistency)

# --- OBJECT SETTINGS ---
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 12
PLAYER_SPEED = 10
CPU_MAX_SPEED = 9               # CPU paddle max speed per frame
BALL_SPEED = 2                  # Initial ball speed
MAX_BALL_SPEED = PADDLE_WIDTH + BALL_SIZE - 1  # Hard limit for ball velocity (any faster and it can jump past a paddle in one frame)
SPEED_INCREMENT = 1.0           # Ball speed increase after each paddle hit

# Initialize pygame modules
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - CPU")
clock = pygame.time.Clock()     # Controls frame rate
font = pygame.font.SysFont(None, 48)  # Font for score display

# --- GAME OBJECTS ---
# Player paddle (left), CPU paddle (right), Ball (center)
player = pygame.Rect(20, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
cpu = pygame.Rect(WIDTH - 20 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect((WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)

# Ball velocity components (x, y)
# Starts in a random direction for both axes
ball_vel = [float(BALL_SPEED * random.choice((1, -1))),
            float(BALL_SPEED * random.choice((1, -1)))]

# Player and CPU scores
score_player = 0
score_cpu = 0

# --- FUNCTION: Reset ball after a point ---
def reset_ball(serving_to_player=True):
    """Repositions the ball in the center and serves it in the correct direction."""
    ball.center = (WIDTH // 2, HEIGHT // 2)
    dir_x = -1 if serving_to_player else 1  # Serve direction (player is on the left)
    dir_y = random.choice((1, -1))          # Random vertical direction
    ball_vel[0] = BALL_SPEED * dir_x
    ball_vel[1] = BALL_SPEED * dir_y

# --- FUNCTION: Adjust ball velocity after paddle collision ---
def set_ball_speed_after_hit(paddle):
    """Increases ball speed slightly and adjusts its reflection angle based on hit position."""
    current_speed = (ball_vel[0] ** 2 + ball_vel[1] ** 2) ** 0.5  # Magnitude of velocity
    new_speed = min(MAX_BALL_SPEED, current_speed + SPEED_INCREMENT)

    # Calculate offset: how far from paddle center the ball hit (-1.0 to +1.0)
    offset = (ball.centery - paddle.centery) / (PADDLE_HEIGHT / 2)
    offset = max(-1, min(1, offset))  # Clamp offset within range

    # Determine horizontal direction (depends on which paddle was hit)
    x_dir = 1 if paddle is player else -1

    # Compute vertical velocity from offset
    vy = new_speed * offset
    # Calculate horizontal component to maintain total speed
    vx_sq = max(0.0, new_speed**2 - vy**2)
    vx = (vx_sq ** 0.5) * x_dir

    # Prevent vx from becoming too small (avoid near-vertical bounces)
    # The ball moves int(vx) pixels per frame, so below 1 it would stop moving sideways
    if abs(vx) < 1:
        vx = 1.0 * x_dir
        vy = (max(0.0, new_speed**2 - vx**2) ** 0.5) * (1 if vy >= 0 else -1)

    # Apply new velocity
    ball_vel[0], ball_vel[1] = vx, vy

# --- FUNCTION: Draw everything on screen ---
def draw():
    """Renders all visual elements: background, paddles, ball, and score."""
    screen.fill((0, 0, 0))  # Clear screen to black

    # Draw dashed middle line
    for y in range(0, HEIGHT, 20):
        if (y // 20) % 2 == 0:
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH // 2 - 1, y, 2, 10))

    # Draw paddles and ball
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), cpu)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    # Render and draw scores
    sp = font.render(str(score_player), True, (200, 200, 200))
    sc = font.render(str(score_cpu), True, (200, 200, 200))
    screen.blit(sp, (WIDTH // 4 - sp.get_width() // 2, 20))
    screen.blit(sc, (3 * WIDTH // 4 - sc.get_width() // 2, 20))

    pygame.display.flip()  # Update the full display

# --- MAIN GAME LOOP ---
running = True
while running:
    dt = clock.tick(FPS)  # Wait to maintain consistent FPS

    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- PLAYER INPUT ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED
    player.y = max(0, min(HEIGHT - PADDLE_HEIGHT, player.y))  # Keep player in window

    # --- CPU MOVEMENT ---
    # CPU moves toward ball, limited by CPU_MAX_SPEED for difficulty balance
    if cpu.centery < ball.centery - 6:
        cpu.y += min(CPU_MAX_SPEED, ball.centery - cpu.centery)
    elif cpu.centery > ball.centery + 6:
        cpu.y -= min(CPU_MAX_SPEED, cpu.centery - ball.centery)
    cpu.y = max(0, min(HEIGHT - PADDLE_HEIGHT, cpu.y))

    # --- BALL MOVEMENT ---
    ball.x += int(ball_vel[0])
    ball.y += int(ball_vel[1])

    # --- WALL COLLISIONS (Top & Bottom) ---
    if ball.top <= 0:
        ball.top = 0
        ball_vel[1] = -ball_vel[1]
    if ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT
        ball_vel[1] = -ball_vel[1]

    # --- PADDLE COLLISIONS ---
    if ball.colliderect(player) and ball_vel[0] < 0:
        ball.left = player.right
        set_ball_speed_after_hit(player)
    if ball.colliderect(cpu) and ball_vel[0] > 0:
        ball.right = cpu.left
        set_ball_speed_after_hit(cpu)

    # --- SCORING ---
    if ball.left <= 0:                # CPU scores
        score_cpu += 1
        reset_ball(serving_to_player=True)
    if ball.right >= WIDTH:           # Player scores
        score_player += 1
        reset_ball(serving_to_player=False)

    # --- RENDER FRAME ---
    draw()

# --- EXIT ---
pygame.quit()
sys.exit()

# This concludes the real-world example of Pygame.
# Future Stages may cover more advanced topics like sound, animations, and complex game mechanics. 
# For now, thank you for following along!

# Happy Coding!