#################################################################
# FILE : larges_and_smallest.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex2
# DESCRIPTION: largest_and_smallest func returns largest and smallest values out of the 3 given numbers
# last checks in check_largest_and_smallest func checks the cases of:
# negative numbers, zero, numbers in order and high numbers
#################################################################

def largest_and_smallest(n1, n2, n3):
    """
    gets 3 numbers (n1, n2, n3)
    returns: the largest and the smallest of them
    """
    max_n = n1
    min_n = n1

    if n2 > max_n:
        max_n = n2
    elif n2 < min_n:
        min_n = n2

    if n3 > max_n:
        max_n = n3
    elif n3 < min_n:
        min_n = n3

    return max_n, min_n


def check_largest_and_smallest() -> bool:
    """
    tests largest_and_smallest func
    """
    largest, smallest = largest_and_smallest(17, 1, 6)
    if largest != 17 or smallest != 1:
        return False

    largest, smallest = largest_and_smallest(1, 17, 16)
    if largest != 17 or smallest != 1:
        return False

    largest, smallest = largest_and_smallest(1, 1, 2)
    if largest != 2 or smallest != 1:
        return False

    largest, smallest = largest_and_smallest(-1, 1, 0)
    if largest != 1 or smallest != -1:
        return False

    largest, smallest = largest_and_smallest(-9, 0, 1000)
    if largest != 1000 or smallest != -9:
        return False

    return True


if __name__ == "__main__":
    print(check_largest_and_smallest())
