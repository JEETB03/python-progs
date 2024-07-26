# import colorgram

# rgb_colors = []
# colors = colorgram.extract('1.jpg', 40)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g                           ##  To extract color from a picture.
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

import turtle as turtle_module
import random

hirst = turtle_module.Turtle()
turtle_module.colormode(255)
hirst.speed("fastest")  # Adjust speed as needed
hirst.penup()
hirst.hideturtle()

colors = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), 
          (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), 
          (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), 
          (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), 
          (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), 
          (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), 
          (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), 
          (15, 76, 110), (243, 15, 14), (38, 43, 221)]

hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)

# Adjust grid parameters
num_of_dots = 100
dot_distance = 50
dot_size = 20
num_dots_per_row = 10

for dot_count in range(1, num_of_dots + 1):
    hirst.dot(dot_size, random.choice(colors))
    hirst.forward(dot_distance)
    
    if dot_count % num_dots_per_row == 0:
        hirst.setheading(90)
        hirst.forward(dot_distance)
        hirst.setheading(180)
        hirst.forward(dot_distance * num_dots_per_row)
        hirst.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()