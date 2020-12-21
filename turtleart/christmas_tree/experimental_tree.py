from turtle import *
from random import randint


speed(20)

laenge = 300
bgcolor("cyan")

##########################################################
# 1. FUNKTIONEN

def tannenbaum():
    pensize(10)
    pencolor("brown")
    fillcolor("brown")
    begin_fill()
    forward(15)
    left(90)
    forward(60)
    left(90)
    forward(30)
    left(90)
    forward(60)
    left(90)
    forward(15)
    end_fill()
    left(90)
    forward(60)
    right(90)
    fillcolor("green")
    pencolor("green")
    begin_fill()
    for hfgue in range(5):
        global laenge
        dreieck(laenge)
        laenge = laenge - laenge / 5

    end_fill()


def dreieck(laenge):
    forward(laenge / 2)
    left(120)
    forward(laenge)
    left(120)
    forward(laenge)
    left(120)
    forward(laenge / 2)
    left(90)
    forward(laenge / 2.5)
    right(90)
    print(pos())
    kugel()


def kugel():
    kugelfarbe = "red"
    if randint(1, 2) == 1:
        kugelfarbe = "blue"
    pencolor(kugelfarbe)
    fillcolor(kugelfarbe)
    begin_fill()
    circle(15,360)
    end_fill()

def stern():
    zackenlaenge = 80
    pencolor("red")
    pensize(1)
    left(144)
    backward(zackenlaenge)
    forward(zackenlaenge)
    right(144)
    for zacken in range(45):
        forward(zackenlaenge)
        right(144)
        zackenlaenge = zackenlaenge -2
    
def jumpto(x, y):
    penup()
    goto(x, y)
    pendown()


##########################################################

# 2. AKTION
jumpto(0, -270)
tannenbaum()

jumpto(0,285)

penup()
backward(40)
fillcolor("yellow")
begin_fill()
pendown()
stern()
end_fill()



jumpto(100, -180)
kugel()
jumpto(-100, -180)
kugel()
jumpto(-20, -100)
kugel()
jumpto(-40, 10)
kugel()
jumpto(-20, 160)
kugel()
jumpto(30, 85)
kugel()
jumpto(-60, -60)
kugel()
jumpto(50, 0)
kugel()

hideturtle()
done()