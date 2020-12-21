import turtle as T
import math

T.width (5)

amplitude = 30
frequency = 6
frequency2 = 7

T.penup()
T.goto(-300,0)
T.pendown()

for i in range (-300,300,frequency):
    y = (math.sin(i))* (2*math.pi*amplitude)
    T.goto(i,y)

T.pencolor ("red")
T.penup()
T.goto (-300,0)
T.pendown()

for i in range (-300,300,frequency2):
    y = (math.sin(i))* (2*math.pi*amplitude)
    T.goto(i,y)

T.hideturtle()