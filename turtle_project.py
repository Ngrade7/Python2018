#turtle_project.py nrg

import tkinter as tk
import turtle

def star(t,x,y):
    t.goto(x,y)
    for x in range (0,540,5):
        t.color('#ff0000')
        t.width(1.5)
        t.forward(x + 0.5)
        t.left(151)
        t.speed(0)

def stem(t,x,y):
    t.goto(x,y)
    for x in range (0,360,-100):
        t.color('#00ff00')
        t.width(5)
        t.forward(0)
        t.down(400)


def work():
    tw = turtle.Screen()
    tw.clear()
    t = turtle.Turtle()
    t.width(5)
    # *******************
    star(t,0,0)
    stem(t,0,-100)


    tw.exitonclick()

work()
