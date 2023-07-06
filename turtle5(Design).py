# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 00:15:35 2022

@author: SHANTANU GARAIN
"""

from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(500):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)
done()