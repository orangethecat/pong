from turtle import Turtle, Screen

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(pos)
        self.speed("fastest")


    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(),new_y)


    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(),new_y)

