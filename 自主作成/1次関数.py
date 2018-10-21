# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 10:27:10 2018

@author: yagie
"""
a=input().split(",")
#a=[傾き,y切片]
import math as m
from turtle import *
def axis():
    pencolor('red')
    for i in range(4):
        fd(300)
        lt(90)
        penup()
        setpos(0,0)
        pendown()
def function(x,y):
    pencolor('black')
    lt(m.degrees(m.atan(x)))
    penup()
    setpos(0,y)
    pendown()
    fd(300)
    bk(600)
axis()
function(int(a[0]),int(a[1]))
done()
if int(a[0])!=0:
    if int(a[1])>0:
        print("y="+a[0]+"x+"+a[1])
    elif int(a[1])==0:
            print("y="+a[0]+"x")
    else:
        print("y="+a[0]+"x"+a[1])
else:
    print("y="+a[1])
    