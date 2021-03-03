#how to use event listner in turtle graphics
import turtle as t

tim = t.Turtle()
screen = t.Screen()

def forward():
    tim.forward(20)

def backward():
    tim.backward(20)

def counterclock_wise():
    tim.setheading(tim.heading() + 10)

def clock_wise():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(counterclock_wise, 'a')
screen.onkey(clock_wise, 'd')
screen.onkey(clear, 'c')

screen.listen()
screen.exitonclick()
