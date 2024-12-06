import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the pen color to blue
my_turtle.pencolor("blue")

# Draw a square
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Keep the window open
turtle.done()
