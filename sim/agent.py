from tabnanny import check
from fire_station import fire_station
from location import location

from typing import List, Optional
import numpy as np
import string
import random

from parameters import SAVE_CUTOFF_DISTANCE, MOVE_SPEED

class agent():
    """
    Basic agent class all other agents will extend from
    """
    def __init__(self, start_location: fire_station, locations: List[location]):
        self.start_position = start_location.position
        self.current_position = start_location.position
        self.num_saved = 0
        self.checked_locations = []
        self.survivor_locations = []
        self.target_location = self.plan_next_destination(locations)
        self.unique_name = self.generate_name()
        self.agent_type = ''
        self.cooldown = 0

    def tick(self, locations: List[location], people_location: Optional[location]):
        if self.cooldown > 0:
            self.cooldown -= 1
            return
        elif self.target_location is None:
            self.target_location = self.plan_next_destination(locations)
        
        if np.linalg.norm(self.target_location.position - self.current_position) < SAVE_CUTOFF_DISTANCE:
            self.save_survivors()
        else:
            move_direction = (self.target_location.position - self.current_position) / np.linalg.norm(self.target_location.position - self.current_position)
            self.current_position += move_direction * MOVE_SPEED

    def plan_next_destination(self, locations: List[location]):
        pass

    def save_survivors(self):
        pass

    def __str__(self):
        checked_locations_string = ""
        for loc in self.checked_locations:
            checked_locations_string += str(loc)
            checked_locations_string += '|'
        checked_locations_string = checked_locations_string[:-1]
        survivor_locations_string = ""
        for loc in self.survivor_locations:
            survivor_locations_string += str(loc)
            survivor_locations_string += '|'
        survivor_locations_string = survivor_locations_string[:-1]
        save_string = str.format("{},{},{},{},{},{},{},{},{},{},{}",
            str(self.start_position[0]), str(self.start_position[1]), str(self.current_position[0]), str(self.current_position[1]), str(self.num_saved),
            str(self.target_location), str(self.cooldown), checked_locations_string, survivor_locations_string, self.unique_name, self.agent_type
        )
        return save_string

    def create_agent_from_string(agent_string: str, agent_name: str):
        pass

    def generate_name(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(20))

    def __eq__(self, other):
        if isinstance(other, agent):
            if np.array_equal(self.start_position, other.start_position) and \
                np.array_equal(self.current_position, other.current_position) and \
                self.num_saved == other.num_saved and \
                self.target_location == other.target_location and \
                self.cooldown == other.cooldown and \
                self.unique_name == other.unique_name and \
                self.agent_type == other.agent_type:
                return True
        return False