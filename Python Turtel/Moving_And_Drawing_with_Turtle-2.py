import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen color and size
t.pencolor("red")
t.pensize(2)

# Set the animation speed (slower)
t.speed(2)

# Move the turtle forward and draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Undo the last drawing action (square)
t.undo()

# Move to a new position and draw a triangle
t.penup()  # Lift the pen
t.goto(50, -50)
t.pendown()  # Put the pen down
for _ in range(3):
    t.forward(80)
    t.left(120)

# Get the turtle's current heading
current_heading = t.heading()
print("Current heading:", current_heading)

# Show the x and y coordinates
x_coord = t.xcor()
y_coord = t.ycor()
print("Current position: (", x_coord, ",", y_coord, ")")

# Set measurement units to radians
t.radians()

# Stamp the turtle's image twice
t.stamp()
t.forward(50)
t.stamp()

# Set measurement units back to degrees
t.degrees()

# Draw a blue dot
t.penup()
t.goto(-100, 0)
t.pendown()
t.dot(size=10, color="blue")

# Clear all stamps
t.clearstamps()

# Keep the window open
turtle.done()
