import turtle

turtle.speed(5)

for side_length in range(50, 100, 10):
    for i in range(8):
        turtle.forward(side_length)
        turtle.left(45)
turtle.exitonclick()