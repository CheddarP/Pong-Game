from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 80, "normal")
LINE_FONT = ("Courier", 60, "bold")
WIN_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.points_to_win = 5
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_l, move=False, align=ALIGNMENT, font=SCORE_FONT)
        self.goto(100, 200)
        self.write(self.score_r, move=False, align=ALIGNMENT, font=SCORE_FONT)
        self.mid_line()

    def r_point(self):
        self.clear()
        self.score_r += 1
        self.update_scoreboard()

    def l_point(self):
        self.clear()
        self.score_l += 1
        self.update_scoreboard()

    def mid_line(self):
        self.goto(0,-400)
        self.write("\n\n | \n\n | \n\n | \n\n | \n\n | \n\n |", move=False, align=ALIGNMENT, font=LINE_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=SCORE_FONT)
        if self.score_l == self.points_to_win:
            self.goto(-200, -200)
            self.write("You Win!", move=False, align=ALIGNMENT, font=WIN_FONT)
        elif self.score_r == self.points_to_win:
            self.goto(200, -200)
            self.write("You Win!", move=False, align=ALIGNMENT, font=WIN_FONT)


