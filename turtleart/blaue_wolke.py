#Farbverlauf
from turtle import *
bgcolor("orange")
# i = Schleifen-Zähler
i = 0
# f = Farbe
f=0
# d = Kreisgröße
d=100
speed(0)
colormode(255)
while i <= 3000:
    pencolor(12,255-f,255-f*2)
    fillcolor(12,255-f,255-f*2)
    begin_fill()
    circle(d,360)
    end_fill()
    left(30)
    i=i+30
    f=f+1
    d=d-1
hideturtle()

done()