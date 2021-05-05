import sys
import os.path
from typing import Tuple

# types:
Result = Tuple[str, int]  # single result of list of results this file needs to output

# consts:
WORDS_FILE_NAME = 1
MATRIX_FILE_NAME = 2
OUTPUT_FILE_NAME = 3
DIRECTIONS = 4


def main():
	if len(sys.argv) != 5:  # ? 5 or 4?
		# print("not good: arguments are not valid")
		return  # end of program

	wordlist = read_wordlist(sys.argv[WORDS_FILE_NAME])  # if file doesn't exist, program will end
	if not wordlist:
		return  # end of program
	# [print(w) for w in wordlist]
	matrix = read_matrix(sys.argv[MATRIX_FILE_NAME])
	if not matrix:
		return  # end of program
	# _print_matrix(matrix)
	dirs = sys.argv[DIRECTIONS]
	# print("-" * 30)
	results = find_words(wordlist, matrix, dirs)  # Tuple type
	if not results:
		return  # end of program
	# print("\nFINAL: ", results_dict, end="\n\n")
	write_output(results, sys.argv[3])


# def _print_matrix(matrix):
# print("matrix:")
# print("[")
# for row in range(len(matrix)):
# 	print(" [", end=" ")
# 	for column in range(len(matrix[0])):
# 		print(f"{matrix[row][column]}", end=", ")
# 	print("]")
# print("]")


def read_wordlist(file_name: str):
	"""
		if file doesn't exist, returns False,
		else, returns the file content as a list or words
	"""
	if not os.path.isfile(file_name):
		print("not good: word file does not exist")
		return False
	with open(file_name, 'r') as word_file:
		return [word.rstrip() for word in word_file]


def read_matrix(file_name: str):
	"""
	if file doesn't exist, returns False,
	else, returns the file content as a matrix
	"""
	if not os.path.isfile(file_name):
		print("not good: matrix file does not exist")
		return False
	with open(file_name, 'r') as matrix_file:
		return [row.rstrip().split(",") for row in matrix_file]


def find_words(word_list: [str], matrix: [[str]], directions: str) -> [Result]:
	"""
	:param word_list: list of words to search
	:param matrix: 2d list representing the letter matrix: [ [ letter, letter ], [letter, letter] ]
	:param directions: part or all of: "udrlwxyz"
	:return: Result[] (== [ (word, count), (word, count) ]) a list of tuples made of words from <word_list> and a count of their appearance in <matrix>
	"""
	results_dict = {}
	dir_funcs = {"u": {"func": search_direction_u, "searched": False},  # up
		"d": {"func": search_direction_d, "searched": False},  # down
		"r": {"func": search_direction_r, "searched": False},  # right
		"l": {"func": search_direction_l, "searched": False},  # left
	}
	diagonal_funcs = {"w": {"func": search_diagonal_ur, "searched": False},  # up-right
		"x": {"func": search_diagonal_ul, "searched": False},  # up-left
		"y": {"func": search_diagonal_dr, "searched": False},  # down-right
		"z": {"func": search_diagonal_dl, "searched": False}  # down-left
	}

	number_of_rows = len(matrix)
	number_of_columns = len(matrix[0])

	for user_direction in directions:
		# print('user_direction: ', user_direction)
		if user_direction in diagonal_funcs:
			if callable(diagonal_funcs[user_direction]["func"]) and not diagonal_funcs[user_direction]["searched"]:
				results_dict = diagonal_funcs[user_direction]["func"](word_list, matrix, results_dict, number_of_columns, number_of_rows)
				diagonal_funcs[user_direction]["searched"] = True
		elif user_direction in dir_funcs:
			if callable(dir_funcs[user_direction]["func"]) and not dir_funcs[user_direction]["searched"]:
				for col in range(number_of_columns):
					for row in range(number_of_rows):
						results_dict = dir_funcs[user_direction]["func"](col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows)
			# end directions for loop:
			# print("all results_dict: ", results_dict)
			dir_funcs[user_direction]["searched"] = True
		else:
			# invalid direction will stop program here - not getting to output file
			# if there is a need to check that ALL directions from user are valid even earlier than here - it will come out less efficient (another loop on directions).
			print(f"{user_direction} is not a valid direction")
			return False
	return list(results_dict.items())


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
	# print("pos: ", row, col, " || value: ", matrix[row][col])
	word_to_check = ""
	row_to_add = row
	while row_to_add < number_of_rows:
		# print("row_to_add: ", row_to_add, end=" <---> ")
		# print("letter to add: ", matrix[row_to_add][col])
		word_to_check = matrix[row_to_add][col] + word_to_check  # add to beginning (UP search)
		# if len(word_to_check) > 1: print("--> checking word: ", word_to_check)
		if len(word_to_check) > 1 and word_to_check in word_list:
			add_word_to_dict(word_to_check, results_dict)
		row_to_add += 1
	return results_dict


def search_direction_d(col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows):
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
	return results_dict


