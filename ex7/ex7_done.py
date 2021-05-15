def print_to_n(n):
    """
    recursively prints all numbers from 1 to n
    """
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


def digit_sum(n):
    """
    :param n: non-negative number
    :returns: sum of digits
    """
    if n <= 0:
        return n
    return n % 10 + digit_sum(int(n / 10))


def is_prime(n):
    """ checks whether <n> is a prime number
    Args:
        n (int): bigger than 1
    Returns:
        boolean
    """
    return not has_divisor_smaller_than(n, int(n ** 0.5)+1)  # check whehter n has a divisor
    # if True -> n is not a prime
    # else, if False -> n is a prime cos he has no divisors


def has_divisor_smaller_than(n, k):
    if k <= 1:
        return False
    if n % k == 0:
        return True
    return has_divisor_smaller_than(n, k - 1)
