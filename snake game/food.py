from turtle import Turtle
import random

class Food(Turtle):
    """Manages the food that the snake eats."""
    
    def __init__(self):
        super().__init__()  # Inherit from the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # Resize the food
        self.color("green")
        self.speed("fastest")
        self.refresh()  # Position the food at a random location
        
    def refresh(self):
        """Move the food to a new random position."""
        ran_x = random.randint(-320, 320)  # Ensure the food does not appear outside the screen
        ran_y = random.randint(-320, 320)
        self.goto(ran_x, ran_y)  # Place the food at the new position
