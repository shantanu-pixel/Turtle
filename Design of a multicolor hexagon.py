# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:12:52 2021

@author: SHANTANU GARAIN
"""

import turtle
colors = ["red", "purple", "blue", 
          "green", "orange", "yellow"]
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)