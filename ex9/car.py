MOVES = {"u": "u", "d": "d", "l": "l", "r": "r"}


class Car:
    """
    A car with the properties name, length, location, orientation
    the car is meant to be placed on a Board as part of a rush-hour Game
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coords = []
        if self.orientation == 1:  # ---
            for i in range(self.length):
                coords.append((self.location[0], self.location[1]+i))
        if self.orientation == 0:  # |
            for i in range(self.length):
                coords.append((self.location[0]+i, self.location[1]))
        return coords

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        if self.orientation == 0:  # |
            return {"d": "down we go", "u": "up and up and up"}
        return {"l": "to the leeeeeft", "r": "right away to the right"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        if self.orientation == 0:
            # orientation is |
            if movekey == MOVES["d"]:
                # after last part of car:
                col = self.location[1]
                new_row = self.location[0]+self.length
                return [(new_row, col)]
            elif movekey == MOVES["u"]:
                col = self.location[1]
                new_row = self.location[0]-1  # before car
                return [(new_row, col)]
        else:
            # orientation is --- (1)
            if movekey == MOVES["r"]:
                row = self.location[0]
                new_col = self.location[1] + \
                    self.length  # after car to the right
                return [(row, new_col)]
            elif movekey == MOVES["l"]:
                row = self.location[0]
                new_col = self.location[1]-1  # before car to the left
                return [(row, new_col)]
        return []

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """

        if movekey == MOVES["d"]:
            if self.orientation != 0:
                return False
            self.location = (self.location[0]+1, self.location[1])
        elif movekey == MOVES["u"]:
            if self.orientation != 0:
                return False
            self.location = (self.location[0]-1, self.location[1])
        elif movekey == MOVES["r"]:
            if self.orientation != 1:
                return False
            self.location = (self.location[0], self.location[1]+1)
        elif movekey == MOVES["l"]:
            if self.orientation != 1:
                return False
            self.location = (self.location[0], self.location[1]-1)
        else:
            return False
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
