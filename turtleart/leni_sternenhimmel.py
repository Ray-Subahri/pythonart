from turtle import *

bgcolor("black")
pencolor("yellow")

speed(0)

distance = 130
radius = 220
for stars in range(100):
    fillcolor("yellow")
    begin_fill()
    for a in range(10):
        
        forward(45)
        right(108)
    end_fill()
    right(radius)
    radius = radius - (radius*0.1)
    distance = distance + (distance*0.1)
    penup()
    forward(distance)
    pendown()

done()