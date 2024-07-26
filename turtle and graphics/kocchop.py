from turtle import Turtle, Screen
import random

kocchop = Turtle()
kocchop.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#direction = [0, 90, 180, 270]
             ## 0 = East, 90 = North, 180 = West, 270 = South

# kocchop.forward(10)
# kocchop.penup()
# kocchop.forward(10)                ##For dotted line
# kocchop.pendown()
# kocchop.forward(10)
# kocchop.penup()
# kocchop.forward(10)
# kocchop.pendown()
# kocchop.forward(10)
# kocchop.penup()
# kocchop.forward(10)
# kocchop.pendown()


# kocchop.right(75) 
# kocchop.forward(100) 
  
# for i in range(4):               ## For Star shape
#     kocchop.right(144) 
#     kocchop.forward(100) 
      
# kocchop.done() 


# num_sides = 3
# side_length = 70
# angle = 360.0 / num_sides  
  
# for i in range(num_sides): 
#     kocchop.forward(side_length)        ## For any 2d shape having 3 or more sides
#     kocchop.right(angle) 
      
# kocchop.done() 


# for _ in range(300):
#     kocchop.color(random.choice(colors))
#     kocchop.forward(30)                                 ## Random color and random walk
#     kocchop.setheading(random.choice(direction))
#     kocchop.pensize(10)
    
kocchop.speed("fastest")


# def spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         kocchop.color(random.choice(colors))
#         kocchop.circle(100)                                   ##Spirograph
#         kocchop.setheading(kocchop.heading() + size_of_gap)
        
# spirograph(10)




screen = Screen()
screen.exitonclick()
