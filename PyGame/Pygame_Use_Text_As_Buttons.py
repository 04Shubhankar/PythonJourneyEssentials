import pygame

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Text Buttons")  # Set the title of the window

# Define colors
black = (0, 0, 0)
bg = (127, 127, 127)  # Gray background color

# Create a font object
font = pygame.font.SysFont("Arial", 14)  # Create a font with Arial font and size 14

# Render text surfaces
text1 = font.render("START", True, black)  # Render "START" text in black
text2 = font.render("PLAY", True, black)   # Render "PLAY" text in black
text3 = font.render("STOP", True, black)  # Render "STOP" text in black

# Create rectangles for each text surface
rect1 = text1.get_rect(topleft=(10, 10))  # Position the "START" button at (10, 10)
rect2 = text2.get_rect(topleft=(100, 10))  # Position the "PLAY" button at (100, 10)
rect3 = text3.get_rect(topleft=(200, 10))  # Position the "STOP" button at (200, 10)

# Game loop
done = False
while not done:
    # Event handling
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the user closed the window
            done = True  # Set done to True to exit the loop

        if event.type == pygame.MOUSEBUTTONDOWN:  # Check if a mouse button is clicked
            mouse_pos = event.pos  # Get the mouse position

            # Check if the clicked position is within the bounds of the "START" button
            if rect1.collidepoint(mouse_pos):
                # Handle "START" button click (e.g., print a message)
                print("START Button was pressed")
            if rect2.collidepoint(mouse_pos):
                # Handle "START" button click (e.g., print a message)
                print("Play Button was pressed")
            if rect3.collidepoint(mouse_pos):
                # Handle "START" button click (e.g., print a message)
                print("Quit Button was pressed")

    # Fill the screen with the background color
    screen.fill(bg)

    # Draw the text surfaces on the screen
    screen.blit(text1, rect1)
    screen.blit(text2, rect2)
    screen.blit(text3, rect3)

    # Update the display to show the changes
    pygame.display.update()

# Quit Pygame
pygame.quit()
