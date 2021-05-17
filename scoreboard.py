from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
SCOREBOARD_POSITION = (0, 260)
PLAY_AGAIN_MESSAGE = "Do you want to play again? Enter Yes or No"


class Scoreboard(Turtle):
    """Initialize a scoreboard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        """Update the score displayed on the scoreboard"""
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        """Increase the score"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """Display a GAME OVER message"""
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def play_again(self, screen):
        """Ask user if he/she would like to play again"""
        play_again = screen.textinput(title="Play again", prompt=PLAY_AGAIN_MESSAGE)
        while play_again.lower() not in ["yes", "no"]:
            play_again = screen.textinput(title="Play again", prompt=PLAY_AGAIN_MESSAGE)
        if play_again.lower() == "yes":
            return True
        else:
            return False