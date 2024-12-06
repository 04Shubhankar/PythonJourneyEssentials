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

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)  # Get the name of the pressed key
            print(key, "Key is Pressed")

        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)  # Get the name of the released key
            print(key, "Key is released")

    # Game logic (empty in this basic example)

    # Rendering (empty in this basic example)

    # Update the display to show the changes
    pygame.display.update()
