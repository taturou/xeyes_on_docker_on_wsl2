from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.setup(width=600, height=600)

def move_forward():
    tim.forward(10)

def move_back():
    tim.back(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def reset():
    tim.reset()

screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_back)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
#