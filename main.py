from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet the Winner", prompt="Who will win the race, pick the color.")

all_turtles =[]
y_positions = [-60, -20, 20, 60, 100, 140]
colors = ["green", "violet", "blue", "red", "yellow", "red"]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You Won!")
            else:
                print("You Loose!")



screen.exitonclick()