from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup the game screen
screen = Screen()
screen.setup(width=700, height=700)  
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates for manual control

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key bindings for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")  
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    """Main game loop. Updates the screen and checks for collisions."""
    screen.update()
    time.sleep(0.1)  # Delay to control the speed of the game
    snake.move()
    
    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random position
        snake.body_extend()  # Extend the snake's body
        scoreboard.increase_score()  # Update the score
        
    # Check if the snake has hit the wall
    if (snake.head.xcor() > 340 or snake.head.xcor() < -340 or 
        snake.head.ycor() > 340 or snake.head.ycor() < -340):
            scoreboard.reset_score()
            snake.reset()
            
    # Check if the snake has collided with itself
    for segment in snake.segments[1:]:  # Skip checking collision with the head itself
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()

# Close the game window when clicked
screen.exitonclick()
