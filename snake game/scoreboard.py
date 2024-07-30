from turtle import Turtle

class Scoreboard(Turtle):
    """Handles the score display and game over messages."""
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)  # Position the scoreboard at the top of the screen
        self.hideturtle()
        self.update_scoreboard()  # Display the initial score
        
    def update_scoreboard(self):
        """Clear the old score and display the new score."""
        self.clear()  # Remove the old score display
        self.write(f"Score: {self.score}  ", align='center', font=("Arial", 24, "normal"))
        
    def increase_score(self):
        """Increment the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_scoreboard()  # Refresh the score display
        
    def game_over(self):
        """Display a game over message when the game ends."""
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write("Game over!", align='center', font=("Arial", 24, "normal"))
