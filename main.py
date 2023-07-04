import pygame
pygame.init()
pygame.font.init()

# Create solution for the screen
WIDTH = 1000
HEIGHT = 800

# Set Frame Per Second for the main
FPS = 60

# Set solution for the screen
full_screen = pygame.FULLSCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT), full_screen)

# Set caption for the screen
pygame.display.set_caption("Pong")

# Draw a white line in the middle of the screen
def draw_line():
    line_thickness = 12
    pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), line_thickness)

# Insert image
player = pygame.image.load("player.png")
player_rect = player.get_rect()
player_rect.x = 0
player_rect.y = HEIGHT // 2 - player_rect.height // 2

computer = pygame.image.load("computer.png")
computer_rect = computer.get_rect()
computer_rect.x = 980
computer_rect.y = HEIGHT // 2 - computer_rect.height // 2

ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
ball_rect.x = WIDTH / 2
ball_rect.y = HEIGHT / 2
x_speed, y_speed = 5,9

# Insert sounds
lose_sound = pygame.mixer.Sound("lose.wav")
paddles_sound = pygame.mixer.Sound("paddles.wav")
wall_sound = pygame.mixer.Sound("wall.wav")

# Draw font
FONT = pygame.font.SysFont("Bahnschrift", 150)
score = 0
score_01 = 0

# Draw the screen
def draw():
    screen.fill((0, 0, 0))
    draw_line()
    score_text = FONT.render(str(score), 1, "white")
    score_text_01 = FONT.render(str(score_01), 1, "white")
    screen.blit(score_text, (WIDTH / 2 - 115, 10))
    screen.blit(score_text_01, (WIDTH / 2 + 35, 10))
    screen.blit(player, player_rect)
    screen.blit(computer, computer_rect)
    screen.blit(ball, ball_rect)
    pygame.display.update()

# Bouncing ball
def bouncing_ball():
    global x_speed, y_speed
    ball_rect.x += x_speed
    ball_rect.y += y_speed
    

    # Collisons with screen borders
    if ball_rect.bottom >= HEIGHT or ball_rect.top <= 0:
        y_speed *= -1

# Core of the game
def main():
    global x_speed, y_speed, score, score_01
    clock = pygame.time.Clock()  # Set the fast of the main
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        # Create movement for paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if computer_rect.y > 0:
                computer_rect.y -= 5
        if keys[pygame.K_DOWN]:
            if computer_rect.y < HEIGHT - computer_rect.height:
                computer_rect.y += 5
        if keys[pygame.K_w]:
            if player_rect.y > 0:
                player_rect.y -= 5
        if keys[pygame.K_s]:
            if player_rect.y < HEIGHT - player_rect.height:
                player_rect.y += 5
        bouncing_ball()

        if player_rect.colliderect(ball_rect) or computer_rect.colliderect(ball_rect):
            x_speed *= -1
            paddles_sound.play()
        if ball_rect.x > WIDTH:
            ball_rect.x = WIDTH / 2
            ball_rect.y = HEIGHT / 2
            ball_rect.x += x_speed
            ball_rect.y += y_speed
            score = score + 1
            lose_sound.play()
        if ball_rect.x < 0:
            ball_rect.x = WIDTH / 2
            ball_rect.y = HEIGHT / 2
            ball_rect.x += x_speed
            ball_rect.y += y_speed
            score_01 = score_01 + 1
            lose_sound.play()
            

        draw()

    pygame.quit()
    quit()

# Check if the program run directly
if __name__ == "__main__":
    main()
