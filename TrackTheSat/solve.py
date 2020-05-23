import datetime
from skyfield.api import load, EarthSatellite, Topos

"""
Track-a-sat control system
Latitude: 52.5341
Longitude: 85.18
Satellite: PERUSAT 1
Start time GMT: 1586789933.820023
720 observations, one every 1 second
Waiting for your solution followed by a blank line...

"""

def build_ts(time_num):
    return load.timescale()

def build_sat(sat_name):
    tle1, tle2 = sat_dict[sat_name]
    return EarthSatellite(tle1, tle2, sat_name)

def build_topos(lat, lon):
    return Topos(lat, lon)

sat_dict = {}

with open('Data/active.txt','r') as f:
    data = f.readlines()
    data = [l.replace('\n', "").rstrip() for l in data]

for index, line in enumerate(data[::3]):
    sat_dict[line] = data[index],data[index+1]

# Setup
lat = 52.5341
lon = 85.18
demo_time = 1586789933.820023
sat_name = "PERUSAT 1"

# Building sat / topos object
bluffton = build_topos(lat, lon)
sat = build_sat(sat_name)

ts = load.timescale().utc(datetime.date.fromtimestamp(demo_time))

print(ts)

difference = sat - bluffton

