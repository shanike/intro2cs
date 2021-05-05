import sys
import os.path
from typing import Tuple

# types:
Result = Tuple[str, int]  # single result of list of results this file needs to output


def main():
    print("YO:", sys.argv)

    if len(sys.argv) != 5:  # ? 5 or 4?
        print("not good: arguments are not valid")
        exit()  # end of program

    wordlist = read_wordlist(sys.argv[1])  # if file doesn't exist, program will end
    [print(w) for w in wordlist]
    matrix = read_matrix(sys.argv[2])  # if file doesn't exist, program will end
    _print_matrix(matrix)
    dirs = sys.argv[4]
    print("-" * 30)
    results_dict = find_words(wordlist, matrix, dirs)
    print("FINAL: ", results_dict)


def _print_matrix(matrix):
    print("matrix:")
    print("[")
    for row in range(len(matrix)):
        print(" [", end=" ")
        for column in range(len(matrix[0])):
            print(f"{matrix[row][column]}", end=", ")
        print("]")
    print("]")


def read_wordlist(file_name: str):
    """ """
    with open(file_name, 'r') as word_file:
        if os.path.isfile(word_file.name):
            return [word.rstrip() for word in word_file]
        print("not good: word file does not exist")
        exit()  # end of program


def read_matrix(file_name):
    with open(file_name, 'r') as matrix_file:
        if os.path.isfile(matrix_file.name):
            return [row.rstrip().split(",") for row in matrix_file]
        print("not good: matrix file does not exist")
        exit()  # end of program


def find_words(word_list: [str], matrix: [[str]], directions: str) -> [Result]:
    """
    :param word_list: list of words to search
    :param matrix: 2d list representing the letter matrix: [ [ letter, letter ], [letter, letter] ]
    :param directions: part or all of: "udrlwxyz"
    :return: Result[] (== [ (word, count), (word, count) ]) a list of words from <word_list> and a count of their appearance in <matrix>
    """
    results_dict = {}
    dir_funcs = {
        "u": search_direction_u,
        "d": search_direction_d,
        "r": search_direction_r,
        "l": True,
        "w": True,
        "x": True,
        "y": True,
        "z": True
    }
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for user_direction in directions:
        print('user_direction: ', user_direction)
        for col in range(number_of_columns):
            for row in range(number_of_rows):
                if callable(dir_funcs[user_direction]):
                    results_dict = dir_funcs[user_direction](col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows)
        print('all results_dict: ', results_dict)
    return results_dict


def search_direction_d(col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows):
    # # for col in range(number_of_columns):
    # by columns
    # # for row in range(number_of_rows):
    # print("pos: ", row, col, " || value: ", matrix[row][col])
    word_to_check = ""
    row_to_add = row
    while row_to_add < number_of_rows:  # collect all letters (DOWN) to a word, and check if in word_list
        # print("row_to_add: ", row_to_add, end=" <---> ")
        # print("letter to add: ", matrix[row_to_add][col])
        word_to_check += matrix[row_to_add][col]
        # if len(word_to_check) > 1: print("--> checking word: ", word_to_check)
        if len(word_to_check) > 1 and word_to_check in word_list:
            add_word_to_dict(word_to_check, results_dict)
        row_to_add += 1
    # end while -- next loop is for letter in [1][0] (going down)
    return results_dict


