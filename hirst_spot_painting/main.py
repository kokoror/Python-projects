import turtle as t
import colorgram
import random

t.colormode(255) # set rgb color code

colors = colorgram.extract('image.jpg', 20)
# first color's rgb code can be accessed by colors[0].rgb

def random_color():
    ramdom_number = random.randint(10, 19)
    return colors[ramdom_number].rgb

tim = t.Turtle()
tim.penup()
tim.hideturtle()

for i in range(10):
    for j in range(10):

        tim.setpos(-250 + j * 50, -250 + i * 50)
        tim.dot(20, random_color())

screen = t.Screen()
screen.exitonclick()
