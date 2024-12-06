import turtle
import random

# Set the drawing speed to the fastest
turtle.speed("fastest")

# Set color mode to RGB with values from 0 to 255
turtle.colormode(255)

# Function to draw a 5-sided shape with random colors and varying side lengths
def draw_shape(n, x, angle):
    # Generate random RGB values for pen and fill colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Set pen and fill colors
    turtle.pencolor(r, g, b)
    turtle.fillcolor(r, g, b)

    # Start filling the shape
    turtle.begin_fill()

    # Draw the shape
    for _ in range(5):
        turtle.forward(5 * n - 5 * _)
        turtle.right(x)
        turtle.forward(5 * n - 5 * _)
        turtle.right(72 - x)

    # End filling the shape
    turtle.end_fill()

    # Turn the turtle
    turtle.right(angle)

# Set the parameters for the shape
n = 30
x = 144
angle = 18

# Draw the shape
draw_shape(n, x, angle)

# Keep the turtle graphics window open
turtle.done()
