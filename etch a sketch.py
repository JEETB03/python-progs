from turtle import Turtle, Screen

jb = Turtle()
screen = Screen()

def move_forward():
    jb.forward(10)
    
def move_backward():
    jb.backward(10)
    
def move_left():
    new_left = jb.heading() + 10
    jb.setheading(new_left)
    
def move_right():
    new_right = jb.heading() - 10
    jb.setheading(new_right)    
    
def clear():
    jb.clear()
    jb.penup()
    jb.home()
    jb.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()