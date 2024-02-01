# Example file showing a basic pygame "game loop"
import pygame
from utilities import Button

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
button_begin = Button([280, 50], "Let's Begin", [380, 302])
button_begin_loop = True


while running:
    events = pygame.event.get()
    for event in events:  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill('white')

    if button_begin_loop:
        # Button 1 Control
        button_begin.render(screen)
        if button_begin.clicked(events):
            print("Game Logic goes here")
            button_begin_loop = False

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
quit()
