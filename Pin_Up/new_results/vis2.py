import matplotlib.pyplot as plt
import pandas as pd

building_data = pd.read_csv('./target_data_2.csv')

house_to_house_agents = open('./save_states/ijqlGf/ijqlGf-agents--1.txt', 'r')
ten_min_agents = open('./save_states/ijqlGf/ijqlGf-AIxwAt-agents--1.txt', 'r')
sixy_min_agents = open('./save_states/ijqlGf/ijqlGf-TxPbpo-agents--1.txt', 'r')
two_hour_agents = open('./save_states/ijqlGf/ijqlGf-bKQUyW-agents--1.txt', 'r')
six_hour_agents = open('./save_states/ijqlGf/ijqlGf-NuQcHY-agents--1.txt', 'r')
fully_informed_agents = open('./save_states/ijqlGf/ijqlGf-nuRfQv-agents--1.txt', 'r')

saved_survivor_titles = [
    'inf',
    '216000',
    '7200',
    '3600',
    '600',
    '0'
]
saved_survivor_data = [1901, 1979, 2130, 2225, 2487, 2604]

# plt.bar(saved_survivor_titles, saved_survivor_data)
# plt.title('Survivor Saved with variable base camp relay times (22% of homes with survivors)')
# plt.xlabel('time between location send (s)')
# plt.ylabel('survivors saved')
# plt.ylim([1800, 2700])

h2h_agent_paths = []
for line in house_to_house_agents.readlines():
    line_data = line.split(',')
    location_string = line_data[7]
    locational_strings = location_string.split('|')
    agent_xs = []
    agent_ys = []
    for location_string in locational_strings:
        location_string = location_string[1:-1]
        data_strings = location_string.split(';')
        agent_xs.append(float(data_strings[0]))
        agent_ys.append(float(data_strings[1]))
    h2h_agent_paths.append((agent_xs, agent_ys))

ten_min_agent_paths = []
for line in ten_min_agents.readlines():
    line_data = line.split(',')
    location_string = line_data[7]
    locational_strings = location_string.split('|')
    agent_xs = []
    agent_ys = []
    for location_string in locational_strings:
        location_string = location_string[1:-1]
        data_strings = location_string.split(';')
        agent_xs.append(float(data_strings[0]))
        agent_ys.append(float(data_strings[1]))
    ten_min_agent_paths.append((agent_xs, agent_ys))

sixy_min_agent_paths = []
for line in sixy_min_agents.readlines():
    line_data = line.split(',')
    location_string = line_data[7]
    locational_strings = location_string.split('|')
    agent_xs = []
    agent_ys = []
    for location_string in locational_strings:
        location_string = location_string[1:-1]
        data_strings = location_string.split(';')
        agent_xs.append(float(data_strings[0]))
        agent_ys.append(float(data_strings[1]))
    sixy_min_agent_paths.append((agent_xs, agent_ys))

two_hour_agent_paths = []
for line in two_hour_agents.readlines():
    line_data = line.split(',')
    location_string = line_data[7]
    locational_strings = location_string.split('|')
    agent_xs = []
    agent_ys = []
    for location_string in locational_strings:
        location_string = location_string[1:-1]
        data_strings = location_string.split(';')
        agent_xs.append(float(data_strings[0]))
        agent_ys.append(float(data_strings[1]))
    two_hour_agent_paths.append((agent_xs, agent_ys))

six_hour_agent_paths = []
for line in six_hour_agents.readlines():
    line_data = line.split(',')
    location_string = line_data[7]
    locational_strings = location_string.split('|')
    agent_xs = []
    agent_ys = []
    for location_string in locational_strings:
        location_string = location_string[1:-1]
        data_strings = location_string.split(';')
        agent_xs.append(float(data_strings[0]))
        agent_ys.append(float(data_strings[1]))
    six_hour_agent_paths.append((agent_xs, agent_ys))

fully_informed_agent_paths = []
for line in fully_informed_agents.readlines():
    line_data = line.split(',')
    location_string = line_data[7]
    locational_strings = location_string.split('|')
    agent_xs = []
    agent_ys = []
    for location_string in locational_strings:
        location_string = location_string[1:-1]
        data_strings = location_string.split(';')
        agent_xs.append(float(data_strings[0]))
        agent_ys.append(float(data_strings[1]))
    fully_informed_agent_paths.append((agent_xs, agent_ys))

