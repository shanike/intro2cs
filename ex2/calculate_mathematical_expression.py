#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex2
# DESCRIPTION: calculate value of a provided str mathematival expression
#################################################################
PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE1 = "/"
DIVIDE2 = ":"


def calculate_mathematical_expression(num1, num2, operator):
    """
    :param num1: int or float
    :param num2: int or float
    :param operator: one of the following: '+' ,'-' ,'*' ,' :'
    :return: calculated value of operator on num1 and num2
    """
    num2 = float(num2)
    num1 = float(num1)
    if operator == PLUS:
        return num1 + num2
    elif operator == TIMES:
        return num1 * num2
    elif operator == DIVIDE1 or operator == DIVIDE2:
        if not num2:
            return
        return num1 / num2
    elif operator == MINUS:
        return num1 - num2
    return


def calculate_from_string(strr):
    """
    calculates the mathematical expression in the given string variable
    :param strr: <number><space><operation><space><number>
    :return: the value of the given mathematical expression
    """
    split_str = strr.split()
    return calculate_mathematical_expression(split_str[0], split_str[2], split_str[1])


print(calculate_mathematical_expression(0, -1, '/'))
