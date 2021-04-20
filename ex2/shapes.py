#################################################################
# FILE : shapes.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex2
# DESCRIPTION: calculate area of a selected shape
#################################################################

import math


def calc_circle():
    radius = float(input(""))
    return math.pi * (radius ** 2)


def calc_rect():
    a = float(input(""))
    b = float(input(""))
    return a * b


def calc_triangle():
    a = float(input(""))
    return ((a ** 2) * math.sqrt(3)) / 4


CIRCLE = 1
RECTANGLE = 2
TRIANGLE = 3


def shape_area():
    chosen_val = int(input('Choose shape (1=circle, 2=rectangle, 3=triangle): '))
    if chosen_val == CIRCLE:
        return calc_circle()
    if chosen_val == RECTANGLE:
        return calc_rect()
    if chosen_val == TRIANGLE:
        return calc_triangle()
