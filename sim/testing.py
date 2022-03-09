from cgi import test
import string
from h2h_agent import h2h_agent
from informed_agent_1 import informed_agent_1
from location import location
from fire_station import fire_station
from simulation import simulation

def test_location_save_and_load():
    test_location1 = location(1.0, 2.0)
    test_location1.populate_with_survivors(20)
    string_test_location1 = location.create_from_string(str(test_location1))
    assert (test_location1 == string_test_location1), 'test_location_1 did not save correctly'
    test_location2 = location(2.0, 99999.0)
    test_location2.populate_with_survivors(99999999)
    test_location2.searched = True
    string_test_location2 = location.create_from_string(str(test_location2))
    assert (test_location2 == string_test_location2), 'test_location_2 did not save correctly'
    print('------> location set up correctly')

def test_h2h_agent_save_and_load():
    test_locations = []
    test_location1 = location(1.0, 2.0)
    test_location2 = location(2.0, 3.0)
    test_location2.populate_with_survivors(33)
    test_location3 = location(33, 99)
    test_location3.populate_with_survivors(100)
    test_locations.append(test_location1)
    test_locations.append(test_location2)
    test_locations.append(test_location3)
    
    fire_station_test = fire_station(1.5, 2.0, 1)

    test_h2h_agent = h2h_agent(fire_station_test, test_locations)

    string_test_h2h_agent = h2h_agent.create_agent_from_string(str(test_h2h_agent), test_h2h_agent.agent_type)
    assert (string_test_h2h_agent == test_h2h_agent), 'agents are not equal'
    print('------> h2h agent set up correctly')

def test_informed_agent_1_save_and_load():
    test_locations = []
    test_location1 = location(1.0, 2.0)
    test_location2 = location(2.0, 3.0)
    test_location2.populate_with_survivors(33)
    test_location3 = location(33, 99)
    test_location3.populate_with_survivors(100)
    test_locations.append(test_location1)
    test_locations.append(test_location2)
    test_locations.append(test_location3)
    
    fire_station_test = fire_station(1.5, 2.0, 1)

    test_informed_agent = informed_agent_1(fire_station_test, test_locations)

    string_test_informed_agent = informed_agent_1.create_agent_from_string(str(test_informed_agent), test_informed_agent.agent_type)
    assert (string_test_informed_agent == test_informed_agent), 'agents are not equal'
    print('------> informed agent 1 set up correctly')

def test_simulation_save_and_load():
    test_sim = simulation('./test_data.csv', 'h2h_agent')
    repeat_sim = simulation.load_state(
        './save_states/' + test_sim.name + '-sim-start.txt',
        './save_states/' + test_sim.name + '-locs-start.txt',
        './save_states/' + test_sim.name + '-agent-start.txt'
    )
    repeat_sim.save_state(
        './save_states/' + repeat_sim.name + '-sim-start(COPY).txt',
        './save_states/' + repeat_sim.name + '-locs-start(COPY).txt',
        './save_states/' + repeat_sim.name + '-agent-start(COPY).txt'
    )
    assert (repeat_sim == test_sim), 'Simulations are not equal after save'
    print('------> simulator is set up correctly')

def test_simulation_replay_with_new_agent():
    test_sim = simulation('./test_data.csv', 'h2h_agent')
    repeat_sim = simulation.replay_sim_with_new_agents(
        './save_states/' + test_sim.name + '-sim-start.txt',
        './save_states/' + test_sim.name + '-locs-start.txt',
        './save_states/' + test_sim.name + '-agent-start.txt',
        'informed_agent_1'
    )
    repeat_sim.save_state('', '', '')
    assert (repeat_sim == test_sim), 'Simulation replayability is not correct'
    print('------> simulation is set up correctly for replayability')

if __name__ == '__main__':
    test_location_save_and_load()
    test_h2h_agent_save_and_load()
    test_informed_agent_1_save_and_load()
    test_simulation_save_and_load()
    test_simulation_replay_with_new_agent()