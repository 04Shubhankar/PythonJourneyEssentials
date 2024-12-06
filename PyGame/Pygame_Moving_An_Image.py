image_filename = "pygame.png"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Moving Image")  # Set the title of the window

# Load the image
img = pygame.image.load(image_filename)  # Load an image from the file "pygame.png"

# Set the initial x-coordinate of the image
x = 0

while True:
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:  # Check if the user closed the window
            exit()  # Exit the program

    # Draw the image at the specified x-coordinate and y-coordinate of 100
    screen.blit(img, (x, 100))

    # Update the x-coordinate
    x += 0.5  # Move the image to the right by 0.5 pixels

    # If the image goes beyond the right edge of the screen, wrap it around to the left
    if x > 400:
        x = 0

    # Update the display to show the changes
    pygame.display.update()
