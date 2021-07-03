from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-170,260)
        self.score = 0
        with open("scorekeeper.txt") as file:
            self.highscore = int(file.read())
        # self.highest()
        self.show_score()


    def show_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("scorekeeper.txt", 'w') as f:
                f.write(f"{self.highscore}")
        self.write(f"SCORE: {self.score} HIGHEST SCORE: {self.highscore}",font = ("Arial", 20, "normal"))


    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",font = ("Arial", 20, "normal"))

    def reset_board(self):
        self.clear()
        self.score = 0
        self.show_score()
