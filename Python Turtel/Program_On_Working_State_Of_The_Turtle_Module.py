import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen color to red
t.color("red")

# Draw a square with side length 100
for i in range(4):
    t.forward(100)
    t.right(90)

# Save the current state of the turtle
state = t._dict

# Lift the pen, move to a new position, and put the pen down
t.penup()
t.goto(-50, -50)
t.pendown()

# Set the pen color to blue
t.color("blue")

# Draw a circle with radius 50
t.circle(50)

# Restore the previous state of the turtle
t._dict.update(state)

# Draw another square with side length 100, overlapping the previous one
for i in range(4):
    t.forward(100)
    t.right(90)

# Keep the turtle graphics window open
turtle.done()