def search_direction_u(col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows):
    """
    gets a position in the letters-matrix, finds all words in matrix that can be created from letters in an UP search
    and checks if they exist in word_list. if they do- -> added them to :param results_dict:
    :param col: col index
    :type col: int
    :param row: row index
    :type row: int
    :param word_list: list of words to find in matrix
    :type word_list: [str]
    :param matrix: 2d letters list
    :type matrix: [[str]]
    :param results_dict: dict of all words found in matrix with a count of their appearance in matrix
    :type results_dict: Dict[str, int]
    :param number_of_columns: in matrix
    :type number_of_columns: int
    :param number_of_rows: in matrix
    :type number_of_rows: int
    :return: updated :param results_dict:
    :rtype: :type results_dict:
    """
    # for col in range(number_of_columns):
    # by columns
    # for row in range(number_of_rows - 1, 0, -1):  # from: last row to: second row --> don't need to check first row, cos words must have more than one letter and we're going up
    print("pos: ", row, col, " || value: ", matrix[row][col])
    word_to_check = ""
    row_to_add = row
    while row_to_add < number_of_rows:
        # print("row_to_add: ", row_to_add, end=" <---> ")
        # print("letter to add: ", matrix[row_to_add][col])
        word_to_check = matrix[row_to_add][col] + word_to_check  # add to beginning (UP search)
        if len(word_to_check) > 1: print("--> checking word: ", word_to_check)
        if len(word_to_check) > 1 and word_to_check in word_list:
            add_word_to_dict(word_to_check, results_dict)
        row_to_add += 1
    return results_dict


def search_direction_r(word_list, matrix, results_dict, number_of_columns, number_of_rows):
    for col in range(number_of_columns):
        # by columns
        for row in range(number_of_rows):
            # print("pos: ", row, col, " || value: ", matrix[row][col])
            word_to_check = ""
            column_to_add = col
            while column_to_add < number_of_columns:
                # print("column_to_add: ", column_to_add, end=" <---> ")
                # print("letter to add: ", matrix[row][column_to_add])
                word_to_check += matrix[row][column_to_add]
                # if len(word_to_check) > 1: print("--> checking word: ", word_to_check)
                if len(word_to_check) > 1 and word_to_check in word_list:
                    add_word_to_dict(word_to_check, results_dict)
                column_to_add += 1
            # end while -- next loop is for letter in [1][0] (going down)
    return results_dict


def search_direction_l(word_list, matrix, results_dict, number_of_columns, number_of_rows):
    for col in range(number_of_columns - 1, ):
        # by columns
        for row in range(number_of_rows):
            # print("pos: ", row, col, " || value: ", matrix[row][col])
            word_to_check = ""
            column_to_add = col
            while column_to_add < number_of_columns:
                # print("column_to_add: ", column_to_add, end=" <---> ")
                # print("letter to add: ", matrix[row][column_to_add])
                word_to_check += matrix[row][column_to_add]
                # if len(word_to_check) > 1: print("--> checking word: ", word_to_check)
                if len(word_to_check) > 1 and word_to_check in word_list:
                    add_word_to_dict(word_to_check, results_dict)
                column_to_add += 1
            # end while -- next loop is for letter in [1][0] (going down)
    return results_dict


def add_word_to_dict(word, result_dict):
    if word in result_dict:
        result_dict[word] += 1
    else:
        result_dict[word] = 1


def write_output(results: [Result], filename):
    """
    :param results: list of results in the following format: (word, count)
    
    """
    pass
    """
    input:

    python3
    0 wordsearch.py
    1  word_file
    2   matrix_file
    3    output_file
    4     directions

    output:

    word,number
    word,number
    word,number
    """


if __name__ == '__main__':
    main()

"""
x
    y
        (x,y)
            direction DOWN: and len(word_to_check) > 1 (not top row)
            word_to_check = ""
            for item in current_x_axis:
                word_to_check += item
                # check word (word_to_check)

            direction UP: and len(word_to_check) > 1 (not bottom row)
            word_to_check = ""
            for item in current_x_axis:
                word_to_check += item
                # check word (word_to_check)

            direction RIGHT: and len(word_to_check) > 1 (NOT left-most column)
            word_to_check=""
            for letter in current_y_axis:
                word_to_check += letter
                # check word (word_to_check)

            direction LEFT: and len(word_to_check) > 1 (not right-most column)
            word_to_check-""
            for letter in current_y_axis:
                word_to_check += letter
                # check word (word_to_check)

            direction DIAGONAL-RIGHT-BOTTOM:
            word_to_check = ""
            for letter in max(current_x, current_y):
                word_to_check += matrix[letter][letter]

"""
