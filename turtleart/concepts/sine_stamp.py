from turtle import *
import math


j = 0

shape("circle")
penup()



for i in range(-180, 181):
    goto(i, math.cos(math.radians(i)) * 100) 
    if j % 20 == 0:
        stamp()
    j = j + 1



done()