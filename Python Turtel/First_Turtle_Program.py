import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the animation speed to the fastest
t.speed(0)

# Lift the pen to move without drawing
t.penup()

# Move the turtle to the starting position (-200, 0)
t.goto(-200, 0)

# Put the pen down to start drawing
t.pendown()

def draw_square():
    # Draw a square with side length 100
    for i in range(4):
        t.forward(100)
        t.right(90)

    # Move the turtle forward 20 units 20 times without drawing
    for i in range(20):
        t.penup()
        t.forward(20)
        t.pendown()

# Call the function to draw a square
draw_square()

# Keep the window open until it's closed manually
turtle.done()
