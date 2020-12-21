#Polarlicht
from turtle import *
from random import randint

i = 0
f=0
d=500
speed(0)

pensize(randint(2, 3))
colormode(255)
bgcolor(0,255,0)
penup()
goto(0,-550)
pendown()
while i <= 600:
    pencolor(255,255-f*2,0+f)
    fillcolor(255,255-f*2,0+f)
    begin_fill()
    circle(d,360)
    end_fill()
    i=i+5
    f=f+1
    d=d-2
penup()



# turn randomly left or right to a random degree
def turn(number):
    degree = randint(30, 170)
    if number == 0:
        right(degree)
    else:
        left(degree)

# change pencolor and fillcolor randomly   
def randomcolor():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    fillcolor(red, green, blue)
    pencolor(red, green, blue)

# paint a randomly colored flower with different fillcolor and pencolor
def flower():
    i = 0
    j = 0
    size = randint(12, 19)
    while i <= 360:
        begin_fill()
        circle(size, 360)
        left(60)
        i=i+60
        end_fill()
    randomcolor()
    while j <= 360:
        circle(size, 360)
        left(60)
        j=j+60
        

# main program:
# paint a field of flower while staying in a certain range and providing location-data
for number_lines in range(30):
    penup()
    if distance(0, 0) > 300:
        setheading(towards(0, 0)+(randint(10, 60)))
        forward(randint(100, 250))
        pendown()
        randomcolor()
        flower()
        print("let's go back!")
        print(position())
    else:
        forward(randint(100, 250))
        pendown()
        randomcolor()
        flower()
        turn(randint(0, 1))
        print(position())

hideturtle()
done()
