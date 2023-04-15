import turtle
from colorgram import colorgram
from turtle import Turtle, Screen
import random

choice = ""
turtle.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "Wheat",
           "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]


# Function to create Damien Hirst paint
def create_hirst_paint(name_object):
    """Function to create Damien Hirst paint"""
    color_list = []

    name_object.penup()
    name_object.setheading(220)
    name_object.forward(560)
    name_object.setheading(0)

    colors = colorgram.extract('./image/picture.jpg', 30)


    for color in colors:
        unique_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_list.append(unique_color)

    # extract color from pictures
    for i in range(1, 101):

        name_object.dot(20, random.choice(color_list))
        name_object.forward(40)
        if i % 10 == 0:
            # turn the face left by 90 degree
            name_object.setheading(90)
            name_object.forward(40)
            # turn the face left
            name_object.setheading(180)
            name_object.forward(400)
            # put the face right
            name_object.setheading(0)


# Function get random color R,G,B
def random_color():
    """Function get random color R,G,B"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)

    return my_color


# Function to create spirograph
def make_spirograph(name_object, grade):
    """Function to create spirograph"""
    for _ in range(int(360/grade)):
        color = random_color()
        name_object.color(color)
        name_object.right(grade)
        name_object.circle(100)
    name_object.clear()


# Function to generate turtle random wolk with random color
def random_walk(name_object):
    """Function to do turtle random wolk with random color"""
    name_object.pensize(5)

    for i in range(21):
        color = random_color()
        name_object.setheading(random.choice(direction))
        name_object.color(color)
        name_object.forward(random.randint(0, 100))
    name_object.clear()


# Function to do create different shapes
def create_different_shapes(name_object, size):
    """Function to do create different shapes"""
    for i in range(3, size+1):
        color = random_color()
        name_object.color(color)
        angle = 360 / i
        for _ in range(i):
            name_object.forward(50)
            name_object.right(angle)
    name_object.clear()


# Function to do create dash line
def create_dash_line(name_object):
    for i in range(10):
        name_object.forward(10)
        name_object.penup()
        name_object.forward(10)
        name_object.pendown()
    name_object.clear()


# Function to do create square
def create_square(name_object):
    """Function to do create square"""
    for i in range(4):
        name_object.forward(100)
        name_object.right(90)
    name_object.clear()


tommy = Turtle()
tommy.shape("turtle")
tommy.penup()
tommy.goto(-200,200)
tommy.pendown()
tommy.speed("normal")

create_square(tommy)
create_dash_line(tommy)
create_different_shapes(tommy, 9)
random_walk(tommy)
make_spirograph(tommy, 5)
create_hirst_paint(tommy)

screen = Screen()

screen.exitonclick()

