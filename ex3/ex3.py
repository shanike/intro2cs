# RESOURCES: https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops


# todo: check
def input_list():
    num_arr = []
    sum = 0
    while True:
        num = input("")
        if not num or not len(num):
            break
        num = float(num)
        num_arr.append(num)
        sum += num
    num_arr.append(sum)
    return num_arr


# todo: check
def inner_product(vec1, vec2):
    inner_product_sum = 0
    if len(vec1) != len(vec2):
        return None
    if not len(vec1):  # length of vec1 and of vec2 are 0 (len(vec1) == len(vec2))
        return 0
    for i, num1 in enumerate(vec1):
        inner_product_sum += num1 * vec2[i]

    return inner_product_sum


if __name__ == '__main__':
    # print(input_list())
    def factorial_list(n):
        list = []
        for first_i in range(1, n + 1):  # 1 / 2 / 3 / 4
            inner_list = []
            for inner_i in range(1, first_i + 1):  # 1: 1, 2: 1 / 2
                inner_list.append(inner_i)
            list.append(inner_list)
        return list


    print("helllllo: ", factorial_list(4))
