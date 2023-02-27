import pygame
import random
import os

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

# Set up the font
FONT = pygame.font.SysFont(None, 30)

# Set up the button
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_COLOR = (255, 255, 255)
BUTTON_TEXT_COLOR = BLACK
BUTTON_TEXT = "Add More"
BUTTON_X = WIDTH // 2 - BUTTON_WIDTH // 2
BUTTON_Y = 10

# Load the logos
LOGO_IMAGES = [os.path.join("assets", f"dvdlogo-0{i}.svg") for i in range(1, 9)]
LOGOS = [pygame.image.load(image).convert_alpha() for image in LOGO_IMAGES]
LOGO_RECT = LOGOS[0].get_rect()
LOGO_SPEED_X = 5
LOGO_SPEED_Y = 5

# Set up the logo list
LOGO_LIST = []

# Set up the maximum number of logos
MAX_LOGOS = 64

# Load the background music
pygame.mixer.music.load("assets/リサフランク420.wav")
pygame.mixer.music.play(-1)  # -1 loops the music

# Set up the game loop
running = True
logo_index = 0
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
    SCREEN.fill(BLACK)

    # Draw the button
    pygame.draw.rect(SCREEN, BUTTON_COLOR, (BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
    button_text = FONT.render(BUTTON_TEXT, True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT // 2))
    SCREEN.blit(button_text, button_text_rect)

    # Draw the logos
    for logo in LOGO_LIST:
        SCREEN.blit(LOGOS[logo[4]], (logo[0], logo[1]))
        logo[0] += logo[2]
        logo[1] += logo[3]
        if logo[0] < 0 or logo[0] + LOGO_RECT.width > WIDTH:
            logo[2] = -logo[2]
        if logo[1] < 0 or logo[1] + LOGO_RECT.height > HEIGHT:
            logo[3] = -logo[3]

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    CLOCK.tick(60)

# Quit pygame
pygame.quit()

