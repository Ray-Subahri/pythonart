import turtle

screen = turtle.Screen()
screen.setup(800, 500)
screen.title('Fischkörper')
turtle.speed(10)
turtle.hideturtle()

def draw_oval(x, y, big_radius, small_radius, tilt):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(-45 + tilt)
    turtle.color('red')
    turtle.circle(big_radius, 90)
    print(turtle.heading()) # 45°
    turtle.color('blue')
    turtle.circle(small_radius, 90)
    print(turtle.heading()) # 135°
    print(turtle.pos())
    turtle.color('red')
    turtle.circle(big_radius, 90)
    print(turtle.heading()) # 225°
    turtle.color('blue')
    turtle.circle(small_radius, 90)
    print(turtle.heading()) # 315° (= -45°)

#draw_oval(-100, -100, 100, 50, 90)

draw_oval(-200, 0, 300, 10, 0)

#draw_oval(0, -200, 60, 30, 45)

turtle.done()