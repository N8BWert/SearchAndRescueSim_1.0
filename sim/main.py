import pandas as pd
from signal import SIGINT, signal
from sys import exit

from simulation import simulation

from typing import Optional

sim = None

def handler(signum, frame):
    print('saving the simulation...')
    sim.save_state('', '', '')
    print('done saving, program exiting')
    exit(0)

if __name__ == '__main__':
    print('Load From File y/n')
    load_from_file = input()
    if load_from_file == 'y':
        print('Replay previous sim with new agents y/n')
        replay_previous_sim = input()
        if replay_previous_sim == 'y':
            print('Simulation Start File Name: ')
            sim_start_file_name = input()
            print('Simulation Loc Start File Name: ')
            location_start_file_name = input()
            print('Agent Start File Name: ')
            agent_start_file_name = input()
            print('Enter New Agent Type: ')
            new_agent_name = input()
            sim = simulation.replay_sim_with_new_agents(
                simulation_start_file=sim_start_file_name,
                location_start_file=location_start_file_name,
                agent_start_file=agent_start_file_name,
                agent_name=new_agent_name
            )
        elif replay_previous_sim == 'n':
            print('Simulation Start File Name: ')
            sim_start_file_name = input()
            print('Simulation Loc Start File Name: ')
            location_start_file_name = input()
            print('Agent Start File Name: ')
            agent_start_file_name = input()
            sim = simulation.load_state(
                simulation_state_file=sim_start_file_name,
                location_state_file=location_start_file_name,
                agent_start_file=agent_start_file_name
            )
        else:
            print('Unknown Input...Quitting')
            exit(0)
    elif load_from_file == 'n':
        print('What Type of Agent to Test: ')
        agent_type = input()
        if agent_type == 'h2h_agent':
            sim = simulation('./target_data_2.csv', './target_stations_2.csv', 'h2h_agent')
        elif agent_type == 'informed_agent_1':
            sim = simulation('./target_data_2.csv', './target_stations_2.csv', 'informed_agent_1')
        elif agent_type == 'all_knowing_agent':
            sim = simulation('./target_data_2.csv', './target_stations_2.csv', 'all_knowing_agent')
        else:
            print('Unknown Input...Quitting')
            exit(0)
    else:
        print('Unknown Input...Quitting')
        exit(0)

    signal(SIGINT, handler)
    sim.run_sim()