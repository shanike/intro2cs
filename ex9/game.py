import sys
import os
from typing import List
from board import Board
from car import Car
from helper import load_json


class Game:
    """
    Add class description here
    """
    POSSIBLE_CAR_NAMES = ('R', 'G', 'W', 'O', 'B', 'Y')
    USED_CAR_NAMES = []
    VALID_MOVES = {"u": "u", "d": "d", "l": "l", "r": "r"}

    QUIT_SIGN = "!"
    QUIT_MSG = ""

    WON = 'WON_GAME'
    WON_MSG = "YOU WON!"

    INVALID_MOVE_MSG = "\n-----------\n* sorry, invalid move. try again:\n-----------\n"

    def __init__(self, board: Board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        self.board = board
        print('\n-----------\ninitial board:\n-----------\n')
        print(board);

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        while True:  # until got valid input
            move = input()
            if move == "!":
                return Game.QUIT_SIGN

            valid_move = self.validate_user_move(move)
            if valid_move:
                break  # valid, continue in life, you're free
            print(Game.INVALID_MOVE_MSG)

        # ask board to move the car:
        car_name, move_dir = valid_move
        move_success = self.board.move_car(car_name, move_dir)

        # check if a car is in target location:
        if self.board.cell_content(self.board.target_location()):
            return Game.WON

        if not move_success:
            print(Game.INVALID_MOVE_MSG)
        if move_success == Game.WON:
            return Game.WON
        print(self.board)
        return move

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while True:
            move = self.__single_turn()
            if move == Game.QUIT_SIGN:
                # end game, quit
                print(Game.QUIT_MSG)
                return
            if move == Game.WON:
                # end game, won
                print(Game.WON_MSG)
                return

    def validate_user_move(self, valid_move):
        car_name, *move_dir = valid_move.split(",")
        if len(move_dir) != 1:
            return False
        move_dir = move_dir[0]
        if car_name in Game.POSSIBLE_CAR_NAMES and move_dir in Game.VALID_MOVES:
            return car_name, move_dir
        return False


"""
    main
"""


def load_cars(json_filepath):
    """get and return cars as a dictionairy from .json file
    """
    if not json_filepath or not os.path.exists(json_filepath):
        print('please enter a valid json file path')

    return load_json(json_filepath)


def add_cars_to_board(bo: Board, cars):
    """create cars from car_config json file and add them to given <board> bo

        :param bo: {Board} -- board
        :param cars: {dict from a json car config}
    """
    for car_name in cars:
        car_value = cars[car_name]
        if not isinstance(car_value, list) or len(car_value) != 3:
            continue
        if not validate_car(car_name, car_value[0], car_value[1], car_value[2]):
            continue
        car = Car(car_name, car_value[0], (car_value[1][0], car_value[1][1]), car_value[2])
        bo.add_car(car)


def validate_car(name, length, location, orientation):
    if not (2 <= length <= 4):
        return False
    if name not in Game.POSSIBLE_CAR_NAMES:
        return False
    if orientation != 0 and orientation != 1:
        return False
    if name in Game.USED_CAR_NAMES:
        return False
    if not isinstance(location, List):
        return False
    if len(location) != 2:
        return False
    for lo in location:
        if not isinstance(lo, int):
            return False
    Game.USED_CAR_NAMES.append(name)
    return True


def main():
    # init board
    b = Board()
    # get cars
    cars = load_cars(sys.argv[1])
    # add cars to board
    add_cars_to_board(b, cars)
    # init game
    game = Game(b)
    # play
    game.play()


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    main()
