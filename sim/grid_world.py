import pandas as pd
import numpy as np

target_data = pd.read_csv('target_data.csv')
station_data = pd.read_csv('target_stations.csv', sep=';')

target_data['y'] = np.round(target_data['y'])
target_data['x'] = np.round(target_data['x'])

y_range = max(target_data['y']) - min(target_data['y'])
x_range = max(target_data['x']) - min(target_data['x'])

station_data['y'] = station_data['y'] < max(target_data['y'])
station_data['x'] = station_data['x'] < max(target_data['x'])

station_data['y'] = np.round(station_data['y'])
station_data['x'] = np.round(station_data['x'])

print(y_range)
print(x_range)