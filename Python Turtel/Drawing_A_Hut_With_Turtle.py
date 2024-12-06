import turtle as t
import math

# Set up the turtle
t.speed(3)  # Adjust the speed as desired

# Function to draw a rectangle (walls of the hut)
def drawRectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw an equilateral right triangle (roof)
def drawTriangle(length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

# Function to draw a door (rectangle)
def drawDoor(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height-70)
        t.left(90)
    t.end_fill()

# Draw the hut
def drawHut():
    # Draw the base (walls) of the hut
    t.penup()
    t.goto(-50, -50)  # Move turtle to starting position
    t.pendown()
    drawRectangle(100, 100, 'burlywood')

    # Draw the roof
    t.penup()
    t.goto(-50, 50)  # Move turtle to the top of the walls
    t.setheading(0)  # Ensure the turtle is facing right
    t.pendown()
    drawTriangle(100, 'sienna')

    # Draw the door
    t.penup()
    t.goto(-15, -50)  # Move turtle to position for the door
    t.setheading(90)  # Ensure the turtle is facing up
    t.pendown()
    drawDoor(30, 50, 'brown')

# Call the drawHut function to draw the complete hut
drawHut()

# Hide the turtle and display the window
t.hideturtle()
t.done()
