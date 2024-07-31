from turtle import Turtle

class Ball(Turtle):
    """Class to manage the ball in the Pong game."""
    
    def __init__(self):
        """Initialize the ball with default settings."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        """Move the ball according to its current speed."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the direction of the ball's vertical movement."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the direction of the ball's horizontal movement and increase speed."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball to the center of the screen and reverse its horizontal direction."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