fig, axs = plt.subplots(2, 3)

# axs[0, 0].scatter(building_data['x'].to_numpy(), building_data['y'].to_numpy(), c='r')
axs[0, 0].plot(h2h_agent_paths[0][0], h2h_agent_paths[0][1], 'o:b')
# axs[0, 0].plot(h2h_agent_paths[1][0], h2h_agent_paths[1][1], 'o:w')
# axs[0, 0].plot(h2h_agent_paths[2][0], h2h_agent_paths[2][1], 'o:g')
# axs[0, 0].plot(h2h_agent_paths[3][0], h2h_agent_paths[3][1], 'o:c')
# axs[0, 0].plot(h2h_agent_paths[4][0], h2h_agent_paths[4][1], 'o:m')
# axs[0, 0].plot(h2h_agent_paths[5][0], h2h_agent_paths[5][1], 'o:y')
# axs[0, 0].plot(h2h_agent_paths[6][0], h2h_agent_paths[6][1], 'o:k')
# axs[0, 0].plot(h2h_agent_paths[7][0], h2h_agent_paths[7][1], 'o:w')
# axs[0, 0].plot(h2h_agent_paths[8][0], h2h_agent_paths[8][1], 'o:b')
axs[0, 0].set_title('house to house search coverage')
axs[0, 0].set_xlabel('x position (m)')
axs[0, 0].set_ylabel('y position (m)')

# axs[0, 1].scatter(building_data['x'].to_numpy(), building_data['y'].to_numpy(), c='r')
axs[0, 1].plot(ten_min_agent_paths[0][0], ten_min_agent_paths[0][1], 'o:b')
# axs[0, 1].plot(ten_min_agent_paths[1][0], ten_min_agent_paths[1][1], 'o:w')
# axs[0, 1].plot(ten_min_agent_paths[2][0], ten_min_agent_paths[2][1], 'o:g')
# axs[0, 1].plot(ten_min_agent_paths[3][0], ten_min_agent_paths[3][1], 'o:c')
# axs[0, 1].plot(ten_min_agent_paths[4][0], ten_min_agent_paths[4][1], 'o:m')
# axs[0, 1].plot(ten_min_agent_paths[5][0], ten_min_agent_paths[5][1], 'o:y')
# axs[0, 1].plot(ten_min_agent_paths[6][0], ten_min_agent_paths[6][1], 'o:k')
# axs[0, 1].plot(ten_min_agent_paths[7][0], ten_min_agent_paths[7][1], 'o:w')
# axs[0, 1].plot(ten_min_agent_paths[8][0], ten_min_agent_paths[8][1], 'o:b')
axs[0, 1].set_title('10 minute relay search coverage')
axs[0, 1].set_xlabel('x position (m)')
axs[0, 1].set_ylabel('y position (m)')

# axs[0, 2].scatter(building_data['x'].to_numpy(), building_data['y'].to_numpy(), c='r')
axs[0, 2].plot(sixy_min_agent_paths[0][0], sixy_min_agent_paths[0][1], 'o:b')
# axs[0, 2].plot(sixy_min_agent_paths[1][0], sixy_min_agent_paths[1][1], 'o:w')
# axs[0, 2].plot(sixy_min_agent_paths[2][0], sixy_min_agent_paths[2][1], 'o:g')
# axs[0, 2].plot(sixy_min_agent_paths[3][0], sixy_min_agent_paths[3][1], 'o:c')
# axs[0, 2].plot(sixy_min_agent_paths[4][0], sixy_min_agent_paths[4][1], 'o:m')
# axs[0, 2].plot(sixy_min_agent_paths[5][0], sixy_min_agent_paths[5][1], 'o:y')
# axs[0, 2].plot(sixy_min_agent_paths[6][0], sixy_min_agent_paths[6][1], 'o:k')
# axs[0, 2].plot(sixy_min_agent_paths[7][0], sixy_min_agent_paths[7][1], 'o:w')
# axs[0, 2].plot(sixy_min_agent_paths[8][0], sixy_min_agent_paths[8][1], 'o:b')
axs[0, 2].set_title('60 minute relay search coverage')
axs[0, 2].set_xlabel('x position (m)')
axs[0, 2].set_ylabel('y position (m)')

