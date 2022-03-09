from location import location

class fire_station(location):
    def __init__(self, x_location: float, y_location: float, num_search_teams: int):
        super().__init__(x_location, y_location)
        self.num_teams = num_search_teams