import pygame
import random
import os
corners_hit = 0

# Initialize pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
CLOCK = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the font
FONT = pygame.font.SysFont(None, 30)

# Set up the button
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_COLOR = BLACK
BUTTON_TEXT_COLOR = WHITE
BUTTON_TEXT = "Add More"
BUTTON_X = WIDTH // 2 - BUTTON_WIDTH // 2
BUTTON_Y = 10

# Load the logos
LOGO_IMAGES = [os.path.join("assets", f"dvdlogo-0{i}.svg") for i in range(1, 9)]
LOGOS = [pygame.image.load(image).convert_alpha() for image in LOGO_IMAGES]
LOGO_RECT = LOGOS[0].get_rect()
LOGO_SPEED_X = 3 
LOGO_SPEED_Y = 3

# Set up the logo list
LOGO_LIST = []

# Set up the maximum number of logos
MAX_LOGOS = 512

# Load the background image
BACKGROUND = pygame.image.load("assets/background.png").convert()

# Load the background music
pygame.mixer.music.load("assets/リサフランク420.wav")
pygame.mixer.music.play(-1)  # -1 loops the music

# Set up the game loop
running = True
logo_index = 0
score = 0  # Initialize score variable
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(LOGO_LIST) < MAX_LOGOS:
                LOGO_LIST.append([random.randint(0, WIDTH - LOGO_RECT.width),
                                  random.randint(0, HEIGHT - LOGO_RECT.height),
                                  LOGO_SPEED_X,
                                  LOGO_SPEED_Y,
                                  logo_index])
                logo_index = (logo_index + 1) % len(LOGOS)

    # Clear the screen
    SCREEN.blit(BACKGROUND, (0, 0))

    # Draw the button
    pygame.draw.rect(SCREEN, BUTTON_COLOR, (BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
    button_text = FONT.render(BUTTON_TEXT, True, WHITE)
    button_text_rect = button_text.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT // 2))
    SCREEN.blit(button_text, button_text_rect)

    # Draw the logos and update the score
    for logo in LOGO_LIST:
        SCREEN.blit(LOGOS[logo[4]], (logo[0], logo[1]))
        logo[0] += logo[2]
        logo[1] += logo[3]
        if logo[0] < 0 or logo[0] + LOGO_RECT.width > WIDTH:
            logo[2] = -logo[2]
            score += 1  # increment the score when a logo hits a side
        if logo[1] < 0 or logo[1] + LOGO_RECT.height > HEIGHT:
            logo[3] = -logo[3]
            score += 1
	# Draw the logos and update the score
    for logo in LOGO_LIST:
        SCREEN.blit(LOGOS[logo[4]], (logo[0], logo[1]))
        logo[0] += logo[2]
        logo[1] += logo[3]
        if logo[0] < 0 or logo[0] + LOGO_RECT.width > WIDTH:
            logo[2] = -logo[2]
            score += 1  # increment the score when a logo hits a side
        if logo[1] < 0 or logo[1] + LOGO_RECT.height > HEIGHT:
            logo[3] = -logo[3]
            score += 1  # increment the score when a logo hits a side
        if logo[0] < 0 and logo[1] < 0 or logo[0] < 0 and logo[1] + LOGO_RECT.height > HEIGHT \
                or logo[0] + LOGO_RECT.width > WIDTH and logo[1] < 0 \
                or logo[0] + LOGO_RECT.width > WIDTH and logo[1] + LOGO_RECT.height > HEIGHT:
            corners_hit += 1  # increment the corner hit count when a logo hits a corner

    # Draw the score and corner hit count
    score_text = FONT.render(f"Walls Hit: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

    corner_hit_text = FONT.render(f"Corners Hit: {corners_hit}", True, WHITE)
    SCREEN.blit(corner_hit_text, (10, 30))

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    CLOCK.tick(60)

pygame.quit()
