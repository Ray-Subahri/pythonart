from turtle import *
from random import randint


speed(14)

laenge = 300
colormode(255)
bgcolor(39, 66, 111)

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
 


def kugel():
    rot = [202, 48, 48]
    blau = [ 19, 101, 255 ]
    lila = [ 125, 60, 152 ]
    d_gruen = [ 31, 102, 22 ]
    magenta = [ 201, 36, 178 ]
    cyan = [ 18, 216, 255 ]
    farbliste = [rot, blau, lila, d_gruen, magenta, cyan]

    kugelfarbe = farbliste[randint(0, len(farbliste) -1)]
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

pencolor("white")
fillcolor("white")
jumpto(-600, -250)
begin_fill()
goto(600, -250)
goto(600, -670)
goto(-600, -670)
end_fill()

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


#### Girlande
pencolor("yellow")
pensize(2)

jumpto(-138, -180)
setheading(towards(120, -150))
right(9.7)
circle(800, 18.8)
setheading(towards(-100, -48))
left(10)
circle(-700, 20)
goto(-100, -48)
setheading(towards(82.80, 38.4))
right(10)
circle(600, 19)
goto(82.80, 38.4)
setheading(towards(-67.44, 108))
left(10)
circle(-500, 18)
goto(-67.44, 108)
setheading(towards(54, 165))
right(10)
circle(400, 17)
goto(54, 165)
setheading(towards(-46, 178))
left(10)
circle(-300,15)
goto(-46, 178)


#### Kugeln platzieren

jumpto(-80, -195)
kugel()

jumpto(100, -200)
kugel()

jumpto(-100, -140)
kugel()

jumpto(-30, -100)
kugel()

jumpto(40, -80)
kugel()

jumpto(-60, -60)
kugel()



jumpto(50, 0)
kugel()

jumpto(-30, 40)
kugel()

jumpto(30, 85)
kugel()

jumpto(-20, 160)
kugel()

jumpto(20, 200)
kugel()

###


hideturtle()
done()