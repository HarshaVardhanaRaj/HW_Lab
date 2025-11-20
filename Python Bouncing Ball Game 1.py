import pygame
import sys

pygame.init()


# --- Window Screen Settings ---
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Game")


# --- Colors ---
BG = (0, 0, 0) #RGB format
ball_color   = (255, 255, 0) #RGB format


# --- Ball Settings ---
x, y = screen_width // 2, screen_height // 2   #starting position of the ball
radius = 30
speed_x = 10
speed_y = 10
 

clock = pygame.time.Clock() #determines fps of the gameplay


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    x += speed_x
    y += speed_y

    # Bounce off walls
    if x - radius <= 0 or x + radius >= screen_width:
        speed_x = -speed_x

    if y - radius <= 0 or y + radius >= screen_height:
        speed_y = -speed_y

    # Draw everything
    screen.fill(BG)
    pygame.draw.circle(screen, ball_color, (x, y), radius)

    pygame.display.flip()
    clock.tick(60) #determines fps of the gameplay