def search_direction_r(col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows):
	# print("pos: ", row, col, " || value: ", matrix[row][col])
	word_to_check_r = ""
	column_to_add = col
	while column_to_add < number_of_columns:
		# print("column_to_add: ", column_to_add, end=" <---> ")
		# print("letter to add: ", matrix[row][column_to_add])
		word_to_check_r += matrix[row][column_to_add]
		# if len(word_to_check_r) > 1: print("--> checking word right: ", word_to_check_r)
		if len(word_to_check_r) > 1 and word_to_check_r in word_list:
			add_word_to_dict(word_to_check_r, results_dict)
		column_to_add += 1
	return results_dict


def search_direction_l(col, row, word_list, matrix, results_dict, number_of_columns, number_of_rows):
	# print("pos: ", row, col, " || value: ", matrix[row][col])
	word_to_check = ""
	column_to_add = col
	while column_to_add < number_of_columns:
		# print("column_to_add: ", column_to_add, end=" <---> ")
		# print("letter to add: ", matrix[row][column_to_add])
		word_to_check = matrix[row][column_to_add] + word_to_check  # add to beginning of word_to_check cos LEFT search
		# if len(word_to_check) > 1: print("--> checking word: ", word_to_check)
		if len(word_to_check) > 1 and word_to_check in word_list:
			add_word_to_dict(word_to_check, results_dict)
		column_to_add += 1
	# end while -- next loop is for letter in [1][0] (going down)
	return results_dict


def search_diagonal_dr(word_list, matrix, results_dict, number_of_columns, number_of_rows):
	# print("dr")
	for row in range(0, number_of_rows - 1):  # no need to check last row
		for col in range(0, number_of_columns - 1):  # no need to check last col
			# print("pos: ", row, col)
			row_to_check = row + 1
			col_to_check = col + 1
			word_to_check = matrix[row][col]  # add first letter not, and start col_to_check and row_to_check from +1, cos don't need to check it alone
			# print("col_to_check: ", col_to_check, "row_to_check: ", row_to_check)
			while col_to_check < number_of_columns and row_to_check < number_of_rows:
				word_to_check += matrix[row_to_check][col_to_check]
				# print("word_to_check: ", word_to_check)
				if word_to_check in word_list:
					add_word_to_dict(word_to_check, results_dict)
				row_to_check += 1
				col_to_check += 1
	return results_dict


def search_diagonal_dl(word_list, matrix, results_dict, number_of_columns, number_of_rows):
	# print("dl")
	for row in range(0, number_of_rows - 1):  # no need to check last row
		for col in range(1, number_of_columns):  # no need to check left-most col
			# print("pos: ", row, col)
			row_to_check = row + 1
			col_to_check = col - 1
			word_to_check = matrix[row][col]  # add first letter not, and start col_to_check and row_to_check from +1, cos don't need to check it alone
			# print("col_to_check: ", col_to_check, "row_to_check: ", row_to_check)
			while col_to_check > -1 and row_to_check < number_of_rows:
				word_to_check += matrix[row_to_check][col_to_check]
				# print("word_to_check: ", word_to_check)
				if word_to_check in word_list:
					add_word_to_dict(word_to_check, results_dict)
				row_to_check += 1
				col_to_check -= 1
	return results_dict


def search_diagonal_ur(word_list, matrix, results_dict, number_of_columns, number_of_rows):
	# print("dr")
	for row in range(1, number_of_rows):  # no need to check first row
		for col in range(0, number_of_columns - 1):  # no need to check right-most col
			# print("pos: ", row, col)
			col_to_check = col + 1
			row_to_check = row - 1
			word_to_check = matrix[row][col]  # add first letter not, and start col_to_check and row_to_check from +1, cos don't need to check it alone
			# print("col_to_check: ", col_to_check, "row_to_check: ", row_to_check)
			while col_to_check < number_of_columns and row_to_check > 0:
				word_to_check += matrix[row_to_check][col_to_check]
				# print("word_to_check: ", word_to_check)
				if word_to_check in word_list:
					add_word_to_dict(word_to_check, results_dict)
				col_to_check += 1
				row_to_check -= 1
	return results_dict


def search_diagonal_ul(word_list, matrix, results_dict, number_of_columns, number_of_rows):
	# print("ul")
	for row in range(1, number_of_rows):  # no need to check first row
		for col in range(1, number_of_columns):  # no need to check left-most col
			# print("pos: ", row, col)
			col_to_check = col - 1
			row_to_check = row - 1
			word_to_check = matrix[row][col]  # add first letter, and start col_to_check and row_to_check with next letter, cos don't need to check it alone
			# print("col_to_check: ", col_to_check, "row_to_check: ", row_to_check)
			while col_to_check > 0 and row_to_check > 0:
				word_to_check += matrix[row_to_check][col_to_check]
				# print("word_to_check: ", word_to_check)
				if word_to_check in word_list:
					add_word_to_dict(word_to_check, results_dict)
				col_to_check -= 1
				row_to_check -= 1
	return results_dict


def add_word_to_dict(word, result_dict):
	if word in result_dict:
		result_dict[word] += 1
	else:
		result_dict[word] = 1


def write_output(results: [Result], filename):
	"""
	:param results: list of results in the following format: (word, count)
	:param filename: name of file to write to
	"""
	# print("write to output", filename)
	with open(filename, 'w') as output_file:
		for name, count in results:
			output_file.write(name + "," + str(count) + "\n")


if __name__ == '__main__':
	main()
