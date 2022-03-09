import pandas as pd

# Upper latitude is white hills, Louisiana
UPPER_LATITUDE = 30.5980
# Lower latitude is Addis, Louisiana
LOWER_LATITUDE = 30.3538
# Left latitude is Livingston, Louisiana
LEFT_LONGITUDE = -91.2104
# Right latitude is st Bernard, Louisiana
RIGHT_LONGITUDE = -91.0009

louisiana_data = pd.read_csv('./louisiana_data_2.csv')

target_data = louisiana_data[louisiana_data['latitude'] < UPPER_LATITUDE]
target_data = target_data[target_data['longitude'] > LEFT_LONGITUDE]
target_data = target_data[target_data['longitude'] < RIGHT_LONGITUDE]

target_data.to_csv('target_data_2.csv')

station_data = pd.read_csv('./stations_2.csv', sep=';')

stat_data = station_data[station_data['latitude'] < UPPER_LATITUDE]
stat_data = stat_data[stat_data['longitude'] > LEFT_LONGITUDE]
stat_data = stat_data[stat_data['longitude'] < RIGHT_LONGITUDE]

stat_data.to_csv('./target_stations_2.csv', sep=';')

target_data = pd.read_csv('target_data_2.csv')

min_x = min(target_data['x'])
print('minimum x: {}'.format(min_x))
print('maximum x: {}'.format(max(target_data['x'])))
min_y = min(target_data['y'])
print('minimum y: {}'.format(min_y))
print('maximum y: {}'.format(max(target_data['y'])))

data_offset = (min_x, min_y)

target_data['x'] = target_data['x'] - min_x
target_data['y'] = target_data['y'] - min_y

print('new minimum x: {}'.format(min(target_data['x'])))
print('new minimum y: {}'.format(min(target_data['y'])))
print('new maximum x: {}'.format(max(target_data['x'])))
print('new maximum y: {}'.format(max(target_data['y'])))

target_data.to_csv('target_data_2.csv')

station_data = pd.read_csv('target_stations_2.csv', sep=';')

station_data['x'] = station_data['x'] - min_x
station_data['y'] = station_data['y'] - min_y

station_data.to_csv('target_stations_2.csv', sep=';')