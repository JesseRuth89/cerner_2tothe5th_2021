#!/usr/bin/env python3
from datetime import datetime
import turtle
from time import sleep

def define_clock():
    clock = turtle.Turtle()
    clock.ht()
    clock.speed(0)
    clock.penup()
    clock.setposition(0, 200)
    clock.pendown()
    for i in range(12):
        clock.penup()
        clock.circle(-200, 5)
        clock.pendown()
        clock.circle(-200, 20)
        clock.penup()
        clock.circle(-200, 5)
        clock.write(str(i+1), False, align="Center")
    clock.penup()
    clock.left(90)
    clock.forward(30)
    clock.write("Analog Clock", False, align="Center")

def hour_hand():
    hr = turtle.Turtle()
    hr.ht()
    hr.degrees(360)
    hr.penup()
    hr.left(90)
    hr.right((30 * datetime.now().hour) + (.5 * datetime.now().minute))
    hr.pensize(5)
    hr.pendown()
    hr.forward(100)

def minute_hand():
    min = turtle.Turtle()
    min.ht()
    min.pensize(3)
    min.degrees(360)
    min.left(90)
    min.right(6 * datetime.now().minute)
    min.forward(180)

def load_clock():
    define_clock()
    hour_hand()
    minute_hand()

if __name__ == '__main__':
    while True:
        my_screen = turtle.Screen()
        load_clock()
        turtle.done()
        sleep(60)
