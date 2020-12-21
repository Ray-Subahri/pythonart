import turtle



wn = turtle.Screen()
wn.setup(420, 320)
wn.bgcolor("black")

t = turtle.Turtle()
t.pencolor("red")
t.pensize(4)
t.shape("circle")
t.speed(30)

n = 0

while n < 7:
    n = n + 1
    t.penup()
    t.setpos(0, -n * 20)
    t.pendown()
    t.circle(20 * n)
    t.stamp()

wn.exitonclick()