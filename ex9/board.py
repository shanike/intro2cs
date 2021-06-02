

from typing import Dict, List
from car import Car


MOVES = {"u": "u", "d": "d", "l": "l", "r": "r"}


class Board:
    """
    A board for the game rush hour, which includes cells with either a Car instrances or an empty sign.
    The board has a method in charge of moving the cars on it 
    """
    BOARD_LENGTH = 7
    EMPTY_CELL = "-"

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.cars: Dict[str, Car] = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        cells_to_print = ""
        curr_row = ""

        cells = self.cell_list()
        for i in range(len(cells)):
            cell = cells[i]
            if cell == self.target_location():
                value = "-> EXIT"
            else:
                value = self.cell_content(cell)
            if not value:
                value = "-"
            curr_row += value + "  "
            if i+1 == len(cells) or cells[i][0] != cells[i+1][0]:
                cells_to_print += curr_row+"\n"
                curr_row = ""

        return cells_to_print

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        coords = []
        for row in range(Board.BOARD_LENGTH):
            for col in range(Board.BOARD_LENGTH):
                loc = (row, col)
                coords.append(loc)
        coords.append(self.target_location())
        return sorted(coords)

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        legal_moves = []
        for car_name in self.cars:  # each car
            car = self.cars[car_name]
            car_poss_moves = car.possible_moves()  # legal car-moves for this car
            for car_poss_move in car_poss_moves:  # {<move> : <description>}
                # get required empty cells for this move to heppen
                required_cells = car.movement_requirements(car_poss_move)
                for required_cell in required_cells:
                    all_cells = self.cell_list()
                    # if cell is empty, move is legal
                    if required_cell in all_cells and not self.cell_content(required_cell):
                        # required cell is on board, and is empty
                        legal_moves.append(
                            (car.get_name(), car_poss_move, car_poss_moves[car_poss_move]))
        return legal_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car_name in self.cars:
            car = self.cars[car_name]
            for car_coord in car.car_coordinates():
                if car_coord[0] == coordinate[0] and car_coord[1] == coordinate[1]:
                    return car_name

    def add_car(self, car: Car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"

        for car_coord in car.car_coordinates():
            if car_coord not in self.cell_list():
                # cell is not on board
                return False
            if self.cell_content(car_coord):
                # cell is occupied, not good
                return False
        car_name = car.get_name()
        if car_name in self.cars:
            return False
        self.cars[car_name] = car

        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # check if we have this car on board:
        if name not in self.cars:
            return False

        curr_car = self.cars[name]

        required_locs = curr_car.movement_requirements(movekey)
        for required_loc in required_locs:
            cells = self.cell_list()
            if required_loc not in cells:
                # not on board, bye
                return False
            if self.cell_content(required_loc):
                # cell is occupied, bye
                return False

        # location is available on board --> can ask car to move!!! :
        if not curr_car.move(movekey):
            return False

        return True
