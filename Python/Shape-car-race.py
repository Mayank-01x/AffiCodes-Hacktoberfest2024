import pygame
import time
import random

pygame.init()

# Set display size and colors
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (169, 169, 169)  # Color for the obstacles
wheel_color = (0, 0, 0)  # Wheels will be black

car_width = 50
car_height = 80  # Height increased to give space for wheels

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Simple Car Game')
clock = pygame.time.Clock()


def display_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Score: {count}", True, black)
    gameDisplay.blit(text, (0, 0))


def obstacles(obs_x, obs_y, obs_width, obs_height, color):
    pygame.draw.rect(gameDisplay, color, [obs_x, obs_y, obs_width, obs_height])


def car(x, y):
    # Draw car body as a blue rectangle
    pygame.draw.rect(gameDisplay, blue, [x, y, car_width, car_height])

    # Draw wheels as black circles
    wheel_radius = 10
    wheel_offset_x = 10  # Distance of wheels from car sides
    wheel_offset_y = car_height - wheel_radius  # Distance from top of the car

    # Front wheel
    pygame.draw.circle(gameDisplay, wheel_color, (x + wheel_offset_x, y + wheel_offset_y), wheel_radius)
    # Rear wheel
    pygame.draw.circle(gameDisplay, wheel_color, (x + car_width - wheel_offset_x, y + wheel_offset_y), wheel_radius)


def crash():
    font = pygame.font.SysFont('comicsansms', 75)
    text_surface = font.render('You Crashed!', True, red)
    text_rect = text_surface.get_rect(center=(display_width / 2, display_height / 2))
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0

    obs_startx = random.randrange(0, display_width - 100)
    obs_starty = -600
    obs_speed = 7
    obs_width = 100
    obs_height = 100

    score = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # Create obstacles
        obstacles(obs_startx, obs_starty, obs_width, obs_height, gray)
        obs_starty += obs_speed
        car(x, y)
        display_score(score)

        if x > display_width - car_width or x < 0:
            crash()

        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(0, display_width - 100)
            score += 1
            obs_speed += 0.5

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
