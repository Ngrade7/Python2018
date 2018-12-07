# plot-dictionary.py nrg
import tkinter as tk
import turtle

def main():
	#table is a dictionary
	table = {-100:27.5, -90:25, -80:22.5,-70:20, -60:17.5,-50:15, -40:12.5, 
				-30:10, -20:7.5, -10:5, 0:0, 10:-5, 20:-7.5, 
				30:-10, 40:-12.5, 50:-15, 60:-17.5, 70:-20, 
				80:-22.5, 90:-25, 100:-27.5}
				
	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	#turtle graphics
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#twin = turtle.Screen()
	for h,k in table.items(): # get the items in the directionary
		print(h, k) # trace code
		#x,y = table[n]
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(5)
	twin.exitonclick()
	
main()

""" 
This code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
Each key has a value of - as an integer.
To retrieve the values in the dictionary "table" a for loop is used.
The x coordinate on a python turtle screen corresponds to a h while
the y value cooresponds to k.
*********************************
for h,k in table.items():  #get the items in teh dictionary 
		print(h,k) #trace code
h and k are then ploted using
		t.goto(h,k)
		t.pendown()
		t.circle(5)
"""
