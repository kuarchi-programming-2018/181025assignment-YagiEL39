# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
a=input().split(" ")

from turtle import *
pencolor('powderblue')
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
done()