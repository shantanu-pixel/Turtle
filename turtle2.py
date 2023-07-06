# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:54:25 2021

@author: SHANTANU GARAIN
"""

from turtle import *
#cLcoding
from random import randint
bgcolor('black')
x = 1
speed(0)
while x < 400:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    colormode(255)
    pencolor(r,g,b)
    fd(50 + x)
    rt(90.991)
    x = x+1