# axs[1, 0].scatter(building_data['x'].to_numpy(), building_data['y'].to_numpy(), c='r')
axs[1, 0].plot(two_hour_agent_paths[0][0], two_hour_agent_paths[0][1], 'o:b')
# axs[1, 0].plot(two_hour_agent_paths[1][0], two_hour_agent_paths[1][1], 'o:w')
# axs[1, 0].plot(two_hour_agent_paths[2][0], two_hour_agent_paths[2][1], 'o:g')
# axs[1, 0].plot(two_hour_agent_paths[3][0], two_hour_agent_paths[3][1], 'o:c')
# axs[1, 0].plot(two_hour_agent_paths[4][0], two_hour_agent_paths[4][1], 'o:m')
# axs[1, 0].plot(two_hour_agent_paths[5][0], two_hour_agent_paths[5][1], 'o:y')
# axs[1, 0].plot(two_hour_agent_paths[6][0], two_hour_agent_paths[6][1], 'o:k')
# axs[1, 0].plot(two_hour_agent_paths[7][0], two_hour_agent_paths[7][1], 'o:w')
# axs[1, 0].plot(two_hour_agent_paths[8][0], two_hour_agent_paths[8][1], 'o:b')
axs[1, 0].set_title('2 hour relay search coverage')
axs[1, 0].set_xlabel('x position (m)')
axs[1, 0].set_ylabel('y position (m)')

# axs[1, 1].scatter(building_data['x'].to_numpy(), building_data['y'].to_numpy(), c='r')
axs[1, 1].plot(six_hour_agent_paths[0][0], six_hour_agent_paths[0][1], 'o:b')
# axs[1, 1].plot(six_hour_agent_paths[1][0], six_hour_agent_paths[1][1], 'o:w')
# axs[1, 1].plot(six_hour_agent_paths[2][0], six_hour_agent_paths[2][1], 'o:g')
# axs[1, 1].plot(six_hour_agent_paths[3][0], six_hour_agent_paths[3][1], 'o:c')
# axs[1, 1].plot(six_hour_agent_paths[4][0], six_hour_agent_paths[4][1], 'o:m')
# axs[1, 1].plot(six_hour_agent_paths[5][0], six_hour_agent_paths[5][1], 'o:y')
# axs[1, 1].plot(six_hour_agent_paths[6][0], six_hour_agent_paths[6][1], 'o:k')
# axs[1, 1].plot(six_hour_agent_paths[7][0], six_hour_agent_paths[7][1], 'o:w')
# axs[1, 1].plot(six_hour_agent_paths[8][0], six_hour_agent_paths[8][1], 'o:b')
axs[1, 1].set_title('6 hour relay search coverage')
axs[1, 1].set_xlabel('x position (m)')
axs[1, 1].set_ylabel('y position (m)')

# axs[1, 2].scatter(building_data['x'].to_numpy(), building_data['y'].to_numpy(), c='r')
axs[1, 2].plot(fully_informed_agent_paths[0][0], fully_informed_agent_paths[0][1], 'o:b')
# axs[1, 2].plot(fully_informed_agent_paths[1][0], fully_informed_agent_paths[1][1], 'o:w')
# axs[1, 2].plot(fully_informed_agent_paths[2][0], fully_informed_agent_paths[2][1], 'o:g')
# axs[1, 2].plot(fully_informed_agent_paths[3][0], fully_informed_agent_paths[3][1], 'o:c')
# axs[1, 2].plot(fully_informed_agent_paths[4][0], fully_informed_agent_paths[4][1], 'o:m')
# axs[1, 2].plot(fully_informed_agent_paths[5][0], fully_informed_agent_paths[5][1], 'o:y')
# axs[1, 2].plot(fully_informed_agent_paths[6][0], fully_informed_agent_paths[6][1], 'o:k')
# axs[1, 2].plot(fully_informed_agent_paths[7][0], fully_informed_agent_paths[7][1], 'o:w')
# axs[1, 2].plot(fully_informed_agent_paths[8][0], fully_informed_agent_paths[8][1], 'o:b')
axs[1, 2].set_title('fully knowledgable agent search coverage')
axs[1, 2].set_xlabel('x position (m)')
axs[1, 2].set_ylabel('y position (m)')

plt.show()