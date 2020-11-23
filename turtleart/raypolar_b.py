#Polarlicht
from turtle import *
e = 0
height = -100

penup()
goto(-400,-100)
pendown()


    pencolor(0,0+e*2,0+e)
    fillcolor(0,0+e*2,0+e)
    begin_fill()
    goto(400,height)
    goto(400,-500)
    goto(-400,-500)
    goto(-400,height)
    end_fill()
    i=i+5
    height=height-5

hideturtle()