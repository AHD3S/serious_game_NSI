# Example file showing a basic pygame "game loop"
import pygame
from utilities import *

# Pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1080, 540), pygame.RESIZABLE)
FONT = pygame.font.Font(None, 32)

# Initialize clock and running flag
clock = pygame.time.Clock()
running = True

# Create button and input box instances
button_begin = Button(280, 500, 200, 50, "Let's Begin", [255, 255, 255], [0, 0, 0], True)
input_name = InputBox(100, 100, 140, 32, FONT)

# Create a custom menu
my_custom_menu = InfoBox(
    "Title of the Menu",
    [
        Button(280, 500, 200, 50, "Nice", [255, 255, 255], [0, 0, 0], True)
    ]
)

# Load and set the custom font for the InfoBox title
info_box_title_font = pygame.font.Font("OpenSans-Bold.ttf", 24)
set_info_box_title_font(info_box_title_font)

# Main game loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        input_name.handle_event(event, FONT)
    
    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Update and draw the input box
    input_name.update()
    input_name.draw(screen)

    # Render and check if the "Let's Begin" button is clicked
    button_begin.verif_render(screen)  
    if button_begin.clicked(events):
        print("Game Logic goes here")
        button_begin.actif = False
        menu_manager.open_menu(my_custom_menu)
    
    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

# Quit Pygame
pygame.quit()
quit()
