import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
is_race_on = True

# set up prompt
user_bet = screen.textinput(title='Enter your bet!', prompt='which color do you think will win the race?')

color = ['red', 'blue', 'green', 'yellow', 'orange', 'pink']
# initiate a tutle list
turtles = []

# create six turtle instances with different states and append them to turtles list
# looks like the instance can have the same name, but each has different states
for i in range(6):

    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=100 - 40 * i)
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

# the reason to have a list is in the last loop there could be multiple turtles at the destination.
# we want the first turtle.
winner = []

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner.append(turtle.pencolor())

# print(winner)

if winner[0] == user_bet:
    print("you've won!")
else:
    print(f'you lost, {winner[0]} is the winner!')

screen.exitonclick()
