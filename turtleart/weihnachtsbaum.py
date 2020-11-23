from turtle import *


# Geschwindigkeit
speed(10)

# Anleitung zum Tannenbaum
def tannenbaum():
    pensize(30)
    pencolor("brown")
    left(90)
    forward(60)
    right(90)
    fillcolor("green")
    pencolor("green")
    begin_fill()
    for hfgue in range(3):
        forward(60)
        left(120)
        forward(120)
        left(120)
        forward(120)
        left(120)
        forward(60)
        left(90)
        forward(60)
        right(90)
    end_fill()

# Hier wird das Bild gemalt (5 Tannenbäume auf einer Wiese)
bgcolor("#97ff00")

tannenbaum()

penup()
goto(200,-100)
pendown()
tannenbaum()

penup()
goto(-200,-100)
pendown()
tannenbaum()

penup()
goto(400,0)
pendown()
tannenbaum()

penup()
goto(-400,0)
pendown()
tannenbaum()


done()