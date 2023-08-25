from turtle import  Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwoards():
    tim.backward(10)

def left_turn():
    tim.left(60)
def right_turn():
    tim.right(55)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    #

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwoards)
screen.onkey(key="a", fun=left_turn)
screen.onkey(key="d", fun=right_turn)
screen.onkey(key="c", fun=clear)
screen.exitonclick()


#more turtles
# class or blueprint
#Jimmy, tom, tommy, timmy
#
