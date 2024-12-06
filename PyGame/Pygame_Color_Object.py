import pygame  # Import the Pygame library

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((500, 400))  # Create a window with dimensions (width, height)

# Create a color object
color = pygame.Color(255, 0, 0)  # Red color

# Create a rectangle object
rect = pygame.Rect(200, 150, 100, 100)  # Rectangle at (200, 150) with width 100 and height 100

# Draw the rectangle on the screen
pygame.draw.rect(screen, color, rect)

# Update the display to show the changes
pygame.display.update()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the user closed the window
            running = False  # Set running to False to exit the loop

# Quit Pygame
pygame.quit()
