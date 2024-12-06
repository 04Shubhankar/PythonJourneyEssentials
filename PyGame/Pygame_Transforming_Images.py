import pygame

pygame.init()  # Initialize Pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Create a window with dimensions (width, height)
pygame.display.set_caption("Flip Image")  # Set the title of the window

# Load the image
img1 = pygame.image.load("pygame.png")  # Load the image from the file "pygame.png"

# Create copies of the original image
img2 = img1.copy()  # Create a copy of img1
img3 = img1.copy()  # Create another copy of img1

# Flip the images horizontally and vertically
img2 = pygame.transform.flip(img2, True, False)  # Flip img2 horizontally
img3 = pygame.transform.flip(img3, False, True)  # Flip img3 vertically

# Set up the background color
bg = (127, 127, 127)  # Gray background color

# Game loop
done = False
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user closed the window
            done = True  # Set done to True to exit the loop

    # Fill the screen with the background color
    screen.fill(bg)

    # Get the rectangle for the original image
    rect1 = img1.get_rect()
    rect1.center = 200, 50  # Center the rectangle at (200, 50)

    # Draw the original image
    screen.blit(img1, rect1)

    # Get the rectangle for the horizontally flipped image
    rect2 = img2.get_rect()
    rect2.center = 200, 150  # Center the rectangle at (200, 150)

    # Draw the horizontally flipped image
    screen.blit(img2, rect2)

    # Update the display to show the changes
    pygame.display.update()

# Quit Pygame
pygame.quit()
