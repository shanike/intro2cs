#################################################################
# FILE : ex7.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex7
#################################################################


"""
#################
### print_to_n ###
#################
"""


from collections import Counter


def print_to_n(n):
    """
    recursively prints all numbers from 1 to n
    """
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


"""
#################
### digit_sum ###
#################
"""


def digit_sum(n):
    """
    :param n: non-negative number
    :returns: sum of digits
    """
    if n <= 0:
        return n
    return n % 10 + digit_sum(int(n / 10))


"""
################
### is_prime ###
################
"""


def is_prime(n):
    """ checks whether <n> is a prime number
    Args:
        n (int): bigger than 1
    Returns:
        boolean
    """
    if n <= 1:
        return False  # a prime number is bigger than 1
    # check whehter n has a divisor
    return not has_divisor_smaller_than(n, int(n ** 0.5)+1)
    # if True -> n is not a prime
    # else, if False -> n is a prime cos he has no divisors


"""
################################
### has_divisor_smaller_than ###
################################
"""


def has_divisor_smaller_than(n, k):
    if k <= 1:
        return False
    if n % k == 0:
        return True
    return has_divisor_smaller_than(n, k - 1)


"""
######################
### print_sequences ###
######################
"""


def print_sequences(char_list, n, seq=""):
    """prints all sequence options of <n> chars from <char_list>
    """

    # need to add chars to a string many times, till string is as long as n. will add chars to it, according to
    # interate over <char_list>. for each char iterate over <char_list> while concatenating chars to the string,
    # till string is as long as <n> -> print string
    #

    if len(seq) == n:
        print(seq)
        return

    for c in char_list:
        print_sequences(char_list, n, seq+c)


"""
####################################
### print_no_repetition_sequences ###
####################################
"""


def print_no_repetition_sequences(char_list, n, seq=""):
    """prints all sequence options of <n> unique chars from <char_list>
    """

    # tested efficiency compared to:
    """
    if c in seq:
        continue
    """
    # showed that it might take less time, but will have more iterations over char_list and over the whole recursion

    if len(seq) == n:
        print(seq)
        return

    for i in range(len(char_list)):
        c = char_list[i]
        print_no_repetition_sequences(
            list_without_char(char_list, i), n, seq+c)


def list_without_char(char_list, index_to_remove):
    new_char_list = char_list[:]
    del new_char_list[index_to_remove]
    return new_char_list
    # [char_in_list for char_in_list in char_list if char_in_list != char_to_remove]


"""
###################
### parentheses ###
###################
"""


OPENING_P = "("
CLOSING_P = ")"


def parentheses(n):
    """returns <n> valid parentheses pairs

    Args:
        n (int): >= 0
    """
    return _parentheses_helper(n)


def _parentheses_helper(n):
    """recursively adds parentheses to a building-valid-parentheses-expression (<p_str>)
    until finished adding all expressions for <n> pairs of parentheses

    Args:
        n (int): num of parenthese paris
        p_str (str)
    """
    if n < 1:
        return [""]

    prevs = _parentheses_helper(n-1)
    print('prevs: ', prevs);

    for i, prev in enumerate(prevs):  # (())
        print('prev: ', prev);
        p_str = ""
        cnt = 0
        for j, prev_p in enumerate(prev):  # (
            print('prev_p: ', prev_p);
            if prev_p == OPENING_P:
                cnt += 1
            else:
                cnt -= 1
            p_str += prev_p
            if cnt == 0:
                p_str += CLOSING_P
        p_str = OPENING_P + p_str
        prevs[i] = p_str

    return prevs
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

print("RETURNED:", parentheses(3))

def can_add_opening_par(p_str, n):
    p_counter = Counter(p_str)
    return p_counter[OPENING_P] < n


def can_add_closing_par(p_str, n):
    if not p_str:
        return False
    p_counter = Counter(p_str)
    return p_counter[OPENING_P] > p_counter[CLOSING_P] and p_counter[CLOSING_P] < n


"""
##################
### flood_fill ###
##################
"""

NEIGHBORS_POS_BY_CNT = {
    "0": (0, 0),  # me
    "1": (-1, 0),
    "2": (1, 1),
    "3": (1, -1),
    "4": (-1, -1),
}


def flood_fill(image, start):
    """
    floods an image with water (;
    will flood current position if empty and previous position's neighbors if empty
    * fill == '*'
    * empty == '.'

    Args:
        image (matrix): [[str]] that is filled with '*' and '.' with a '*' border
        start (tuple of row_idx, column_idx): is an empty cell to start the flood from
    """
    image[start[0]][start[1]] = "*"  # update start
    # update neighbors (doesn't check emptiness of <start>)
    update_neighbors(image, start)


def update_neighbors(image, start, cnt=0):
    """check 4 neighbors and if one is empty, start checking it's neighbors
    will stop when checked 4 neighbors
    """
    if cnt > 4:  # me + 4 dirs
        return

    pos_to_check = get_next_pos(start, cnt)

    # always in borders of image bcos the מסגרת is astrids
    if image[pos_to_check[0]][pos_to_check[1]] == ".":
        print(f"{pos_to_check} is a . ")
        image[pos_to_check[0]][pos_to_check[1]] = "*"
        # start nother update circle, but don't include me
        update_neighbors(image, pos_to_check, 1)

    # need to inc start values for each of 4 directions
    update_neighbors(image, pos_to_check, cnt + 1)


def get_next_pos(curr_pos_t, cnt):
    """returns position of next neighbor

    Args:
        curr_pos_t (like <start>)
        cnt (int)
    """
    curr_and_neighbor = zip(curr_pos_t, NEIGHBORS_POS_BY_CNT[str(cnt)])
    # get position of neighbor by adding NEIGHBORS_POS_BY_CNT[cnt] values to each current position values respectively
    next_pos = tuple([curr_pos + get_to_neighbor_pos for curr_pos,
                     get_to_neighbor_pos in curr_and_neighbor])
    return next_pos


def play_hanoi(hanoi, n, src, dst, temp):

    if n < 1:
        return

    play_hanoi(hanoi, n-1, src, temp, dst)

    hanoi.move(src_tower=src, dest_tower=dst)

    play_hanoi(hanoi, n-1, temp, dst, src)
