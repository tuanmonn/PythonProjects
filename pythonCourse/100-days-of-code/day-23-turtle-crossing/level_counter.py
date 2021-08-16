from turtle import Turtle

COUNTER_POSITION = (-380, 260)
class LevelCounter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(COUNTER_POSITION)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", font=("Courier", 20, "bold"))

    def level_up(self):
        self.clear()
        self.level +=1
        self.update_level()

    def game_over(self):
        game_over_text = Turtle()
        game_over_text.hideturtle()
        game_over_text.write("Game over you loser!", align="center", font=("Courier", 20, "bold"))
