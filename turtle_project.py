#turtle_project.py nrg

import tkinter as tk
import turtle

def star(t,x,y):
    t.goto(x,y)
    for x in range (0,1440,15):
        t.color('#ff0000')
        t.width(1)
        t.forward(x + 0.5)
        t.left(151)




def work():
    tw = turtle.Screen()
    tw.clear()
    t = turtle.Turtle()
    t.width(3)
    # *******************
    star(t,10,10)

    tw.exitonclick()

work()
