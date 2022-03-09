from location import location
from fire_station import fire_station
from informed_agent_1 import informed_agent_1
from h2h_agent import h2h_agent
from agent import agent

from typing import List, Optional
import numpy as np
import pandas as pd
import random
import string

from parameters import TIME_BETWEEN_SENDS, TOTAL_POPULATION, MAX_PEOPLE_PER_LOCATION
from sim.all_knowing_agent import all_knowing_agent

save_state_prefix = './save_states/'
results_prefix = './results/'

class grid_sim():
    """
    Grid sim governing body for the running of the simulation
    """
    num_timesteps = 48 * 3600
    total_survivors = 0

    def __init__(self, location_file, fire_stations, agent_name):
        print('Initializing Sim...')
        if location_file == '' and agent_name == '':
            return
        self.timesteps_left = self.num_timesteps
        print('Generating Locations')
        self.max_x, self.max_y = self.get_max_min_from_locations(location_file)
        self.locations = self.generate_locations(location_file)
        print('Generating Sim Name')
        self.name = self.generate_name()
        print('Generating Agents')
        self.old_name = ''
        self.agents = self.add_agents(agent_name)
        print('Saving Start State')
        print('Initializing Locs sent to agents')
        self.locs_sent_to_agents = self.init_locs_sent_to_agents()
        self.save_state(
            save_state_prefix + self.name + '-sim-start.txt',
            save_state_prefix + self.name + '-locs-start.txt',
            save_state_prefix + self.name + '-agent-start.txt'
        )

    def generate_locations(self, city_building_file: str):
        locations = pd.read_csv(city_building_file)
        num_survivors = TOTAL_POPULATION
        locs = []
        for x in range(0, np.ceil(self.max_x / 10)):
            for y in range(0, np.ceil(self.max_y / 10)):
                locs[x][y] = False
        for index, series in locations.iterrows():
            x = series['x']
            y = series['y']
            rand_num = np.random.randint(0, 2)
            survivors_at_location = 0
            if rand_num == 1 and num_survivors > 0:
                survivors_at_location = np.random.randint(1, MAX_PEOPLE_PER_LOCATION + 1)
                self.total_survivors += survivors_at_location
            new_location = location(x, y)
            new_location.populate_with_survivors(survivors_at_location)
            locs[np.round(x / 10), np.round(y / 10)] = new_location
            if survivors_at_location != 0:
                self.locations_with_survivors.append(new_location)
        return locs

    def get_max_min_from_locations(location_file):
        loc_file = pd.read_csv(location_file, 'r')
        x_max = max(loc_file['x'])
        y_max = max(loc_file['y'])
        return x_max, y_max

    def generate_name(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(6))

    def add_agents(self, station_file, agent_name: str):
        station_file = pd.read_csv(station_file, sep=';')
        agent_list = []
        for index, series in station_file.iterrows():
            position = np.zeros(2)
            position[0] = series['x']
            position[1] = series['y']
            if agent_name == 'informed_agent':
                new_agent = informed_agent_1(position, self.get_next_target(position))
                agent_list.appned(new_agent)
            elif agent_name == 'h2h_agent':
                new_agent = h2h_agent(position, self.get_next_target(position))
            elif agent_name == 'all_knowing':
                new_agent = all_knowing_agent(position, self.get_next_target(position))
        return agent_list

    def get_next_target(self, position: np.ndarray):
        initial_index = np.round(position / 10)
        distance_offset = 1
        current_offset = (distance_offset, 0)
        target_location = None
        while target_location is None:
            if self.locations[initial_index[0] + current_offset[0], initial_index[1] + current_offset[1]] is not None:
                target_location = self.locations[initial_index[0] + current_offset[0], initial_index[1] + current_offset[1]]
                return target_location
            if current_offset == (distance_offset, 0):
                current_offset = (distance_offset - 1, )