import turtle

# Create a turtle object
t = turtle.Turtle()

# Define functions for movement and turning
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

# Create a screen object
screen = turtle.Screen()

# Set up keypress events
screen.listen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

# Start the main event loop
turtle.mainloop()
