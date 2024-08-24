import turtle
import math


def draw_shield():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-70, 50)  # Start position for the shield

    # Draw the red shield background
    turtle.pendown()
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.goto(70, 50)
    turtle.goto(0, 120)
    turtle.goto(-70, 50)
    turtle.end_fill()

    # Draw the yellow stripe
    turtle.penup()
    turtle.goto(-70, 50)
    turtle.pendown()
    turtle.color("black", "yellow")
    turtle.begin_fill()
    turtle.goto(70, 50)
    turtle.goto(50, 0)
    turtle.goto(-50, 0)
    turtle.goto(-70, 50)
    turtle.end_fill()

    # Draw the blue stripe
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.goto(50, 0)
    turtle.goto(70, -50)
    turtle.goto(-70, -50)
    turtle.goto(-50, 0)
    turtle.end_fill()


# Setup the screen
turtle.setup(800, 800)
turtle.speed(10)

# Draw the outer circle (white background)
turtle.penup()
turtle.pensize(4)
turtle.goto(0, -180)
turtle.pendown()
turtle.color("black", "white")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# Draw the inner red circle
turtle.penup()
turtle.pensize(4)
turtle.goto(0, -125)
turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
turtle.circle(145)
turtle.end_fill()

draw_shield()

# Draw the leaf
turtle.penup()
turtle.goto(0, 10)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.goto(-10, 40)
turtle.goto(0, 70)
turtle.goto(10, 40)
turtle.goto(0, 10)
turtle.end_fill()

# Variables for positioning the text
radius = 175 # The radius of the text circle, adjusted for lower position
text = "FENERBAHÇE SPOR KULÜBÜ"
angle_step = 270 / len(text)  # Half circle
turtle.color("black")
# Starting angle (adjust this to center the text)
start_angle = 220  # Start from top and go clockwise

# Draw each letter in a curved fashion
turtle.penup()
for i, char in enumerate(text):
    angle = start_angle - i * angle_step  # Adjusted to make the text appear straight
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    turtle.goto(x, y)
    turtle.setheading(angle)  # Adjusted for correct text orientation
    turtle.pendown()
    turtle.write(char, align="center", font=("arial rounded", 22, "bold"))
    turtle.penup()

# Draw "1907" at the bottom
# Variables for positioning the "1907" text
radius_1907 = 165  # The radius for the "1907" text
year_text = "1907"
angle_step_year = 7  # Adjust based on the length of "1907"
start_angle_year = -99  # Start from the bottom for "1907"

# Set the color to black
turtle.color("black")

# Draw the "1907" text in a curved fashion
turtle.penup()
for i, char in enumerate(year_text):
    angle = start_angle_year + i * angle_step_year
    x = radius_1907 * math.cos(math.radians(angle))
    y = radius_1907 * math.sin(math.radians(angle))

    turtle.goto(x, y)
    turtle.setheading(angle + 90)  # Rotate text outward
    turtle.pendown()
    turtle.write(char, align="center", font=("Arial", 24, "bold"))
    turtle.penup()

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
