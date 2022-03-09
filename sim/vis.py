import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

building_data = pd.read_csv('./target_data_2.csv')
station_data = pd.read_csv('./target_stations_2.csv', sep=';')

saved_survivor_titles = [
    'inf',
    '216000',
    '7200',
    '3600',
    '600',
    '0'
]
saved_survivor_data_1 = [2388, 2437, 2447, 2499, 2570, 2627]
saved_survivor_data_2 = [2394, 2441, 2467, 2460, 2559, 2618]

building_x_points = building_data['x'].to_numpy()
building_y_points = building_data['y'].to_numpy()

station_x_points = station_data['x'].to_numpy()
station_y_points = station_data['y'].to_numpy()

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(building_x_points, building_y_points, 'ob')
axs[0, 0].set_title('Baton Rouge - Building Points')
axs[0, 0].set_xlabel('x coordinate (m)')
axs[0, 0].set_ylabel('y coordinate (m)')

axs[0, 1].plot(station_x_points, station_y_points, 'or')
axs[0, 1].set_title('Baton Rouge - Station Points')
axs[0, 1].set_xlabel('x coordinate (m)')
axs[0, 1].set_ylabel('y coordinate (m)')

axs[1, 0].plot(building_x_points, building_y_points, 'ob')
axs[1, 0].plot(station_x_points, station_y_points, 'or')
axs[1, 0].set_title('Baton Rouge - All Buildings (Including Fire Stations)')
axs[1, 0].set_xlabel('x coordinate (m)')
axs[1, 0].set_ylabel('y coordinate (m)')

ind = np.arange(6)
width = 0.5

trial_1 = axs[1, 1].bar(ind, saved_survivor_data_1, color='b', width=width - 0.1)
trial_2 = axs[1, 1].bar(ind + width, saved_survivor_data_2, color='r', width=width - 0.1)
axs[1, 1].set_xticks(ind + width / 2)
axs[1, 1].set_xticklabels(saved_survivor_titles)
axs[1, 1].set_ylim([2300, 2700])
axs[1, 1].set_xlabel('time between location send (s)')
axs[1, 1].set_ylabel('survivors saved')
axs[1, 1].legend((trial_1[0], trial_2[0]), ('seed 1', 'seed 2'))

plt.show()
