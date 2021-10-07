#!/usr/bin/env python3
from datetime import datetime
import turtle

clock = turtle.Turtle()
hour = turtle.Turtle()
min = turtle.Turtle()
my_screen = turtle.Screen()
clock.speed(0)
hour.speed(0)
clock.penup()
clock.setposition(0, 200)
clock.pendown()
clock.ht()
for i in range(12):
    clock.penup()
    clock.circle(-200, 5)
    clock.pendown()
    clock.circle(-200, 20)
    clock.penup()
    clock.circle(-200, 5)
    clock.write(str(i+1), False, align="Center")


turtle.done()