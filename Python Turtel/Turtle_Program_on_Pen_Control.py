import turtle  # Import the turtle graphics module

# Create a turtle object called 'pen' to draw on the screen
pen = turtle.Turtle()

# Set the pen color to red
pen.pencolor("red")

# Move the pen forward by 100 units in the current direction
pen.forward(100)

# Rotate the pen 90 degrees to the left
pen.left(90)

# Move the pen forward by 50 units
pen.forward(50)

# Change the pen color to blue
pen.pencolor("blue")

# Rotate the pen 45 degrees to the right
pen.right(45)

# Move the pen forward by 75 units
pen.forward(75)

# Lift the pen up so that moving it won’t draw on the screen
pen.penup()

# Move the pen to the origin point (0, 0) without drawing
pen.goto(0, 0)

# Put the pen back down to start drawing again
pen.pendown()

# Change the pen color to green
pen.pencolor("green")

# Begin drawing a square pattern with a side length of 50 units
# The outer 'for' loop iterates 4 times to create 4 squares
for i in range(4):
    # Inner loop is attempting to position the turtle to start each side of a square
    for j in range(4):
        pen.goto(0, j + 200)  # Move to a position above the origin each time, which is unexpected
        pen.forward(50)       # Move forward 50 units to draw one side of the square
        pen.left(90)          # Turn 90 degrees to the left to prepare for the next side

    # After drawing one square, move forward by 50 units
    pen.forward(50)

    # Rotate left 90 degrees to set up for the next square
    pen.left(90)

# Keep the turtle graphics window open until it’s manually closed
turtle.done()
