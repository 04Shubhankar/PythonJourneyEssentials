import pygame, sys  # Import Pygame and sys modules

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((640, 480))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Hello World")  # Set the title of the window

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the user closed the window
            pygame.quit()  # Quit Pygame
            sys.exit()  # Exit the program

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # Get the mouse position
            print("x={}, y={}".format(pos[0], pos[1]))  # Print the mouse position

    # Game logic (empty in this basic example)

    # Rendering (empty in this basic example)

    # Update the display to show the changes
    pygame.display.update()
