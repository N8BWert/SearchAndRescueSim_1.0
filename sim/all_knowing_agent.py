from agent import agent
from location import location
from fire_station import fire_station

from typing import List, Optional
import numpy as np

from parameters import TIME_TO_RESCUE_PERSON, NO_PEOPLE_COOLDOWN

class all_knowing_agent(agent):
    """
    agent that knows the location of all survivors
    """
    def __init__(self, start_location: fire_station, locations: List[location]):
        if start_location == '':
            return
        super().__init__(start_location, locations)
        self.agent_type = 'all_knowing_agent'

    def tick(self, locations: List[location], people_location: Optional[location]):
            super().tick(locations, None)

    def plan_next_destination(self, locations: List[location]):
        closest_distance = np.linalg.norm(locations[0].position - self.current_position)
        closest_location = locations[0]
        for i in range(0, len(locations)):
            if not locations[i].searched:
                distance = np.linalg.norm(locations[i].position - self.current_position)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_location = locations[i]
        return closest_location

    def save_survivors(self):
        if self.target_location.num_people != 0:
            self.cooldown = self.target_location.num_people * TIME_TO_RESCUE_PERSON
            self.num_saved += self.target_location.num_people
            print(self.unique_name + ' has found survivors!!!')
        else:
            self.cooldown = NO_PEOPLE_COOLDOWN
            print(self.unique_name + ' has searched a building, however there were no survivors :(')
        self.target_location.searched = True
        self.checked_locations.append(self.target_location)
        self.target_location = None

    def create_agent_from_string(agent_string: str, agent_name: str):
        new_agent = all_knowing_agent('', '')
        data = agent_string.split(',')
        new_agent.start_position = np.zeros(2)
        new_agent.start_position[0] = float(data[0])
        new_agent.start_position[1] = float(data[1])
        new_agent.current_position = np.zeros(2)
        new_agent.current_position[0] = float(data[2])
        new_agent.current_position[1] = float(data[3])
        new_agent.num_saved = int(data[4])
        new_agent.target_location = location.create_from_string(data[5])
        new_agent.cooldown = int(data[6])
        new_agent.checked_locations = []
        if data[7] != '':
            locations = data[7].split('|')
            for string_loc in locations:
                new_agent.checked_locations.append(location.create_from_string(string_loc))
        new_agent.survivor_locations = []
        survivors = data[8].split('|')
        if data[8] != '':
            for string_survivor in survivors:
                new_agent.survivor_locations.append(location.create_from_string(string_survivor))
        new_agent.unique_name = data[9]
        new_agent.agent_type = agent_name
        return new_agent