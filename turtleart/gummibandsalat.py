from turtle import *
from random import randint

speed(0)
colormode(255)
bgcolor(255, 195, 0)
pensize(randint(2, 4))

def turn(number):
    degree = randint(30, 170)
    if number == 0:
        right(degree)
    else:
        left(degree)
        
def randomcolor():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    fillcolor(red, green, blue)
    pencolor(red, green, blue)

def flower():
    i = 0
    while i <= 360:
        circle(randint(16,60),360)
        left(30)
        i=i+30



for number_lines in range(100):
    penup()
    if distance(0, 0) > 200:
        setheading(towards(0, 0)+(randint(10, 40)))
        forward(randint(30, 120))
        pendown()
        randomcolor()
        flower()
        print("let's go back!")
        print(position())
    else:
        forward(randint(30, 120))
        pendown()
        randomcolor()
        flower()
        turn(randint(0, 1))
        print(position())
penup()
goto(0, 0)
hideturtle()
done()