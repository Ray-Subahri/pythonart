from turtle import *

screen = Screen()
screen.setup(800, 500)
screen.title('Fischkörper')
speed(10)
hideturtle()

def koerper(x, y, big_radius, small_radius, tilt):
    up()
    goto(x, y)
    down()
    seth(-45 + tilt)
    color('red')
    circle(big_radius, 90)
    print(heading()) # 45°
    color('blue')
    circle(small_radius, 90)
    print(heading()) # 135°
    print(pos())
    color('red')
    circle(big_radius, 90)
    print(heading()) # 225°
    color('blue')
    circle(small_radius, 90)
    print(heading()) # 315° (= -45°)

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

koerper(-200, 0, 300, 10, 0)
schwanzflosse()

done()