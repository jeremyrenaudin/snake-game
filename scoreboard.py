from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """Initialize a scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        """Update the score displayed on the scoreboard"""
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        """Increase the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        """Display a GAME OVER message"""
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)