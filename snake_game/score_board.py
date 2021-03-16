from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__() # if use score = Turtle here cant have attribute score, therefore need to inherit from turtle
        self.score = 0
        self.penup()
        self.goto(0, 270) # have to move the turtle before write
        self.color('white')
        self.hideturtle()

        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)