import pygame  # Import the Pygame library

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((640, 480))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Hello World")  # Set the title of the window

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the user closed the window
            running = False  # Set running to False to exit the loop

    # Game logic (empty in this basic example)

    # Rendering
    screen.fill((255, 255, 255))  # Fill the screen with white color (RGB values)
    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 100, 100))  # Draw a blue rectangle
    pygame.display.update()  # Update the display to show the changes

# Quit Pygame
pygame.quit()
