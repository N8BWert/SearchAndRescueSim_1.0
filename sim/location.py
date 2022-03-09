import numpy as np

class location(object):
    """
    Singular location for the search and rescue team to search.
    """
    def __init__(self, x_coordinate: float, y_coordinate: float):
        self.x = x_coordinate
        self.y = y_coordinate
        self.position = np.zeros(2)
        self.searched = False
        self.position[0] = x_coordinate
        self.position[1] = y_coordinate
        self.num_people = 0

    def populate_with_survivors(self, num_people: int):
        self.num_people = num_people

    def __str__(self):
        searched_string = ''
        if self.searched:
            searched_string = '1'
        return str.format("[{};{};{};{}]", str(self.x), str(self.y), searched_string, str(self.num_people))

    def create_from_string(string: str):
        newloc = location(0, 0)
        information = string [1:-1]
        information = information.split(';')
        newloc.x = float(information[0])
        newloc.y = float(information[1])
        newloc.searched = bool(information[2])
        newloc.position = np.zeros(2)
        newloc.position[0] = newloc.x
        newloc.position[1] = newloc.y
        newloc.num_people = int(information[3])
        return newloc

    def __eq__(self, other):
        if isinstance(other, location):
            if self.x == other.x and self.y == other.y and self.searched == other.searched and self.num_people == other.num_people:
                return True
        return False