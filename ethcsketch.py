from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clockwise():
    tim.left(20)

def anticlockwise():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(move_forward, "d")
screen.onkey(move_backward, "a")
screen.onkey(clockwise, "w")
screen.onkey(anticlockwise, "s")
screen.onkey(clear, "c")
screen.exitonclick()
