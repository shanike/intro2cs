#################################################################
# FILE : math_print.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: A simple program with 6 useful math functions
# WEB PAGES I USED: https://docs.python.org/3/library/math.html
#################################################################


import math


def golden_ratio():
    """prints the golden ratio which is ( 1 + sqrt of 5 ) / 2"""
    print((1 + math.sqrt(5)) / 2)


def six_squared():
    """prints the the value of 6^2"""
    print(pow(6, 2))  # using pow and not math.pow bcos we want an int and not a float value


def hypotenuse():
    """prints the hypotenuse of a right-angled triangle in which the legs are 12 and 5"""
    tzela1, tzela2 = 12, 5
    print(math.sqrt(math.pow(tzela1, 2) + math.pow(tzela2, 2)))  # square root of 12^2 plus 5^2


def pi():
    print(math.pi)


def e():
    print(math.e)


def squares_area():
    squares_area_str = ""
    for tzela in range(1, 11):
        squares_area_str += str(tzela * tzela) + " "
    print(squares_area_str[:-1])


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
