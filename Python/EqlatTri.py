import turtle

def tri(n):
    turtle.speed(10)
    for i in range(3):
        turtle.forward(n)
        turtle.left(120)

len = input("Please enter length of one side of Equilateral Triangle")
len = int(len)
print(tri(len))

turtle.exitonclick()