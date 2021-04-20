#################################################################
# FILE : larges_and_smallest.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex2
# DESCRIPTION: calculate quadratic equation according to parameters from user
#################################################################

import math


def quadratic_equation(a, b, c):
    """
    calculates a quadratic equation according to given numbers: a, b and c
    returns two values: either 2 numbers, or a number and None, or 2 Nones
    """
    inside_sqrt = (b ** 2) - (4 * a * c)
    if inside_sqrt < 0:
        return None, None
    res1 = ((0 - b) + math.sqrt(inside_sqrt)) / (2 * a)
    if inside_sqrt == 0:
        return res1, None
    res2 = ((0 - b) - math.sqrt(inside_sqrt)) / (2 * a)
    return res1, res2


def quadratic_equation_user_input():
    """
    calculates a quadratic equation according to 3 numbers given by the user
    then, prints the solution(s)
    """
    user_input = input("Insert coefficients a, b, and c: ")
    n1, n2, n3 = user_input.split(" ")  # split user_input on space, placing all characters from user in an array
    n1, n2, n3 = float(n1), float(n2), float(n3)
    if n1 == 0:
        print("The parameter 'a' may not equal 0")
        return
    res1, res2 = quadratic_equation(float(n1), float(n2), float(n3))
    if res1 is not None and res2 is not None:
        print(f"The equation has 2 solutions: {res1} and {res2}")
        return
    elif res1 is not None:
        print(f"The equation has 1 solution: {res1}")
        return
    print("The equation has no solutions")


if __name__ == "__main__":
    quadratic_equation_user_input()
