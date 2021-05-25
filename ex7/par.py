from collections import Counter

OPENING_P = "("
CLOSING_P = ")"


def parentheses(n):
    """returns <n> valid parentheses pairs

    Args:
        n (int): >= 0
    """
    return _parentheses_helper(n)


def _parentheses_helper(n, p_str=""):
    """recursively adds parentheses to a building-valid-parentheses-expression (<p_str>)
    until finished adding all expressions for <n> pairs of parentheses

    Args:
        n (int): num of parenthese paris
        p_str (str)
    """
    res1, res2 = [], []
    still_going = False
    can_open = can_add_opening_par(p_str, n)
    can_close = can_add_closing_par(p_str, n)
    if can_open:
        still_going = True
        res1 = _parentheses_helper(n, p_str + OPENING_P)
    if can_close:
        still_going = True
        res2 = _parentheses_helper(n, p_str + CLOSING_P)

    if still_going:
        # we're on the way back to root,
        # merge results
        return res1 + res2

    # got to end of tree
    # none are possible (neither open nor close)
    return [p_str]


def can_add_opening_par(p_str, n):
    p_counter = Counter(p_str)
    return p_counter[OPENING_P] < n


def can_add_closing_par(p_str, n):
    if not p_str:
        return False
    p_counter = Counter(p_str)
    return p_counter[OPENING_P] > p_counter[CLOSING_P] and p_counter[CLOSING_P] < n


res = parentheses(3)
