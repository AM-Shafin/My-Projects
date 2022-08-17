from itertools import count
import turtle

turtle.color("orange")
turtle.speed(6)
turtle.bgcolor("black")
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1

turtle.exitonclick()