from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0,240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}        {self.right_score}", align="center", font=("Courier",50,"bold"))

    def update_left_score(self):
        self.left_score += 1
        self.update_score()

    def update_right_score(self):
        self.right_score += 1
        self.update_score()

    def game_end(self,winner):
        result = Turtle()
        result.goto(0, 0)
        result.penup()
        result.hideturtle()
        result.color("white")
        result.write(f"Game Over, the winner is {winner}", align="center", font=("Courier", 30, "bold"))





