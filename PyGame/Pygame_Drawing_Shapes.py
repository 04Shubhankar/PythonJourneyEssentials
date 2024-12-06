import pygame

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Shape Drawing")  # Set the title of the window

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw shapes
    pygame.draw.rect(screen, red, pygame.Rect(100, 30, 60, 60))  # Red rectangle
    pygame.draw.polygon(screen, blue, [(25, 90), (76, 125), (375, 100), (150, 25), (60, 150)])  # Blue polygon
    pygame.draw.circle(screen, white, (170, 180), 60)  # White circle
    pygame.draw.line(screen, red, (10, 175), (300, 10), 4)  # Red line
    pygame.draw.ellipse(screen, green, (275, 150, 130, 180))  # Green ellipse

    # Update the display
    pygame.display.flip()

pygame.quit()
