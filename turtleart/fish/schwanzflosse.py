from turtle import *



screen = Screen()
screen.setup(800, 500)
screen.title('Schwanzflosse')
speed(5)
hideturtle()

def schwanzflosse():
    up()
    goto(224.26,14.14)
    down()
    fillcolor("green")
    begin_fill()
    left(20)
    forward(70)
    right(140)
    forward(50)
    left(80)
    forward(50)
    right(150)
    forward(80)
    goto(224.26,14.14)
    end_fill()


done()
