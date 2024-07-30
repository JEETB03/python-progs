from turtle import Turtle

# Constants for movement directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Initial positions of the snake segments
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20  # Distance the snake moves with each step

class Snake:
    """Manages the snake's behavior and movement."""
    
    def __init__(self):
        self.segments = []  # List to hold the snake's body segments
        self.create_snake()
        self.head = self.segments[0]  # The head of the snake is the first segment

    def create_snake(self):
        """Create the initial snake with its starting segments."""
        for position in starting_positions:
            self.add_seg(position)
          
    def add_seg(self, position):
        """Add a new segment to the snake's body."""
        new_seg = Turtle(shape="square")  # Create a new segment
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)  # Place the segment at the given position
        self.segments.append(new_seg)
    
    def body_extend(self):
        """Add a new segment to the end of the snake's body."""
        self.add_seg(self.segments[-1].position())  # Extend the snake from the last segment
        

    def move(self):
        """Move the snake forward and update the position of each segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Move each segment to the position of the previous segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)  # Move the head forward

    def up(self):
        """Change the snake's direction to up, if not already moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down, if not already moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left, if not already moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right, if not already moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
