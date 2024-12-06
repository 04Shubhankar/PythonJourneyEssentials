from pygame.locals import *
import pygame

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Shoot the Arrow")  # Set the title of the window

# Define colors
white = (255, 255, 255)
bg = (127, 127, 127)  # Gray background color

# Load sound and image
sound = pygame.mixer.Sound("sound.wav")  # Load a sound effect
img = pygame.image.load("arrow.png")  # Load an arrow image

# Create a font object
font = pygame.font.SysFont("Arial", 14)  # Create a font with Arial font and size 14

# Render the "SHOOT" text
text1 = font.render("SHOOT", True, bg)  # Render the text "SHOOT" in the background color

# Create rectangles for the text and image
rect1 = text1.get_rect(midbottom=(200, 300))  # Position the "SHOOT" text at the bottom center
rect2 = img.get_rect(midtop=(200, 270))  # Position the arrow image at the top center

# Game loop
kup = 0
psmode = True
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user closed the window
            done = True  # Set done to True to exit the loop
        elif event.type == pygame.KEYDOWN:  # Check if a key is pressed
            if event.key == pygame.K_SPACE:  # Check if the spacebar is pressed
                sound.play()  # Play the sound effect
                kup = 1  # Set the `kup` flag to 1 to indicate the arrow should move up

    # Update the arrow's position
    if kup:
        y -= 2  # Move the arrow up by 2 pixels
        rect2.top = y  # Update the arrow's position

    # Fill the screen with the background color
    screen.fill(bg)

    # Draw the text and image on the screen
    screen.blit(text1, rect1)
    screen.blit(img, rect2)

    # Update the display to show the changes
    pygame.display.update()

# Quit Pygame
pygame.quit()
