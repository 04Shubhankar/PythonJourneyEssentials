import pygame

pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake and food initial positions
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_size = 10
snake_speed = 10

food_x = 200
food_y = 200

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= snake_speed
    if keys[pygame.K_RIGHT]:
        snake_x += snake_speed
    if keys[pygame.K_UP]:
        snake_y -= snake_speed
    if keys[pygame.K_DOWN]:
        snake_y += snake_speed

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        # Increase snake length
        snake_size += 10
        # Generate new food position
        food_x = random.randrange(0, screen_width)
        food_y = random.randrange(0, screen_height)

    # Draw the game objects
    screen.fill(black)
    pygame.draw.rect(screen, white, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])

    pygame.display.update()

pygame.quit()
