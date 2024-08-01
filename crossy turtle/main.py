import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

## Screen configurations
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

## Object Declaration
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

## Listening for keystrokes
screen.listen()
screen.onkey(player.move_up, "space")

game_is_on = True

while game_is_on:
    """Game continuation logic"""
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    ## Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break
    
    ## Check if player reached the finish line and move to next level
    if player.finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
