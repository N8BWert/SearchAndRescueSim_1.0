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

from parameters import TIME_BETWEEN_SENDS, TOTAL_POPULATION, MAX_PEOPLE_PER_LOCATION, DISCOVER_PERCENTAGE
from all_knowing_agent import all_knowing_agent

save_state_prefix = './save_states/'
results_prefix = './results/'

class simulation():
    """
    Basic governing body for the running of the simulation
    """
    num_timesteps = 48 * 3600
    total_survivors = 0

    def __init__(self, location_file: str, fire_stations: str, agent_name: str):
        print('Initializing Sim...')
        if location_file == '' and agent_name == '':
            return
        self.timesteps_left = self.num_timesteps
        print('Generating Locations')
        self.locations = self.generate_locations(location_file)
        print('Populating Locations with Survivors')
        self.locations_with_survivors = self.get_locations_with_survivors(self.locations)
        print('Generating Fire Stations')
        self.fire_stations = self.generate_fire_stations(fire_stations)
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

    def add_agents(self, agent_name: str):
        agent_list = []
        if agent_name == 'informed_agent_1':
            for station in self.fire_stations:
                new_agent = informed_agent_1(station, self.locations)
                agent_list.append(new_agent)
        elif agent_name == 'h2h_agent':
            for station in self.fire_stations:
                new_agent = h2h_agent(station, self.locations)
                agent_list.append(new_agent)
        elif agent_name == 'all_knowing_agent':
            print('creating all knowing agents')
            for station in self.fire_stations:
                new_agent = all_knowing_agent(station, self.locations_with_survivors)
                print(new_agent.target_location)
        return agent_list

    def tick(self):
        if self.timesteps_left % TIME_BETWEEN_SENDS == 0:
            new_survivor_location = self.get_random_survivor_location()
            closest_agent_index = self.get_closest_agent_to_location(new_survivor_location)
            self.locs_sent_to_agents[closest_agent_index].append(new_survivor_location)
            for i in range(0, len(self.agents)):
                if i == closest_agent_index:
                    self.agents[i].tick(self.locations, new_survivor_location)
                else:
                    self.agents[i].tick(self.locations, None)
            self.timesteps_left -= 1
            return
        for agent in self.agents:
            if agent.agent_type == 'all_knowing_agent':
                agent.tick(self.locations_with_survivors, None)
            else:
                agent.tick(self.locations, None)
        self.timesteps_left -= 1

    def generate_locations(self, city_building_file: str):
        locations = pd.read_csv(city_building_file)
        num_survivors = TOTAL_POPULATION
        locs = []
        for index, series in locations.iterrows():
            x = series['x']
            y = series['y']
            rand_num = np.random.randint(0, 100)
            survivors_at_location = 0
            if rand_num < DISCOVER_PERCENTAGE:
                survivors_at_location = np.random.randint(1, MAX_PEOPLE_PER_LOCATION + 1)
                self.total_survivors += survivors_at_location
            new_location = location(x, y)
            new_location.populate_with_survivors(survivors_at_location)
            locs.append(new_location)
        return locs

    def get_locations_with_survivors(self, locations: List[location]):
        locations_with_survivors = []
        for loc in locations:
            if loc.num_people != 0:
                locations_with_survivors.append(loc)
        return locations_with_survivors

    def generate_fire_stations(self, fire_station_file: str):
        fire_stations = pd.read_csv(fire_station_file, delimiter=';')
        stations = []
        for index, series in fire_stations.iterrows():
            x = series['x']
            y = series['y']
            new_station = fire_station(x, y, 1)
            stations.append(new_station)
        return stations

    def get_random_survivor_location(self):
        index = np.random.randint(0, len(self.locations_with_survivors))
        new_survivor_location = self.locations_with_survivors[index]
        self.locations_with_survivors.remove(new_survivor_location)
        return new_survivor_location

    def get_closest_agent_to_location(self, loc: location):
        smallest_distance = np.inf
        closest_agent_index = 0
        for i in range(0, len(self.agents)):
            distance = np.linalg.norm(self.agents[i].current_position - loc.position)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_agent_index = i
        return closest_agent_index

    def save_state(self, simulation_state_file: Optional[str], location_state_file: Optional[str], agent_state_file: Optional[str]):
        if simulation_state_file == '':
            simulation_state_file = save_state_prefix + self.name + '-sim-' + str(self.timesteps_left) + '.txt'
            location_state_file = save_state_prefix + self.name + '-locs-' + str(self.timesteps_left) + '.txt'
            agent_state_file = save_state_prefix + self.name + '-agents-' + str(self.timesteps_left) + '.txt'
        if self.old_name != '':
            simulation_state_file = save_state_prefix + self.old_name + '-' + self.name + '-sim-' + str(self.timesteps_left) + '.txt'
            location_state_file = save_state_prefix + self.old_name + '-' + self.name + '-locs-' + str(self.timesteps_left) + '.txt'
            agent_state_file = save_state_prefix + self.old_name + '-' + self.name + '-agents-' + str(self.timesteps_left) + '.txt'

        sim_file = open(simulation_state_file, 'w')
        loc_file = open(location_state_file, 'w')
        agent_file = open(agent_state_file, 'w')

        sim_file.write(str(self))
        for loc in self.locations:
            loc_file.write(str(loc))
            loc_file.write('\n')
        for agent in self.agents:
            agent_file.write(str(agent))
            agent_file.write('\n')

        sim_file.close()
        loc_file.close()
        agent_file.close()

    def load_state(simulation_state_file: str, location_state_file: str, agent_state_file: str):
        new_sim = simulation('', '')
        sim_file = open(simulation_state_file, 'r')
        loc_file = open(location_state_file, 'r')
        agent_file = open(agent_state_file, 'r')

        sim_data = sim_file.readline()
        sim_data = sim_data.split(',')
        new_sim.num_timesteps = int(sim_data[0])
        new_sim.old_name = sim_data[1]
        new_sim.name = new_sim.generate_name()
        new_sim.timesteps_left = int(sim_data[2])

        new_sim.locations = []

        for line in loc_file.readlines():
            line = line[0:-1]
            new_sim.locations.append(location.create_from_string(line))

        new_sim.agents = []

        for line in agent_file.readlines():
            if 'h2h_agent' in line:
                new_sim.agents.append(h2h_agent.create_agent_from_string(line, 'h2h_agent'))
            elif 'informed_agent_1' in line:
                new_sim.agents.append(informed_agent_1.create_agent_from_string(line, 'informed_agent_1'))

        agent_to_locs_string = sim_data[3].split('?')
        new_sim.locs_sent_to_agents = {}
        [new_sim.locs_sent_to_agents.setdefault(i, []) for i in range(len(new_sim.agents))]
        for agent_to_loc in agent_to_locs_string:
            num_to_loc_string = agent_to_loc[1:-1]
            num_to_loc_string = num_to_loc_string.split(':')
            agent_num = int(num_to_loc_string[0])
            if len(num_to_loc_string) > 0 and num_to_loc_string[1] != '':
                new_sim.locs_sent_to_agents[agent_num] = []
                locs = num_to_loc_string[1][:-1].split('|')
                for loc in locs:
                    new_sim.locs_sent_to_agents[agent_num].append(location.create_from_string(loc))
            else:
                new_sim.locs_sent_to_agents[agent_num] = []

        new_sim.locations_with_survivors = new_sim.get_locations_with_survivors(new_sim.locations)

        sim_file.close()
        loc_file.close()
        agent_file.close()

        return new_sim

    def replay_sim_with_new_agents(simulation_start_file: str, location_start_file: str, agent_start_file: str, agent_name: str):
        new_sim = simulation('', '', '')
        sim_file = open(simulation_start_file, 'r')
        loc_file = open(location_start_file, 'r')
        agent_file = open(agent_start_file, 'r')

        sim_data = sim_file.readline()
        sim_data = sim_data.split(',')
        new_sim.num_timesteps = int(sim_data[0])
        new_sim.old_name = sim_data[1]
        new_sim.name = new_sim.generate_name()
        new_sim.timesteps_left = int(sim_data[2])

        new_sim.locations = []

        for line in loc_file.readlines():
            line = line[0:-1]
            new_sim.locations.append(location.create_from_string(line))

        new_sim.agents = []

        for line in agent_file.readlines():
            if agent_name == 'h2h_agent':
                new_sim.agents.append(h2h_agent.create_agent_from_string(line, 'h2h_agent'))
            elif agent_name == 'informed_agent_1':
                new_sim.agents.append(informed_agent_1.create_agent_from_string(line, 'informed_agent_1'))
            elif agent_name == 'all_knowing_agent':
                new_sim.agents.append(all_knowing_agent.create_agent_from_string(line, 'all_knowing_agent'))

        agent_to_locs_string = sim_data[3].split('?')
        new_sim.locs_sent_to_agents = {}
        [new_sim.locs_sent_to_agents.setdefault(i, []) for i in range(len(new_sim.agents))]
        for agent_to_loc in agent_to_locs_string:
            num_to_loc_string = agent_to_loc[1:-1]
            num_to_loc_string = num_to_loc_string.split(':')
            agent_num = int(num_to_loc_string[0])
            if len(num_to_loc_string) > 0 and num_to_loc_string[1] != '':
                new_sim.locs_sent_to_agents[agent_num] = []
                locs = num_to_loc_string[1][:-1].split('|')
                for loc in locs:
                    new_sim.locs_sent_to_agents[agent_num].append(location.create_from_string(loc))
            else:
                new_sim.locs_sent_to_agents[agent_num] = []

        new_sim.locations_with_survivors = new_sim.get_locations_with_survivors(new_sim.locations)

        sim_file.close()
        loc_file.close()
        agent_file.close()

        return new_sim

    def save_results(self, outfile: str):
        out = open(outfile, 'w')
        people_saved = 0
        for agent in self.agents:
            people_saved += agent.num_saved
        out.write('SIM: {} - Survivors saved: {}'.format(self.name, people_saved))
        out.close()

    def generate_name(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(6))

    def __str__(self):
        agents_to_locs_string = '{'
        for key in self.locs_sent_to_agents:
            agents_to_locs_string += str(key) + ':'
            if self.locs_sent_to_agents[key] != []:
                for loc in self.locs_sent_to_agents[key]:
                    agents_to_locs_string += str(loc) + '|'
                agents_to_locs_string = agents_to_locs_string[:-1]
            agents_to_locs_string += '}?{'
        agents_to_locs_string = agents_to_locs_string[:-2]
        string = '{},{},{},{}'.format(
            str(self.num_timesteps), self.name, str(self.timesteps_left), agents_to_locs_string
        )
        return string

    def init_locs_sent_to_agents(self):
        agents_to_locations = {}
        for i in range(0, len(self.agents)):
            agents_to_locations[i] = []
        return agents_to_locations

    def print_survivors_saved(self):
        num_saved = 0
        for i in range(0, len(self.agents)):
            num_saved += self.agents[i].num_saved
        print('Num survivors saved: {}\nTotal survivors: {}'.format(num_saved, self.total_survivors))

    def run_sim(self):
        print('RUNNING SIM')
        current_timestep = 0
        while self.timesteps_left >= 0:
            self.tick()
            current_timestep += 1

            if current_timestep % 3600 == 0:
                self.print_survivors_saved()
                print('Current timestep: {}\n{} timesteps left'.format(current_timestep, self.timesteps_left))
        self.print_survivors_saved()
        print('Sim has finished running')
        self.save_state('', '', '')
        self.save_results('./results/' + self.name + '-results.txt')

    def __eq__(self, other):
        if isinstance(other, simulation):
            if self.timesteps_left == other.timesteps_left and \
                len(self.locations) == len(other.locations) and \
                len(self.locations_with_survivors) == len(other.locations_with_survivors):
                return True
        return False