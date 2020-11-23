from turtle import *

fillcolor("red")

begin_fill()
for a in range(10):
    forward(100)
    left(108)
end_fill()    
    
penup()
goto(0,-120)
pendown()

fillcolor("yellow")

begin_fill()
for a in range(10):
    forward(100)
    left(108)
end_fill()

done()