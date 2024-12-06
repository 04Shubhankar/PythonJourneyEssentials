import pygame  # Import the Pygame library

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Image Example")  # Set the title of the window

# Load the image
img = pygame.image.load('pygame.png')  # Load an image from the file "pygame.png"

# Set up the background color
bg = (127, 127, 127)  # Gray color

# Game loop
done = False
while not done:
    # Event handling
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the user closed the window
            done = True  # Set done to True to exit the loop

    # Fill the screen with the background color
    screen.fill(bg)

    # Get the rectangle representing the image's dimensions
    rect = img.get_rect()

    # Set the center of the rectangle to (200, 150)
    rect.center = 200, 150

    # Draw the image on the screen
    screen.blit(img, rect)

    # Update the display to show the changes
    pygame.display.update()

# Quit Pygame
pygame.quit()
