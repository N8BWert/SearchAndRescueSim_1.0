import pandas as pd
import math
import numpy as np

louisiana_data = pd.read_csv('louisiana.csv', delimiter=',')
station_data = pd.read_csv('station_coordinates.txt', delimiter=';')

print(louisiana_data.columns)
print(station_data.columns)

louisiana_data['y'] = louisiana_data['latitude'] * 111139
louisiana_data['x'] = (louisiana_data['longitude'] * 111139)

louisiana_data.to_csv('louisiana_data_2.csv', sep=',')

station_data['y'] = station_data['latitude'] * 111139
station_data['x'] = (station_data['longitude'] * 111139)

station_data.to_csv('stations_2.csv', sep=';')