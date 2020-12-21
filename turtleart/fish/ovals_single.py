import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.title('Oval with 4 Arcs - PythonTurtle.Academy')
turtle.speed(1)
turtle.shape('turtle')


turtle.up()
turtle.goto(-140, -75)
turtle.down()
turtle.seth(-45)
turtle.color('red')
turtle.circle(200, 90)

print(turtle.heading()) # 45°

turtle.color('blue')
turtle.circle(100, 90)

print(turtle.heading()) # 135°

turtle.color('red')
turtle.circle(200, 90)

print(turtle.heading()) # 225°

turtle.color('blue')
turtle.circle(100, 90)

print(turtle.heading()) # 315° (= -45°)





turtle.done()