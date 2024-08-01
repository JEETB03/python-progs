from turtle import Turtle

### constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Player settings"""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)
        self.speed(0)
        
    def move_up(self):
        """Player movement"""
        self.forward(MOVE_DISTANCE)
        
    def finish_line(self):
        """Check if player reached finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def goto_start(self):
        """Player reset to start position"""
        self.goto(STARTING_POSITION)  # reset player position to start position
        