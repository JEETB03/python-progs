from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """Scoreboard"""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score()
        
    def update_score(self):
        """Update the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        """Increase level and update scoreboard"""
        self.level += 1
        self.update_score()
        
    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        self.goto(0, -50)
        self.write(f"Final Score: {self.level - 1}", align="center", font=FONT)
