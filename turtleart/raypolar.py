#Polarlicht
from turtle import *
i = 0
f=0
d=500
speed(0)
colormode(255)
bgcolor(255,255,0)
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
#TODO research screen methods (e.g. go to left border of screen)
goto(-400,-100)
pendown()

# block mit horizontalem farbverlauf
e = 0
height = -100
while i <= 300:
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
done()
