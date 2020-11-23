from turtle import *

speed(0)
width = Screen().window_width()
height = Screen().window_height()
x = width/2
y = height/2
f = 0
colormode(255)
bgcolor(255,255,0)

topleftcorner = (-x, y)
toprightcorner = (x, y)
botleftcorner = (-(x), -(y))
botrightcorner = (x, -(y))

goto(-x, y)
for i in range(250):
    pencolor(255,255-f,0+f)
    fillcolor(255,255-f,0+f)
    begin_fill()
    goto(x, y)
    goto(x, -(y))
    goto(-(x), -(y))
    goto(-x, y)
    end_fill()
    y = y - 2
    f = f + 2

hideturtle()
done()