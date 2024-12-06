import pygame  # Import the Pygame library

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Concentric Circles")  # Set the title of the window

# Define colors
white = (255, 255, 255)  # White color
red = (255, 0, 0)  # Red color
green = (0, 255, 0)  # Green color
blue = (0, 0, 255)  # Blue color
bg = (127, 127, 127)  # Gray background color

# Game loop
done = False
while not done:
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the user closed the window
            done = True  # Set done to True to exit the loop

    # Fill the screen with the background color
    screen.fill(bg)

    # Draw concentric circles
    pygame.draw.circle(screen, red, (200, 150), 60, 2)  # Red circle
    pygame.draw.circle(screen, green, (200, 150), 80, 2)  # Green circle
    pygame.draw.circle(screen, blue, (200, 150), 100, 2)  # Blue circle

    # Update the display to show the changes
    pygame.display.update()

# Save the image to a file
pygame.image.save(screen, "circle.png")

# Quit Pygame
pygame.quit()
