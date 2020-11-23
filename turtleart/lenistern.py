from turtle import *

bgcolor("purple")
pencolor("pink")

fillcolor("blue")
begin_fill()

for leni in range(10):
    forward(100)
    right(108)
end_fill()

penup()
goto(-200,200)
pendown()
fillcolor("green")
begin_fill()

for leni in range(10):
    forward(100)
    right(108)
end_fill()


done()

