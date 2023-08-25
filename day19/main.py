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



import random
import turtle
from turtle import  Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race")
print(user_bet)
number_turtles = 6
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

is_race_on = False

for i in range(0,6):
    x = Turtle(shape="turtle")
    x.color(colors[i])
    x.penup()
    x.goto(x=-230,y=y_positions[i])
    all_turtles.append(x)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 230:
            is_race_on = False
            if turtle.color() == user_bet:
                print(f"You won the race, turtle with {turtle.color()} won the race")
            else:
                print(f"You lost the race, turtle with {turtle.color()} won the race")
        turtle.forward(random.randint(0,10))

