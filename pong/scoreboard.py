from turtle import Turtle

class Scoreboard(Turtle):
    """Class to manage and display the scoreboard."""

    def __init__(self):
        """Initialize the scoreboard with scores and position."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # Hide the turtle pointer
        self.l_score = 0  # Left player score
        self.r_score = 0  # Right player score
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display with current scores."""
        self.clear()  # Clear previous score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increment the left player's score by 1 and update the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increment the right player's score by 1 and update the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
