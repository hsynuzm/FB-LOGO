import turtle
import math

def draw_curved_triangle():
    turtle.penup()
    turtle.color("#000000", "#163962")
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.goto(-126, 90)  # Move to the starting point
    turtle.pendown()
    turtle.circle(145, 60)  # Draw an arc with radius 145 and 60 degrees
    ending_x, ending_y = turtle.pos()

    # Draw the symmetric arc
    turtle.goto(ending_x, ending_y)  # Go to the end point of the first arc
    turtle.right(120)
    turtle.circle(145, 60)  # Draw the symmetric arc with negative radius
    ending_x, ending_y = turtle.pos()
    # Draw a straight line to connect the bottom parts
    turtle.goto(ending_x, ending_y)  # Go to the end point of the left arc
    turtle.goto(-126, 90)
    turtle.penup()
    turtle.end_fill()

def draw_bottom_shield():
    turtle.penup()
    turtle.color("#000000", "#163962")
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.goto(-126, 90)
    turtle.pendown()
    turtle.right(78)
    turtle.circle(500, 27)
    ending_x, ending_y = turtle.pos()
    turtle.goto(ending_x, ending_y)
    turtle.left(40)
    turtle.circle(145, 20)
    ending_x, ending_y = turtle.pos()
    turtle.goto(ending_x, ending_y)
    turtle.left(42)
    turtle.circle(500, 27)
    turtle.penup()
    turtle.end_fill()

def draw_yellow_line():
    turtle.penup()
    turtle.color("#000000", "#ffed00")
    turtle.pensize(0)
    turtle.begin_fill()
    turtle.goto(-126, 90)
    turtle.pendown()
    turtle.right(156)
    turtle.circle(500, 10)
    ending_x, ending_y = turtle.pos()
    turtle.goto(-ending_x, ending_y)
    turtle.left(137.5)
    turtle.circle(500, 10)
    turtle.penup()
    turtle.end_fill()

def draw_filled_star(size, color):
    turtle.penup()
    turtle.goto(-85, -125)  # Place the star at the center of the page
    turtle.pendown()
    size = 10
    turtle.width(4)
    angle = 120
    turtle.fillcolor("BLACK")
    turtle.begin_fill()

    # Draw the star
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()

def draw_filled_star2(size, color):
    turtle.penup()
    turtle.goto(85, -125)  # Place the star at the center of the page
    turtle.pendown()
    size = 10
    turtle.width(4)
    angle = 120
    turtle.fillcolor("BLACK")
    turtle.begin_fill()

    # Draw the star
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()

# Setup the screen
turtle.setup(800, 800)
turtle.speed(0)

# Draw the outer circle (white background)
turtle.penup()
turtle.pensize(3)
turtle.goto(0, -180)
turtle.pendown()
turtle.color("#000000", "white")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# Draw the inner red circle
turtle.penup()
turtle.pensize(3)
turtle.goto(0, -125)
turtle.pendown()
turtle.color("#000000", "#e20025")
turtle.begin_fill()
turtle.circle(145)
turtle.end_fill()

draw_curved_triangle()
draw_bottom_shield()
draw_yellow_line()
draw_filled_star(10, "black")
draw_filled_star2(10, "black")

# Draw the leaf
turtle.penup()
turtle.goto(0, 10)
turtle.pendown()
turtle.color("#39a642")
turtle.begin_fill()
turtle.goto(-20, 40)
turtle.goto(0, 70)
turtle.goto(20, 40)
turtle.goto(0, 10)
turtle.end_fill()

# Variables for positioning the text
radius = 175  # The radius of the text circle, adjusted for lower position
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
