import pygame

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Hello World")  # Set the title of the window

# Create a font object
font = pygame.font.SysFont("Arial", 36)  # Create a font with Arial font and size 36

# Render the text
text = font.render("Hello, World!", True, (255, 0, 0))  # Render the text "Hello, World!" in red color with anti-aliasing

# Display the text on the screen
screen.blit(text, (200, 150))  # Blit the text surface onto the screen at (200, 150)

# Update the display to show the changes
pygame.display.update()

# Game loop
while True:
    # Event handling
    events = pygame.event.get()  # Get all events from the event queue
    for event in events:
        if event.type == pygame.QUIT:  # Check if the user closed the window
            break  # Exit the loop

# Quit Pygame
pygame.quit()
