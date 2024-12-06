import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen color and size
t.pencolor("blue")
t.pensize(3)

# Move the turtle forward 100 units
t.forward(100)

# Turn the turtle right by 90 degrees
t.right(90)

# Move the turtle backward 50 units
t.backward(50)

# Turn the turtle left by 45 degrees
t.left(45)

# Get the current heading of the turtle
current_heading = t.heading()
print("Current heading:", current_heading)

# Set the turtle's x-coordinate to 50
t.setx(50)

# Set the turtle's y-coordinate to -100
t.sety(-100)

# Set the turtle's heading to 180 degrees (south)
t.seth(180)

# Move the turtle forward 100 units
t.forward(100)

# Return the turtle to its starting position and heading
t.home()

# Keep the window open
turtle.done()
