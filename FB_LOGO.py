class Patch_txt_angle:
    def RawTurtleDOTwrite(self, arg, move=False, align="left", font=("Arial", 11, "normal"), txt_angle=0):
        if self.undobuffer:
            self.undobuffer.push(["seq"])
            self.undobuffer.cumulate = True
        end = self._write(str(arg), align.lower(), font, txt_angle)
        if move: 
            x, y = self.pos() 
            self.setpos(end, y)
        if self.undobuffer: 
            self.undobuffer.cumulate = False
        
    def RawTurtleDOT_write(self, txt, align, font, txt_angle):
        item, end = self.screen._write(self._position, txt, align, font, self._pencolor, txt_angle)
        self.items.append(item)
        if self.undobuffer: 
            self.undobuffer.push(("wri", item))
        return end
    
    def TurtleScreenBaseDOT_write(self, pos, txt, align, font, pencolor, txt_angle):
        x, y = pos 
        x = x * self.xscale 
        y = y * self.yscale
        anchor = {"left": "sw", "center": "s", "right": "se"}
        item = self.cv.create_text(x - 1, -y, text=txt, anchor=anchor[align],
                                   fill=pencolor, font=font, angle=txt_angle)
        x0, y0, x1, y1 = self.cv.bbox(item)
        self.cv.update()
        return item, x1 - 1

import turtle
import math

# Patching turtle's write methods
turtle.RawTurtle.write = Patch_txt_angle.RawTurtleDOTwrite
turtle.RawTurtle._write = Patch_txt_angle.RawTurtleDOT_write
turtle.TurtleScreenBase._write = Patch_txt_angle.TurtleScreenBaseDOT_write

# Function to draw a curved triangle
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
    turtle.circle(145, 60)  # Draw the symmetric arc
    ending_x, ending_y = turtle.pos()
    # Draw a straight line to connect the bottom parts
    turtle.goto(ending_x, ending_y)  # Go to the end point of the left arc
    turtle.goto(-126, 90)
    turtle.penup()
    turtle.end_fill()

# Function to draw the bottom shield
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

# Function to draw the yellow line
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

# Function to draw a filled star (for the left star)
def draw_filled_star(size, color):
    turtle.penup()
    turtle.goto(-85, -125)  # Position the star
    turtle.pendown()
    size = 10
    turtle.width(4)
    angle = 120
    turtle.fillcolor("BLACK")
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()

# Function to draw another filled star (for the right star)
def draw_filled_star2(size, color):
    turtle.penup()
    turtle.goto(85, -125)  # Position the star
    turtle.pendown()
    size = 10
    turtle.width(4)
    angle = 120
    turtle.fillcolor("BLACK")
    turtle.begin_fill()

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

# Drawing the different elements on the shield
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

# Text "FENERBAHÇE SPOR KULÜBÜ"
txt = "FENERBAHÇE SPOR KULÜBÜ"
radius = 150  # Radius for text placement
angle_step = 270 / len(txt)  # Angle between each character
tt = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor("black")

# Starting and stopping angles for text placement
start_angle = 220
txt_angle = 0

# Loop to place each character along the circular path
for i, char in enumerate(txt):
    angle = start_angle - i * angle_step  # Calculate the angle
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    tt.penup()
    tt.goto(x, y + 20)
    tt.setheading(angle + 90)  # Rotate the text to face the center
    tt.pendown()
    tt.color("black")
    tt.write(char, font=("arial rounded", 22, "bold"), align="center", txt_angle=txt_angle + 118)
    txt_angle -= 1125 / 100
    tt.penup()

tt.hideturtle()

# Draw "1907" at the bottom
radius_1907 = 165  # Radius for the "1907" text
year_text = "1907"
angle_step_year = 7  # Angle step between each digit
start_angle_year = -99  # Starting angle for "1907"

# Draw the "1907" text in a curved fashion
turtle.penup()
for i, char in enumerate(year_text):
    angle = start_angle_year + i * angle_step_year
    x = radius_1907 * math.cos(math.radians(angle))
    y = radius_1907 * math.sin(math.radians(angle))
    turtle.color("BLACK")
    turtle.goto(x, y-10)
    turtle.setheading(angle + 90)  # Rotate text outward
    turtle.pendown()
    turtle.write(char, align="center", font=("Arial", 24, "bold"))
    turtle.penup()

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
